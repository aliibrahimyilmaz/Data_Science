with open("test_data.txt", "w") as datei_handler:
    datei_handler.write("\ntest")

# append mit Modus a anhängen an eine Datei ODER falls nicht besteht, neu schreiben
with open("data_xyz.txt", "a") as datei_handler:
    datei_handler.writelines('test33\n')
    datei_handler.writelines(['\nSee you soon!', '\nOver and out.'])

with open('data.csv', "r") as datei_handler:
    # read and print the entire file line by line
    string_liste = []
    for zeile in datei_handler:
        print(zeile.strip().split(','))
