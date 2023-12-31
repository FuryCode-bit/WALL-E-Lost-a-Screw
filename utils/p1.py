def identifica_genero(name):
    """
    Esta função tenta prever o gênero de um humanoide com base no nome fornecido.

    Args:
        name (str): O nome a ser analisado para determinar o gênero.

    Returns:
        bool: Retorna True se o nome estiver na lista de nomes conhecidos, False caso contrário.
    """
    with open('./utils/listaNomes.txt', 'r') as file:
        for line in file:
            if line.lower().find(name.lower()) != -1:
                return True

    return False