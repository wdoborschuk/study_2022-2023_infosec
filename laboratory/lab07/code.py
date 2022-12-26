# Laboratory Work
# Theme: Discrete logarthmification
# Author: Vladimir Doborschuk

# --- Modules ---

import numpy as np

# --- Functions ---

# --- mod(a, b) ---

def mod(a ,b):
	return a % b

# --- find mod order ---

def order(a, p):
    x = 1
    while mod(a**x - 1, p) != 0:
        x += 1
        
    return x

# --- Pollard's P-method for Log ---

'''
a - основание
b - значение остатка
p - простое число
'''
def po_method(a: int, b: int, p: int):
    print(f"\n{a}^(x) = {b} mod {p}")
    print("-----------------------------------------------------------------")
    print('|\tc\t|\tlog c\t|\td\t|\tlog d\t|')
    print("-----------------------------------------------------------------")
    
    u = np.random.randint(4)
    v = np.random.randint(4)
    r = order(a, p)
    
    c = mod(np.power(a, u) * np.power(b, v), p)
    d = c
    
    u_c, u_d = u, u
    v_c, v_d = v, v
    
    print(f'|\t{c}\t|\t{u_c}+{v_c}x\t|\t{d}\t|\t{u_d}+{v_d}x\t|')
    
    def f(x, u_x, v_x):
        if x < r:
            return mod(a*x, p), u_x + 1, v_x
        else:
            return mod(b*x, p), u_x, v_x + 1            

    c, u_c, v_c = f(c, u_c, v_c)
    tmp_d = f(d, u_d, v_d)
    d, u_d, v_d = f(tmp_d[0], tmp_d[1], tmp_d[2])
    
    while mod(c, p) != mod(d, p):
        print(f'|\t{c}\t|\t{u_c}+{v_c}x\t|\t{d}\t|\t{u_d}+{v_d}x\t|')
        c, u_c, v_c = f(c, u_c, v_c)
        tmp_d = f(d, u_d, v_d)
        d, u_d, v_d = f(tmp_d[0], tmp_d[1], tmp_d[2])
        
    print(f'|\t{c}\t|\t{u_c}+{v_c}x\t|\t{d}\t|\t{u_d}+{v_d}x\t|')
    print("-----------------------------------------------------------------")
    
    x = 1
    # print(v_c - v_d, u_d - u_c)
    while mod((v_c - v_d)*x, r) != mod(u_d - u_c, r):
        x += 1
        
    print(f"x = {x}")
    print(f"\n{a}^({x}) = {b} mod {p}")
    print("-----------------------------------------------------------------")
    return x

# --- Main ---

def main():
    po_method(10, 64, 107)
    po_method(2, 1, 15)
    
    
if __name__ == "__main__":
    main()
