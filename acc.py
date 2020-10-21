# COPYRIGHT 2020 - RUSHI RANADE'S APPS
# ENHANCED ENCRYPTION
# CHECK MY OTHER ENCRYPTION REPO
def encryptor(text,s, n): 
    result = "" 
    for i in range(len(text)):
        char = text[i] 
  
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)
        if (s * n) <=26:
            s = s * n
        else:
            s = (s - n) * n
  
    return result
