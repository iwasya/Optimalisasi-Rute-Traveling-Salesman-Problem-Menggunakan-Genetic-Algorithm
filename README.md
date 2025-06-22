# 🧬 Genetic Algorithm untuk Traveling Salesman Problem (TSP)

Proyek ini merupakan implementasi algoritma genetika untuk menyelesaikan permasalahan Traveling Salesman Problem (TSP) menggunakan Python. Dataset digunakan berasal dari [Kaggle TSP Dataset](https://www.kaggle.com/datasets/whenamancodes/traveling-salesman-problem) yang berisi koordinat 2D dari beberapa kota.

---

## 📌 Deskripsi Proyek

- Membangun model Genetic Algorithm (GA) untuk mencari rute optimal dari TSP.
- Menggunakan dataset nyata dalam format `.csv` berisi titik koordinat kota.
- Menampilkan rute terbaik hasil optimasi dan grafik konvergensi fitness.
- Cocok untuk pembelajaran tentang optimasi, metaheuristik, dan AI.

---

## 🧠 Metode: Genetic Algorithm (GA)

- **Representasi kromosom**: urutan indeks kota (list integer)
- **Inisialisasi populasi**: acak
- **Seleksi**: tournament selection
- **Crossover**: ordered crossover (OX)
- **Mutasi**: swap mutation
- **Evaluasi**: total jarak tempuh
- **Output**: rute terpendek, visualisasi rute & grafik fitness

---

## 📁 Struktur File

```bash
.
├── TSP.py                   # Script utama untuk menjalankan GA
├── medium (1).csv           # Dataset koordinat kota (tanpa header)
└── README.md                # Dokumentasi proyek

▶️ Cara Menjalankan
Pastikan sudah menginstal dependensi:

bash
Copy
Edit
pip install pandas numpy matplotlib
Jalankan script Python:

bash
Copy
Edit
python TSP.py
Pastikan file medium (1).csv berada di path yang sesuai dengan file_path di script.


