print("Bem-Vindo!")

while True:
    pergunta = input("Quer começar? (S/N): ").upper()
    if pergunta == "S":
        print("Começando...\n")
        pontuacao = 0

        print("Em que continente fica o Egito?\n a) Ásia\n b) África\n c) Europa")
        resposta = input("Resposta: ").upper()
        if resposta == "B":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Quem pintou a obra 'Mona Lisa'?\n a) Leonardo da Vinci\n b) Michelangelo\n c) Pablo Picasso")
        resposta = input("Resposta: ").upper()
        if resposta == "A":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Qual é o menor país do mundo?\n a) Vaticano\n b) Mônaco\n c) Malta")
        resposta = input("Resposta: ").upper()
        if resposta == "A":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Qual oceano banha a costa do Brasil?\n a) Atlântico\n b) Pacífico\n c) Índico")
        resposta = input("Resposta: ").upper()
        if resposta == "A":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Quem foi o cientista que propôs a teoria da relatividade?\n a) Isaac Newton\n b) Albert Einstein\n c) Galileu Galilei")
        resposta = input("Resposta: ").upper()
        if resposta == "B":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Qual é o maior osso do corpo humano?\n a) Tíbia\n b) Coluna vertebral\n c) Fêmur")
        resposta = input("Resposta: ").upper()
        if resposta == "C":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Em que ano o homem pisou na Lua pela primeira vez?\n a) 1965\n b) 1969\n c) 1972")
        resposta = input("Resposta: ").upper()
        if resposta == "B":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Qual país é conhecido como 'a terra do sol nascente'?\n a) China\n b) Japão\n c) Coreia do Sul")
        resposta = input("Resposta: ").upper()
        if resposta == "B":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Qual é o idioma oficial do Canadá, além do inglês?\n a) Francês\n b) Espanhol\n c) Alemão")
        resposta = input("Resposta: ").upper()
        if resposta == "A":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print("Qual destes elementos químicos é um gás nobre?\n a) Hélio\n b) Oxigênio\n c) Nitrogênio")
        resposta = input("Resposta: ").upper()
        if resposta == "A":
            print("✅")
            pontuacao += 1
        else:
            print("❌")

        print(f"\nQuiz acabou... Pontuação final: {pontuacao}/10")
        break

    elif pergunta == "N":
        print("OK 😐 Até a próxima!")
        break
    else:
        print("Digite apenas 'S' ou 'N'!")
