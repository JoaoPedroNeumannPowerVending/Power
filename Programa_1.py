# Inicialização das variáveis
brancos = 0
nulos = 0
votos_validos = 0
eleitores = 0

# Loop de votação
while True:
    # Entrada do usuário
    voto = input("Por favor, digite o número do candidato desejado (de 10 a 19). (Para BRANCO digite B e para NULO digite um digito fora da lista apresentada): ")

    # Verificação do voto
    if voto.lower() == "b":
        brancos += 1
        print("Voto confirmado!")
    elif voto.isdigit() and int(voto) >= 10 and int(voto) <= 19:
        votos_validos += 1
        print("Voto confirmado!")
    else:
        nulos += 1
        print("Voto nulo!")

    # Contabilização do eleitor
    eleitores += 1

    # Exibição do andamento da votação
    print("Brancos:", brancos)
    print("Nulos:", nulos)
    print("Votos válidos:", votos_validos)
    print("Eleitores:", eleitores)
    print('------------------------------------------------------------------------')

    # Pergunta para encerrar votação
    encerrar = input("Encerrar votação? (S/N): ")
    if encerrar.lower() == 's':
        break

# Exibição dos resultados
print('---------------------------------------------------------------------------------')
print("Número de eleitores:", eleitores)
print("Brancos:", brancos, f"votos ({brancos / eleitores * 100:.2f}% do total de votos)")
print("Votos válidos:", votos_validos, f"votos ({votos_validos / eleitores * 100:.2f}% do total de votos)")
print("Nulos:", nulos, f"votos ({nulos / eleitores * 100:.2f}% do total de votos)")
