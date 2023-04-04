def fibonacci(num):
    n1 = 0
    n2 = 1
    if num == n1 or num == n2:
        return f'O número {num} pertence a sequência de Fibonacci.'
    while num > n2:
        soma = n1 + n2
        n1 = n2
        n2 = soma
        if num == n2:
            return f'O número {num} pertence a sequência de Fibonacci.'
    return f'O número {num} não pertence a sequência de Fibonacci.'


print(fibonacci(10))
