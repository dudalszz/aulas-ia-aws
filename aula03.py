#Desafio 
#Criar um programa que verifique a idade e maioridade

#Passo 1: Criar uma variável
#Passo 2: Criar uma estrutura de condição para verificar a idade
#Passo 3: Exibir a frase adequada de acordo com a idade da pessoa.

idade = int(input("Digite sua idade:"))

if idade >= 18: 
    print("Você é maior de idade");

elif idade >= 12:
    print("Você é adolescente");

else:
    print("Você é uma criança")        
