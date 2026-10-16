def to_rna(dna_strand: str) -> str:
    dna_strand = list(dna_strand)
    for index,dna in enumerate(dna_strand):
        dna_strand[index] = {
            "G" : "C",
            "C" : "G",
            "T" : "A",
            "A" : "U",
            ""  : "" ,
        }.get(dna)
    rna_strand = str(dna_strand.copy())
    rna_strand = rna_strand.replace("[","")
    rna_strand = rna_strand.replace("]","")
    rna_strand = rna_strand.replace(",","")
    rna_strand = rna_strand.replace("'","")
    rna_strand = rna_strand.replace(" ", "")
    return rna_strand