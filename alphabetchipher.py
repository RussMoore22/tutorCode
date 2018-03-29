

def decode(Alphabet, k, alphabetStr,keyIndexer):

    keyword = input("enter the keyword: ")
    message = input("enter the secret message: ")
    keyword = keyword.upper()
    message = message.upper()
    decodeStr = []
    endMessage = ''

    for letter in message:
        k += 1
        if k == len(keyword):
            k = 0

        indexValue = keyIndexer[keyword[k]]
        try:
            #print(Alphabet[Alphabet.index(letter)-indexValue])
            decodeStr.append((Alphabet[Alphabet.index(letter)-indexValue]))
        except:
            #print(Alphabet[Alphabet.index(letter)-indexValue +26])
            decodeStr.append((Alphabet[Alphabet.index(letter)-indexValue +26]))

    for l in decodeStr:
        endMessage = endMessage + l

    print(endMessage.lower())


def encode(Alphabet, k, alphabetStr,keyIndexer):
    keyword = input("enter the keyword: ")
    message = input("enter the secret message: ")
    keyword = keyword.upper()
    message = message.upper()
    encodedMessage = []
    endingMessage = ''

    for letter in message:
        k += 1
        if k == len(keyword):
            k = 0
        try:
            encodedMessage.append(Alphabet[Alphabet.index(letter) + Alphabet.index(keyword[k])])
        except:
            encodedMessage.append(Alphabet[Alphabet.index(letter) + Alphabet.index(keyword[k]) - 26])
    for l in encodedMessage:
        endingMessage = endingMessage + l
    print(endingMessage)


def askUser():
    ans = input('for decoding message, enter d\nfor encoding message, enter e\n----->')
    return ans


keyIndexer = {}
Alphabet = []
k = -1
alphabetStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in alphabetStr:
    Alphabet.append(letter)

for i in range(len(Alphabet)):
    keyIndexer[Alphabet[i]] = i

ans = askUser()
if ans == 'd':
    decode(Alphabet,k,alphabetStr,keyIndexer)
elif ans == 'e':
    encode(Alphabet,k,alphabetStr,keyIndexer)
else:
    askUser()
