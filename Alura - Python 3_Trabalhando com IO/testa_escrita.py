

arquivo_contatos = open('dados/contatos-escrita.csv', 'a+', encoding='latin_1')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Denise,deni@deni.com\n'
            '13,Tamires,tami@tami.com.br\n'
            '14,Rafaela,rafa@rafa.com\n']

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()

arquivo_contatos.seek(28)
arquivo_contatos.write('12, Denise, deni@deni.com\n'.upper())
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)
