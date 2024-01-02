"""
45703, Marco Bernardes
46811, Ana Lúcia Ferreira
"""
 
'''
PERGUNTAS:
1. DONE
2. DONE
3. DONE
4. DONE
5. DONE
6. DONE
7. DONE
8. DONE
'''
 
import time
import networkx as nx
from utils.utils import *
from utils.previsoes import *
from utils.ambiente import *
from utils.probabilidades import *

# Lista com os objetos que o robot teve contacto
pilha = []

# Lista com as pessoas que o robot teve contacto
encontros = []

# Número da zona atual
posAtual = 10

G = criarGrafo()
nodeAtual = G.nodes[posAtual]

tempoDecorrido = time.time()

# Tempo inicial (em segundos) em que a bateria se encontrava a 100%
tempo100 = time.time()
tempoDecorrido = time.time()

# Criar Rede Bayesiana
criarRedeBayesiana()
 
'''
Esta função identifica cada objeto em que o robot entra em contacto e vai inserindo numa pilha.
Para identificar um humano é usado uma lista de prefixos com os títulos disponíveis. 
Assim sempre que o robot entrar em contacto com um humano de género masculino vai inserir apenas o seu nome numa pilha de nome pilha_resp1
(Nomear a pilha de male_pilha ou obj_pessoas poderia deixar os humanos um tanto... objetificados ou confusos com outras coisas, então optei por um nome mais simples! 🤖)
'''

def work(posicao, bateria, objetos):
 
	global tempo_final
	global tempo_decorrido
 
	global posAtual
	global nodeAtual
 
	# Deteta se a posição atual é diferente dos pontos extremos da zona atual se sim, procura a nova zona
	if posicao[0] <= nodeAtual["coord"][0][0] or posicao[0] >= nodeAtual["coord"][1][0] \
	or posicao[1] <= nodeAtual["coord"][0][1] or posicao[1] >= nodeAtual["coord"][1][1]:
		posAtual, nodeAtual = mudarZona(posicao, posAtual)
		updateListaVisitas(posAtual)
		
	person_prefixes = ['operário_', 'visitante_', 'supervisor_']
	operario_prefix = 'operário_'
	supervisor_prefix = 'supervisor_'
	maquina_prefix = 'máquina_'

	if objetos and isinstance(objetos, list) and len(objetos) == 1:
		obj = objetos[0]
 		# Se o objeto é uma zona e o tipo da zona atual ainda não tiver sido alterado
		if obj.startswith("zona_") and compTipoZona(nodeAtual, "sem identificação"):
			nodeAtual["tipo"] = obj[len("zona_"):]
		elif obj.startswith(maquina_prefix):
			maquina_value = obj[len(maquina_prefix):]
			if maquina_value not in nodeAtual["maquinas"]:
				nodeAtual["maquinas"].append(maquina_value)
		elif obj.startswith(operario_prefix):
			operario_value = obj[len(operario_prefix):]
			if operario_value not in nodeAtual["operarios"]:
				nodeAtual["operarios"].append(operario_value)
		elif obj.startswith(supervisor_prefix):
			supervisor_value = obj[len(supervisor_prefix):]
			if supervisor_value not in nodeAtual["supervisores"]:
				nodeAtual["supervisores"].append(supervisor_value)
		else:
			for prefix in person_prefixes:
				if obj.startswith(prefix) and obj not in pilha and obj[len(prefix):] not in pilha:
					obj_without_prefix = obj[len(prefix):]
					pilha.append(obj_without_prefix)
					if identifica_genero(obj_without_prefix) == True:
						encontros.append(obj)
						#print("pilha: ", pilha)
						#print("encontros: ", encontros)
						#pilha.append(obj)
					break
 
	updateListaBateriaTempo(bateria)
	givePosicao(posicao)
	# print("dados: ", posicao, bateria, objetos, time.perf_counter())
 

def resp1():
	''' Qual foi a penúltima pessoa do sexo masculino que viste? '''

	if len(encontros) >= 2:
		penultimo = encontros[-2]
		print("O penultimo elemento é: ", penultimo)
	else:
		print("Não existe informação suficiente")
 
def resp2():
	''' Em que tipo de zona estás agora? '''

	print("A zona", posAtual, "é do tipo", nodeAtual["tipo"])
 
def resp3():
	''' Qual o caminho para a zona de empacotamento? '''

	if compTipoZona(nodeAtual, "empacotamento"):
		print("Já estou na zona de empacotamento")
	else:
		dest = procurarTipoZona("empacotamento")
		if dest == -1:
			print("Ainda não sei a localização da zona de empacotamento")
		else:
			# nx.shortest_path devolve o caminho composto apenas pelos numeros das zonas
			print("O caminho desde a zona", posAtual, "até a zona de empacotamento", dest, "é:", nx.shortest_path(G, posAtual, dest))
 
def resp4():
	''' Qual a distância até ao laboratório? '''

	if compTipoZona(nodeAtual, "laboratório"):
		print("Já estou no laboratório")
	else:
		dest = procurarTipoZona("laboratório")
		if dest == -1:
			print("Ainda não sei a localização do laboratório")
		else:
			caminho = nx.shortest_path(G, posAtual, dest) # Encontrar caminho
			distTotal = distancia(caminho)
			print("A distância desde a zona", posAtual, "até o laboratório", dest, "é", distTotal)
 
def resp5():
	''' Quanto tempo achas que demoras a ir de onde estás até ao escritório? '''
	
	if compTipoZona(nodeAtual, "escritório"):
		print("Já estou no escritório")
	else:
		dest = procurarTipoZona("escritório")
		if dest == -1:
			print("Ainda não sei a localização do escritório")
		else:
			caminho = nx.shortest_path(G, posAtual, dest) 
			distTotal = distancia(caminho)
			#print("A distância desde a zona", posAtual, "até o escritório", dest, "é", distTotal)

			print("A previsão de chegada ao escritório é de ", PrevisaoTempoporDistancia(distTotal), "segundos")
		
def resp6():
	''' Quanto tempo achas que falta até ficares sem bateria? '''
	try:
		# Chama a função para estimar o tempo necessáriopara ficar sem bateria
		tempo_estimado = PrevisaoPorBateria()
	 
		# Exibe o tempo estimado para atingir o nível de bateria desejado
		print(f"Tempo estimado para atingir 0% de bateria: {tempo_estimado:.2f} segundos")
	except ValueError:
		print("Não existem dados suficientes para fazer previsão")
def resp7():
	''' Qual é a probabilidade da próxima pessoa a encontrares ser um supervisor? '''

	try:
		print("A P(Supervisor) =", probabilidadeProximoSerSupervisor(G))
	except ZeroDivisionError:
		print("Não existe informação suficiente no mundo conhecido!")
		
def resp8():
	''' Qual é a probabilidade de encontrar um operário numa zona se estiver lá uma 
	máquina mas não estiver lá um supervisor? '''
	
	res = calcularProbabilidade(G,{'maquina': 1, 'supervisor': 0}, 'operario', 1) 
	if res == -1:
		print("Não existe informação suficiente no mundo conhecido!")
	else:
		print("A P(Operário|Máquina,!Supervisor) =", res)

