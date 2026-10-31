"""Converts DNA to RNA"""

COMPLEMENT = {
            "G" : "C",
            "C" : "G",
            "T" : "A",
            "A" : "U",
            ""  : "" ,
}

def to_rna(dna_strand: str) -> str:
    """Returns the RNA strand complement of a DNA strand
    
    Parameters:
    dna_strand: The DNA strand.

    Returns:
    The RNA strand.
    """
    return "".join(COMPLEMENT[dna] for dna in dna_strand)