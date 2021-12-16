# Repository Analisis Sentimen Ulasan Aplikasi Classroom di Google PlayStore Menggunakan SVM & Logistic Regression
Repository ini merupakan repository dokumentasi dalam melakukan analisis sentimen menggunakan SVM & Logistic Regression pada ulasan aplikasi classroom di google playstore
```bash 

Disusun Oleh Kelompok 1: 
1. Aqiel Mubarok (7A PSTI)
2. Dodi Muhamad Iqbal (7B PSTI)
```
## Background
Era pandemi covid-19 berdampak buruk bagi masyarakat dunia dan mengakibatkan  berbagai sektor terkena imbas adanya virus corona baik dari sektor keuangan maupun sektor pendidikan. Segala aktivitas harus dilakukan secara daring atau Work From Home salah satunya adalah lembaga-lembaga sekolah terpaksa melakukan pembelajaran secara online hal tersebut dikarenakan sebagai upaya mencegah penyebaran virus covid-19. Banyaknya platform-platform online dapat memudahakan sarana pembelajaran daring salah satunya adalah Platform Google Classrooom. Penggunaan Google Classroom dinilai baik karena dalam penggunaanya memliki banyak fitur untuk melaksanakan pembelajara daring. Namun nyatanya sebuah inovasi sistem ini terkdang tidak semuanya menerima dan beranggapan aplikasi ini sangat efektif untuk digunakan. dari banyaknya ulasan pengguna terhadap aplikasi GC masih banyak yang mengeluh dengan memberikan ulasan negatif tetapi juga tidak sedikit merekan bernaggapan positif. Oleh karena itu dengan adanya sentiment analysis ini dapat memberikan informasi terkait anggapan pungguna bernilai postif maupun neagtif terhadap aplikasi Google Classroom.

## Objective
Analisis sentiment ini dilakukan untuk mengetahui tingkat akurasi sentiment dari kedua model yaitu SVM dan Logistic Regression

## Project Structure
1. Folder data. Berisikan file data mentah atau proses pradataset

   [`proses_pradataset.csv`](./data/proses_pradataset.csv)
  
2. Folder model. berisikan file hasil training model

   [`logistic_regression.py`](./model/logistic_regression.py)
   
   Hasil training model Logistic Regression
   
   [`support_vector_machine.py`](./model/support_vector_machine.py)
   
   Hasil training model Support Vectore Machine
   
3. Folder output. berisikan file dataset yang digunakan untuk analisis sentimen

   [`hasil_proses_pradataset.tsv`](./output/hasil_proses_pradataset.tsv)
   
4. Folder src. Berisikan file-file notebook atau python, diantaranya:

   [`dataset_ulasan_aplikasi_classroom.py`](./src/dataset_ulasan_aplikasi_classroom.py)

   Notebook yang digunakan untuk scrapping data
   
   [`sentimen_analysis_classroom.py`](./src/sentimen_analysis_classroom.py)

   Notebook yang digunakan untuk analisis sentimen dan pre-processing data
   
## Metrics
Matrics yang kami gunakan ialah metrics accuracy
```bash 
#Build Classfier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.80)
```
