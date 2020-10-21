from acc import encrypt
word = input("Enter the word: ")
hashamount = int(input("Hash amount. Recommended: 100 :- "))
n = int(input("Enter a number that indicates how many letters you want to change: "))
helper = input("Enter a word that acts as the encryption helper: ")
for i in range(hashamout):
    a, word = word[:n], word[n:]
    word = word + a + encrypt(helper, 4, n) # n-4Shift Encryption
    n = n + 1
print(f"Cipher: {word}")
