def caesar_decrypt(enc_wort: str, index: int = 1) -> str:
    """
    ABC (1) => BCD, z.b. hans = ibot
    """
    # word = [chr(ord(char) - index) for char in enc_wort]
    word = list(chr(ord(char) - index) for char in enc_wort)
    return word

enc_wort = "ibot"
verschiebungs_index = 1
geheimes_wort = caesar_decrypt(enc_wort, verschiebungs_index)
print(geheimes_wort)