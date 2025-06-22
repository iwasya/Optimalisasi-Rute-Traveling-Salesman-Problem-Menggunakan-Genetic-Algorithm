# 🧬 Genetic Algorithm untuk Traveling Salesman Problem (TSP)

Proyek ini merupakan implementasi algoritma genetika untuk menyelesaikan permasalahan Traveling Salesman Problem (TSP) menggunakan Python. Dataset digunakan berasal dari [Kaggle TSP Dataset](https://www.kaggle.com/datasets/mexwell/traveling-salesman-problem) yang berisi koordinat 2D dari beberapa kota.

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
```
▶️ Cara Menjalankan
Instalasi dependensi:

```bash
pip install pandas numpy matplotlib
```
Eksekusi program:
```bash
python TSP.py
```
> 🔔 Pastikan file medium (1).csv berada di direktori yang sesuai dengan file_path pada script.
![Screenshot 2025-06-22 213339](https://github.com/user-attachments/assets/60239b9f-8752-42e2-9367-b6fb8ac5513a)
![Screenshot 2025-06-22 213322](https://github.com/user-attachments/assets/0919b251-6560-4200-b424-51dd58c59412)
![Screenshot 2025-06-22 213305](https://github.com/user-attachments/assets/de5f928c-97fb-4273-8e0e-7f24ef1f170f)

