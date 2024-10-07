ddict = {}
for i in range(ord('A'), ord('Z') + 1):
    if (i - 65 < 10):
        ddict['0' + str(i - 65)] = chr(i)
    else:
        ddict[str(i - 65)] = chr(i)
ddict['99'] = ' '

for x in ddict.keys():
    print(x + ": " + ddict[x])

def convert(character, offset):
    if character == " ":
        return character
    if ord('A') <= ord(character)-offset:
        return chr(ord(character)-offset)
    return chr(ord(character)-offset+26) 

def decode(msg, offset):
    offset %= 26
    ans = "".join([ddict[msg[i-1] + msg[i]] for i in range(len(msg)) if i % 2 == 1])
    return "".join([convert(c, offset) for c in ans])

def decode_with_love(msg):
    for i in range(0, 26):
        if "LOVE" in decode(msg, i):
            return decode(msg, i)
