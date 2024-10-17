def make_bouquet(shop, number):
    shop.insert(0,('X',0,0))
    for x in shop:
        for y in shop:
            for z in shop:
                if x[0] != "P" and y[0] != "P" and z[0] != "P":
                    continue
                if x[1] + y[1] + z[1] == number:
                    return True
    return False
    
    
def minimum_cost(shop, number):
    shop.insert(0,('X',0,0))
    ans = -1
    for x in shop:
        for y in shop:
            for z in shop:
                if x[0] != "P" and y[0] != "P" and z[0] != "P":
                    continue
                if x[1] + y[1] + z[1] == number:
                    cost = x[2] + y[2] + z[2]
                    if ans == -1:
                        ans = cost
                    else:
                        ans = min(ans, cost)
    return ans