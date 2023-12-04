import os

os.system("cls")
print("Temos dois arquivos: bloco_texto.txt e dados.txt")
print("Qual deles você deseja apagar?")
es = input("Digite \n - 1 para bloco_texto\n - 2 para dados.txt\n: ")

p = input("Você realmente deseja apagar o arquivo?[s,n]: ")

if p == "s":
    if es == "1":
        os.remove("bloco_texto.txt")
    else:
        os.remove("dados.txt")
    print("O arquivo foi apagado com sucesso!")
else:
    print("Operação cancelada")            
