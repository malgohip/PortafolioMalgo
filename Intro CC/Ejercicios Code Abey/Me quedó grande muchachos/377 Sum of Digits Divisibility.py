def sum_of_digits(n):
    """Calcula la suma de los dígitos de un número."""
    return sum(int(digit) for digit in str(n))

def find_kth_number(k):
    """Encuentra el k-ésimo número cuya suma de dígitos es divisible por 10."""
    count = 0
    number = 19  # El primer número cuya suma de dígitos es divisible por 10 es 19
    while count < k:
        if sum_of_digits(number) % 10 == 0:
            count += 1
        number += 1
    return number - 1

def main(input_data):
    """Procesa los datos de entrada y devuelve los resultados."""
    lines = input_data.strip().split('\n')
    T = int(lines[0])
    results = []
    for i in range(1, T + 1):
        K = int(lines[i])
        results.append(find_kth_number(K))
    return ' '.join(map(str, results))

# Datos de entrada
input_data = """
3
1
2
10
"""

# Ejecución
print(main(input_data))