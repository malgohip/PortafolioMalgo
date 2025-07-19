import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from PIL import Image

# Parámetro: número de componentes principales (autovectores) a conservar
num_componentes = 25  # Puedes cambiar este número

# 1. Cargar base de datos de rostros
data = fetch_olivetti_faces(shuffle=True, random_state=42)
X = data.data  # Cada imagen está vectorizada (4096 dimensiones)
images = data.images  # Imágenes originales en 64x64

# 2. Seleccionar imagen a reconstruir (por ejemplo, la primera)
imagen_original = X[0]
imagen_reshaped = images[0]

# 3. Aplicar PCA para compresión y reconstrucción
pca = PCA(n_components=num_componentes)
X_transformado = pca.fit_transform(X)  # Reducir dimensionalidad
imagen_reconstruida = pca.inverse_transform(X_transformado[0])  # Reconstrucción

# 4. Guardar la imagen reconstruida como PNG
imagen_reconstruida_2D = imagen_reconstruida.reshape(64, 64)
img = Image.fromarray((imagen_reconstruida_2D * 255).astype(np.uint8))
img.save(f"rostro_reconstruido_{num_componentes}_componentes.png")

# 5. Mostrar original vs reconstruida
plt.figure(figsize=(8,4))
plt.subplot(1, 2, 1)
plt.title("Imagen original")
plt.imshow(imagen_reshaped, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f"Reconstruida con {num_componentes} componentes")
plt.imshow(imagen_reconstruida_2D, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()


img_original = Image.fromarray((imagen_reshaped * 255).astype(np.uint8))
img_original.save("rostro_original.png")