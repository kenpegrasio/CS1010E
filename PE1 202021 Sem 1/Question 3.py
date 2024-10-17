def calculate_areas(w_list, h_list):
    compressed_h = [0, 0, 0]
    for idx in range(len(h_list)):
        compressed_h[idx % 3] += h_list[idx]
    ans = [0, 0, 0]
    for row in range(len(w_list)):
        for i in range(3):
            ans[i] += w_list[row] * compressed_h[(3 + i - row) % 3]
    return tuple(ans)