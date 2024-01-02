'''
Função: A função tenta prever o gênero de uma pessoa encontrada com base no nome fornecido.

Recebe: O nome a ser analisado para determinar o gênero.

Retorna: Boleano: True -> caso o nome esteja na lista de nomes masculinos 
                  False -> caso o nome não esteja na lista de nomes masculinos 
'''

def identifica_genero(name):
    with open('./utils/listaNomes.txt', 'r') as file:
        for line in file:
            if line.lower().find(name.lower()) != -1:
                return True
    return False