def per_cipher_i(s, n):
    ans = ""
    for i in range(0, len(s), n):
        ans += s[i:i+n][::-1]
    return ans

def per_cipher_r(s, n):
    if s == "":
        return ""
    return s[0:n][::-1] + per_cipher_r(s[n:], n)

def per_cipher_o(s, n):
    return "".join([s[i:i+n][::-1] for i in range(0, len(s), n)])