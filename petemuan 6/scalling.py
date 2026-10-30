import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("Foto.jpg")

# Periksa apakah gambar berhasil dimuat
if img is None:
    print("Error: Gambar 'Foto.jpg' tidak ditemukan atau gagal dimuat.")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Scaling dengan faktor 0.5 (memperkecil gambar)
    hasil_05 = cv2.resize(
        img,
        None,
        fx=0.5,
        fy=0.5,
        interpolation=cv2.INTER_LINEAR
    )

    # Scaling dengan faktor 2 (memperbesar gambar)
    hasil_2 = cv2.resize(
        img,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_LINEAR
    )

    # Menampilkan informasi ukuran di console
    print("Ukuran gambar asli       :", img.shape)
    print("Ukuran setelah scaling 0.5:", hasil_05.shape)
    print("Ukuran setelah scaling 2.0:", hasil_2.shape)

    # Menampilkan gambar perbandingan (1 baris, 3 kolom)
    plt.figure(figsize=(15, 5))

    # 1. Gambar Asli
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title(f"Asli\n{img.shape[1]} x {img.shape[0]}")
    plt.axis("off")

    # 2. Gambar Scaling 0.5x
    plt.subplot(1, 3, 2)
    plt.imshow(hasil_05)
    plt.title(f"Scaling 0.5x (Kecil)\n{hasil_05.shape[1]} x {hasil_05.shape[0]}")
    plt.axis("off")

    # 3. Gambar Scaling 2x
    plt.subplot(1, 3, 3)
    plt.imshow(hasil_2)
    plt.title(f"Scaling 2x (Besar)\n{hasil_2.shape[1]} x {hasil_2.shape[0]}")
    plt.axis("off")

    plt.tight_layout()
    plt.show()