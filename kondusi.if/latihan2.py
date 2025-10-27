print("Program mengurutkan data")

n = int(input("Masukkan jumlah bilangan (minimal 3): "))

bilangan = []
for i in range(n):
    angka = int(input(f"Bilangan ke-{i+1}: "))
    bilangan.append(angka)

bilangan.sort()

print("Urutan bilangan:", *bilangan)
