def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Read the number of vertices
    num_vertices = int(data[0])
    
    # Read the vertices
    vertices = []
    for i in range(1, num_vertices + 1):
        x, y = map(float, data[i].strip().split())
        vertices.append((x, y))
    
    # Calculate the area
    area = calculate_polygon_area(vertices)
    
    # Print the result
    print(f"{area:.1f}")

# Example usage (for local testing, uncomment below lines and replace input with your data):
# if __name__ == "__main__":
#     import io
#     import sys
#     input_data = "5\n51 9\n77 10\n92 71\n62 84\n29 94\n"
#     sys.stdin = io.StringIO(input_data)
#     main()def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Read the number of vertices
    num_vertices = int(data[0])
    
    # Read the vertices
    vertices = []
    for i in range(1, num_vertices + 1):
        x, y = map(float, data[i].strip().split())
        vertices.append((x, y))
    
    # Calculate the area
    area = calculate_polygon_area(vertices)
    
    # Print the result
    print(f"{area:.1f}")

# Example usage (for local testing, uncomment below lines and replace input with your data):
if __name__ == "__main__":
    import io
    import sys
    input_data = "11\n3140 442\n6002 859\n6957 1192\n9678 3790\n9749 4559\n9128 6511\n6695 9557\n5467 9937\n4396 9467\n562 6748\n1392 2737\n"
    sys.stdin = io.StringIO(input_data)
    main()