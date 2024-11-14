#extraindo textos da internet#
import requests
import bs4

#criando as variáveis para execução#
url = 'https://url...'
requisicao = requests.get(url)
extracao = bs4.BeautifulSoup(requisicao.text,'html.parser')

#executando a extração#
print (extracao.text[:2000].strip())

#extrair somente os titulos h2 da url#
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Título: ', titulo)

#conta a quantidade de título e de parágrafos #
contar_titulo = 0
contar_paragrafo = 0
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulo = contar_titulo + 1
    elif linha_texto. name == 'p':
        contar_paragrafo = contar_paragrafo + 1
print (contar_titulo)
print (contar_paragrafo)

#Exibir somente os textos das tags 'h2' e 'p'#
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print ('titulo: \n', titulo)
    elif linha_texto. name == 'p':
        paragrafo = linha_texto.text.strip()
        print ('paragrafo: \n', paragrafo)

#exibir tags aninhadas#
for titulo in extracao.find_all('h2'):
    print('\n titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('texto do link: ', a.text.strip(), '| URL:', a['href'])