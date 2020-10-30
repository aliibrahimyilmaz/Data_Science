code = {
'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
'0': '-----',
',': '--..--',
'.': '.-.-.-',
'?': '..--..',
'/': '-..-.',
'-': '-....-',
'(': '-.--.',
')': '-.--.-'
}


def mors_controller(word):
    """Kontrolle für undefinierte Zeichen in Morscode"""
    controller_list = []
    for element in word:
        if element in code.keys():
            controller_list.append(element)
        else:
            return False
    return controller_list


def mors_translator(user_input):
    """User-Eingabe wird in das Morsalphabet übertragen und zurückgegeben"""
    output = user_input.upper()
    if mors_controller(output):
        alphabet_list = mors_controller(output)
        mors_list = []
        for element in alphabet_list:
            mors_list.append(code[element])
        result = "/".join(mors_list)
        return result
    else:
        return "not implemented"

# Übertragung in das Morsalphabet
while True:
    user_input = input("Hallo, Willkommen beim Alfatraining Morscode Übersetzer!"
                       " Bitte gebe eine Zeichenkette ein! ODER zum Abbruch 'q': ")
    if user_input == "q":
        print("Auf Wiedersehen")
        break
    print(mors_translator(user_input))