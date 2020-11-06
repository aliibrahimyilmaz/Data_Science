def caesar_encrypt(klar_wort: str, index: int = 1) -> str:
    """
    ABC (1) => BCD, z.b. hans = ibot
    """
    enc_list = []
    for char in klar_wort:
        new_ord = ord(char) + index
        new_char = chr(new_ord)
        enc_list.append(new_char)
    return "".join(enc_list)

klar_wort = "*deniz"
verschiebungs_index = 1
geheimes_wort = caesar_encrypt(klar_wort, verschiebungs_index)
print(geheimes_wort)