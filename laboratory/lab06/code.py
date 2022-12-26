# Laboratory Work
# Theme: Distribution of numbers into factors
# Author: Vladimir Doborschuk

# --- Modules ---

import numpy as np

# --- Functions ---

# --- mod(a, b) ---

def mod(a ,b):
	return a % b

# --- Pollard's P-method ---

'''
n - целое число
c - начальное значение
f - сжимающая функция
'''
def pollard(n: int, c: int, f):
    d = 1
    cnt = 0
    a, b = c, c
    
    print(f"a = {a}, b = {b}")
    
    while d == 1:
        a = mod(f(a), n)
        b = mod(f(b), n)
        d = np.gcd(a - b, n)
        
        if mod(cnt, 100) == 0 or d != 1:
            print(f"iteration {cnt+1}: a = {a}, b = {b}, d = {d}")

        cnt += 1
        
    if d == n:
        print("Делитель не найден")
        return None
    
    return d

# --- Test ---

def pollard_test(n, c):
    print(f'Поллард {n}\n---------')
    f = lambda x: np.power(x, 2) + mod(np.random.randint(1, np.floor(np.sqrt(n))), n)
    p = pollard(n, c, f)
    
    if p != None:
        print(f'Нетривиальный делитель {n}: p = {p}')
        
    print(f'---------\n')

# --- Main ---

def main():
    pollard_test(1359331, 1)
    pollard_test(137, 5)
    pollard_test(322, 12)
    
if __name__ == "__main__":
    main()