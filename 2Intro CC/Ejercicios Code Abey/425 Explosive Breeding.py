def total_rats(M, P, N, D):
    # Initialize the list to keep track of the number of rats of each age
    rats = [0] * (D + 1)
    
    # Start with one newborn rat
    rats[0] = 1
    
    # Simulate the process
    for day in range(D):
        if rats[day] > 0:
            # Rats that are mature today will reproduce
            maturity_day = day + M
            if maturity_day <= D:
                rats[maturity_day] += rats[day] * N
            
            # Reproduction every P days after maturity
            breeding_day = day + M + P
            while breeding_day <= D:
                rats[breeding_day] += rats[day] * N
                breeding_day += P
    
    # Total number of rats is the sum of all rats at all days
    total_rats_count = sum(rats)
    
    return total_rats_count

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().strip().split()))
    
    M = data[0]
    P = data[1]
    N = data[2]
    D = data[3]
    
    result = total_rats(M, P, N, D)
    print(result)

# Example usage (for local testing, uncomment below lines and replace input with your data):
if __name__ == "__main__":
    import io
    import sys
    input_data = "25 19 18 194\n"
    sys.stdin = io.StringIO(input_data)
    main()