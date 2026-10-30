import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("Foto.jpg")

# Periksa apakah gambar berhasil dimuat
if img is None:
    print("Error: Gambar 'Foto.jpg' tidak ditemukan atau gagal dimuat.")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 1. Horizontal Flip (flipCode = 1)
    # Mencerminkan gambar secara horizontal (sumbu Y)
    horizontal_flip = cv2.flip(img, 1)

    # 2. Vertical Flip (flipCode = 0)
    # Mencerminkan gambar secara vertikal (sumbu X)
    vertical_flip = cv2.flip(img, 0)

    # Menampilkan informasi ukuran di console
    print("Ukuran gambar asli:", img.shape)

    # Menampilkan gambar perbandingan (1 baris, 3 kolom)
    plt.figure(figsize=(15, 5))

    # Gambar Asli
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title("Gambar Asli")
    plt.axis("off")

    # Gambar Horizontal Flip
    plt.subplot(1, 3, 2)
    plt.imshow(horizontal_flip)
    plt.title("Horizontal Flip (flipCode = 1)")
    plt.axis("off")

    # Gambar Vertical Flip
    plt.subplot(1, 3, 3)
    plt.imshow(vertical_flip)
    plt.title("Vertical Flip (flipCode = 0)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()