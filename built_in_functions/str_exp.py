b = bytes('Zöö', encoding='utf-8')
print(b)                                          # b'Z\xc3\xb6\xc3\xb6'
print(str(b, encoding='ascii', errors='ignore'))  # Z # str function only accept bytes
print(str(b, encoding='ascii', errors='strict'))  # UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 1: ordinal not in range(128)
'''
encoding - Defaults of UTF-8. Encoding of the given object
errors - response when decoding fails. There are six types of error response
strict - default response which raises a UnicodeDecodeError exception on failure
ignore - ignores the unencodable unicode from the result
replace - replaces the unencodable unicode to a question mark ?
xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
backslashreplace - inserts a \uNNNN espace sequence instead of unencodable unicode
namereplace - inserts a \N{...} escape sequence instead of unencodable unicode
'''