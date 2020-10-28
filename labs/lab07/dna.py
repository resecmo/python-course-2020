#from abc import ABC
from random import randint


class IdentityMapping:  # auxiliary class to be used as an identity mapping
    def __getitem__(self, item):
        return item

    def __contains__(self, item):
        return True


class BioSeq:
    complements = IdentityMapping()  # todo?

    def __init__(self, seq: str):
        for ch in seq:
            if ch not in self.complements:
                raise ValueError("invalid base letter")
        self.seq = seq

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self.seq + other.seq)
        elif isinstance(self, type(other)):
            return type(other)(self.seq + other.seq)
        else:
            return NotImplemented

    def __radd__(self, other):
        pass  # todo

    def __mul__(self, other):
        if isinstance(other, type(self)):
            _type = type(self)
        elif isinstance(self, type(other)):
            _type = type(other)
        else:
            return NotImplemented

        new_seq = ""
        for pair in zip(self.seq, other.seq):
            new_seq += pair[randint(0, 1)]
        new_seq += (self.seq[len(new_seq):]
                    if len(self.seq) > len(other.seq)
                    else other.seq[len(new_seq):])

        return _type(new_seq)

    def __str__(self):
        return str(type(self).__name__) + ": " + self.seq

    def __getitem__(self, item):
        return self.seq[item]

    def __eq__(self, other):
        if isinstance(self, type(other)) and isinstance(other, type(self)):
            return self.seq == other.seq
        else:
            return NotImplemented

    def complementary_seq(self):
        result = ""
        for ch in self.seq:
            result += self.complements[ch]
        return result


class Rna(BioSeq):
    complements = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, seq):  # todo: make abstract?
        for ch in seq:
            if ch not in self.complements:
                raise ValueError("invalid base letter")
        super().__init__(seq)

    def complement(self):
        return Dna(self.complementary_seq())


class Dna(BioSeq):
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, seq):
        for ch in seq:
            if ch not in self.complements:
                raise ValueError("invalid base letter")
        super().__init__(seq)

    def __getitem__(self, item):
        return [self.seq[item], self.complements[self.seq[item]]]

    def __str__(self):
        return str(type(self).__name__) + ": " + self.seq + " " + self.complementary_seq()


def test():
    seq = BioSeq("ACTTGCTAGC")
    dna1 = Dna("ACTATAGTAGAAAAAGCA")
    dna2 = Dna("ACTCG")
    print(seq, dna1, seq + dna1, dna1 + seq, dna1 + dna2, sep='\n')

    rna1 = Rna("UGUAGA")
    print(dna1 + rna1)

    print(Dna.complements)

    print(Rna("AAAAAAA") * Rna("ACGUCAGAU"))



if __name__ == "__main__":
    test()
