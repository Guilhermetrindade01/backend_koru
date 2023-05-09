def retornar_produto(produto):
    texto_saida = f"Nome: {produto['nome']}\n Descrição: {produto['descricao']} \n Lançamento: {produto['lancamento']} \n Valor: {produto['valor']} \n Peso: {produto['peso']}"
    return texto_saida     
    
produto_principal = {}

produto_principal ["nome"] = input("Por favor, informe o nome do produto: ")
produto_principal ["descricao"] = input("Por favor, informe a descrição do produto: ")
produto_principal ["lancamento"] = int (input("Por favor informe o ano de lançamento do produto: "))
produto_principal ["valor"] = float(input("Por favor, informe o valor do produto em reais: "))
produto_principal ["peso"] = float(input("Por favor, informe o peso do produto em kg: "))

print(retornar_produto(produto_principal))