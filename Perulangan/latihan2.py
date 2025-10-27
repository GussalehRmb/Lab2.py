import random

def generate_random_numbers():

    n = int(input("Masukkan jumlah n: "))
    print(f"masukkan jumlah n {n}")
    
    count = 0
    
    while count < n:
    
        for i in range(1):
            random_num = random.random()  
    
            if random_num < 0.5:
                print(random_num)
                count += 1
                
                if count >= n:
                    break

if __name__ == "__main__":
    generate_random_numbers()