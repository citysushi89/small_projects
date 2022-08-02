# encoderDecoder, encodes or decodes user inputted Text
# NOTE: Morse Code uses periods (.) and regular dashes (-), | is the break character

import pyperclip


# list alphabet
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# dict morse code
MORSE_CODE_DICT = {"a": ".-|", "b": "-...|", "c": "-.-.|", "d": "-..|", "e": ".|", "f": "..-.|", "g": "--.|",
                   "h":	"....|", "i": "..|", "j": ".---|", "k": "-.-|", "l": ".-..|", "m": "--|", "n": "_.|",
                   "o":	"---|", "p": ".--.|", "q": "--.-|", "r": ".-.|", "s": "...|", "t": "-|", "u": "..-|",
                   "v":	"... -|", "w": ".--|", "x": "-..-|", "y": "-.--|", "z": "--..|"}


while True:
    # ask user for input conditions
    user_input = input("Input the message you would like to type here: ").lower()
    encryption_or_decryption = input("Do you want to encrypt or decrypt?:").lower()
    user_method = input("Would you like to Use Morse Code or the Caesar Cipher?").lower()
    # Get the key to encrypt/decrypt Caesar Cipher with
    if user_method == "caesar cipher":
        while True:
            try:
                key = int(input("Please enter the key (0 to 25) to use."))
                break
            except ValueError:
                print("Invalid input, select a integer in the range (0 to 25)")


    # If Morse Code AND encryption
    if user_method == "morse code" and encryption_or_decryption == "encrypt":
        # Converting user input into a list to make it iterable
        # (Have to put this in the if statements because it messes with decrpyting Morse Code)
        user_input_list = [item for item in user_input]
        morse_code_output = ""
        for item in user_input_list:
            if item in MORSE_CODE_DICT:
                new_item = MORSE_CODE_DICT[item]
            elif item == " ":
                new_item = " "
            else:
                new_item = item
            morse_code_output += new_item
        pyperclip.copy(morse_code_output)
        print(morse_code_output)
        print(f"Fully {encryption_or_decryption}ed {user_method} text copied to clipboard.")

    # If Morse Code AND decryption
    elif user_method == "morse code" and encryption_or_decryption == "decrypt":
        morse_code_output = ""
        # set up getting keys based on values
        keys_list = list(MORSE_CODE_DICT.keys())
        values_list = list(MORSE_CODE_DICT.values())
        # temp_list allows for the Morse Code to be grouped appropriately then checked against its letter counterpart
        temp_string = ""

        for item in user_input:
            temp_string += item
            for value in values_list:
                if temp_string == value:
                    position = values_list.index(temp_string)
                    # Add letter to output
                    morse_code_output += keys_list[position]
                    # Clear temp string for next letter
                    temp_string = ""
                # If the string is a space
                elif temp_string == " ":
                    morse_code_output += " "
                    temp_string = ""
        print(morse_code_output)
        pyperclip.copy(morse_code_output)
        print(f"Fully {encryption_or_decryption}ed {user_method} text copied to clipboard.")

    # If Caesar Cipher AND encryption
    elif user_method == "caesar cipher" and encryption_or_decryption == "encrypt":
        message_encoded_list = []
        message_encoded_string = ''
        message_decoded_list = []
        message_decoded_string = ''
        for item in user_input:
            if item == " ":
                message_encoded_list.append(item)
                pass
            else:
                new_letter_index = (int(ALPHABET.index(item)) + int(key)) % len(ALPHABET)
                message_encoded_list.append(ALPHABET[new_letter_index])

        # Compiling and printing the encoded message
        for letter in message_encoded_list:
            message_encoded_string += letter
        pyperclip.copy(message_encoded_string)
        print(message_encoded_string)
        print("Full encrypted text copied to clipboard.")
        print(f"Fully {encryption_or_decryption}ed {user_method} text copied to clipboard.")

    # If Caesar Cipher AND decryption
    elif user_method == "caesar cipher" and encryption_or_decryption == "decrypt":
        message_encoded_list = []
        message_encoded_string = ''
        message_decoded_list = []
        message_decoded_string = ''
        for item in user_input:

            if item == " ":
                message_decoded_list.append(item)
            else:
                new_letter_index = (int(ALPHABET.index(item)) - int(key)) % len(ALPHABET)
                message_decoded_list.append(ALPHABET[new_letter_index])

        # Compiling and printing the decoded message
        for letter in message_decoded_list:
            message_decoded_string += letter
        pyperclip.copy(message_decoded_string)
        print(message_decoded_string)
        print("Full decrypted text copied to clipboard.")
        print(f"Fully {encryption_or_decryption}ed {user_method} text copied to clipboard.")
    else:
        print("Failed, please input valid options")

    repeat = input("Do you have another message to encrypt or decrypt? Y/N").lower()
    if repeat == "y" or repeat == "yes":
        continue
    else:
        break
