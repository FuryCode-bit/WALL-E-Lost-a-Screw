import matplotlib.pyplot as plt
import networkx as nx
import math
 
# Variáveis globais
posicaoRobot = 0
G = nx.Graph()
 
def givePosicao(posicao):
	global posicaoRobot 
	posicaoRobot = posicao
 
# Transferir a posição atual do robot para as funções de resposta
def getPosicao():
	return posicaoRobot
 
'''
Nesta função criamos um grafo que vai corresponder às ligações entre as zonas da fábrica.
Cada nodo (número da zona) tem os seguintes atributos:
	- tipo: tipo da zona
		ex: sem identificação, corredor, entrada, laboratório, etc.
	- coord: coordenadas do canto superior esquerdo e canto inferior direito
		no caso do nodo 11 necessita de mais pontos já que este é constituído por 2 retângulos
Cada aresta (ligação entre duas zonas) tem o seguinte atributo:
	- ligacao: indica um ponto em comum entre as duas zonas
		este atributo será utilizado para calcular a distância entre zonas
'''
def criarGrafo():
	global G
 
	for i in range(15):
		G.add_node(i, tipo = "sem identificação", maquinas=[], operarios=[], supervisores=[])
	for i in range(1,5):
		G.add_node(i, tipo = "corredor")
	G.add_node(10, tipo = "entrada")
 
	coordenadas = ([
		(0, {"coord": [[155,230],[485,335]]}),
		(1, {"coord": [[30,140],[150,375]]}),
		(2, {"coord": [[155,140],[485,185]]}),
		(3, {"coord": [[30,380],[520,435]]}),
		(4, {"coord": [[525,180],[635,435]]}),
		(5, {"coord": [[30,30],[150,135]]}),
		(6, {"coord": [[180,30],[285,135]]}),
		(7, {"coord": [[330,30],[485,135]]}),
		(8, {"coord": [[530,30],[770,185]]}),
		(9, {"coord": [[640,230],[770,285]]}),
		(10, {"coord": [[640,330],[770,385]]}),
		(11, {"coord": [[530,440],[640,570],[640,430],[770,570]]}),
		(12, {"coord": [[330,440],[485,570]]}),
		(13, {"coord": [[180,440],[285,570]]}),
		(14, {"coord": [[30,440],[150,570]]}),
	])
	G.add_nodes_from(coordenadas)
 
	# Ligacoes entre zonas
	edge_list = [
		# Corredor 1
		(1, 0), (1, 2), (1, 3), (1, 5),
		# Corredor 2
		(2, 6), (2, 7),
		# Corredor 3
		(3, 4), (3, 12), (3, 13), (3, 14),
		# Corredor 4
		(4, 8), (4, 9), (4, 10), (4, 11)
	]
	G.add_edges_from(edge_list)
 
	# Ponto de ligação entre duas zonas
	ligZonas = {
		(1, 0): {"ligacao": [150, 280]},
		(1, 2): {"ligacao": [150, 175]},
		(1, 3): {"ligacao": [90, 380]},
		(1, 5): {"ligacao": [90, 140]},
		(2, 6): {"ligacao": [230, 140]},
		(2, 7): {"ligacao": [410, 140]},
		(3, 4): {"ligacao": [530, 410]},
		(3, 12): {"ligacao": [410, 440]},
		(3, 13): {"ligacao": [230, 440]},
		(3, 14): {"ligacao": [90, 440]},
		(4, 8): {"ligacao": [585, 180]},
		(4, 9): {"ligacao": [635, 260]},
		(4, 10): {"ligacao": [635, 360]},
		(4, 11): {"ligacao": [585, 440]}
	}
	nx.set_edge_attributes(G, ligZonas)
 
	# Draw the graph
	nx.draw_networkx(G, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
 
	# Display the graph
	plt.show()
 
	return G
 
# Atualizar a zona atual	
def mudarZona(posicao, posAtual):
	for i in G[posAtual]:
		teste = G.nodes[i]["coord"]
		if posicao[0] >= teste[0][0] and posicao[0] <= teste[1][0] \
		and posicao[1] >= teste[0][1] and posicao[1] <= teste[1][1]:
			posAtual = i
			nodeAtual = G.nodes[posAtual]
			print("Mudança de zona para: ", i) #Comentar depois
		elif i == 11:
			if posicao[0] >= teste[2][0] and posicao[0] <= teste[3][0] \
			and posicao[1] >= teste[2][1] and posicao[1] <= teste[3][1]:
				posAtual = i
				nodeAtual = G.nodes[posAtual]
				print("Mudança de zona para: ", i) #Comentar depois
 
	return posAtual, G.nodes[posAtual]
 
# Verifica se a zona tem o tipo dado
def compTipoZona(node, tipo):
	if node["tipo"] == tipo:
		return True
	return False
 
# Procura a zona que contém o tipo dado
def procurarTipoZona(tipo):
	dest = -1
	for i in range(15):
		if compTipoZona(G.nodes[i], tipo):
			dest = i
			break
 
	return dest
 
def pontoMedio(posicao):
	pontoMedioX = (posicao[0][0] + posicao[1][0])/2
	pontoMedioY = (posicao[0][1] + posicao[1][1])/2
 
	return [pontoMedioX, pontoMedioY]
 
# Calcula a distância de um dado caminho
def distancia(caminho):
	distTotal = 0
	posAnterior = [0,0]
 
	for i in range(len(caminho) - 1):
		zonaAtual = caminho[i]
		nodeZona = G.nodes[zonaAtual]
		ligacao = G[zonaAtual][caminho[i + 1]]["ligacao"]
 
		# Se for a zona inicial utiliza a posição onde o robot se encontra
		if posAnterior == [0,0]:
			pos = getPosicao()
		# Se for um corredor utiliza a posição anterior
		elif compTipoZona(nodeZona, "corredor"):
			pos = posAnterior
		# Ou então utiliza o ponto médio da zona
		else:
			pos = pontoMedio(nodeZona["coord"])
		distZona = math.sqrt((pos[0] - ligacao[0])**2 + (pos[1] - ligacao[1])**2)
		distTotal = distTotal + round(distZona)
		posAnterior = ligacao
 
	return distTotal

def probabildadeProximoSerSupervisor():

	#TODO -> Não esquecer documentar a implementação
	## Input: G.nodes(data=True)
	"""
	Determina a probabilidade de a proxima pessoa ser um supervisor
	Contabiliza os "objetos" agrupando-os de forma individual

	Returns:
		float: probabilidade de a proxima pessoa avistada ser um supervisor
	"""
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
