alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#importing art from art.py
from art import logo
print(logo)

#functions
def caesar(text,shift,direction):
    text_list =""
    if direction == "decode":
        shift *= -1
    
    for letter in text:
        if letter in alphabet:
            num = alphabet.index(letter)
            new_pos = (num+shift) % 26
            text_list += alphabet[new_pos]
        else:
            text_list += letter
            #python have negative index of list means list[-1] means last element of list
            # if (new_pos) >= 0:
            #     text_list += alphabet[new_pos]
            # else:
            #     new_pos = new_pos + 26
            #     text_list += alphabet[new_pos]
        
    print(f"Your {direction}ed message is: {text_list}.\n")    
#call the caesar function here
option = "yes"

while option == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the Security Key: "))
    
    caesar(text ,shift, direction)
    
    option = input("Do you want to use the Encryption/Decryption tool again Yes | No : ").lower()

print("\nSayoNara!!\n")