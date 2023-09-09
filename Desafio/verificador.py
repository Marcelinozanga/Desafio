import os
os.system('cls')

print("◙-----------------------------------SEJA BEM VINDO AO MEU PROGRAMA----------------------------------◙")
print("◙----------------------------------------✌---BY MR SKYBLACK---✌------------------------------------◙")
print("◙------------------------------------SEJA BEM VINDO AO MEU PROGRAMA----------------------------------◙")

verificar=[]

print("|..........👌MEMORIZADOR DE PALAVRAS👌..........|")
pala=input("         Digite uma palavra: ")
print("|..........👌MEMORIZADOR DE PALAVRAS👌..........|")


while pala != "SAIR":
    verificar.append(pala)
    print("|..........👌MEMORIZADOR DE PALAVRAS👌..........|")
    pala=input("Digite uma palavra ou digite SAIR para fechar o programa: ")
os.system('cls')
print("◙----------------------------------SALA DAS MEMORIAS----------------------------------------◙")
print("◙---------------------------------- BY MR SKYBLACK---------------------------◙")
print("◙----------------------------------SALA DAS MEMORIAS----------------------------◙")

print("SEJA BEM-VINDO A SALA DA MEMORIA SR. ")
print("palavras digitadas logo a baixo👇👇")
print("------------------------------------")

for x in verificar:
    print("----------------------")
    print("palavra digitada: "+x)
    print("-----------------------")

print("◙----------------------------------FIM DO PROGRAMA----------------------------------------◙")
print("◙---------------------------------- BY MR SKYBLACK---------------------------◙")
print("◙----------------------------------FIM DO PROGRAMA----------------------------◙")