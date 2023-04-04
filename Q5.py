def inverter(palavra):  # maneira fácil e rápida
    return palavra[::-1]


def inverter2(palavra):  # maneira 2 utilizando indexação
    invertida = []
    for n in range(len(palavra) - 1, -1, -1):
        invertida.append(palavra[n])
    return ''.join(invertida)


print(inverter('abacaxi'))
print(inverter2('abacaxi'))
