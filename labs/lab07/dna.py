from random import randint
from string import ascii_letters


class BioSeq:
    # any ascii letter is allowed to be used in generalized sequence
    complements = {x: y for (x, y) in zip(list(ascii_letters), list(ascii_letters))}

    def __init__(self, seq: str):
        if not isinstance(seq, str):
            raise ValueError("seq must be str")

        for ch in seq:
            if ch not in self.complements:
                raise ValueError("invalid base letter: {}".format(ch))
        self.seq = seq

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self.seq + other.seq)
        elif isinstance(self, type(other)):
            return type(other)(self.seq + other.seq)
        else:
            return NotImplemented

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
            # for unclear reasons, returning NotImplemented doesn't work as expected
            raise ValueError("can't compare {} with {}".format(type(self), type(other)))

    def complementary_seq(self):
        result = ""
        for ch in self.seq:
            result += self.complements[ch]
        return result


class Rna(BioSeq):
    complements = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, seq):
        super().__init__(seq)

    def complement(self):
        return Dna(self.complementary_seq())


class Dna(BioSeq):
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, seq):
        super().__init__(seq)

    def __getitem__(self, item):
        return [self.seq[item], self.complements[self.seq[item]]]

    def __str__(self):
        return str(type(self).__name__) + ": " + self.seq + " " + self.complementary_seq()


def test():
    # construction test
    try:
        dna0 = Dna("AGCTGUG")
    except ValueError as e:
        assert str(e) == "invalid base letter: U"

    try:
        rna0 = Rna("CAGUTUGCA")
    except ValueError as e:
        assert str(e) == "invalid base letter: T"

    seq = BioSeq("chyq")
    dna1 = Dna("GACT")
    dna2 = Dna("ACTCG")
    rna1 = Rna("UGUAGA")

    # __str__ and __add__ test
    assert str(seq) == "BioSeq: chyq"
    assert str(dna1) == "Dna: GACT CTGA"
    assert str(seq + dna1) == "BioSeq: chyqGACT"
    assert str(dna1 + seq) == "BioSeq: GACTchyq"
    assert str(dna1 + dna2) == "Dna: GACTACTCG CTGATGAGC"

    try:
        print(dna1 + rna1)
    except TypeError as e:
        assert str(e) == "unsupported operand type(s) for +: 'Dna' and 'Rna'"

    # indexing test
    assert dna1[3] == ["T", "A"]
    assert rna1[2] == "U"

    # complement test
    assert dna1.complementary_seq() == "CTGA"
    assert rna1.complementary_seq() == "ACATCT"

    #print(Dna.complements)

    # __mul__ test (not really tests anything)
    print(Rna("AAAAAAA") * Rna("ACGUCAGAU"))
    print(dna1 * dna2)

    # __eq__ test
    assert Dna("ATCTA") == Dna("ATC") + Dna("TA")
    assert Rna("UGUAGA") == Rna("UGU") + Rna("AGA")
    try:
        Rna("AAA") == Dna("AAA")
    except ValueError as e:
        assert str(e) == "can't compare <class '__main__.Rna'> with <class '__main__.Dna'>"


if __name__ == "__main__":
    test()
