b = bytes('Zöö', encoding='utf-8')
print(b)                                          # b'Z\xc3\xb6\xc3\xb6'
print(str(b, encoding='ascii', errors='ignore'))  # Z # str function only accept bytes