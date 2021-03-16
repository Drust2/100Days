"""
Day 80 - Professional Portfolio 1 - Morse Code
Author: Juan Rodriguez
16/03/2021

Note: For this code, there is 1 space between letters and 3 spaces between words. 
This is useful to implement a decoding function and to make the message more realistic.

Mind that this code is missing some symbols.
To exit the code you can write 'exit' at the message prompt
"""
# 
# Creating a dictionary. This is a modified dictionary from https://www.geeksforgeeks.org/morse-code-translator-python/
morse_code_dict = { 'A': '.-', 'B': '-...', 
                    'C' :'-.-.', 'D': '-..', 'E': '.', 
                    'F': '..-.', 'G': '--.', 'H': '....', 
                    'I': '..', 'J': '.---', 'K': '-.-', 
                    'L': '.-..', 'M': '--', 'N': '-.', 
                    'O': '---', 'P': '.--.', 'Q': '--.-', 
                    'R': '.-.', 'S': '...', 'T': '-', 
                    'U': '..-', 'V': '...-', 'W': '.--', 
                    'X': '-..-', 'Y': '-.--', 'Z': '--..', 
                    '1': '.----', '2': '..---', '3': '...--', 
                    '4': '....-', '5': '.....', '6': '-....', 
                    '7': '--...', '8': '---..', '9': '----.', 
                    '0': '-----', ',': '--..--', '.': '.-.-.-', 
                    '?': '..--..', '/': '-..-.', '-': '-....-', 
                    '(': '-.--.', ')': '-.--.-', '&': '.-...',
                    ';': '-.-.-', '=': '-...-',
                    '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
                    '@': '.--.-.', '$': '...-..-', '!': '-.-.--'
                    } 

# Main function that controls the program. It's used to create recursion
run = True
def main(execution, message): 

    def encoding(to_encode): 
        transcript = ""
        for letter in to_encode:
            if letter == " ":
                transcript += "   "
            else:
                transcript += f" {morse_code_dict[letter]}"                
        return transcript
    
    def decoding(to_decode):
        transcript = ""
        decode_list = to_decode.split(" ")
        for i in range(1, len(decode_list)):
            if decode_list[i] == "":
                if decode_list[i-1] == "":
                    pass         
                else:
                    transcript += " "
            else:
                for key in morse_code_dict:
                    if morse_code_dict[key] == decode_list[i]:
                        transcript += key
        return transcript
    
    if execution == 1:
        encoded_message = encoding(message) 
    elif execution == 2:
        encoded_message = decoding(message)
        
    return encoded_message

# Execute the code until the user writes 'exit' at start
while run:
    try:
        to_encode = input('Please input the text to encode: ').upper()
        if to_encode == "":
            raise ValueError
    except ValueError:
        print("You must enter a message. Please, try again.")    
    else:
        if to_encode == 'EXIT':
            run = False
        else:
            encoded_message = main(execution=1, message=to_encode)
            print(f"\n{encoded_message}")
            decode_error = True
            while decode_error:
                try:
                    decode_prompt = input("Do you want to decode back this message? Press 'Y' for yes or 'N' to encode another message: ").lower()
                    if decode_prompt != 'y' and decode_prompt != 'n':
                        raise ValueError
                except ValueError:
                        print("Please enter a valid input")
                else:
                    if decode_prompt == 'y':
                        decoded_message = main(execution=2, message=encoded_message)
                        print(f"Here is the message once again decoded:\n{decoded_message}")
                        decode_error = False
                    else:
                        decode_error = False

