import pandas as pd 

#Para funcionar precisa executar "pip install pandas" e "pip install openpyxl" 

#importa a tabela 
x = pd.read_excel("202110_CPGF.csv", engine='openpyxl')
#Adiciona a coluna count
x["COUNT"] = 1

#--------------Soma total------------------- 
valor_transacao = x ["VALOR TRANSAÇÃO"]
print()
print(f'Qual a soma total das movimentações utilizando o CPGF? {sum(valor_transacao):.2f}') 
print('.')
print('.')
print('.')
print('.')
print('.')

#----Soma das movimentações sigilosas----- 
transacao_sigilosa = x["TRANSAÇÃO"] == 'Informações protegidas por sigilo'
print(f'Qual a soma das movimentações sigilosas? {sum(valor_transacao[transacao_sigilosa]):.2f}')
print('.')
print('.')
print('.')
print('.')
print('.')

#Orgão que mais realizou movimentações sigilosas e o seu valor somado
colunas = ["NOME ÓRGÃO", "VALOR TRANSAÇÃO","COUNT"] 
nome_orgao = x[transacao_sigilosa][colunas].groupby(["NOME ÓRGÃO"]).sum()
print('Qual o Órgão que mais realizou movimentações sigilosas no período e qual o valor (somado)?')
print(nome_orgao.sort_values(by = ["COUNT"], ascending=False).head(1))
print('.')
print('.')
print('.')
print('.')
print('.')
#O nome do portador que mais realizou saques no período? Qual a soma dos saques realizada por ele? Qual o nome do Órgão desse portador?
colunas = ["NOME ÓRGÃO","VALOR TRANSAÇÃO","NOME PORTADOR","COUNT"] 
nome_portador = x[x["TRANSAÇÃO"] == 'SAQUE CASH/ATM BB'][colunas].groupby(["NOME PORTADOR", "NOME ÓRGÃO"]).sum()
print('O nome do portador que mais realizou saques no período? Qual a soma dos saques realizada por ele? Qual o nome do Órgão desse portador?')
print(nome_portador.sort_values(by = ["COUNT"], ascending=False).head(1))
print('.')
print('.')
print('.')
print('.')
print('.')

#Qual o nome do favorecido que mais recebeu compras realizadas utilizando o CPGF?
print('Qual o nome do favorecido que mais recebeu compras realizadas utilizando o CPGF?')
colunas = ["NOME FAVORECIDO","COUNT"] 
nome_favorecido = x[x["TRANSAÇÃO"] == 'COMPRA A/V - R$ - APRES'][colunas].groupby(["NOME FAVORECIDO"]).sum()
print(nome_favorecido.sort_values(by = ["COUNT"], ascending=False).head(1))






 






