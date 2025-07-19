import math

def rotate_point(point, axis, angle):
    """ Rota un punto alrededor de un eje dado en grados """
    # Normalizar el eje
    norm = math.sqrt(sum(x**2 for x in axis))
    axis = [x / norm for x in axis]
    
    # Convertir el ángulo a radianes
    angle = math.radians(angle)
    
    # Componentes del eje
    x, y, z = axis
    
    # Componentes de rotación
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    one_minus_cos = 1 - cos_theta
    
    # Matriz de rotación
    rotation_matrix = [
        [cos_theta + x**2 * one_minus_cos, x * y * one_minus_cos - z * sin_theta, x * z * one_minus_cos + y * sin_theta],
        [y * x * one_minus_cos + z * sin_theta, cos_theta + y**2 * one_minus_cos, y * z * one_minus_cos - x * sin_theta],
        [z * x * one_minus_cos - y * sin_theta, z * y * one_minus_cos + x * sin_theta, cos_theta + z**2 * one_minus_cos]
    ]
    
    # Rotar el punto
    px, py, pz = point
    rotated_point = [
        rotation_matrix[0][0] * px + rotation_matrix[0][1] * py + rotation_matrix[0][2] * pz,
        rotation_matrix[1][0] * px + rotation_matrix[1][1] * py + rotation_matrix[1][2] * pz,
        rotation_matrix[2][0] * px + rotation_matrix[2][1] * py + rotation_matrix[2][2] * pz
    ]
    
    return rotated_point

def transform_and_rotate(Lx, Ly, Lz, Theta):
    """ Calcula las coordenadas de los puntos después de rotación """
    # Coordenadas iniciales
    points = [
        (0, 0, 109),
        (109 * math.sqrt(8/9), 0, -109/3),
        (-109 * math.sqrt(2/9), 109 * math.sqrt(2/3), -109/3),
        (-109 * math.sqrt(2/9), -109 * math.sqrt(2/3), -109/3)
    ]
    
    # Vector del eje de rotación
    axis = (Lx, Ly, Lz)
    
    # Obtener la coordenada del centro de rotación
    center = (0, 0, 0)
    
    # Mover los puntos para que el centro esté en el origen
    translated_points = [(p[0] - center[0], p[1] - center[1], p[2] - center[2]) for p in points]
    
    # Rotar los puntos
    rotated_points = [rotate_point(p, axis, Theta) for p in translated_points]
    
    # Regresar a las coordenadas originales
    final_points = [(p[0] + center[0], p[1] + center[1], p[2] + center[2]) for p in rotated_points]
    
    return final_points

def format_output(points):
    """ Formatea la salida como una cadena de 12 valores espaciados """
    return ' '.join(f"{x:.6f} {y:.6f} {z:.6f}" for x, y, z in points)

# Datos de entrada
input_data = """
173151 439349 -881470 73
"""

# Procesar la entrada
lines = input_data.strip().split('\n')
Lx, Ly, Lz, Theta = map(int, lines[0].split())

# Obtener los puntos transformados
points = transform_and_rotate(Lx, Ly, Lz, Theta)

# Formatear y mostrar el resultado
print(format_output(points))