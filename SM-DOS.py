import os

while True:
    # Exibe o prompt de comando
    command = input(os.getcwd() + "> ")
    
    # Verifica se o comando é "cd" para mudar de diretório
    if command.startswith("cd "):
        # Extrai o diretório alvo do comando
        directory = command[3:]
        try:
            os.chdir(directory)
        except OSError:
            print(f"O diretório '{directory}' não existe.")
    
    # Verifica se o comando é "dir" para listar o conteúdo do diretório
    elif command == "dir":
        for file in os.listdir():
            print(file)
    
    # Verifica se o comando é "exit" para sair do programa
    elif command == "exit":
        break
    
    # Executa o comando no shell do sistema operacional
    else:
        os.system(command)
