

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_marcela = '12,Marcela,marc@marcela.com\n'

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo2:
    arquivo2.write(contato_marcela)

