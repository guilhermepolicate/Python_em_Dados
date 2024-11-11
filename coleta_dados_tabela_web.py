#extraindo tabelas da internet com pandas#
import requests
import bs4
import pandas

#criando as variaveis para execução#
response = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history/?guccounter=1')
print (response.text[:600])

soup = bs4.BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

#imprindo o resultado#
print('Pandas: ')
url_dados = pandas.read_html('https://br.financas.yahoo.com/quote/%5EBVSP/history/?guccounter=1')
print(url_dados[0].head(10))
