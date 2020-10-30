import urllib.request
from pprint import pprint

def cmu_dictionary_loader():
    """"Erstellt ein Dictionary aus der Quelle in der URL (Lautsprache)"""
    # http://www.speech.cs.cmu.edu/cgi-bin/cmudict
    url = "http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict.0.7a"
    data = urllib.request.urlopen(url)

    cmu_dict = {}
    for line in data:
        # print(type(line))
        word, *phonetic = line.decode("utf-8").strip().split()
        cmu_dict[word] = phonetic
    return cmu_dict


def cmu_word(string):
    """Sucht das Wort im phonetischen Dictionary und gibt die Lautsprache aus"""
    string = string.upper()
    if string in cmu_dict:
        result = str(cmu_dict.get(string)).strip('[]')
    else:
        result = 'Dieses Wort befindet sich nicht im Dictionary.'
    return result

def cmu_list(string):
    """Listet alle Worte im phonetischen Dictionary, die mit dem Anfangsbuchstaben übereinstimmen,
    der übergeben wird"""
    string = string.upper()
    result = []
    for x in cmu_dict.keys():
        if string == x[0]:
            result.append(x)
    if len(result) > 0:
        result
    else:
        result = 'Keine Entsprechung vorhanden.'
    return result

def cmu_user_input():
    user_input = input('Bitte Suchwort (für Lautsprache) oder Anfangsbuchstabe (für vorhandene Wörter) eingeben!:')
    return user_input

methods = {
    'WORD': cmu_word,
    'LIST': cmu_list,
}

def cmu_method_selection_and_execute(string):
    if len(string) == 1:
        result = methods.get('LIST')(string)
    else:
        result = methods.get('WORD')(string)
    return result

def cmu_pretty_printer(result):
    pprint(result)


# Programm Start
cmu_dict = cmu_dictionary_loader()
status = True
while status:
    user_choice = cmu_user_input()
    if user_choice == '*':
        print('Auf Wiedersehen.')
        break
    else:
        result = cmu_method_selection_and_execute(user_choice)
        cmu_pretty_printer(result)


