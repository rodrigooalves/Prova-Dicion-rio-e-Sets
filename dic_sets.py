alunos = {}  # Inicializa o dicionário vazio para armazenar os alunos

while True:
    print("\nOpções:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == "1":
        matricula = input("Informe o número de matrícula do aluno: ")
        nome = input("Informe o nome do aluno: ")
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

    elif opcao == "2":
        matricula = input("Informe o número de matrícula do aluno a ser removido: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Aluno removido com sucesso!")
        else:
            print("Número de matrícula não encontrado.")

    elif opcao == "3":
        print("\nLista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
