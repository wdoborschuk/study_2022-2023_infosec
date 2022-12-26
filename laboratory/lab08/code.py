# Laboratory Work
# Theme: Arithmetic for big numbers
# Author: Vladimir Doborschuk

# --- Functions ---

def mod(a ,b):
	return a % b

def big_sum(u, v, b):
    u_ = str(u)
    v_ = str(v)
    
    j = len(u_) - 1
    
    if j != len(v_) - 1:
        print("bad N")
        return None
    
    k = 0
    
    w = ""
    
    while j >= 0:
        w_ = mod(int(u_[j]) + int(v_[j]) + k, b)
        w += str(w_)
        k = (int(u_[j]) + int(v_[j]) + k) // b
        j = j - 1
    
    w += str(k)
    return int(w[::-1])

def big_differ(u, v, b):
    u_ = str(u)
    v_ = str(v)
    
    j = len(u_) - 1
    
    if j != len(v_) - 1:
        print("bad N")
        return None
    
    k = 0
    
    w = ""
    
    while j >= 0:
        w_ = mod(int(u_[j]) - int(v_[j]) + k, b)
        w += str(w_)
        k = (int(u_[j]) - int(v_[j]) + k) // b
        j = j - 1

    return int(w[::-1])

def big_multiple(u, v, b):
    u_ = str(u)
    v_ = str(v)
    
    j = len(v_) - 1
    w = [0] * (j * len(u_))
    
    while j >= 0:
        if v_[j] == 0:
            w[j] = 0
            j = j - 1
        else:
            i = len(u_) - 1
            k = 0
            while i >= 0:
                t = int(u_[i]) * int(v_[j]) + w[i+j] + k
                w[i+j] = mod(t, b)
                k = t // b
                i = i - 1
            w[j] = k
            j = j - 1

    return int("".join(list(map(str, w))))

# --- Main ---

def main():
    x = 874
    y = 775
    
    print(f"Sum: {x} + {y} (10)")
    print(big_sum(x, y, 10))
    
    print(f"Differ: {x} - {y} (10)")
    print(big_differ(x, y, 10))
    
    print(f"Multiplication: {x} * {y} (10)")
    print(big_multiple(x, y, 10))
    
if __name__ == "__main__":
    main()