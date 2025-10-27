print("Output Perulangan Bertingkat (Nested Loop)")

for baris in range(10):
    for kolom in range(10):
        nilai = baris + kolom
    
        print(f"{nilai:4}", end="")
    
    print()

print("\nPenjelasan:")
print("- Baris ke-i dan kolom ke-j menghasilkan nilai i + j")
print("- Baris 0: 0+0=0, 0+1=1, 0+2=2, ..., 0+9=9")
print("- Baris 1: 1+0=1, 1+1=2, 1+2=3, ..., 1+9=10")
print("- Dan seterusnya...")