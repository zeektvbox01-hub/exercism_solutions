"""Converts DNA to RNA"""

import re

def to_rna(dna_strand: str) -> str:
    """Returns the RNA strand complement of a DNA strand
    
    Parameters:
    dna_strand: The DNA strand.

    Returns:
    The RNA strand.
    """
    dna_strand = list(dna_strand)
    for index, dna in enumerate(dna_strand):
        dna_strand[index] = {
            "G" : "C",
            "C" : "G",
            "T" : "A",
            "A" : "U",
            ""  : "" ,
        }.get(dna)
    return re.sub(r"[,'\s+\[\]]","",str(dna_strand))