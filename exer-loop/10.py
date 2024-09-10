senha = "Eduardo12"
while True:
    tenta = input("Digite a senha: ")
    if senha == tenta:
        print("Acesso liberado. Seja bem-vindo")
        break
    else:
        print("Acesso negado, tente novamente.")