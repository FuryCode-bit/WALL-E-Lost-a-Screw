import pyAgrum as gum

def probabilidadeProximoSerSupervisor():
	'''
	 A _> Máquina
	 B -> Operário
	 C -> Supervisor

	Solução: P(C) = P(C | A, B) * P(A, B) + P(C | ¬A, B) * P(¬A, B) + P(C | A, ¬B) * P(A, ¬B) + P(C | ¬A, ¬B) * P(¬A, ¬B)
	'''	
	"""
	Determina a probabilidade de a proxima pessoa ser um supervisor
	Contabiliza os "objetos" agrupando-os de forma individual

	Returns:
		float: probabilidade de a proxima pessoa avistada ser um supervisor
	"""

	global G
	
	# Contadores
	counters = {
		"countA": 0,
		"countB": 0,
		"countC": 0
	}

	for node in G.nodes(data=True):
		counters["countA"] += len(node[1]["maquinas"]) if len(node[1]["maquinas"]) > 0 else 0
		counters["countB"] += len(node[1]["operarios"]) if len(node[1]["operarios"]) > 0 else 0
		counters["countC"] += len(node[1]["supervisores"]) if len(node[1]["supervisores"]) > 0 else 0

	# print("countA: ", counters["countA"])
	# print("countB: ", counters["countB"])
	# print("countC: ", counters["countC"])

	total_objects = counters["countA"] + counters["countB"] + counters["countC"]
	print("total_objects: ", total_objects)

	pA = counters["countA"] / total_objects
	pB = counters["countB"] / total_objects

	pBAC = (pA * pB * 0.8)
	pBnAC = ((1 - pA) * pB * 0.5)
	pCandB = pBAC + pBnAC

	return pCandB / pB

'''
Cria um Rede Bayesiana que relaciona as probabilidades numa zona estarem presentes:
	supervisor: este nodo utiliza as probabilidades fornecidas no enunciado
	maquina: baseada no numero de máquinas observadas
	operario: a probabilidade de um operário estar presente está dependente da existência de máquinas
'''

def criarRedeBayesiana():
	global bn
	global maquina
	global operario
	global supervisor
	bn=gum.BayesNet('LocalizacaoObjetos')
	
	# Criar nodos
	maquina = bn.add(gum.LabelizedVariable('maquina','maquina',2))
	operario = bn.add(gum.LabelizedVariable('operario','operario',2))
	supervisor = bn.add(gum.LabelizedVariable('supervisor','supervisor',2))
	
	# Criar arestas
	bn.addArc(maquina, operario)
	bn.addArc(maquina, supervisor)
	bn.addArc(operario, supervisor)
	
	# Definir probabilidades que nao serao alteradas (neste caso so as do supervisor)
	bn.cpt(supervisor)[{'maquina': 0, 'operario': 0}] = [0.9,0.1] 
	bn.cpt(supervisor)[{'maquina': 1, 'operario': 0}] = [0.8,0.2]
	bn.cpt(supervisor)[{'maquina': 0, 'operario': 1}] = [0.5,0.5]
	bn.cpt(supervisor)[{'maquina': 1, 'operario': 1}] = [0.2,0.8]

'''
Percorre todas as zonas para atualizar na rede bayesiana as 
probabilidades que serão alteradas à medida que o WALL-E explora a fábrica
	numZonasMaquina: número de zonas descobertas que tem pelo menos uma máquina
	numZonasOperarioMaquina: número de zonas descobertas que tem pelo menos um operário e um máquina
	numZonasOperarioNaoMaquina: número de zonas descobertas que tem pelo menos um operário mas não tem máquina
'''

def atualizarProbRede(G):
	numZonasTotal = 10 # 15 zonas da fábrica menos entrada e corredores
	numZonasMaquina = 0
	numZonasOperarioMaquina = 0
	numZonasOperarioNaoMaquina = 0
	
	# Conta o número de zonas que tem os parâmetros que desejamos
	for i in range(15):
		if i not in range(1,4) and i != 10:
			# Se tem alguma máquina na zona
			if G.nodes[i]["maquinas"] != []:
				numZonasMaquina += 1
				# Se tem operário e máquina na mesma zona
				if G.nodes[i]["operarios"] != []:
					numZonasOperarioMaquina += 1
			else:
				# Se tem operário e não tem máquina
				if G.nodes[i]["operarios"] != []:
					numZonasOperarioNaoMaquina += 1
		
	# Calcular probabilidades
	probMaquina = numZonasMaquina / numZonasTotal			
	
	probOperarioNaoMaquina = numZonasOperarioNaoMaquina / numZonasTotal # P(O & !M) = nOperario&!Maquina / nZonas
	probOperarioSeNaoMaquina = probOperarioNaoMaquina / (1 - probMaquina) # P(O | !M) = P(O & !M) / P(!M)
	
	probOperarioMaquina = numZonasOperarioMaquina / numZonasTotal # P(O & M) = nOperario&Maquina / nZonas
	probOperarioSeMaquina = probOperarioMaquina / probMaquina # P(O | M) = P(O & M) / P(M)
	
	# Atualizar probabilidades na rede
	bn.cpt(maquina)[{}] = [1 - probMaquina, probMaquina]
	bn.cpt(operario)[{'maquina': 0}] = [1 - probOperarioSeNaoMaquina, probOperarioSeNaoMaquina]
	bn.cpt(operario)[{'maquina': 1}] = [1 - probOperarioSeMaquina, probOperarioSeMaquina]
	
'''
Calcula a probabilidade tendo em conta os parâmetros fornecidos
	d: evidência
	q: probabilidade que queremos calcular
	num: 0 ou 1, indica se queremos a probabilidade de q ser falso (0) ou verdadeiro (1)

Devolve: 
	valor da probabilidade pedida ou 
	-1 se ainda não tivermos informação suficiente (onde irá dar divisão por zero)
'''

def calcularProbabilidade (G,d,q,num):
	try:
		atualizarProbRede(G)
		
		ie = gum.LazyPropagation(bn)
		ie.setEvidence(d)
		ie.makeInference()
		
		return ie.posterior(q)[num]
	except ZeroDivisionError:
		return -1
