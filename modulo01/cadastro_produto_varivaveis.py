def exibir_produto():
    print (f"Nome: {nome_produto}")
    print (f"Descrição: {descricao_produto}")
    print (f"Ano Do Lançamento: {ano_lancamento_produto}")
    print (f"Valor do produto: {valor_produto}")
    print (f"Peso do produto: {peso_produto}")   

def retornar_produto():
    texto_saida = f"Nome: {nome_produto}\n Descrição: {descricao_produto} \n Ano Do Lançamento: {ano_lancamento_produto} \n Valor Do Produto: {valor_produto} \n Peso Do produto: {peso_produto}"
    return texto_saida     

print('CADASTRO DE PRODUTOS')

#INICIANDO A COLETA DE DADOS INFORMADOS PELO USUÁRIO
nome_produto = input("Por favor, informe o nome do produto: ")
descricao_produto = input("Por favor, informe a descrição do produto: ")
ano_lancamento_produto = int (input("Por favor informe o ano de lançamento do produto: "))
valor_produto = float(input("Por favor, informe o valor do produto em reais: "))
peso_produto = float(input("Por favor, informe o peso do produto em kg: "))

#EXIBIÇÃO SIMPLES DAS VARIÁVEIS 
# print(nome_produto)
# print(descricao_produto)
# print(ano_lancamento_produto)
# print(valor_produto)
# print(peso_produto)

#EXIBIÇÃO DAS VARIÁVEIS USANDO TEXTO
# print (f"Nome: {nome_produto}")
# print (f"Descrição: {descricao_produto}")
# print (f"Ano Do Lançamento: {ano_lancamento_produto}")
# print (f"Valor do produto: {valor_produto}")
# print (f"Peso do produto: {peso_produto}")

#exibir_produto()

