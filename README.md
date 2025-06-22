Tentu, ini versi lengkap README-nya yang bisa kamu *copy-paste* langsung ke GitHub:

```markdown
# 🧬 Genetic Algorithm untuk Traveling Salesman Problem (TSP)

Proyek ini merupakan implementasi algoritma genetika untuk menyelesaikan *Traveling Salesman Problem* (TSP) menggunakan Python. Dataset yang digunakan berasal dari [Kaggle TSP Dataset](https://www.kaggle.com/datasets/mexwell/traveling-salesman-problem), berisi koordinat 2D dari sejumlah kota.

---

## 📌 Deskripsi Proyek

- Membangun model *Genetic Algorithm* (GA) untuk mencari rute optimal TSP
- Menggunakan dataset `.csv` berisi titik koordinat kota
- Menampilkan rute terbaik hasil optimasi dan grafik konvergensi nilai fitness
- Proyek ini cocok untuk pembelajaran tentang algoritma optimasi, metaheuristik, dan AI

---

## 🧠 Metode: Genetic Algorithm (GA)

- **Representasi kromosom**: urutan indeks kota (*list of integers*)
- **Inisialisasi populasi**: secara acak
- **Seleksi**: tournament selection
- **Crossover**: ordered crossover (OX)
- **Mutasi**: swap mutation
- **Evaluasi**: total jarak tempuh rute
- **Output**: rute terpendek, visualisasi rute optimal, dan grafik konvergensi fitness

---

## 📁 Struktur Direktori

```bash
.
├── TSP.py            # Script utama untuk menjalankan GA
├── medium (1).csv    # Dataset koordinat kota (tanpa header)
└── README.md         # Dokumentasi proyek
```

---

## ▶️ Cara Menjalankan

1. **Instalasi dependensi:**

   ```bash
   pip install pandas numpy matplotlib
   ```

2. **Eksekusi program:**

   ```bash
   python TSP.py
   ```

> 🔔 Pastikan file `medium (1).csv` berada di direktori yang sesuai dengan `file_path` pada script.

---

```

