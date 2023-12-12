import time
import gender_guesser.detector as gender
import networkx as nx


# !!!!!!!!!!!!!!! NAO TE ESQUEÇAS DE COLOCAR COMENTARIOS !!!!!!!!!!!!!!!
  # Comentários? Eles foram adicionados, mas acabaram por fugir para uma festa de binários e agora estão a meter conversa com os bytes! 🕺🔤


pilha = []
Melancia = []

'''
# Esta função é como uma bola de cristal 🎱: ela prevê o gênero do humanóide com base no nome!
# Suponho que no estado em que estamos a seguir enquanto sociedade, seja algo que deixe de funcionar nos próximos anos.
# Mas acredito que num curto espaço de 2 meses, esta função seja suficiente.
'''

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

'''
Esta função identifica cada objeto em que o WALL-E entra em contacto e vai inserindo numa pilha.
Para identificar um humano é usado uma lista de prefixos com os títulos disponíveis. 
Assim sempre que o WALL-E entrar em contacto com um humano de género masculino vai inserir apenas o seu nome numa pilha de nome pilha_resp1
(Nomear a pilha de male_pilha ou obj_pessoas poderia deixar os humanos um tanto... objetificados ou confusos com outras coisas, então optei por um nome mais simples! 🤖)
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
  					Melancia.append(obj)
  					print("pilha: ", pilha)
  					print("Melancia: ", Melancia)
  					#pilha.append(obj)
  				break
 
	#print("print: ", posicao, bateria, objetos) 
    
    # print("dados: ", posicao, bateria, objetos)

'''
Esta função começa por verificar quantas pessoas de género masculino o WALL-E esteve em contacto.
Se apenas teve em contacto com uma (ou com nenhuma) ele indica que não possui informação suficiente para resolver o problema.
Se tiver toda a informação necessária, vai indicar o nome da penúltima pessoa que encontrou!
'''

def resp1():
  	if len(Melancia) >= 2:
  		penultimate = Melancia[-2]
  		print("O penultimo elemento é: ", penultimate)
  	else:
  		print("Não existe informação suficiente")

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
