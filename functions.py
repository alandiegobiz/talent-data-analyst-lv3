from itertools import cycle

def validador_cpf(cpfcriado):
    cpfconvertido = [int(char) for char in cpfcriado if char.isdigit()]

    if len(cpfconvertido) != 11:
        return False

    if cpfconvertido == cpfconvertido[::-1]:
        return False

    for i in range (9, 11):
        value = sum((cpfconvertido[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpfconvertido[i]:
            return False
    return True

def validador_cnpj(cnpj):
    if len(cnpj) != 14:
        return False

    if cnpj in (c * 14 for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True