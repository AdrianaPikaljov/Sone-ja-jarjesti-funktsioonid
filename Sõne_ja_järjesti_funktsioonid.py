
while True:
    print("Menüü:")
    print("1. Pööra string")
    print("2. Arvuta stringi pikkus")
    print("3. Arvuta eseme esinemisajad listis")
    print("4. Eemalda duplikaadid listist")
    print("5. Sorteeri list")
    print("6. Ühenda kaks stringi")
    print("7. Jagage string eraldajaga")
    print("8. Kas string koosneb ainult numbritest?")
    print("9. Kas string koosneb ainult tähtedest?")
    print("10. Lisa element listi")
    print("0. Välju programm")
    valik = input("Vali valik (0-10): ")

    if valik == "1":
        s = input("Sisesta string pööramiseks: ")
        print(f"Pööratud string: {s[::-1]}")
        elif valik == "2":
            s = input("Sisesta string pikkuse arvutamiseks: ")
            print(f"Stringi pikkus: {len(s)}")