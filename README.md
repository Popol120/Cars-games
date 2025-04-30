# Cara Menginstall Game Balapan Python

Untuk menjalankan game balapan Python yang saya berikan sebelumnya, Anda perlu menginstall beberapa komponen. Berikut panduan lengkapnya:

## 1. Install Python

Jika Anda belum memiliki Python:
- Download Python terbaru dari [python.org](https://www.python.org/downloads/)
- Pilih versi yang sesuai dengan sistem operasi Anda (Windows/macOS/Linux)
- Saat install, pastikan untuk mencentang "Add Python to PATH"
- Ikuti proses install sampai selesai

Verifikasi installasi:
```bash
python --version
# atau
python3 --version
```

## 2. Install Pygame

Pygame adalah library yang digunakan untuk membuat game dalam Python. Install dengan:

**Windows:**
```bash
pip install pygame
```

**macOS/Linux:**
```bash
pip3 install pygame
```

## 3. Menjalankan Game

1. Buat file baru dengan nama `game_balapan.py`
2. Salin kode game yang saya berikan sebelumnya ke dalam file tersebut
3. Simpan file
4. Jalankan game dengan:

**Windows:**
```bash
python game_balapan.py
```

**macOS/Linux:**
```bash
python3 game_balapan.py
```

## Troubleshooting

Jika mengalami masalah:

1. **Error module not found**: Pastikan Pygame terinstall dengan benar
   ```bash
   pip install --upgrade pygame
   ```

2. **Python tidak dikenali**: Pastikan Python sudah ditambahkan ke PATH

3. **Game tidak muncul**: Coba jalankan sebagai administrator (Windows) atau dengan sudo (Linux/macOS)

## Opsi Lain: Menggunakan IDE

Anda juga bisa menggunakan IDE seperti:
- Visual Studio Code (dengan ekstensi Python)
- PyCharm
- Thonny

Caranya:
1. Install IDE pilihan Anda
2. Buat project baru
3. Buat file Python baru
4. Salin kode game
5. Jalankan melalui menu Run/Run Module

Apakah Anda memerlukan penjelasan lebih detail tentang salah satu langkah di atas?
