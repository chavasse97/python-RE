# 1
text = "УВИДИМ ВАДИМА И УДИВИМ"
freqs = {}
for char in text:
    if char in freqs:
        freqs[char] += 1
    else:
        freqs[char] = 1

# [вес, [символы], {коды}]
nodes = []
for char, weight in freqs.items():
    nodes.append([weight, [char], {char: ""}])

# build
while len(nodes) > 1:
    # weight sort
    for i in range(len(nodes)):
        for j in range(0, len(nodes) - i - 1):
            if nodes[j][0] > nodes[j + 1][0]:
                nodes[j], nodes[j + 1] = nodes[j + 1], nodes[j]
    
    # lowest weight
    left = nodes.pop(0)
    right = nodes.pop(0)
    
    # prefix
    for char in left[2]:
        left[2][char] = "0" + left[2][char]
    for char in right[2]:
        right[2][char] = "1" + right[2][char]
        
    # combine
    combined_weight = left[0] + right[0]
    combined_chars = left[1] + right[1]
    
    # corts+codes
    combined_codes = left[2]
    for char, code in right[2].items():
        combined_codes[char] = code
        
    nodes.append([combined_weight, combined_chars, combined_codes])

# final codes
huff_codes = nodes[0][2]

# launch
print("Table of freq and codes:")
for char in freqs:
    print(f"Char: '{char}' | Freq: {freqs[char]} | Code: {huff_codes[char]}")
print('\nMessage:', end=' ')

for char in text:
    print(huff_codes[char], end=' ')
print('\nРавномерно: 22 символа * log2(7) бит = 22 * 3 = 66 бит')
print('Наш размер: 2*3 + 3*3 + 6*2 + 3*3 + 3*3 + 3*3 + 2*3 = 6+9+12+9+9+9+6 = 60 бит')
