import random

print('-' * 30)
print('Verificação na Sequência de Fibonacci')
print('-' * 30)

# Gerando um número aleatório para verificar
numero = random.randint(0, 100)  # Gera um número aleatório entre 0 e 100
print(f'O número aleatório gerado foi: {numero}')

# Caso especial: se o número gerado for 0
if numero == 0:
    print('~' * 30)
    print('0 → FIM')
    print('~' * 30)
    print('O número 0 pertence à sequência de Fibonacci.')
else:
    T1 = 0  # Primeiro termo da sequência
    T2 = 1  # Segundo termo da sequência

    # Exibindo os primeiros termos
    print('~' * 30)
    print(f'{T1} → {T2}', end='')

    # Inicialização da variável de controle
    pertence = (numero == T1 or numero == T2)

    # Calculando os próximos termos da sequência
    while T2 < numero:
        TN = T1 + T2
        print(f' → {TN}', end='')  # Mostrando a sequência
        T1 = T2
        T2 = TN
        # Verifica se o termo atual é igual ao número gerado
        if TN == numero:
            pertence = True

    print(' → FIM')
    print('~' * 30)

    # Exibe o resultado com base na verificação
    if pertence:
        print(f'O número {numero} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')

print('-' * 30)