nota = int(input("Digite Sua Nota: "))

if nota >= 7:
    print("Aprovado")
else:
    if nota < 5:
        print("Reprovado!")
    else:
        print("Recuperação")