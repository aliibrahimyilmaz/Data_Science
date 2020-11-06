def caesar_decrypt(enc_wort: str, index: int = 1) -> str:
    """
    BCD(-1) => ABC , z.b. ibot = hans
    """
    word_list = []
    for char in enc_wort:
        new_ord = ord(char) - index
        new_char = chr(new_ord)
        word_list.append(new_char)
    return "".join(word_list)

enc_wort = "efoj{"
verschiebungs_index = 1
geheimes_wort = caesar_decrypt(enc_wort, verschiebungs_index)
print(geheimes_wort)