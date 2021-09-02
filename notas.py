alunos=[]
temp=[]
while True:
    nome=input('Nome: ').upper()
    temp.append(nome)
    nota1=float(input('Nota1: '))
    temp.append(nota1)
    nota2=float(input('Nota2: '))
    temp.append(nota2)
    alunos.append(temp[:])
    temp.clear()
    r=str(input('Quer continuar[S/N]: ')).strip()[0]
    if r in 'Nn':
        break
    elif r not in 'NnSs':
        r=str(input('RESPOSTA INVÁLIDA [S/N]!: '))
print('-='*21)  
print(f'{"Nº Nome":<10}   {"Média"}')
print('-'*20)
for n, a in enumerate(alunos):
    print(f'{n}  {alunos[n][0]:<10}{(alunos[n][1]+alunos[n][2])/2:.2f}')
print('-'*20)
while True:
    n=int(input('Mostrar notas de qual aluno (999 interrompe): '))
    print(f'As notas do/a {alunos[n][0]} foram {alunos[n][1]} e {alunos[n][2]}')
    if n==999:
        break 

    




    