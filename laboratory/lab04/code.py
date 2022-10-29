# Laboratory Work
# Theme: Greatest Common Divisor Algorithms
# Author: Vladimir Doborschuk

# --- Modules ---

# empty

# --- Functions ---

# --- Euclid Algorithm ---
def euclid(a: int, b: int):
    if a == 0 or b == 0:
        print("Non zero numbers should be used")
        return
    
    r_0 = a
    r_1 = b
    
    if a < b:
        r_0, r_1 = r_1, r_0
    
    while True:
        r =  r_0 % r_1
        if r == 0:
            return r_1
        
        r_0 = r_1
        r_1 = r
        
# --- Binary Euclid Algorithm ---
def binary_euclid(a: int, b: int):
    if a == 0 or b == 0:
        print("Non zero numbers should be used")
        return
    
    r_0 = a
    r_1 = b
    
    if a < b:
        r_0, r_1 = r_1, r_0
    
    g = 1
    
    while r_0 % 2 == 0 and r_1 % 2 == 0:
        r_0 = int(r_0 / 2)
        r_1 = int(r_1 / 2)
        g = 2*g
        
    u, v = r_0, r_1

    while u != 0:
        while u % 2 == 0:
            u = int(u / 2)
        while v % 2 == 0:
            v = int(v / 2)
        if u >= v:
            u = u - v
        else:
            v = v - u
        
    return g*v

# --- Extended Euclid Algorithm ---
def extended_euclid(a: int, b: int):
    if a == 0 or b == 0:
        print("Non zero numbers should be used")
        return
    
    r_0, r_1 = a, b
    
    x = [1, 0]
    y = [0, 1]
    
    if a < b:
        r_0, r_1 = r_1, r_0
        x, y = y, x
    
    while True:
        r =  r_0 % r_1
        if r == 0:
            return (r_1, x[1], y[1])
        
        q = int((r_0 - r)/r_1)
        r_0 = r_1
        r_1 = r
        
        x_ = x[0] - q*x[1]
        x[0] = x[1]
        x[1] = x_
        
        y_ = y[0] - q*y[1]
        y[0] = y[1]
        y[1] = y_
        
# --- Extended Binary Euclid Algorithm ---
def extended_binary_euclid(a: int, b: int):
    if a == 0 or b == 0:
        print("Non zero numbers should be used")
        return
    
    r_0 = a
    r_1 = b
    
    A, B, C, D = 1, 0, 0, 1
    
    if a < b:
        r_0, r_1 = r_1, r_0
    
    g = 1
    
    while r_0 % 2 == 0 and r_1 % 2 == 0:
        r_0 = int(r_0 / 2)
        r_1 = int(r_1 / 2)
        g = 2*g
        
    u, v = r_0, r_1

    while u != 0:
        while u % 2 == 0:
            u = int(u / 2)
            if A % 2 ==0 and B % 2 == 0:
                A = int(A / 2)
                B = int(B / 2)
            else:
                A = int((A + r_1) / 2)
                B = int((B - r_0) / 2)
        while v % 2 == 0:
            v = int(v / 2)
            if C % 2 ==0 and D % 2 == 0:
                C = int(C / 2)
                D = int(D / 2)
            else:
                C = int((C + r_1) / 2)
                D = int((D - r_0) / 2)
        if u >= v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B
        
    if a < b:
        C, D = D, C
    
    return (g*v, C, D)

# --- Tests ---

def test_euclid(a: list, b: list):
    print("EUCLID ALGORITHM\n---")
    result = list(map(lambda a, b: euclid(a, b), a, b))
    for i in range(0, len(a)):
        print(f'НОД({a[i]}, {b[i]}) = {result[i]}')
    print("---\n")
        
def test_binary_euclid(a: list, b: list):
    print("BINARY EUCLID ALGORITHM\n---")
    result = list(map(lambda a, b: binary_euclid(a, b), a, b))
    for i in range(0, len(a)):
        print(f'НОД({a[i]}, {b[i]}) = {result[i]}')
    print("---\n")

def test_extended_euclid(a: list, b: list):
    print("EXTENDED EUCLID ALGORITHM\n---")
    result = list(map(lambda a, b: extended_euclid(a, b), a, b))
    for i in range(0, len(a)):
        print(f'НОД({a[i]}, {b[i]}) = {a[i]} * ({result[i][1]}) + {b[i]} * ({result[i][2]}) = {result[i][0]}')
    print("---\n")
  
def test_extended_binary_euclid(a: list, b: list):
    print("EXTENDED BINARY EUCLID ALGORITHM\n---")
    result = list(map(lambda a, b: extended_binary_euclid(a, b), a, b))
    for i in range(0, len(a)):
        print(f'НОД({a[i]}, {b[i]}) = {a[i]} * ({result[i][1]}) + {b[i]} * ({result[i][2]}) = {result[i][0]}')
    print("---\n")

# --- Main ---

def main():
    a = [16, 3, 91]
    b = [20, 21, 105]
    
    test_euclid(a,b)
    test_binary_euclid(a,b)
    test_extended_euclid(a,b)
    test_extended_binary_euclid(a,b)

if __name__ == "__main__":
    main()
