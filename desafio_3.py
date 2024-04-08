# a) 1, 3, 5, 7, ___

# Aqui, cada número é ímpar e aumenta de 2 em 2. Portanto, o próximo número deve ser 9.

primeiro_numero = 1
constate = 2

numero_termos = 5

sequencia = [primeiro_numero]

while len(sequencia) < numero_termos:
    proximo_numero = sequencia[-1] + constate
    sequencia.append(proximo_numero)
print('==' *40)   
print("Desafio A: => Os números da sequência são:", sequencia, '\n')
print('==' *40)


# b) 2, 4, 8, 16, 32, 64, ____

# Cada número é o dobro do anterior. Portanto, o próximo número deve ser 128 (64 * 2).

primeiro_numero = 2
constate = 2

numero_termos = 7

sequencia = [primeiro_numero]

while len(sequencia) < numero_termos:
    proximo_numero = sequencia[-1] * constate
    sequencia.append(proximo_numero)
    
print("Desafio B: => Os números da sequência são:", sequencia, '\n')
print('==' *40)


# c) 0, 1, 4, 9, 16, 25, 36, ____

# Esses são os quadrados dos números inteiros de 0 a 6. Portanto, o próximo número deve ser 49 (7^2).

num_termos = 8  


sequencia = []


for i in range(num_termos):
    proximo_numero = i ** 2
    sequencia.append(proximo_numero)


print("Desafio C: => Os números da sequência são:", sequencia, '\n')
print('==' *40)

# d) 4, 16, 36, 64, ____

# Esses são os quadrados dos números pares de 2 a 8. Portanto, o próximo número deve ser 100 (10^2).

num_termos = 5  


sequencia = []


for i in range(2, num_termos *2 + 1, 2):
    proximo_numero = i ** 2
    sequencia.append(proximo_numero)


print("Desafio D: => Os números da sequência são:", sequencia, '\n')
print('==' *40)


# e) 1, 1, 2, 3, 5, 8, ____

# Essa é a sequência de Fibonacci começando em 1 e 1. Portanto, o próximo número deve ser a soma dos dois anteriores: 13.

numero_termos = 7

a= 1
b= 1

sequencia = [a, b]

for i in range(numero_termos - 2):
    proximo_numero = a + b
    sequencia.append(proximo_numero)
    a = b
    b = proximo_numero


print("Desafio E: => A sequência é: ", sequencia, '\n')
print('==' *40)


# f) 2, 10, 12, 16, 17, 18, 19, ____

sequencia = [2, 10, 12, 16, 17, 18, 19,]

print("Desafio F: => A sequência é: ", sequencia)
print('==' *40)