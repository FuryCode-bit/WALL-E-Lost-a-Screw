# -*- coding: utf-8 -*-
 
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
4. DONE (I THINK)
5. TODO
6. DONE
7. DONE - Needs Revision
8. TODO
'''
 
import time
import networkx as nx
from utils import p1, p6, ambiente as amb

pilha = []
encontros = []
 
pilhaBateriaTempo = []

# Variáveis para o grafo
posAtual = 10 # Número da zona atual
G = amb.criarGrafo()
nodeAtual = G.nodes[posAtual]

tempoDecorrido = time.time()
tempo100 = time.time()

# esta funcao nao devia de estar no p6?
def updateListaBateriaTempo(bateria):
    global tempoDecorrido, tempo100, pilhaBateriaTempo
    if bateria == 100:
        tempo100 = time.time()
 
    tempoDecorrido = time.time() - tempo100
 
    if int(bateria) % 5 == 0 and int(bateria) != 100:
        pilhaBateriaTempo.append((bateria, tempoDecorrido))
        # print("pilhaBateriaTempo: ", pilhaBateriaTempo)
    if int(bateria) == 0:
        print("Bateria acabou!")
        # print(pilhaBateriaTempo)

'''
Esta função identifica cada objeto em que o WALL-E entra em contacto e vai inserindo numa pilha.
Para identificar um humano é usado uma lista de prefixos com os títulos disponíveis. 
Assim sempre que o WALL-E entrar em contacto com um humano de género masculino vai inserir apenas o seu nome numa pilha de nome pilha_resp1
(Nomear a pilha de male_pilha ou obj_pessoas poderia deixar os humanos um tanto... objetificados ou confusos com outras coisas, então optei por um nome mais simples! 🤖)
'''
def work(posicao, bateria, objetos):
 
	global tempo_final
	global tempo_decorrido
 
	global posatual
	global nodeatual
 
	# Mudança de Zona
	if posicao[0] <= nodeAtual["coord"][0][0] or posicao[0] >= nodeAtual["coord"][1][0] \
	or posicao[1] <= nodeAtual["coord"][0][1] or posicao[1] >= nodeAtual["coord"][1][1]:
		posAtual, nodeAtual = amb.mudarZona(posicao, posAtual)
	
	person_prefixes = ['operário_', 'visitante_', 'supervisor_']
	operario_prefix = 'operário_'
	supervisor_prefix = 'supervisor_'
	maquina_prefix = 'máquina_'
	if objetos and isinstance(objetos, list) and len(objetos) == 1:
		obj = objetos[0]
 		# Mudar Tipo de Zona
		# Cada Node está estruturado da seguinte maneira:
		# Node (
		#  tipo: str	
		#  maquinas: []	
		#  operarios: []	
		#  supervisores: []	
		#  Coord: [[][]]
		
		# A implementação seguinte armazena cada objeto de acordo com o seu prefixo na lista correspondente
		if obj.startswith("zona_") and amb.compTipoZona(nodeAtual, "sem identificação"):
			nodeAtual["tipo"] = obj[len("zona_"):]
			print("Mudança de tipo de zona para: ", nodeAtual["tipo"])
		elif obj.startswith(maquina_prefix):
			nodeAtual["maquinas"].append(obj[len(maquina_prefix):])
			print(nodeAtual)
		elif obj.startswith(operario_prefix):
			nodeAtual["operarios"].append(obj[len(operario_prefix):])
			print(nodeAtual)
		elif obj.startswith(supervisor_prefix):
			# G.nodes[node_key]['values'].append(user_input)
			nodeAtual["supervisores"].append(obj[len(supervisor_prefix):])
			print(nodeAtual)
		else:
			for prefix in person_prefixes:
				if obj.startswith(prefix) and obj not in pilha and obj[len(prefix):] not in pilha:
					obj_without_prefix = obj[len(prefix):]
					pilha.append(obj_without_prefix)
					if p1.identifica_genero(obj_without_prefix) == True:
						encontros.append(obj)
						print("pilha: ", pilha)
						print("encontros: ", encontros)
						#pilha.append(obj)
					break
 
	updateListaBateriaTempo(bateria)
	# print("dados: ", posicao, bateria, objetos, time.perf_counter())
	amb.givePosicao(posicao)
 
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
	print("A zona", posAtual, "é do tipo", nodeAtual["tipo"])

def resp3():
	if amb.compTipoZona(nodeAtual, "empacotamento"):
		print("Já estou na zona de empacotamento")
	else:
		dest = amb.procurarTipoZona("empacotamento")
		if dest == -1:
			print("Ainda não sei a localização da zona de empacotamento")
		else:
			print("O caminho desde a zona", posAtual, "até a zona de empacotamento", dest, "é:", nx.shortest_path(G, posAtual, dest))
 
def resp4():
	if amb.compTipoZona(nodeAtual, "laboratório"):
		print("Já estou no laboratório")
	else:
		dest = amb.procurarTipoZona("laboratório")
		if dest == -1:
			print("Ainda não sei a localização do laboratório")
		else:
			caminho = nx.shortest_path(G, posAtual, dest) # Encontrar caminho
			distTotal = amb.distancia(caminho)
			print("A distância desde a zona", posAtual, "até o laboratório", dest, "é", distTotal)

def resp5():
	pass

def resp6():
	# Chama a função para estimar o tempo necessário
	tempo_estimado = p6.PrevisaoPorBateria(pilhaBateriaTempo)
 
	# Exibe o tempo estimado para atingir o nível de bateria desejado
	print(f"Tempo estimado para atingir 0% de bateria: {tempo_estimado:.2f} segundos")

def resp7():
	print(amb.probabildadeProximoSerSupervisor(G.nodes(data=True)))

def resp8():
	pass
