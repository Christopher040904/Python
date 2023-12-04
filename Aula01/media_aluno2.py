'''
Crie um programa para mostrar se o aluno está
aprovado, reprovado ou em recuperação.
O programa deve pedir 4 notas e realizar o
cálculo da média.
Se a media do aluno for:

    >= 6 -> Aprovado
    <= 4 -> Reprovado
    >4 e <6 -> Recuperação
'''

primb = float (input("Digite a nota do aluno: "))
sengb = float (input("Digite a nota do aluno: "))
tercb = float(input("Digite a nota do aluno: "))
quarb = float (input("Digite a nota do aluno: "))

media = (primb + sengb + tercb + quarb) / 4


media = float(media)
if media >= 7:
    print("Aluno aprovado")
elif media <= 4:
    print("Aluno reprovado")
else:
    print("Aluno em recuperação")    