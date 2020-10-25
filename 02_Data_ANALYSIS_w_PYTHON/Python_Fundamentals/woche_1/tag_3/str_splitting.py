s = "AA-BcesB 92892"
s = s.split()  # default separator ist das leerzeichen

print(s)

s = "AA-9245"
s = s.split("-")
print(s, s[1], type(s[1]))
