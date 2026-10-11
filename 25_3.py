# sh3
# morse
MORSE_DICT = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 
    'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 
    'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 
    'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 
    'Ю': '..--', 'Я': '.-.-',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# rev
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_DICT.items()}

def encrypt_morse(text):
    result = []
    # upper
    for char in text.upper():
        if char == ' ':
            result.append('|')  # sep if space
        elif char in MORSE_DICT:
            result.append(MORSE_DICT[char])
    # sep in word
    return ' '.join(result)

def decrypt_morse(morse_code): # text
    result = []
    # separate
    words = morse_code.split(' | ')
    
    for word in words:
        decoded_word = []
        # find char
        chars = word.split(' ')
        for char in chars:
            if char in REVERSE_MORSE_DICT:
                decoded_word.append(REVERSE_MORSE_DICT[char])
        result.append(''.join(decoded_word))
        
    # build
    return ' '.join(result)

# launch
original_text = "хеллоу ворлд 123123 ааа"

# enc
encrypted = encrypt_morse(original_text)
print("Text: ", original_text)
print("Encrypted: ", encrypted)

# dec
decrypted = decrypt_morse(encrypted)
print("Decrypted: ", decrypted)
