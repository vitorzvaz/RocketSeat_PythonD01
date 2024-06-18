contatos = []

def adicionar_contato(contatos, nome, telefone, email, favorito):
  if favorito == 'S':
    fav = True
  else:
    fav = False
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": fav}
  contatos.append(contato)
  print(f"Contato {nome} adicionado com sucesso!")
  return

def visualizar_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start = 1):
    fav = "✩" if contato["favorito"] else " "
    nome = contato['nome']
    telefone = contato['telefone']
    email = contato['email']
    print(f"\n{indice}. [{fav} ] {nome}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")
  return

def editar_contato(contatos, indice_contato, informacao, nova_informacao):
  ajuste_indice = indice_contato - 1
  if informacao == 1:
    info = "nome"
  elif informacao == 2:
    info = "telefone"
  elif informacao == 3:
    info = "email"
  contatos[ajuste_indice][info] = nova_informacao
  print(f"{info} do contato {indice_contato} atualizado para {nova_informacao}.")
  return

def ver_favoritos(contatos):
  print("\nLista de favoritos:")
  for indice, contato in enumerate(contatos, start = 1):
    fav = "✩" if contato["favorito"] else " "
    if contato["favorito"]:
      nome = contato['nome']
      telefone = contato['telefone']
      email = contato['email']
      print(f"\n{indice}. [{fav} ] {nome}")
      print(f"Telefone: {telefone}")
      print(f"E-mail: {email}")
  return

def marcar_favorito(contatos, indice):
  ajuste_indice = indice - 1
  contatos[ajuste_indice]['favorito'] = True
  print(f"Contato {contatos[ajuste_indice]['nome']} marcado como Favorito!")
  return

def desmarcar_favorito(contatos, indice):
  ajuste_indice = indice - 1
  contatos[ajuste_indice]['favorito'] = False
  print(f"Contato {contatos[ajuste_indice]['nome']} desmarcado como Favorito!")
  return

def apagar_contato(contatos, indice):
  ajuste_indice = indice - 1
  contatos.remove(contatos[ajuste_indice])
  print("Contato removido com sucesso")
  return

print("\nSeja bem vindo a sua agenda pessoal!")

while True:

  print("\nMenu:")
  print("1. Adicionar contato")
  print("2. Visualizar contatos")
  print("3. Editar contato")
  print("4. Favoritos")
  print("5. Apagar contato")
  print("6. Sair")

  escolha = int(input("\nDigite a sua escolha: "))

  if escolha == 1:
    nome = input("\nDigite o nome do contato: ")
    try:
      telefone = int(input("Digite o número de telefone: "))
    except ValueError as e:
      print("Digite um valor numérico.")
    else:
      email = input("Digite o e-mail de contato [Opcional]: ")
      if email == "":
        email = "Não Informado"
      favorito = input("Deseja favoritar esse contato? [S/N] ").upper()
      adicionar_contato(contatos, nome, telefone, email, favorito)
    
  elif escolha == 2:
    visualizar_contatos(contatos)

  elif escolha == 3:
    visualizar_contatos(contatos)
    indice_contato = int(input("\nDigite o número do contato que deseja atualizar: "))
    info_contato = int(input("\nQual informação você deseja atualizar? [1. Nome] [2. Telefone] [3. E-mail]: "))
    if info_contato == 1:
      nova_informacao = input('Digite o novo nome: ')
    elif info_contato == 2:
      nova_informacao = int(input("Digite o novo telefone: "))
    elif info_contato == 3:
      nova_informacao = input("Digite o novo e-mail: ")
    editar_contato(contatos, indice_contato, info_contato, nova_informacao)
  
  elif escolha == 4:
    print('\nMenu Favoritos:')
    print("1. Visualizar favoritos")
    print("2. Marcar Favorito")
    print("3. Desmarcar Favorito")

    try:
      fav_escolha = int(input("Digite sua escolha: "))
    except ValueError as e:
      print("Digite um valor numérico.")
    else:
      if fav_escolha == 1:
        ver_favoritos(contatos)
      elif fav_escolha == 2:
        visualizar_contatos(contatos)
        indice = int(input("\nDigite o contato que deseja favoritar: "))
        marcar_favorito(contatos, indice)
      elif fav_escolha == 3:
        ver_favoritos(contatos)
        indice = int(input("\nDigite o contato que deseja remover dos favoritos: "))
        desmarcar_favorito(contatos, indice)
      else:
        print("Digite uma opção válida")

  elif escolha == 5:
    visualizar_contatos(contatos)
    contato_deletar = int(input("Digite o contato que deseja deletar: "))
    apagar_contato(contatos, contato_deletar)

  elif escolha == 6:
    break
