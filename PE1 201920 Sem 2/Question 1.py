def rotate(bouquet, step):
    ans = []
    for i in range(len(bouquet)):
        ans.append(bouquet[(i + step) % len(bouquet)])
    return tuple(ans)

def flower_I(bouquet, k):
    bouquet = list(bouquet)
    ans = []
    while len(bouquet) > 0:
        bouquet = list(rotate(bouquet, k))
        ans.append(bouquet[-1])
        bouquet = bouquet[:-1]
    return "".join(ans)

def flower_R(bouquet, k):
    if len(bouquet) == 0:
        return ""
    bouquet = list(rotate(bouquet, k))
    return bouquet[-1] + flower_R(bouquet[:-1], k)

def pink_rose(bouquet):
    if "P" not in bouquet:
        return -1
    k = 0
    while flower_R(bouquet, k)[-1] != "P":
        k += 1
    return k