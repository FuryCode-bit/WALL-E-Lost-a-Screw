"""
45703, Marco Bernardes
46811, Ana Lúcia Ferreira
"""

'''
!!!TODO LIST!!!
PERGUNTAS:
1. DONE
2. DONE
3. DONE

TAREFAS NO GERAL:
- Definicao de grafo e atributos || DONE ||
- Atualizar o tipo de zona quando o robot a descobre || DONE ||
'''

import time
import networkx as nx

pilha = []
encontros = []

'''
# Esta função é como uma bola de cristal 🎱: ela prevê o gênero do humanóide com base no nome!
# Suponho que no estado em que estamos a seguir enquanto sociedade, seja algo que deixe de funcionar nos próximos anos.
# Mas acredito que num curto espaço de 2 meses, esta função seja suficiente.
'''
def identify_gender(name):
    with open('utils/p1/listaNomes.txt', 'r') as file:
        for line in file:
            if line.lower().find(name.lower()) != -1:
                return True

    return False


# !!! DEFINICAO GRAFO !!!
G = nx.Graph()

'''
Definicao de atributos:
	Tipo: tipo da zona. por default é "sem identificação"
	Coord: coordenadas do ponto superior esquerdo e inferior direito de cada zona
		A zona 11 precisa de pontos extra
'''
for i in range(15):
	G.add_node(i, tipo = "sem identificação")
for i in range(1,5):
	G.add_node(i, tipo = "corredor")
G.add_node(10, tipo = "entrada")

coordenadas = ([
    (0, {"coord": [[155,230],[485,335]]}),
    (1, {"coord": [[30,165],[150,375]]}),
    (2, {"coord": [[155,165],[485,185]]}),
    (3, {"coord": [[30,380],[525,435]]}),
    (4, {"coord": [[530,180],[635,435]]}),
    (5, {"coord": [[30,30],[135,135]]}),
    (6, {"coord": [[180,30],[285,135]]}),
    (7, {"coord": [[330,30],[485,135]]}),
    (8, {"coord": [[530,30],[770,185]]}),
    (9, {"coord": [[640,230],[770,285]]}),
    (10, {"coord": [[640,330],[770,385]]}),
    (11, {"coord": [[530,440],[640,570],[640,430],[770,570]]}),
    (12, {"coord": [[330,440],[485,570]]}),
    (13, {"coord": [[180,440],[285,570]]}),
    (14, {"coord": [[30,440],[135,570]]}),
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
# !!! FIM DEFINICAO GRAFO !!!

posatual = 10 # numero da zona atual
nodeatual = G.nodes[posatual]

'''
Esta função identifica cada objeto em que o WALL-E entra em contacto e vai inserindo numa pilha.
Para identificar um humano é usado uma lista de prefixos com os títulos disponíveis. 
Assim sempre que o WALL-E entrar em contacto com um humano de género masculino vai inserir apenas o seu nome numa pilha de nome pilha_resp1
(Nomear a pilha de male_pilha ou obj_pessoas poderia deixar os humanos um tanto... objetificados ou confusos com outras coisas, então optei por um nome mais simples! 🤖)
'''
def work(posicao, bateria, objetos):
	time.time()
	
	global posatual
	global nodeatual
	
	# !!! MUDANCA DE ZONA !!!
	if posicao[0] <= nodeatual["coord"][0][0] or posicao[0] >= nodeatual["coord"][1][0] \
	or posicao[1] <= nodeatual["coord"][0][1] or posicao[1] >= nodeatual["coord"][1][1]:
		for i in G[posatual]:
			teste = G.nodes[i]["coord"]
			if posicao[0] >= teste[0][0] and posicao[0] <= teste[1][0] \
			and posicao[1] >= teste[0][1] and posicao[1] <= teste[1][1]:
				posatual = i
				nodeatual = G.nodes[posatual]
				print("Mudança de zona para: ", i)
			elif i == 11:
				if posicao[0] >= teste[2][0] and posicao[0] <= teste[3][0] \
				and posicao[1] >= teste[2][1] and posicao[1] <= teste[3][1]:
					posatual = i
					nodeatual = G.nodes[posatual]
					print("Mudança de zona para: ", i)
	# !!! FIM MUDANCA DE ZONA !!!
	
	person_prefixes = ['operário_', 'visitante_', 'supervisor_']
	if objetos and isinstance(objetos, list) and len(objetos) == 1:
		obj = objetos[0]
		# Mudar tipo de zona
		if obj.startswith("zona_") and nodeatual["tipo"] == "sem identificação":
			nodeatual["tipo"] = obj[len("zona_"):]
			print("Mudança de tipo de zona para: ", nodeatual["tipo"])
		else:
			for prefix in person_prefixes:
				if obj.startswith(prefix) and obj not in pilha and obj[len(prefix):] not in pilha:
					obj_without_prefix = obj[len(prefix):]
					pilha.append(obj_without_prefix)
					if identify_gender(obj_without_prefix) == True:
						encontros.append(obj)
						print("pilha: ", pilha)
						print("encontros: ", encontros)
						#pilha.append(obj)
					break
	
	
	# print("print: ", posicao, bateria, objetos) 
	# print("dados: ", posicao, bateria, objetos)

'''
Esta função começa por verificar quantas pessoas de género masculino o WALL-E esteve em contacto.
Se apenas teve em contacto com uma (ou com nenhuma) ele indica que não possui informação suficiente para resolver o problema.
Se tiver toda a informação necessária, vai indicar o nome da penúltima pessoa que encontrou!
'''

def resp1():
	if len(encontros) >= 2:
		penultimo = encontros[-2]
		print("O penultimo elemento é: ", penultimo)
	else:
		print("Não existe informação suficiente")

def resp2():
	print("A zona", posatual, "é do tipo", nodeatual["tipo"])	

def resp3():
	if nodeatual["tipo"] == "empacotamento":
		print("Já estou na zona de empacotamento!")
	else:
		dest = -1
		for i in range(15):
			if G.nodes[i]["tipo"] == "empacotamento":
				dest = i
				break
		if dest == -1:
			print("Ainda não sei a localização da zona de empacotamento")
		else:
			print("O caminho desde a zona", posatual, "até a zona de empacotamento", dest, "é:", nx.shortest_path(G, posatual, dest))

def resp4():
	pass

def resp5():
	pass

def resp6():
	pass

def resp7():
	pass

def resp8():
	pass
