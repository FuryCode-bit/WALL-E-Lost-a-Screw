import time
import gender_guesser.detector as gender
import networkx as nx
# !!!!!!!!!!!!!!! NAO TE ESQUEÇAS DE COLOCAR COMENTARIOS !!!!!!!!!!!!!!!
pilha = []
pilha_resp1 = []

def identify_gender(name):
    d = gender.Detector()
    return d.get_gender(name)

'''
!!Esta parte que adicionei provavelmente vai ser modificada!!
Isto só serve como base para ver se funciona
Cenas para adicionar:
- Atributos para cada nodo: tipo de zona, coordenadas
- Forma de quando o robot descobre a zona atualizar o nodo
'''
# Ligacoes entre zonas
G = nx.Graph()
edge_list = [
    # Corredor 1
    (1, 0), (1, 2), (1, 5), (1, 3),
    # Corredor 2
    (2, 6), (2, 7),
    # Corredor 3
    (3, 4), (3, 12), (3, 13), (3, 14),
    # Corredor 4
    (4, 8), (4, 9), (4, 10), (4, 11)
    ]
G.add_edges_from(edge_list)

'''
Para encontrar o caminho mais curto o networkx já tem uma funcao implementada
print(nx.shortest_path(G, 6, 11)) o 6 e 11 são exemplos de como funciona -> to-do: implementar isto no futuro adaptado à pergunta
'''

def work(posicao, bateria, objetos):
    time.time()

    valid_prefixes = ['operário_', 'visitante_', 'supervisor_']

    if objetos and isinstance(objetos, list) and len(objetos) == 1:
        obj = objetos[0]
        for prefix in valid_prefixes:
            if obj.startswith(prefix) and obj not in pilha and obj[len(prefix):] not in pilha:
                obj_without_prefix = obj[len(prefix):]
                pilha.append(obj_without_prefix)
                if identify_gender(obj_without_prefix) == 'male':
                    pilha_resp1.append(obj)
                    print("pilha: ", pilha)
                    print("pilha_resp1: ", pilha_resp1)
                break   
    
    # print("dados: ", posicao, bateria, objetos)

def resp1():
    if len(pilha_resp1) >= 2:
        penultimate = pilha_resp1[-2]
        print("O penúltimo elemento é: ", penultimate)
    else:
        print("Não existe informação suficiente...")

def resp2():
    pass

def resp3():
    pass

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
