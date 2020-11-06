def caesar_decrypt(enc_wort: str, index: int = 1) -> str:
    """
    BCD(-1) => ABC , z.b. ibot = hans
    """
    word = "".join([chr(ord(char) - index) for char in enc_wort])
    return word

enc_wort = "BCD"
verschiebungs_index = 1
geheimes_wort = caesar_decrypt(enc_wort, verschiebungs_index)
print(geheimes_wort)