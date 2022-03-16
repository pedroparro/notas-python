print("****************** NOTAS DE ALUNOS ******************")
print("********** DESENVOLVIDO POR PEDRO PARRO **********")
print('\n')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
tot = round((n1+n2+n3)/3,2)
print('Sua média é:',tot)

if tot > 6:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')

