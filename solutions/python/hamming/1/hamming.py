def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    if strand_a == "":
        return 0
    strand_a = " ".join(strand_a)
    strand_b = " ".join(strand_b)
    strand_a = strand_a.split()
    strand_b = strand_b.split()
    length = len(strand_a)
    index = 0
    differences = 0
    while index != length:
        if strand_a[index] != strand_b[index]:
            differences += 1
        index += 1
    return differences
            