import pyAgrum as gum
 
"""
Determina a probabilidade de a proxima pessoa ser um supervisor
Contabiliza os "objetos" agrupando-os de forma individual
 
Explicação: Assumindo que Os supervisores querem avaliar o comportamento dos operários, 
especialmente quando estão a trabalhar com as máquinas. Podemos assumir que existe uma 
forte necessidade de se existe um operário existe uma grande chance de haver um supervisor.
 
Logo poderemos calcular a p(supervisor) = p(supervisor | operario)
 
O que dará p(supervisor) = (p(supervisor, operario))/p(operario)
 
Através da regra da probabilidade total poderemos calcular
P(supervisor, operario)=P(supervisor,maquina,operario)+P(B,¬maquina,supervisor)
 
Returns:
	float: probabilidade de a proxima pessoa avistada ser um supervisor
"""
 
def probabilidadeProximoSerSupervisor(G):  

	# Contadores
	contadorMaquinas = 0
	contadorOperarios = 0
	contadorSupervisores = 0

	for node in G.nodes(data=True):
		contadorMaquinas += len(node[1]["maquinas"]) if len(node[1]["maquinas"]) > 0 else 0
		contadorOperarios += len(node[1]["operarios"]) if len(node[1]["operarios"]) > 0 else 0
		contadorSupervisores += len(node[1]["supervisores"]) if len(node[1]["supervisores"]) > 0 else 0

	total = contadorMaquinas + contadorOperarios + contadorSupervisores
	print("total: ", total)

	pMaquinas = contadorMaquinas / total
	pOperarios = contadorOperarios / total

	probabilidade = ((pMaquinas * pOperarios * 0.8) + ((1 - pMaquinas) * pOperarios * 0.5)) / pOperarios

	return probabilidade

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
Calcula a probabilidade tendo em conta os parâmetros fornecidos
	d: evidência
	q: probabilidade que queremos calcular
	num: 0 ou 1, indica se queremos a probabilidade de q ser falso (0) ou verdadeiro (1)
'''
def calcularProbabilidade (G,d,q,num):
	ie = gum.LazyPropagation(bn)
	ie.setEvidence(d)
	ie.makeInference()
	
	return ie.posterior(q)[num]

'''
Percorre todas as zonas para atualizar na rede bayesiana as 
probabilidades que serão alteradas à medida que o robot explora a fábrica
	numZonasMaquina: número de zonas descobertas que tem pelo menos uma máquina
	numZonasOperarioMaquina: número de zonas descobertas que tem pelo menos um operário e um máquina
	numZonasOperarioNaoMaquina: número de zonas descobertas que tem pelo menos um operário mas não tem máquina
'''
def atualizarProbRede(G):
	numZonasTotal = 0
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
				numZonasTotal += 1
		# Se tem operário e não tem máquina
		if G.nodes[i]["operarios"] != []:
			numZonasOperarioNaoMaquina += 1
			numZonasTotal += 1
		
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
