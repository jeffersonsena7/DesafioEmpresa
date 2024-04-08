def varificar_numero(numero):
    a = 0
    b = 1

    while b < numero:
        a = b
        b = a + b
        print(b, end=', ')

    return b == numero

def main():
    num = int(input('Digite o número:'))
    print()
    if varificar_numero(num):
        print('\n'f"O numero  {num} pertence a sequência.")
    else:
        print('\n'f"O número {num} não pertence a sequência.")

main()
