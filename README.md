# Sentimento-Probabilidade
Objetivo do projeto:
Probabilidade de uma mensagem ser positiva (1) ou negativa (0)

Descrição do projeto:
Primeiro projeto de análise de sentimento onde uma mensagem é enviada a um modelo treinado para que se tenha um retorno com a probabilidade de o texo ser positivo.
Solução pensada para ferramentas de pesquisa de satisfação em diversos seguimentos.

Interpretação do resultado:
p (probabilidade); quanto mais próximo de 1.0 for o resultado maior é a probabilidade da mensagem ser positiva. Quanto mais próximo de 0 (zero) maior a chance de ser uma mensagem negativa.

Parâmetros:
entrada: mensagem
saída: mensagem, p (probabilidade)

Url: https://heroku-aval-sentiment-prob.herokuapp.com/?mensagem="digite_sua_mengasm_aqui"

Exemplo:
https://heroku-aval-sentiment-prob.herokuapp.com/?mensagem="O lanche é maravilhoso e a batata rústica então nem se fala, o atendimento tbm é muito bom!"

retorrno:
{"mensagem": "\"O lanche \u00e9 maravilhoso e a batata r\u00fastica ent\u00e3o nem se fala, o atendimento tbm \u00e9 muito bom!\"", "p": 0.9299146240066799}
