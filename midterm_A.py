def geneticka_predispozice_lecby(nukleo):
    score = 0
    delka = len(nukleo)
    M= nukleo.count("M")
    Z = nukleo.count("Z")
    A = nukleo.count("A")
    if delka > 15:
        score = score + 3
        if M >= 5 :
            score = score + 5
        if Z < 3 :
            score = score +4
        if A > 6:
            score = score - 6
        else:
            score = score + 0
    else:
        score = score + 0
        if M >= 5 :
            score = score + 5
        if Z < 3 :
            score = score +4
        if A > 6:
            score = score - 6
        else:
            score = score + 0

    if score > 5:
        return 3
    elif score <= 5:
        return 9

def vyber_leku(dna,score):
    if dna.count("M") <= 3 and score == 9:
        return "jablko"
    elif dna.count("A") ==5 and dna.count("M") < 2 and score == 3:
        return "injekce"
    else:
        return "prasky"

def samovolna_mutace(dna,lek):
    if lek == "jablko":
        return "Pokemon se uzdravil bez mutace"
    elif lek == "prasky":
        dna = dna.replace("A","M")

    elif lek == "injekce":
        dna = dna.replace("T","M")
        dna = dna.replace("Z", "M")
    pocet_Medidinu = dna.count("M")
    skore = pocet_Medidinu * 3
    if skore > 10:
        return "Pokemon se vyvinul na jeho dalsi level"
    elif skore < 10:
        return "Pokemon se uzdravil, ale nema dostatecnou energii se vyvinout"


def main(dna):
    # for i in dna[0]:
    #     if i != "A" or "T" or "M" or "Z":
    #         return None
    analyzy = []
    score = geneticka_predispozice_lecby(dna)
    lek = vyber_leku(dna,score)
    mutace = samovolna_mutace(dna,lek)

    analyzy.append(score)
    analyzy.append(lek)
    analyzy.append(mutace)
    return analyzy
print(main(["MTZAMTAMTA"]))