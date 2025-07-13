
# Lista que armazenará contatos 
contatos = []

# Função para exibir o menu 
def mostrar_menu (): 
    print ("\n--*************AGENDA DE CONTATOS ***********")
    print (" 1. Adicionar Contato")
    print (" 2. Visualizar Contatos")
    print (" 3. Editar Contato")
    print (" 4. Marcar / Desmarcar Favorito")
    print (" 5. Visualizar Favoritos")
    print (" 6. Deletar Contato")

# Função para adicionar contato 
def adicionar_contato():
    nome = input("Nome:  ")
    telefone = input ("Telefone:   ")
    email = input ("Email:  ")
    favorito = False 
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email, 
        "favorito": favorito
    }
    contatos.append(contato)
    print ("Contato Adicionado com Sucesso!")

# Função para mostrar todos os contatos 
# i = indice c= contato 
def mostrar_contatos(lista):
    if not lista:
        print("Nenhum contato cadastrado.")
    else:
        for i, c in enumerate(lista):
            fav = "★" if c["favorito"] else "  "
            print (f"{i}. [{fav}] {c['nome']} - {c['telefone']} - {c['email']}")

#Função para editar um contato 
def editar_contato (): 
    mostrar_contatos(contatos)
    indice = int (input ("Digite o numero do contato que deseja editar: "))
    if 0 <= len(contatos):
        print ("Deixe em branco se não quiser alterar.")
        nome = input ("Novo nome:" ) or contatos[indice] ["nome"]
        telefone = input ("Novo telefone: ") or contatos [ indice] ["telefone"]
        email = input ("Novo Email:  ") or contatos [indice] ["Email"]
        contatos [indice].update({"nome": nome, "telefone": telefone, "email": email })
        print ("Contato Atualizado!")
    else: 
        print ("Indice Inválido!")

#Função para favoritar ou desfavoritar 
def marcar_favorito():
    mostrar_contatos(contatos)
    indice = int ( input ("Digite o número do contato para marcar/desmarcar como favorito: "))
    if 0 <= indice < len (contatos):
        contatos[indice]["favorito"]= not contatos [indice ["favorito"]]
        status = "favorito" if contatos[indice ["favorito"]] else "não favorito"
        print(f"{contatos[indice]['nome']} agora é {status}.")
    else: 
        print ("índice inválido!")    

# Função para mostrar apenas os favoritos
def mostrar_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]
    print("\n--- CONTATOS FAVORITOS ---")
    mostrar_contatos(favoritos)

# Função para deletar um contato
def deletar_contato():
    mostrar_contatos(contatos)
    indice = int(input("Digite o número do contato a ser deletado: "))
    if 0 <= indice < len(contatos):
        contato_removido = contatos.pop(indice)
        print(f"Contato {contato_removido['nome']} removido com sucesso.")
    else:
        print("Índice inválido!")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        print("\n--- CONTATOS ---")
        mostrar_contatos(contatos)
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        marcar_favorito()
    elif opcao == "5":
        mostrar_favoritos()
    elif opcao == "6":
        deletar_contato()
    elif opcao == "0":
        print("Saindo da agenda... Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")