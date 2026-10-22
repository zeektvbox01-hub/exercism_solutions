CODON_MAP = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "Stop",
    "UAG": "Stop",
    "UGA": "Stop",
}



def proteins(strand):
    codons = []
    for number in range(0,len(list(strand)),3):
        codons.append(strand[number:(number + 3)])
    amino_acids = []
    for codon in codons:
        amino_acid = CODON_MAP[codon]
        if amino_acid == "Stop":
            break
        amino_acids.append(amino_acid)
    return amino_acids