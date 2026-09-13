def to_rna(dna_strand):
    dna_strand = "_".join(dna_strand)
    dna_strand = dna_strand.split("_")
    for index,dna in enumerate(dna_strand):
        dna_strand[index] = {
            "G" : "C",
            "C" : "G",
            "T" : "A",
            "A" : "U",
            ""  : "" ,
        }.get(dna)
    rna_strand = dna_strand.copy()
    rna_strand = str(rna_strand)
    rna_strand = rna_strand.replace("[","")
    rna_strand = rna_strand.replace("]","")
    rna_strand = rna_strand.replace(",","")
    rna_strand = rna_strand.replace("'","")
    rna_strand = rna_strand.replace(" ", "")
    return rna_strand