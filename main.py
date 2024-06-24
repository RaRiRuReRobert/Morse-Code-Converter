# Morse Code Converter Project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '?', '!', ':',
            ]

morse_alphabet = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
    '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
    '/', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
    '.-.-.-', '--..--', '..--..', '..--.', '---...',
]


def to_morse(message):
    new_message = []
    for letter in list(message.lower()):
        position = alphabet.index(letter)
        # print(position)
        # print(morse_alphabet[position])
        new_message.append(morse_alphabet[position])
        # print(new_message)
    morse_message = ' '.join(new_message)
    print(f'Your morse code message is:\n {morse_message}')


def to_type(message):
    new_message = []
    for letter in message.split():
        position = morse_alphabet.index(letter)
        new_message.append(alphabet[position])
    plain_message = ''.join(new_message)
    print(f'Your deciphered message is:\n {plain_message}')


def morse_tool():
    tool = input('Would you like to encode a message to morse code or decode a message from morse code? (type "encode" or "decode"):\n ')
    if tool == 'encode':
        message = input('Please type the message you would like to convert to morse code:\n ')
        to_morse(message)
    elif tool == 'decode':
        message = input('Please type the morse code you would like to decode:\n ')
        to_type(message)
    else:
        print('please only type one of the options')
        morse_tool()

    again = input('Would you like to run this tool again? (type "y" or "n"):\n')
    if again == 'y':
        morse_tool()
    elif again == 'n':
        print("Thank you for using the Morse Conversion Tool! Have a nice day!")

morse_tool()