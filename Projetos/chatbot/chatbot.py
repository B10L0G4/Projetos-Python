# 1- criar ambiente virtual - python -m venv ./env (cria o ambiente virtual)
# > > 2- ativar o ambiente virtual - **source ./env/Scripts/activate** (ativa o ambiente virtual no bash)
# > > 2.1 - ativar o ambinete vitual no windows - **.\env\Scripts\Activate** (ativa o ambiente virtual no cmd)
# > > 3- desativar o ambiente virtual - deactivate (desativa o ambiente virtual no bash)
# > > Desenvolvimento Web com Python , Django ou Flask
# > > 1- instalar o django - pip install django
# > > 2- verificando a versão do django - python -m django --version
# > > 3- _Guardar dependencias do projeto em um arquivo - pip freeze > requirements.txt , para que
# outras pessoas possam instalar as dependencias do projeto nas versões instaladas no momento da criação do arquivo.
# Conforme as dependencias forem sendo atualizadas, o arquivo deve ser atualizado também._


from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')
