from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from utils.ambiente import *
import numpy as np
import time

# Lista com o caminho feito pelo WALL-E
posicoes = []

# Variáveis auxiliares
prevPos = 0
distanciaAcc = 0

# Lista com nodes visitados pelo WALL-E
listaVisitas = [0]

'''
Função: A função tem serve para constuir uma lista de tuplos (bateria, tempo) 
para facilitar na construção da curva. 

Recebe: valor de bateria para constuir uma curva para fazer a previsão através 
de uma lista de tuplos (bateria, tempo).
'''

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
Função: A função serve para constuir uma lista de tuplos (distancia (acumulada), tempo) 
para facilitar na construção da regressão linear. 

Recebe: Posição atual do WALL-E no grafo para constuir uma curva para fazer a previsão através 
de uma lista de tuplos (bateria, tempo)
'''

def updateListaVisitas(posAtual):
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
		distanciaAcc += distancia(caminho)
		
        #print("posicoes: ", posicoes)
		#print("distanciaAcc: ", distanciaAcc)
            
		pilhaDistanciaAccTempo.append((distanciaAcc, tempoDecorrido))

'''
Função: A função constrói um curva dado uma lista de tuplos (bateria, tempo) 
para prever o valor do tempo até ficar sem bateria. 

Recebe: lista de tuplos (bateria, tempo)

Retorna: Estimativa do tempo previsto (em segundos) para ficar sem bateria
'''

def PrevisaoPorBateria():
    global pilhaBateriaTempo

    def non_linear_function(x, a, b, c):
        return a * x ** 2 + b * x + c
 
    # Separar os dados em níveis de bateria e tempos
    battery_levels, elapsed_time = zip(*pilhaBateriaTempo)
 
    # Ajuste da curva aos dados
    params, covariance = curve_fit(non_linear_function, battery_levels, elapsed_time)
 
    # Coeficientes a, b, c
    a, b, c = params
 
    # Estimativa do tempo para o nível de bateria requerido
    time_last = - (0 ** 2) / a + 0 * b + c
 
    return time_last
 
'''
Função: A função constrói um Regressão Linear dado uma lista de tuplos (distancia (acumulada), tempo) 
para prever o valor do tempo até chegar ao escritório. 

Recebe: lista de tuplos (distancia (acumulada), tempo)

Retorna: Estimativa do tempo previsto (em segundos) para chegar ao escritório
'''

def PrevisaoTempoporDistancia(distanciaPrever):
    
    global pilhaDistanciaAccTempo
       
    distancias, tempos = zip(*pilhaDistanciaAccTempo)

    #converte para arrays
    x = np.array(distancias).reshape(-1, 1)
    y = np.array(tempos)

    modelo = LinearRegression()
    modelo.fit(x,y)

    tempo_predict = modelo.predict([[distanciaPrever]])

    return tempo_predict[0]
