#Desafio

#Criar um programa para calcular o valor da gorjeta, baseado no valor total da conta e a porcentagem desejada

def calcular_gorjeta(valor_conta, porcentagem_gorgeta):
    gorjeta = valor_conta * (porcentagem_gorgeta /100)
    return round(gorjeta, 2)

total_conta = 100.00
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta: .2f}, a gorjeta de {porcentagem}% é R${gorjeta: .2f}")