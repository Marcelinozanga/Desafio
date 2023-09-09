import os
from colorama import Fore,Back,Style
os.system('cls')
n_prof=input("Digite seu nome: ")
n_disci=input("Digite a disciplina que lecionas: ")
n_alun=input("Digite o nome do seu aluno/a: ")
nota1=int(input("Digite a primeira nota do aluno: "))
nota2=int(input("Digite a segunda nota do aluno: "))
nota3=int(input("Digite a terceira nota do aluno: "))

media=(nota1+nota2+nota3)/3
m=int(media)
if media >= 10:
    os.system('cls')
    print("Professor " +n_prof + " o/a aluno/a " +n_alun +" teve a nota " +str(m)+ " entretanto está aprovado/a na disciplina de " +n_disci )
else:
    os.system('cls')
    print("Professor " +n_prof + " o/a aluno/a " +n_alun + " teve a nota " +str(m)+ " entretanto está reprovado/a na disciplina de " +n_disci )
