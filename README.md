# Repository Analisis Sentimen Ulasan Aplikasi Classroom di Google PlayStore Menggunakan SVM & Logistic Regression
Repository ini merupakan repository dokumentasi dalam melakukan analisis sentimen menggunakan SVM & Logistic Regression pada ulasan aplikasi classroom di google playstore
```bash 
Disusun Oleh Kelompok 1: 
1. Aqiel Mubarok (7A PSTI)
2. Dodi Muhamad Iqbal (7B PSTI)
```
## Objective
Analisis sentiment ini dilakukan untuk mengetahui tingkat akurasi sentiment dari kedua model yaitu SVM dan Logistic Regression

## Project Structure
1. Folder data. Berisikan file data mentah atau proses pradataset

   [`proses_pradataset.csv`](./data/proses_pradataset.csv)
  
2. Folder model. berisikan file hasil training model

   [`logistic_regression.py`](./model/Logistic Regression.py)
   
   Hasil training model Logistic Regression
   
   [`support_vectore_machine.py`](./model/Support Vector Machine.py)
   
   Hasil training model Support Vectore Machine
   
3. Folder output. berisikan file dataset yang digunakan untuk analisis sentimen

   [`hasil_proses_pradataset.tsv`](./output/hasil_proses_pradataset.tsv)
   
4. Folder src. Berisikan file-file notebook atau python, diantaranya:

   [`dataset_ulasan_aplikasi_classroom.py`](./src/dataset_ulasan_aplikasi_classroom.py)

   Notebook yang digunakan untuk scrapping data
   
   [`sentimen_analysis_classroom.py`](./src/sentimen_analysis_classroom.py)

   Notebook yang digunakan untuk analisis sentimen dan pre-processing data
