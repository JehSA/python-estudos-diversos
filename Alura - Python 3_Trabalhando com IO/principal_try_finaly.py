
try:
    arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

    for linha in arquivo_contatos:
        print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado.')

except PermissionError:
    print('Sem permissão de escrita.')

finally:
    arquivo_contatos.close()
