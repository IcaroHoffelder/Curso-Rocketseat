print("Olá, vamo dale meu caro")
comando = input("Digite um comando: ")

match comando:
    case "oi" | "olá" | "hello":
        print("oi como vai vocÊ")
    case "tchau":
        print("tchau")
    case "TESTE":
        print("testado")
    case _:
        print("DIGITA CERTO PAU NO CU")
