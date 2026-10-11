# 15
# 1010010111
# 1 2 3 4 5 6 7 8 9 1011121314
# ? ? 1 ? 0 1 0 ? 0 1 0 1 1 1
# 0 0 1 0 0 1 0 0 0 1 0 1 1 1

def get_control_bits_count(k):
    r = 1
    while (2 ** r) < (k + r + 1):
        r += 1
    return r

def encode_hamming(data_str):
    # code in 0 1
    data = [int(x) for x in data_str]
    k = len(data)
    r = get_control_bits_count(k)
    n = k + r
    
    code = [0] * n
    
    # info bits
    data_idx = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:  # controls
            continue
        code[i - 1] = data[data_idx]
        data_idx += 1
        
    # val control
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & pos:  # if pos controlled by bit
                if j != pos:
                    parity ^= code[j - 1]
        code[pos - 1] = parity
        
    return "".join(map(str, code))

def decode_and_correct(code_str, k):
    # errors
    code = [int(x) for x in code_str]
    n = len(code)
    r = get_control_bits_count(k)
    
    # synd
    syndrome = 0
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                parity ^= code[j - 1]
        if parity != 0:
            syndrome += pos
            
    # analyse
    if syndrome == 0:
        print("No errors found.")
    else:
        print(f"Single error in bit {syndrome}")
        # correct
        code[syndrome - 1] ^= 1
        print(f"Corrected code: {''.join(map(str, code))}")
        
    # msg
    original_data = []
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            original_data.append(code[i - 1])
            
    return "".join(map(str, original_data))

# launch
if __name__ == "__main__":
    message = "1010010111"
    print(f"Message: {message}")
    
    # code
    encoded = encode_hamming(message)
    print(f"Encoded message: {encoded}")
    print("-" * 50)
    
    corrupted_list = list(encoded)
    error_position = 6  # corrupted bit
    corrupted_list[error_position - 1] = '0' if corrupted_list[error_position - 1] == '1' else '1'
    corrupted = "".join(corrupted_list)
    
    print(f"Corrupted msg with error in {error_position}: {corrupted}")
    
    # decode
    decoded_message = decode_and_correct(corrupted, len(message))
    print(f"Corrected message: {decoded_message}")
