def solve_egg_problem(egg_states, toggles):
    n = len(egg_states)  # Number of eggs
    A = [[0] * n for _ in range(n)]  # Matrix for the toggles
    b = egg_states[:]  # Right-hand side vector (initial states)

    # Fill the matrix A with toggling rules
    for i in range(n):
        line = toggles[i]
        _, toggles_list = line.split(':')
        toggles_indices = list(map(int, toggles_list.split()))
        A[i][i] = 1  # Self-toggling
        for index in toggles_indices:
            A[i][index] = 1  # Toggle other specified eggs

    # Gaussian elimination in GF(2)
    def gaussian_elimination(A, b):
        n = len(A)
        # Augment matrix A with vector b
        M = [A[i] + [b[i]] for i in range(n)]
        
        for col in range(n):
            # Find a row with a 1 in the current column
            if M[col][col] == 0:
                for row in range(col + 1, n):
                    if M[row][col] == 1:
                        M[col], M[row] = M[row], M[col]
                        break
            # Make sure the current column has a leading 1
            for row in range(n):
                if row != col and M[row][col] == 1:
                    M[row] = [(M[row][k] ^ M[col][k]) for k in range(n + 1)]
        
        # Extract the solution
        x = [M[i][-1] for i in range(n)]
        return x
    
    solution = gaussian_elimination(A, b)
    
    # Collect indices of eggs that should be touched
    result_indices = [i for i, value in enumerate(solution) if value == 1]
    
    return result_indices

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Read initial states
    egg_states = list(map(int, data[0].strip().split()))
    
    # Read toggling rules
    toggles = data[1:]
    
    # Solve the problem
    result = solve_egg_problem(egg_states, toggles)
    
    if result:
        print(" ".join(map(str, result)))
    else:
        print("No solution")

# Example usage (for local testing, uncomment below lines and replace input with your data):
if __name__ == "__main__":
    import io
    import sys
    input_data = "1 0 0 1 0 1 0 0 0 1 1 0 0 1 0 1 1 0 1 0\n0: 0 2 18\n1: 1 10 18\n2: 2 4 18\n3: 2 3 5\n4: 4 19\n5: 3 5 13\n6: 6 12 13\n7: 3 7 12\n8: 4 8 14\n9: 7 9 12\n10: 8 10 17\n11: 1 4 11\n12: 10 12 19\n13: 6 13\n14: 3 11 14\n15: 0 10 15\n16: 1 15 16\n17: 9 13 17\n18: 12 13 18\n19: 1 14 19"
    sys.stdin = io.StringIO(input_data)
    main()