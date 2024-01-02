import networkx as nx
import math

def givePosicao(posicao):
	global posicaoRobot 
	posicaoRobot = posicao
 
# Transferir a posição atual do WALL-E para as funções de resposta
def getPosicao():
	return posicaoRobot
 
'''
Nesta função criamos um grafo que vai corresponder às ligações entre as zonas da fábrica.
Cada nodo (número da zona) tem os seguintes atributos:
	tipo: tipo da zona
		ex: sem identificação, corredor, entrada, laboratório, etc.
	coord: coordenadas do canto superior esquerdo e canto inferior direito
		no caso do nodo 11 necessita de mais pontos já que este é constituído por 2 retângulos
	maquinas: nome das maquinas presentes na zona
	operarios: nome dos operarios presentes na zona
	supervisores: nomes dos supervisores presentes na zona
Cada aresta (ligação entre duas zonas) tem o seguinte atributo:
	ligacao: indica um ponto em comum entre as duas zonas
		este atributo será utilizado para calcular a distância entre zonas
'''

def criarGrafo():
	global G
	G = nx.Graph()
	for i in range(15):
		G.add_node(i, tipo = "sem identificação", maquinas=[], operarios=[], supervisores=[])
	for i in range(1,5):
		G.add_node(i, tipo = "corredor")
	G.add_node(10, tipo = "entrada")
 
	coordenadas = ([
		(0, {"coord": [[155,230],[485,335]]}),
		(1, {"coord": [[30,145],[150,375]]}),
		(2, {"coord": [[155,145],[485,185]]}),
		(3, {"coord": [[30,380],[520,435]]}),
		(4, {"coord": [[525,180],[635,435]]}),
		(5, {"coord": [[30,30],[150,145]]}),
		(6, {"coord": [[180,30],[285,145]]}),
		(7, {"coord": [[330,30],[485,145]]}),
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

	return G
 
'''
Recebe as coordenadas do WALL-E e o número da zona atual para descobrir para qual das zonas este se deslocou
	G[posatual]: devolve os vizinhos da zona atual; estes são suficientes para a pesquisa
Devolve:
	posAtual = numero da zona atualizada e
	G.nodes[posAtual] = nodo correspondente à zona atual
'''

def mudarZona(posicao, posAtual):
	for i in G[posAtual]:
		teste = G.nodes[i]["coord"]
		
		# Compara as coordenadas da posição do WALL-E com os pontos extremos da zona que estamos a testar
		if posicao[0] >= teste[0][0] and posicao[0] <= teste[1][0] \
		and posicao[1] >= teste[0][1] and posicao[1] <= teste[1][1]:
			posAtual = i
			nodeAtual = G.nodes[posAtual]
			break
		# Como a zona 11 é composta por dois retângulos testamos o segundo retângulo aqui
		elif i == 11:
			if posicao[0] >= teste[2][0] and posicao[0] <= teste[3][0] \
			and posicao[1] >= teste[2][1] and posicao[1] <= teste[3][1]:
				posAtual = i
				nodeAtual = G.nodes[posAtual]
 
	return posAtual, G.nodes[posAtual]
 
''' 
Verifica se a zona (node) é do tipo dado 
Devolve: 
	True se for do mesmo tipo ou 
	False caso contrário
'''

def compTipoZona(node, tipo):
	if node["tipo"] == tipo:
		return True
	return False
 
'''
Procura o tipo de zona pedido no grafo
Devolve:
	Número da zona correspondente ou
	-1 se não encontrar
'''

def procurarTipoZona(tipo):
	dest = -1
	for i in range(15):
		if compTipoZona(G.nodes[i], tipo):
			dest = i
			break

	return dest

# Encontra o ponto médio da zona pedida
def pontoMedio(posicao):
	pontoMedioX = (posicao[0][0] + posicao[1][0])/2
	pontoMedioY = (posicao[0][1] + posicao[1][1])/2

	return [pontoMedioX, pontoMedioY]
 
'''
Dado um caminho calcula a distância desde a posição atual do WALL-E até ao ponto médio da zona destino
Para realizar os cálculos, utiliza o ponto de ligação entre a zona que estamos a observar e a zona seguinte do caminho
Por fim, faz um cálculo extra para calcular a distância em específico para o ponto médio
'''

def distancia(caminho):
	distTotal = 0
	posAnterior = [0,0]
 
	for i in range(len(caminho) - 1):
		zonaAtual = caminho[i]
		nodeZona = G.nodes[zonaAtual]
		ligacao = G[zonaAtual][caminho[i + 1]]["ligacao"]
 
		# Se for a zona inicial utiliza a posição onde o WALL-E se encontra
		if posAnterior == [0,0]:
			pos = getPosicao()
		# Se for um corredor utiliza a posição anterior
		else:
			pos = posAnterior
		
		distZona = math.sqrt((pos[0] - ligacao[0])**2 + (pos[1] - ligacao[1])**2)
		distTotal = distTotal + round(distZona)
		posAnterior = ligacao
	
	# Calcular distância até ao ponto medio da zona de destino
	pos = pontoMedio(G.nodes[caminho[-1]]["coord"])
	distZona = math.sqrt((pos[0] - ligacao[0])**2 + (pos[1] - ligacao[1])**2)
	distTotal = distTotal + round(distZona)
	
	return distTotal
