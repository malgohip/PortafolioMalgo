def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Number of triangles
    T = int(data[0])
    
    results = []
    
    # Process each triangle
    for i in range(1, T + 1):
        x1, y1, x2, y2, x3, y3 = map(float, data[i].strip().split())
        area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
        results.append(f"{area:.7f}")
    
    # Print results as space-separated values
    print(" ".join(results))

# Example usage (for local testing, uncomment below lines and replace input with your data):
if __name__ == "__main__":
    import io
    import sys
    input_data = "16\n5842 5182 7514 1177 7234 2904\n1845 5615 8744 9672 4569 7779\n6941 4016 6887 9207 9246 8416\n7021 2260 8627 229 2957 4109\n7958 3746 8163 4785 10000 9287\n8380 5513 2474 3292 7295 6347\n6455 2555 6345 5198 3434 4677\n1858 7083 5147 6000 4710 8084\n3131 2667 7777 671 2690 830\n7764 7592 9772 5103 6318 9565\n8484 2842 6191 8177 6716 8667\n9448 7571 7293 9527 9378 574\n6782 8509 9035 635 2110 2758\n2967 9521 1574 2793 3816 8202\n7588 2837 2132 2887 8692 7123\n9674 6380 9673 3256 8305 9702"
    sys.stdin = io.StringIO(input_data)
    main()