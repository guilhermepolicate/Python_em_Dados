#baixando arquivos do MySQL para o Python#
import pymysql
import pandas as pd

#BAIXANDO COM TUPLA#
def conexao_mysql (host, user, password, db, table):
    #Variavel de conexao para informar os dados de busca#
    con = pymysql.connect(host=host, user=user, password=password, db=db)
    #conecta e salva os dados dentro de uma tupla#
    cursor = con.cursor()

    #executar a conexao#
    query = 'select * from' + table
    cursor.execute(query)

    #buscar resultado#
    resultado = cursor.fetchall()

    #exibir resultado#
    print('Tabela MySQL:')
    for linha in resultado:
        print (linha)

    #fechar a conexao#
    con.close()

#conexao_mysql(host='localhost', user='root', password='123456', db='restaurante', table='produtos')

#BAIXANDO COM DATAFRAME PANDAS#
#baixando do MySQL em formato XLSX#
def conexao_mysql (host, user, password, db, table):
    #Variavel de conexao para informar os dados de busca#
    con = pymysql.connect(host=host, user=user, password=password, db=db)
  
    #executar a conexao#
    query = 'select * from' + table
    df = pd.read_sql(query, con)

    #exibir resultado#
    print('Tabela MySQL: \n', df)
    
    #fechar a conexao#
    con.close()
    return df #retornado o Dataframe para converter o arquivo em excel#

#df = conexao_mysql(host='localhost', user='root', password='123456', db='restaurante', table='produtos')
#df.to_excel('produtos.xlsx') #convertendo o arquivo em excel#

#PARA FAZER LEITURA DE ARQUIVO DO EXCEL NO PYTHON#
#Baixando XLSX em SCV#
def conexao_excel(path):
    df = pd.read_excel(path)
    print('produtos.xlsx: \n')
    df.to_csv('produtos.csv')#convertendo o arquivo excel para csv e salvando na pasta do codigo#
#conexao_excel('produtos.xlsx')

#LER ARQUIVO EM CSV#
#Baixando em CVS e salvando em JSON#
def conexao_csv(path):
    df = pd.read_csv(path)
    print('produtos.csv: \n', df)

    #convertendo para json enquanto faz a leitura do arqui excel no formato csv#
    df.to_json('produtos.json')
#conexao_csv('produtos.csv')