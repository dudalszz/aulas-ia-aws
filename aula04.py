#Desafio
#Criar uma calculadora para realizar operções básicas de matemática em Python

#Requisitos
# 1 - A operação matemática deve ser realizada entre dois números
# 2 - As operações básicas válidas são: + - * /
# 3 - O programa deve tratar entradas inválidas 

#Criando uma função de calculadora

def calculadora():
    while True: 
        try: 
            num1 = float(input("Digite o primeiro número:"))
            num2 = float(input("Digite o segundo número:"))
            operacao = input("Digite a operação(+,-,*,/):")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2
            else:
                raise ValueError
            
            print(f"Resultado:{resultado}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente")
        except ZeroDivisionError: 
            print("Erro: Não é permitido dividir por zero. Tente novamente")
        
calculadora()
