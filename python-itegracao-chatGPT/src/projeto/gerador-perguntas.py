
from openai import OpenAI
import json

client = OpenAI(
    api_key = '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'
)

def gerar_questao(topico):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": """"
                Você é um desenvolvedor muito experiente com conhecimento em diferentes
                stacks e conceitos teóricos sobre programação e engenharia de software.
                Você está trabalhando em um processo de contratação e seu trabalho agora é escrever perguntas
                para uma entrevista. Cada pergunta deve ter quatro respostas possíveis e uma delas
                deve ser correta. Escreva essas perguntas no seguinte formato:
                '{"pergunta": "Pergunta", "opcoes": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"], "certa": "Opção 1"}'
            """
        }, {
            "role": "user",
            "content": f"Gere uma questão sobre {topico}."
        }]   
    )

    conteudo = resposta.choices[0].message.content
    return json.loads(conteudo)


pontos = 0
topico = input("Sobre qual tópico você quer responder? ")

while topico:
    print("Carregando...")
    questao = gerar_questao(topico)
    print(questao['pergunta'])

    for i, opcao in enumerate(questao['opcoes'], start=1):
        print(f"{i}) {opcao}")

    resposta = int(input("Escolha uma opção [1-4]: ")) - 1

    escolhida = questao['opcoes'][resposta].lower()
    certa = questao['certa'].lower()

    if escolhida == certa:
        pontos += 1
        print(f'Você acertou! Agora você tem {pontos} pontos\n')
    else:
        print(f'Você errou! A resposta correta era: "{certa}"\n')

    continuar = input("Quer continuar? (S/N) ")

    if continuar.lower() == 'n':
        break

print('Aplicação fechada!!!')
