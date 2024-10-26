class PizzaShop:
    def __init__(self, pos, name, radius, hour_s, hour_e):
        self.pos = pos
        self.name = name
        self.radius = radius
        self.hour_s = hour_s
        self.hour_e = hour_e
    def distance_square_to(self, i, j):
        return (self.pos[0]-i)**2 + (self.pos[1]-j) ** 2

def pd_map(r, c, all_shops, hour):
    delivery_map = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append('.')
        delivery_map.append(row)
    for idx_row in range(r):
        for idx_col in range(c):
            distance = dict()
            for shop in all_shop:
                if not(shop.hour_s <= hour and hour <= shop.hour_e):
                    continue
                cur_dis = shop.distance_square_to(idx_row, idx_col)
                if cur_dis <= shop.radius ** 2:
                    if cur_dis in distance:
                        distance[cur_dis].append(shop.name[0])
                    else:
                        distance[cur_dis] = [shop.name[0]]
            if len(distance) == 0:
                continue
            minimum_distance = min([x for x in distance.keys()])
            if len(distance[minimum_distance]) > 1:
                delivery_map[idx_row][idx_col] = 'X'
            else:
                delivery_map[idx_row][idx_col] = distance[minimum_distance][0]
                
    return delivery_map