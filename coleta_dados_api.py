import requests    

#função para enviar um arquivo#
def enviar_arquivo():
    #caminho do arquivo para upload#
    caminho = 'C:/_arquivo'
    #requisição para envio de arquivo para o site file.io (caminho especifico para cada API#
    requisicao = requests.post('https://url', files={'file': open(caminho ,'rb')})
    #transformando o arquivo binario enviando no formato json para poder ler depois#
    saida_requisicao = requisicao.json()
    print(saida_requisicao, '\n')
    url = saida_requisicao['link']
    print('\n arquivo enviado: link para acesso: ', url)

#função para baixar um arquivo com chave#
def enviar_arquivo_chave():
    #caminho do arquivo e a chave para upload#
    caminho = 'C:/_arquivo' 
    chave_acesso = 'XXXXXXX.XXXXXX-XXXXXX-XXXXXX-XXXXXX' #API KEY#
    #requisição para envio de arquivo para o site file.io (caminho especifico para cada API#
    requisicao = requests.post('https://url', 
    files={'file': open(caminho ,'rb')},
    headers={'Authorization': chave_acesso})
    #transformando o arquivo binario envido no formato json para poder ler depois#
    saida_requisicao = requisicao.json()
    print(saida_requisicao, '\n')
    url = saida_requisicao['link']
    print('\n arquivo enviado: link para acesso: ', url)
    #arquivo vai direto para minha conta com segurança#

#função para receber arquivo 
def receber_arquivo(file_url):
    #requisição para receber arquivo
    requisicao = requests.get(file_url)
    #salvando o arquivo 
    if requisicao.ok:
        with open ('arquivo_baixado.txt', 'wb') as file:
            file.write(requisicao.content)
        print('arquivo baixado com sucesso')
    else:
        print('erro ao baixar o arquivo:', requisicao.json())

#enviar_arquivo()
#enviar_arquivo_chave()
receber_arquivo('https://url')