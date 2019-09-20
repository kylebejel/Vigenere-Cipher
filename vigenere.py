def encrypt(message, key):

    alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    key_index = 0
    new_message = ""

    for ch in message:
        new_ch = alph[(alph.index(ch) + (26 - alph.index(key[key_index])))%26]
        new_message += new_ch
        key_index = (key_index + 1)%len(key)

    print("Original Message: " + message + "\nNew Message: " + new_message)

def __main__():

     message = raw_input("Enter a message to encrypt: ").upper()
     key = raw_input("Enter a key: ").upper()
     encrypt(message, key)

if __name__ == '__main__':
    __main__()