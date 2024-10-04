ddict = {'A':'U', 'G':'C', 'T':'A', 'C':'G'}

def dna_transcription_I(dna):
    res = ""
    for c in dna:
        res += ddict[c]
    return res
    
def dna_transcription_R(dna):
    if dna == "":
        return "";
    return ddict[dna[0]] + dna_transcription_R(dna[1:])