def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha      #desempacotamento

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos