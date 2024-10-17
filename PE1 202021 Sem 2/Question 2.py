
def rna_segment(rna):
    start = False
    ans = ""
    idx = 0
    while idx < len(rna):
        if not start and idx-1 >= 0 and rna[idx - 1] == 'U' and (rna[idx] == 'U' or rna[idx] == 'G'):
            start = True
            ans += rna[idx - 1] + rna[idx]
            idx += 1
            continue
        if start:
            ans += rna[idx] + rna[idx + 1]
            if idx+1 < len(rna) and rna[idx] == 'A' and (rna[idx + 1] == 'A' or rna[idx + 1] == 'C'):
                break
            idx += 2
            continue
        idx += 1
    return ans

ddict = {
    'F': 'acidic',
    'P': 'acidic', 
    'Q': 'acidic', 
    'L': 'non_polar',
    'O': 'non_polar',
    'M': 'basic', 
    'A': 'basic', 
    'C': 'basic', 
    'R': 'basic',
    'S': 'polar',
    'T': 'polar', 
    'Y': 'polar'
}

def poly_property(poly):
    cnt = {
        'acidic': 0,
        'non_polar': 0,
        'basic': 0,
        'polar': 0
    }
    for c in poly:
        if c in ddict:
            cnt[ddict[c]] += 1
    if cnt['acidic'] > cnt['basic']:
        return "Acidic"
    elif cnt['acidic'] < cnt['basic']:
        return "Basic"
    elif cnt['polar'] > cnt['non_polar']:
        return "Polar"
    else:
        return "Neutral"