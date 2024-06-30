# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan pada Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis

Tingkat dropout yang tinggi ini menjadi masalah signifikan bagi Jaya Jaya Institut, karena tidak hanya mempengaruhi citra dan reputasi institusi, tetapi juga berdampak pada efisiensi operasional dan keberhasilan akademik secara keseluruhan. Untuk mengatasi masalah ini, Jaya Jaya Institut berupaya mendeteksi mahasiswa yang berpotensi dropout sejak dini agar dapat memberikan bimbingan khusus dan dukungan yang diperlukan, dengan tujuan mengurangi tingkat dropout dan meningkatkan keberhasilan akademik mahasiswa.

### Cakupan Proyek

Tujuan proyek:  mengurangi tingkat dropout di Jaya Jaya Institut melalui deteksi dini mahasiswa yang berpotensi tidak menyelesaikan pendidikan mereka berdasarkan parameter-parameter yang ada

Berikut adalah cakupan proyek yang dikerjakan:
1. Persiapan
   - menyiapkan library yang dibutuhkan
   - menyiapkan data yang digunakan
2. Data Understanding
   - cek data null
   - cek tipe data
   - mengubah typo
   - EDA
   - import data ke supabase
3. Data Preprocessing
   - train-test split
   - encoding & scaling
4. Modeling
   - model decision tree
   - model random forest
   - model gradient boosting
5. Evaluation
   - evaluasi model decision tree
   - evaluasi model random forest
   - evaluasi model gradient boosting

Hasil akhir proyek:
- dashboard untuk memahami dan memonitor performa mahasiswa
- model machine learning dalam bentuk prototype
- rekomendasi action items

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
#### Virtual Environment
1. Buat virtual environment (venv) pada direktori proyek
   ```
   python3 -m venv venv
   ```
2. Aktifkan virtual environment menggunakan command prompt
   ```
   .\venv\Scripts\activate
   ```
#### Library Installation
3. Install library yang digunakan pada proyek
   ```
   pip install -r requirements.txt
   ```
#### Running Streamlit
Jalankan prototype dengan menggunakan streamlit pada virtual environment yang sudah dibuat
```
streamlit run student_app.py
```
## Business Dashboard

- email metabase: farahfadhilah63@gmail.com
- password: Padparrr25

<div align="center">
   
![image](https://github.com/ffadhilah25/expert-submission2/blob/main/itspadpar-dashboard.jpg)

</div>

Informasi yang didapatkan pada dashboard, antara lain:
- banyaknya mahasiswa yang dropout
- rata-rata admission grade
- jumlah mahasiswa berdasarkan gender dan status
- attendance mahasiswa
- rata-rata umur saat enrollment berdasarkan gender
- pengelompokan application order
- rata-rata previous qualification grade
- banyaknya mahasiswa yang menjadi scholarship holder
- jumlah antara curricular units enrolled vs curricular units approved pada 1st semester
- jumlah antara curricular units enrolled vs curricular units approved pada 2nd semester

## PROTOTYPE

prototype dapat diakses pada: https://expert-submission2-zsak34g5kvhrawbbmmxxxd.streamlit.app/

<div>
   
![image](https://github.com/ffadhilah25/expert-submission2/blob/main/itspadpar-prototype.png)
 
</div>

Terdapat 5 bagian yang perlu diisi pada prototype, yaitu:
1. General information
   - gender
   - marital status
   - nationality
2. Parents information
   - mother's qualification
   - father's qualification
   - mother's occupation
   - father's occupation
3. Others
   - attendance
   - previous qualification
   - educational special needs
   - aplication mode
   - displaced
   - course
   - international student
   - previous qualification grade
   - admission grade
   - debtor
   - scholarship
   - tuition fees up to date
4. Study tracer
   - curricular units enrolled 1st semester
   - curricular units evaluated 1st semester
   - curricular units approved 1st semester
   - curricular units grade 1st semester
   - curricular units enrolled 2nd semester
   - curricular units evaluated 2nd semester
   - curricular units approved 2nd semester
   - curricular units grade 2nd semester
5. Additional information
   - application order
   - age at enrollment
   - unemployement rate
   - inflation rate
   - GDP

Setelah seluruh data dimasukkan, data akan tertampilkan pada bagian 'View the Raw Data'
Untuk menjalankan prediksi, tekan tombol 'Predict' dan akan didapatkan hasil:
- view the preprocessed data
- status mahasiswa (Graduate, Enrolled, Dropout)

## Conclusion

Model machine learning yang digunakan untuk pembuatan prototype adalah model random forest, karena memberikan accuracy yang paling baik dibandingkan dengan 2 model lainnya.

Feature numerikal yang digunakan untuk menyusun model machine learning:
- Curricular_units_1st_sem_enrolled
- Curricular_units_1st_sem_evaluations
- Curricular_units_1st_sem_approved
- Curricular_units_1st_sem_grade
- Curricular_units_2nd_sem_enrolled
- Curricular_units_2nd_sem_evaluations
- Curricular_units_2nd_sem_approved
- Curricular_units_2nd_sem_grade
- Admission_grade
- GDP
- Age_at_enrollment
- Previous_qualification_grade

Faktor yang memengaruhi banyaknya mahasiswa dropout berdasarkan machine learning:
- tuitions fees: banyak mahasiswa dropout karena terkendala dalam membayar uang kuliah (menunggak)
- scholarship: mahasiswa yang tidak mendapatkan beasiswa banyak yang dropout
- both father's and mother's qualification and occupation: kualifikasi dan pekerjaan orang tua (seperti orang tua tidak bisa membaca dan menulis, pekerjaan orang tua yang berupa siswa atau bahkan pegawai yang tidak terampil) menjadi alasan lain banyak mahasiswa yang dropout

### Rekomendasi Action Items

Beberapa hal yang mungkin dapat diterapkan oleh pihak institusi:
- mengadakan aju banding untuk pembayaran tuition fees: agar mahasiswa bisa melakukan pencicilan dalam membayar uang kuliah, disertai dengan syarat-syarat yang memadai (seperti bukti kondisi keuangan, dll)
- membuka lebih banyak scholarship: agar mahasiswa lainnya dapat menjadi penerima beasiswa dan memberikan peluang agar dapat lulus (disertai dengan syarat-syarat yang mudah untuk diikuti mahasiswa)
- memberikan kelas tambahan bagi mahasiswa (untuk mahasiswa dg kualifikasi dan pekerjaan orangtuanya yang kurang baik): agar mahasiswa mendapatkan insight lain (pembelajaran-pembelajaran lain) yang tidak diberikan oleh orang tuanya, kelas tambahan dapat berupa kelas kepemimpinan, dll.
