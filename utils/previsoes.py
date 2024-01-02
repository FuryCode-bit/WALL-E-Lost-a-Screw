from sklearn.linear_model import LinearRegression
import numpy as np
 
from scipy.optimize import curve_fit
from utils import ambiente as amb
 
def PrevisaoPorBateria(data_points):
 
    """
    Args:
        data_points: lista de tuplos (bateria, tempo)
 
    Returns:
        float: Estimativa do tempo previsto para acabar a bateria
    """
    
    def non_linear_function(x, a, b, c):
        return a * x ** 2 + b * x + c
 
    # Separar os dados em níveis de bateria e tempos
    battery_levels, elapsed_time = zip(*data_points)
 
    # Ajuste da curva aos dados
    params, covariance = curve_fit(non_linear_function, battery_levels, elapsed_time)
 
    # Coeficientes a, b, c
    a, b, c = params
 
    # Estimativa do tempo para o nível de bateria requerido
    time_last = - (0 ** 2) / a + 0 * b + c
 
    return time_last
 
def PrevisaoTempoporDistancia(distanciaPrever, pilhaDistanciaAccTempo):
 
	"""
    Args:
        distanciaPrever: Distância do ponto em que o robot se encontra até ao escritório;
        pilhaDistanciaAccTempo: lista de tuplos (distancia acumulada, tempo)
 
    Returns:
        float: Estimativa do tempo previsto para chegar ao escritório 
        desde o ponto em que o robot se encontra
    """
 
	distancias, tempos = zip(*pilhaDistanciaAccTempo)
 
	#converte para arrays
	x = np.array(distancias).reshape(-1, 1)
	y = np.array(tempos)
 
	modelo = LinearRegression()
	modelo.fit(x,y)
 
	tempo_predict = modelo.predict([[distanciaPrever]])
 
	return tempo_predict[0]
