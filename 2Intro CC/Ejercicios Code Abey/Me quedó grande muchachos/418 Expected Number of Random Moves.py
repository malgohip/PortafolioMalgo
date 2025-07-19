def expected_moves(n):
    # Create a list to store expected moves for positions from 0 to n
    E = [0] * (n + 1)
    
    # Base case: at position n, no moves are required
    E[n] = 0
    
    # Calculate expected moves for positions from n-1 to 0
    for i in range(n - 1, -1, -1):
        total = 0
        for r in range(1, n - i + 1):
            total += E[i + r]
        E[i] = 1 + (total / (n - i))
    
    return E[0]

def main():
    import sys
    input = sys.stdin.read
    
    data = input().split()
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        n = int(data[i])
        result = expected_moves(n)
        results.append(f"{result:.8f}")
    
    print(" ".join(results))

# Example usage (for local testing, uncomment below lines and replace input with your data):
if __name__ == "__main__":
    import io
    import sys
    input_data = "11\n6 10 71 288 605 1010 8871 29802 77666 235841 717159\n"
    sys.stdin = io.StringIO(input_data)
    main()