    while True:
        print("menüü:")
        print("1 - teisenda väiketähtedeks")
        print("2 - teisenda suurtähtedeks")
        print("3 - kontrolli, kas sisaldab ainult numbreid")
        print("4 - jaga string eraldaja järgi")
        print("5 - asenda alamsõne")
        print("6 - otsi alamsõne (viimane esinemine)")
        print("7 - otsi alamsõne (esimene esinemine)")
        print("8 - leia stringi pikkus")
        print("9 - korda stringi")
        print("10 - uhenda stringid")
        print("11 - muuda esitähed suur- ja väiketähtedeks")
        print("12 - eemalda tühikud algusest ja lõpust")
        print("13 - kontrolli, kas string algab kindla alamsõnaga")
        print("0 - välju")
    
        valik = input("sisesta valik: ")
    
        if valik == "0":
            break
        elif valik == "1":
            s = input("sisesta string: ")
            print("vaiketähed:", s.lower()) # Teisendab kõik tähed väiketähtedeks
        elif valik == "2":
            s = input("sisesta string: ")
            print("suurtähed:", s.upper())
        elif valik == "3":
            s = input("sisesta string: ")
            print("kas string sisaldab ainult numbreid?", s.isdigit())
        elif valik == "4":
            s = input("sisesta string: ")
            eraldaja = input("sisesta eraldaja: ")
            print("stringi jagamine:", s.split(eraldaja))
        elif valik == "5":
            s = input("sisesta string: ")
            vana = input("sisesta asendatav alamsõne: ")
            uus = input("sisesta uus alamsõne: ")
            print("alamsõne asendamine:", s.replace(vana, uus))
        elif valik == "6":
            s = input("sisesta string: ")
            alamsoone = input("sisesta alamsõne: ")
            print("viimase esinemise indeks:", s.rfind(alamsoone))
        elif valik == "7":
            s = input("sisesta string: ")
            alamsoone = input("sisesta alamsõne: ")
            print("esimese esinemise indeks:", s.find(alamsoone))
        elif valik == "8":
            s = input("sisesta string: ")
            print("stringi pikkus: ", len(s))
        elif valik == "9":
            s = input("sisesta string: ")
            kordus = int(input("mitu korda korrata? "))
            print("stringi kordamine:", s * kordus)
        elif valik == "10":
            s1 = input("sisesta esimene string: ")
            s2 = input("sisesta teine string: ")
            print("stringide ühendamine: ", s1 + s2)
        elif valik == "11":
            s = input("sisesta string: ")
            print("esitähtede muutmine suur- ja väiketähtedeks: ", s.title())
        elif valik == "12":
            s = input("sisesta string: ")
            print("tuhikute eemaldamine: ", s.strip())
        elif valik == "13":
            s = input("sisesta string: ")
            algus = input("sisesta kontrollitav algus: ")
            print("kas string algab alamsõnaga?", s.startswith(algus))
        else:
            print("vale valik, proovi uuesti")
