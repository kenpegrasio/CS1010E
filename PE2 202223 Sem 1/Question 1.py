def encode_char(c, offset, multiplier):
    return chr(97+(ord(c)-97+offset*multiplier)%26)

def encode_I(s1,s2,m):
    ans = ""
    for idx in range(len(s1)):
        ans += encode_char(s1[idx], int(s2[idx]), m)
    return ans

def encode_R(s1,s2,m):
    if len(s1) == 0:
        return ""
    c = encode_char(s1[0], int(s2[0]), m)
    return c + encode_R(s1[1:], s2[1:], m)

def encode_U(s1,s2,m):
    return "".join([chr(97+(ord(s1[idx])-97+int(s2[idx])*m)%26) for idx in range(len(s1))])
