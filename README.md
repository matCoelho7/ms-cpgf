# ms-cpgf
Processo Seletivo

A - Com suas palavras explique o que é lavagem de dinheiro?
Lavagem de dinheiro consiste em encobrir a origem de dinheiro ilegal. 
ela consiste em um esquema para fazer parecer que recursos obtidos por meio de atividades ilegais, 
vieram de atividades 'legais'.

B - O que é Cartão de Pagamento do Governo Federal (CPGF), e qual a sua finalidade.
Cartão de Pagamento do Governo Federal (CPGF)
é um meio de pagamento utilizado pelo governo que funciona de forma similar ao cartão de crédito que utilizamos em nossas vidas, 
porém dentro de limites e regras específicas. O governo utiliza o CPGF para pagamentos de despesas próprias, que possam ser enquadradas como suprimento de fundos.

C – Quem pode utilizar o CPGF?
Pessoas que trabalham para órgãos do governo Federal

D – Qual a URL onde é possível fazer o download dos arquivos do CPGF?
https://www.portaltransparencia.gov.br/download-de-dados/cpgf

E – Qual a URL da paǵina com a descrição dos campos (ou dicionário de dados) da CPGF?
https://www.portaldatransparencia.gov.br/pagina-interna/603393-dicionario-de-dados-cpgf

F - É possível identificar o nome e o documento do portador do CPGF, em todas as
movimentações ou há movimentações onde não é possível identificar o portador?
Existem movimentações que são sigilosas e não é possível identificar.

G – É possível identificar o Órgão do portador do CPGF?
Sim, mas só as movimentações que não são sigilosas.

H - Qual o nome do Órgão cujo código é 20402?
Agência Espacial Brasileira

I - É possível identificar o Nome e Documento (CNPJ) dos favorecidos pela utilização do
CPGF?
Sim, mas só as movimentações que não são sigilosas.

J - É possível identificar a data e o valor das movimentações financeiras do CPGF, em
todas as movimentações? Ou há movimentações onde não é possível identificar as datas e
ou valores?
Existem movimentações que são sigilosas e não é possível identificar.

K (código) – Qual a soma total das movimentações utilizando o CPGF?
O total é de 5619007.95

L (código) – Qual a soma das movimentações sigilosas?
a soma das movimentações sigilosas são 3108731.15

M (código) – Qual o Órgão que mais realizou movimentações sigilosas no período e qual o
valor (somado)?
O órgão que mais fez movimentações sigilosas foi o Departamento de Polícia Federal e o valor somado das movimentações foi de 1207131.92  

N (código) – Qual o nome do portador que mais realizou saques no período? Qual a soma
dos saques realizada por ele? Qual o nome do Órgão desse portador?
O nome do portador: RAFAEL FERREIRA COSTA a soma dos saques: 4520.0 e o órgão desse portador é Instituto Chico Mendes de Conservação da Biodiversidade 


O (código) – Qual o nome do favorecido que mais recebeu compras realizadas utilizando o
CPGF?
MERCADOPAGO.COM REPRESENTACOES LTDA.

P - Descreva qual a abordagem utilizada para desenvolver o código para os ítens de K a O.

Para resolver os exercícios optei por utilizar python e com a biblioteca pandas consegui exportar o arquivo csv e assim podendo manipular as linhas e as colunas do arquivo.

K - Peguei todas as linhas da coluna “VALOR TRANSAÇÃO” e utilizei o metodo sum() para realizar a soma.

L - Fiz um filtro na tabela para retorna todas as transações que fossem iguais a "Informações protegidas por sigilo”, e com a tabela filtrada utilizei o método sum() na coluna VALOR TRANSAÇÃO.

M - Fiz um filtro na tabela para retorna todas as "TRANSAÇÃO" que fossem iguais a "Informações protegidas por sigilo", no python adicionei uma coluna na tabela "COUNT" = 1, fiz um groupby pelo "NOME ÓRGÃO" e somei os campos COUNT e o VALOR DA TRANSAÇÃO, somando o campo COUNT descobri quantas movimentações sigilosas cada órgão realizou e ordenei para que me trouxesse o maior “COUNT”, assim descobrindo quem mais vez movimentações sigilosas e o seu valor somado.

N - Fiz um filtro na tabela para retorna todas as "TRANSAÇÃO" que fossem iguais a "SAQUE CASH/ATM BB", fiz um groupby pelo "NOME PORTADOR" e o "NOME ORGÃO" e somei os campos COUNT e o VALOR DA TRANSAÇÃO, somando o campo COUNT descobri quantos saques foram realizados por cada portador e o seu órgão, e ordenei para que me trouxesse o maior “COUNT”, assim descobrindo quem mais realizou saques e o seu valor somado e o nome do órgão.     

O - Fiz um filtro na tabela para retorna todas as "TRANSAÇÃO" que fossem iguais a "COMPRA A/V - R$ - APRES", realizei um groupby com o "NOME FAVORECIDO" e somei os campos COUNT somando o campo COUNT descobri quantas compras foram realizados para cada favorecido, e ordenei para que me trouxesse o maior “COUNT”, assim descobrindo quem mais recebeu compras utilizando o CPGF
