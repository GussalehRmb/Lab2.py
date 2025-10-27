# NAMA  : AGUS SALEH RUMBOUW
# NIM   : 312510465
# KELAS : TI.25.A.2
# MATKUL: PENGANTAR PEMROGRAMAN

# Latihan1
## menentukan bilangan terbesar dari 4 bilangan menggunakan statement if <a href="https://github.com/GussalehRmb/Latihan_1">Latihan1</a>
## Tujuan
<pre>Membuat program Python sederhana yang meminta input 4 bilangan, kemudian menentukan bilangan yang paling besar menggunakan statement if.</pre>

## Lankah Lankah Pembuatanya
<pre>1. Buka VS Code di laptop jika sudah terinstall dan python 
   Buatkan folder project baru dengan nama misalkan 'latihan1.py'
2. buat file pyton dan didalam nama file itu misalkan nama filenya "latihan1.py"
3. Tuliskan kode berikut ke dalam file "latihan1.py"
4. setelah itu jalankan proramnya di bagian terminal, tekan titik tiga masuk ke terminal dan jalankan terminal baru.
5. terakhir tentukan bilangan besar dari ke 4 bilangan yang di masukan</pre>

## Menentukan nilai besar dari bilangan yang di inputkan

<pre>a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

terbesar = a

if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d

print("Bilangan terbesar adalah:", terbesar)</pre>

Jalankan di terminal "Contoh" :
<pre>masukan bilangan pertama : 15
masukan bilangan kedua : 10
masukan bilangan ketiga : 25
masukan bilangan keempat : 20
  Bilangan terbesar adalah : 25</pre>
# Selesai

# Latihan2 
## Mengurutkan Data <a href="https://github.com/GussalehRmb/Latihan.2/blob/main/latihan2.py">Latihan2</a>
Membuat program Python untuk <b>mengurutkan beberapa data angka</b> berdasarkan nilai input (menimal tiga angka) secara berurutan <b>dari nilai kecil.</b>

## cara membuat file program 
<pre><ul><li>Buka Visual Studio Code (VSC) di laptop
<li> buat folder baru di file manejer 
<li>Contoh filenya misalkan (Latihan2.py)
<li>masukan filenya ke visual studio code.
<li>dan buatkan file Latihan2.py itu di bagian VSC yang sudah dibuat</pre>

## Menginput Program
<pre><li>ketika sudah buatkan foldernya selanjutnya masukan kode program pythonnya dan jalankan programnya.
<li>tetukan hasil programnya di bagian terminal.
<li><b>contoh pada gambar di bawah ini.</pre>
### Contoh Pada Bagian Bawah Ini
<pre>print("Program mengurutkan data")

n = int(input("Masukkan jumlah bilangan (minimal 3): "))

bilangan = []
for i in range(n):
    angka = int(input(f"Bilangan ke-{i+1}: "))
    bilangan.append(angka)

bilangan.sort()

print("Urutan bilangan:", *bilangan)</pre>
### Output Yang Dihasilkan
<pre>Masukan Jumlah bilangan (menimal 3) : 4
Bilangan ke-1: 12
Bilangan ke-2: 10
Bilangan ke-3: 19
Bilangan ke-4: 5
Urutan bilangan: 5 10 12 19</pre>
## Selesai

# Latihan1 
## Program Perulangan Bertingkat (Nested Loop)
###  Deskripsi
Program ini merupakan implementasi perulangan bertingkat (nested loop) yang menghasilkan pola angka berdasarkan penjumlahan indeks baris dan kolom.

### Tujuan Pembelajaran
<li>Memahami konsep perulangan bertingkat (nested loop)
<li>Menerapkan perulangan for dalam Python
<li>Memahami format output dan manipulasi tampilan data

### Algoritma
<li> Perulangan Baris: Iterasi dari baris ke-0 hingga baris ke-9
<li>Perulangan Kolom: Untuk setiap baris, iterasi dari kolom ke-0 hingga kolom ke-9
<li>Perhitungan Nilai: Nilai setiap sel = indeks baris + indeks kolom
<li>Output: Tampilkan nilai dengan format rata kanan selebar 4 karakter</li>

### Rumus
<pre>Nilai [i] [j] = i + j</pre>
<li>dengan nilai i = index baris 0-9
<li>dan nilai j = index kolam 0-9</li>

### Cara Menjalankan
<li>simpan file program ini dengan nama Perulangan1.py
<li> Pastikan filenya sudah tersimpan
<li>Jalankan programnya di bagian terminal Visual Studio Code (VS Code)</pre>

### Contoh Bagian programnya
print("Output Perulangan Bertingkat (Nested Loop)")

<pre>for baris in range(10):
    for kolom in range(10):
        nilai = baris + kolom
    
        print(f"{nilai:4}", end="")
    
    print()

print("\nPenjelasan:")
print("- Baris ke-i dan kolom ke-j menghasilkan nilai i + j")
print("- Baris 0: 0+0=0, 0+1=1, 0+2=2, ..., 0+9=9")
print("- Baris 1: 1+0=1, 1+1=2, 1+2=3, ..., 1+9=10")
print("- Dan seterusnya...")</pre>

###  Output Yang Dihasilkan
Program akan menghasilkan matriks 10x10 dengan pola sebagai berikut:

<pre>0   1   2   3   4   5   6   7   8   9
1   2   3   4   5   6   7   8   9  10
2   3   4   5   6   7   8   9  10  11
3   4   5   6   7   8   9  10  11  12
4   5   6   7   8   9  10  11  12  13
5   6   7   8   9  10  11  12  13  14
6   7   8   9  10  11  12  13  14  15
7   8   9  10  11  12  13  14  15  16
8   9  10  11  12  13  14  15  16  17
9  10  11  12  13  14  15  16  17  18</pre>

### Latihan Perulangan1 Selesai

# Latihan2 
## Perulangan Bilangan Acak
### Menentukan Bilangan n bilangan acak yang nilainya lebih kecil dari 0.5.

### Output Program
<pre>Masukan jumlah n: 4
masukan jumlah n 4
0.303925811026019694
0.3550714579296446
0.20838127205617663
0.2561750761891125</pre>

### Cara kerja program
1. Import Library Random
<pre>import random</pre>
Library untuk menghasilkan bilangan acak.

2. Input Runtime
<pre>n = int(input("Masukkan jumlah n: "))</pre>
Program meminta user memasukkan nilai n saat program berjalan.

3. Kombinasi While dan For Loop

<pre>count = 0
while count < n:
    for i in range(1):
        random_num = random.random()
        if random_num < 0.5:
            print(random_num)
            count += 1
            if count >= n:
                break</pre>

<b>Penjelasan alur:</b>

<li>count = 0 → Inisialisasi counter
<li>while count < n → Loop sampai dapat n bilangan
<li>for i in range(1) → Loop for di dalam while (kombinasi while-for)
<li>random.random() → Generate bilangan acak 0.0 - 1.0
<li>if random_num < 0.5 → Filter hanya bilangan < 0.5
<li>count += 1 → Tambah counter jika memenuhi syarat
<li>break → Keluar dari for loop jika sudah dapat n bilangan</li>

### Mengapa Kombinasi While dan For?

<li>While loop: Memastikan kita mendapat tepat n bilangan yang memenuhi syarat
<li>For loop: Digunakan dalam proses generate bilangan acak
<li>Kombinasi keduanya memenuhi persyaratan tugas

### Cara Menjalankan
<li>Pastikan filenya sudah tersimpan
<li>kemudian Run/Jalankan program di bagian VSC
<li>Tampilan jumlah akan muncul di bagian terminal 

## Selesai