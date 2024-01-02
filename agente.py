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
4. DONE
5. DONE (~)
6. DONE
7. DONE (I THINK)
8. DONE

#TODO -> Arrumar melhor o código e simplificar um pouco (Marco)
'''
 
import time
import networkx as nx
from utils import p1, previsoes as p, ambiente as amb, probabilidades as pb
 
pilha = []
encontros = []
 
pilhaBateriaTempo = []
listaVisitas = [0]
 
# Variáveis para o grafo
posAtual = 10 # Número da zona atual
G = amb.criarGrafo()
nodeAtual = G.nodes[posAtual]
 
tempoDecorrido = time.time()
tempo100 = time.time()

# Criar Rede Bayesiana
pb.criarRedeBayesiana()

ultimaPosicao = None
pilhaDistanciaAccTempo = []
posicoes = []
prevPos = 0
distanciaAcc = 0
'''
# Debug Function
def saveFile(pair):
	with open("pilha.txt", "a") as file:
		file.write(f"{pair}\n")
'''		
# Funções a serem removidas brevemente
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
        
def updateListaVisitas():
	global tempoDecorrido, tempo100, listaVisitas, prevPos, distanciaAcc, posicoes, pilhaDistanciaAccTempo
	if(len(posicoes) > 0):
		if posicoes[-1] != posAtual:
				prevPos = posicoes[-1]
				posicoes.append(posAtual)
	else:
		posicoes.append(posAtual)
		
	if prevPos != 0:
		tempoDecorrido = time.time() - tempo100
		caminho = [prevPos, posAtual]
		distanciaAcc += amb.distancia(caminho)
		#print("posicoes: ", posicoes)
		#print("distanciaAcc: ", distanciaAcc)
		#saveFile((amb.distancia(caminho), distanciaAcc, tempoDecorrido))
		pilhaDistanciaAccTempo.append((distanciaAcc, tempoDecorrido))
 
'''
Esta função identifica cada objeto em que o WALL-E entra em contacto e vai inserindo numa pilha.
Para identificar um humano é usado uma lista de prefixos com os títulos disponíveis. 
Assim sempre que o WALL-E entrar em contacto com um humano de género masculino vai inserir apenas o seu nome numa pilha de nome pilha_resp1
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
		posAtual, nodeAtual = amb.mudarZona(posicao, posAtual)
		updateListaVisitas()
		
	person_prefixes = ['operário_', 'visitante_', 'supervisor_']
	operario_prefix = 'operário_'
	supervisor_prefix = 'supervisor_'
	maquina_prefix = 'máquina_'
	if objetos and isinstance(objetos, list) and len(objetos) == 1:
		obj = objetos[0]
 		# Se o objeto é uma zona e o tipo da zona atual ainda não tiver sido alterado
		if obj.startswith("zona_") and amb.compTipoZona(nodeAtual, "sem identificação"):
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
					if p1.identifica_genero(obj_without_prefix) == True:
						encontros.append(obj)
						#print("pilha: ", pilha)
						#print("encontros: ", encontros)
						#pilha.append(obj)
					break
 
	updateListaBateriaTempo(bateria)
	amb.givePosicao(posicao)
	# print("dados: ", posicao, bateria, objetos, time.perf_counter())
 
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
			# nx.shortest_path devolve o caminho composto apenas pelos numeros das zonas
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
	if amb.compTipoZona(nodeAtual, "escritório"):
		print("Já estou no escritório")
	else:
		dest = amb.procurarTipoZona("escritório")
		if dest == -1:
			print("Ainda não sei a localização do escritório")
		else:
			caminho = nx.shortest_path(G, posAtual, dest) 
			distTotal = amb.distancia(caminho)
			print("A distância desde a zona", posAtual, "até o laboratório", dest, "é", distTotal)
			
			print("A previsão de chegada ao escritório é de ", p.PrevisaoTempoporDistancia(distTotal, pilhaDistanciaAccTempo), "segundos")
 
def resp6():
	global pilhaBateriaTempo
	
	# Chama a função para estimar o tempo necessário
	tempo_estimado = p.PrevisaoPorBateria(pilhaBateriaTempo)
 
	# Exibe o tempo estimado para atingir o nível de bateria desejado
	print(f"Tempo estimado para atingir 0% de bateria: {tempo_estimado:.2f} segundos")
 
def resp7():
	res = pb.calcularProbabilidade(G,{}, 'supervisor', 1) 
	if res == -1:
		print("Não existe informação suficiente no mundo conhecido!")
	else:
		print("A P(Supervisor) =", res)
		
def resp8():
	def resp8():
	res = pb.calcularProbabilidade(G,{'maquina': 1, 'supervisor': 0}, 'operario', 1) 
	if res == -1:
		print("Não existe informação suficiente no mundo conhecido!")
	else:
		print("A P(Operário|Máquina,!Supervisor) =", res)

