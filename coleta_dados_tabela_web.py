#extraindo tabelas da internet com pandas#
import requests
import bs4
import pandas

#criando as variaveis para execução#
response = requests.get('https://url...')
print (response.text[:600])

soup = bs4.BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

#imprindo o resultado#
print('Pandas: ')
url_dados = pandas.read_html('https://url...')
print(url_dados[0].head(10))
