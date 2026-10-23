import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

# 1. Baca gambar yang sangat cerah (sesuaikan path gambar Anda)
image = img.imread("images.jpg")

# Pastikan gambar dalam format float32 untuk manipulasi nilai piksel
img_float = image.astype(np.float32)

# --- METODE 1: Gamma Correction ---
# Menggunakan gamma > 1.0 akan menggelapkan gambar yang terlalu cerah 
# dan memperjelas detail yang hilang/terlalu terang
gamma = 2.5 
normalized = img_float / 255.0
gamma_corrected = np.power(normalized, gamma) * 255.0
img_gamma = np.clip(gamma_corrected, 0, 255).astype(np.uint8)


# --- METODE 2: Kurangi Kecerahan & Tingkatkan Kontras secara Manual ---
def adjust_bright_contrast(img, brightness=-80, contrast=1.8):
    # Mengurangi kecerahan (brightness) dan menaikkan kontras
    mean = 128
    result = mean + contrast * (img - mean) + brightness
    return np.clip(result, 0, 255).astype(np.uint8)

img_manual = adjust_bright_contrast(img_float, brightness=-70, contrast=2.0)


# --- TAMPILKAN HASIL ---
plt.figure(figsize=(15, 5))

# Gambar Asli (Sangat Cerah)
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Gambar Asli (Sangat Cerah)")
plt.axis("off")

# Hasil Metode 1 (Gamma Correction)
plt.subplot(1, 3, 2)
plt.imshow(img_gamma)
plt.title("Hasil: Gamma Correction")
plt.axis("off")

# Hasil Metode 2 (Kurangi Brightness + Kontras)
plt.subplot(1, 3, 3)
plt.imshow(img_manual)
plt.title("Hasil: Manual Adjustment")
plt.axis("off")

plt.tight_layout()
plt.show()