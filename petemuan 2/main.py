import cv2
import matplotlib.pyplot as plt

# 1. Membaca citra dari file
img = cv2.imread('smartclaas.jpeg')

# 2. Konversi BGR ke RGB (Betulkan COLOR_BGR2RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 3. Menampilkan informasi dimensi citra
tinggi, lebar, channel = img.shape
print(f"Dimensi Citra: {lebar} x {tinggi} piksel, dengan {channel} saluran warna.")

# 4. Menampilkan citra
plt.imshow(img_rgb)
plt.title("Citra Pertama Saya")
plt.axis('off')
plt.show()