def citire_initiala():
    with open("input.txt", "r+") as f:
        tabel = []
        stari = [str(x).strip("\n") for x in f.readline().strip().split()]
        alfabet = [str(x).strip("\n") for x in f.readline().strip().split()]
        for stare in stari:
            for litera in alfabet:
                tabel.append((stare, litera, f.readline().strip("\n")))
        stare_initiala = f.readline().strip("\n")
        stari_finale = [str(x).strip("\n") for x in f.readline().strip().split()]
    return tabel, stari, alfabet, stare_initiala, stari_finale


def echivalenta_0(stari, stari_finale):
    final_ech_0 = stari_finale
    non_final_ech_0 = [str(x) for x in stari if x not in stari_finale]
    return final_ech_0, non_final_ech_0


def fct_tranzitie(tabel, stare, litera):
    for tranzitie in tabel:
        if tranzitie[0] == stare and tranzitie[1] == litera:
            return tranzitie[2]


def verificare_echivalenta(tabel, stare1, stare2, litera, echivalenta):
    x = fct_tranzitie(tabel, stare1, litera)
    y = fct_tranzitie(tabel, stare2, litera)
    for set in echivalenta:
        if x in set and y in set:
            return True
    return False


def echivalenta_n(echivalenta, tabel, alfabet, stari):
    set_nou = []
    for set_initial in echivalenta:
        if len(set_initial) > 1:
            for i in range(1, len(set_initial)):
                for j in range(0, i):
                    ok = 1
                    for litera in alfabet:
                        if verificare_echivalenta(tabel, set_initial[i], set_initial[j], litera, echivalenta) is False:
                            ok = 0
                    if ok == 1:
                        if set_initial[j] == "q3" and set_initial[j] == "q5":
                            print("DA")
                        ok_pt_append = 0
                        for subset_in_constructie in set_nou:
                            if set_initial[j] in subset_in_constructie:
                                subset_in_constructie.append(set_initial[i])
                                ok_pt_append = 1
                        if ok_pt_append == 0:
                            set_nou.append([set_initial[j], set_initial[i]])
        else:
            set_nou.append(set_initial)

    for stare in stari:
        ok = 0
        for subset in set_nou:
            if stare in subset:
                ok = 1
        if ok == 0:
            set_nou.append([stare])
    set_nou = [list(set(subset)) for subset in set_nou]
    for subset in set_nou:
        subset.sort()
    return set_nou


def citire_tabel_nou(stari_noi, tabel, alfabet, stare_initiala, stari_finale):
    print("Stari noi :", end=" ")
    for stare_noua in stari_noi:
        print(stare_noua, end=" ")
    print("\n")
    print("Alfabetul este acelasi:", end=" ")
    for litera in alfabet:
        print(litera, end=" ")
    print("\n")
    stare_initiala_nou = [x for x in stari_noi if stare_initiala in x]
    print(f"Noua stare initiala: {''.join(stare_initiala_nou)}", end=" ")
    print("\n")
    stari_finale_noi = []
    for stare_finala in stari_finale:
        stari_finale_noi += [x for x in stari_noi if stare_finala in x]
    print("Noile stari finale:", end=" ")
    for stare_finala_noua in stari_finale_noi:
        print(stare_finala_noua, end=" ")
    print("\n")
    for stare_noua in stari_noi:
        for litera in alfabet:
            print(f"f({stare_noua},{litera})=", end=" ")
            for x in stari_noi:
                if fct_tranzitie(tabel, stare_noua[0:len(stare_initiala)], litera) in x:
                    print(x)


def main():
    tabel, stari, alfabet, stare_initiala, stari_finale = citire_initiala()
    final_ech_0, non_final_ech_0 = echivalenta_0(stari, stari_finale)
    set_initial = [non_final_ech_0, final_ech_0]
    seturi_noi = echivalenta_n(set_initial, tabel, alfabet, stari)
    while seturi_noi != set_initial:
        set_initial = seturi_noi
        seturi_noi = echivalenta_n(seturi_noi, tabel, alfabet, stari)
    seturi_noi_nou = []
    for set_nou in seturi_noi:
        stare_noua = "".join(set_nou)
        seturi_noi_nou.append(stare_noua)
    seturi_noi = seturi_noi_nou
    citire_tabel_nou(seturi_noi, tabel, alfabet, stare_initiala, stari_finale)


if __name__ == "__main__":
    main()
