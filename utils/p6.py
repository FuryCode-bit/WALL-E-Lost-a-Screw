from scipy.optimize import curve_fit
 
def PrevisaoPorBateria(data_points):
    """
    Estima o tempo para o robot ficar sem bateria.
 
    Args:
        data_points (list[tuple[float, float]]): Lista de tuplas contendo os níveis de bateria e os tempos correspondentes.
 
    Returns:
        float: Tempo estimado para atingir o nível de bateria especificado.
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
