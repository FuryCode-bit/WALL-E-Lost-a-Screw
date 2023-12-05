import time
import gender_guesser.detector as gender

pilha = []
pilha_resp1 = []

def identify_gender(name):
    d = gender.Detector()
    return d.get_gender(name)

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