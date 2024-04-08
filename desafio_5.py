dados = str(input('Digite o texto: '))

dados_invertido = ''
for letra in range(len(dados)-1, -1, -1):
    dados_invertido += dados[letra]
print(f'O texto digitado foi {dados}\n\nO texto invertido é {dados_invertido}')