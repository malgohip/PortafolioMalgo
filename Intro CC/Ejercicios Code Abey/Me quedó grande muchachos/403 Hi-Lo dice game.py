def expected_loss(N, K):
    # La expectativa matemática para K rondas
    return K / N

def main(input_data):
    lines = input_data.strip().split('\n')
    G = int(lines[0])
    results = []
    for i in range(1, G + 1):
        N, K = map(int, lines[i].split())
        result = expected_loss(N, K)
        results.append(f"{result:.7f}")
    return ' '.join(results)

# Datos de entrada
input_data = """
13
2 4
4 3
5 8
7 8
8 7
9 15
10 9
12 14
14 11
15 9
16 10
18 6
20 14
"""

# Calcular y mostrar el resultado
print(main(input_data))