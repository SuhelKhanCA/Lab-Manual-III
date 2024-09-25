def encrypt(main_string, symbol):
      
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol
    return encrypted_string

def decrypt(encrypted_string, symbol):
  
    # Split the string using the symbol and filter out empty strings
    decrypted_string = ''.join(part for part in encrypted_string.split(symbol) if part)
    return decrypted_string

def main():
    # Input main string and symbol for encryption
    main_string = input("Enter the main string: ")
    symbol = input("Enter the symbol to embed: ")

    # Encrypt the string
    encrypted_string = encrypt(main_string, symbol)
    print(f"Encrypted String: {encrypted_string}")

    # Decrypt the string
    decrypted_string = decrypt(encrypted_string, symbol)
    print(f"Decrypted String: {decrypted_string}")

if __name__ == "__main__":
    main()
