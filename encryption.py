def encrypt(text, n, m):
    encrypted_text = []

    for char in text:
        if char.islower():  
            if 'a' <= char <= 'm':  
                encrypted_text.append(chr((ord(char) - ord('a') + n * m) % 26 + ord('a')))
            elif 'n' <= char <= 'z':  
                encrypted_text.append(chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a')))
        elif char.isupper():  
            if 'A' <= char <= 'M':  
                encrypted_text.append(chr((ord(char) - ord('A') - n) % 26 + ord('A')))
            elif 'N' <= char <= 'Z':  
                encrypted_text.append(chr((ord(char) - ord('A') + m**2) % 26 + ord('A')))
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def decrypt(text, n, m):
    decrypted_text = []

    for char in text:
        if char.islower():  
            if 'a' <= char <= 'm':  
                decrypted_text.append(chr((ord(char) - ord('a') - n * m) % 26 + ord('a')))
            elif 'n' <= char <= 'z':  
                decrypted_text.append(chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a')))
        elif char.isupper():  
            if 'A' <= char <= 'M':  
                decrypted_text.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
            elif 'N' <= char <= 'Z':  
                decrypted_text.append(chr((ord(char) - ord('A') - m**2) % 26 + ord('A')))
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

def check_decryption(original_text, decrypted_text):
    return original_text == decrypted_text

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):

    with open(file_path, 'w') as file:
        file.write(content)

def main():
    try:
        n = int(input("Enter the value of n: "))
        m = int(input("Enter the value of m: "))
    except ValueError:
        print("Invalid input! Please enter integers for n and m.")
        return

    original_text = read_file("raw_text.txt")

    encrypted_text = encrypt(original_text, n, m)

    write_file("encrypted_text.txt", encrypted_text)

    decrypted_text = decrypt(encrypted_text, n, m)

    if check_decryption(original_text, decrypted_text):
        print("Decryption successful: The decrypted text matches the original.")
    else:
        print("Decryption failed: The decrypted text does not match the original.")

if __name__ == "__main__":
    main()
