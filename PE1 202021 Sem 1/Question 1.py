ddict = {}
for i in range(ord('A'), ord('Z') + 1):
    if (i - 65 < 10):
        ddict[chr(i)] = '0' + str(i - 65)
    else:
        ddict[chr(i)] = str(i - 65)
ddict[' '] = '99'

def encode_I(word):
    return "".join([ddict[c] for c in word])


def encode_R(word):
    if word == "":
        return word
    return ddict[word[0]] + encode_R(word[1:])
