# Laboratory Work
# Theme: Prime Numbers Tests
# Author: Vladimir Doborschuk

# --- Modules ---

import numpy as np

# --- Functions ---

# --- Yakobi's Symbol ---
def yakobi(n: int, a: int):
    if n < 3:
        print("Число n должно быть больше или равно 3")
        return None
    
    if a < 0 or a >= n:
        print("Число a должны быть на интервале [0;n)")
        return None
    
    g = 1
    
    while a != 0 and a != 1:
        k = 0
        a_1 = a

        while divmod(a_1, 2)[1] != 1:
            a_1 = divmod(a_1, 2)[0]

        while (2**k)*a_1 != a:
            k += 1
        
        s = 1
        if k % 2 == 0:
            s = 1
        else:
            if (n == 1 % 8) or (n == -1 % 8):
                s = 1
            elif (n == 3 % 8) or (n == -3 % 8):
                s = -1
        
        if a_1 == 1:
            return g * s
        
        if (n == 3 % 4) and (a_1 == 3 % 4):
            s = -s

        a = n % a_1
        n = a_1
        g = g * s

    if a == 0:
        return 0
    else:
        return g

# --- Fermats Test ---
def fermats(n: int):
    if n % 2 == 0 or n < 5:
        return "Число " + str(n) + " составное"
    
    a = np.random.choice(range(2, n-1))
    
    if (a**(n-1)) % n == 1:
        return "Число " + str(n) + ", вероятно, простое"
    else:
        return "Число " + str(n) + " составное"
        
# --- Soloway-Shtrassen Test ---
def soloway_shtrassen(n: int):
    if n % 2 == 0 or n < 5:
        return "Число " + str(n) + " составное"
    
    a = np.random.randint(2, n-1)
    r = int((a**((n-1)/2)) % n)
    
    if r != 1 and r != (n - 1):
        return "Число " + str(n) + " составное"
        
    s = yakobi(n, a)
    if r == s % n:
        return "Число " + str(n) + " составное"
    else:
        return "Число " + str(n) + ", вероятно, простое"

# --- Miller-Rabin Test ---
def miller_rabin(n: int):
    if n % 2 == 0 or n < 5:
        return "Число " + str(n) + " составное"
    
    r = n - 1
    s = 0
    
    while divmod(r, 2)[1] != 1:
        r = divmod(r, 2)[0]

    while (2**s)*r != n-1:
        s += 1
    
    a = np.random.randint(2, n-1)
    y = (a**r) % n
    
    if y != 1 and y != n - 1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = (y**2) % n
            if y == 1:
                return "Число " + str(n) + " составное"
            j = j + 1
        if y != n - 1:
            return "Число " + str(n) + " составное"
    
    return "Число " + str(n) + ", вероятно, простое"

# --- Tests ---

# no tests

# --- Main ---

def main():
    n = [7, 8, 9, 11, 13, 17, 19, 20, 21, 31, 32]
    
    for n_i in n:
        print(f'\n----ЧИСЛО-{n_i}----\n')
        print(f'Тест Ферма: {fermats(n_i)}')
        print(f'Тест Соловэя-Штрассена: {soloway_shtrassen(n_i)}')
        print(f'Тест Миллера-Рабина: {miller_rabin(n_i)}')

if __name__ == "__main__":
    main()