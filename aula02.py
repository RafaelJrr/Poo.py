# idade = 30 
# tem_cartao = True

# # Inicializa a variável continuar para controlar o loop
# continuar = True

# # Loop while para continuar verificando as condições
# while continuar:
#     # Condição Para Verificar a idade
#     if idade >= 18:
#         # Condição Para Verificar se o Usuário tem Cartão
#         if tem_cartao:
#             print("Você pode comprar o produto.")
#         else:
#             print("Você pode comprar o produto sem um cartão.")
#     else:
#         print("Você é menor de idade e não pode comprar o produto.")

#     # Condição de saída do loop
#     resposta = input("Deseja verificar novamente? (sim/não): ").strip().lower()
#     if resposta != 'sim':
#         continuar = False

# print("Programa finalizado.")


# import array as np

# Cria um array numpy
arr = [1, 2, 3, 4, 5]

# Itera sobre os elementos do array com índices
for indice, elemento in enumerate(arr):
    print(f"Índice {indice}: {elemento}")


# Cria uma tupla
tupla = (1, 2, 3, 4, 5)

# Itera sobre os elementos da tupla com índices
for indice, elemento in enumerate(tupla):
    print(f"Índice {indice}: {elemento}")


#Criando um dicionário com alguns dados 
aluno = { 
    "nome": "João", 
    "idade": 20, 
    "curso": "Engenharia", 
    "notas": [9, 8, 7.5, 10] 
    }
# Acessando elementos do dicionário
print("Nome do aluno:", aluno["nome"]) # Acessa o valor associado à chave "nome" 
print("Idade do aluno:", aluno["idade"]) # Acessa o valor associado à chave "idade"