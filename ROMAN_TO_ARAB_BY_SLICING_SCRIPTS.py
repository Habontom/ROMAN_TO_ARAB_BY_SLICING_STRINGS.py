
txet = input("ZADAJ RIMSKE CISLO, A JA TI HO PREPOCITAM NA NASE: \n")

text = txet + "UROBSIVEVLASY"
print(text[0:])

if text is int():
    print("ZADAJ RIMSKE ZNAKY!")
c = int()

while True:
    if "M" in text[0]:
        c += 1000
        text = text[1:]
        print(c,"\t text")
    else:
        pass

    if "D" in text[0]:
        c += 500
        text = text[1:]
        print(c, "text")
    else:
        pass

    if "C" in text[0]:
        if "C" in text[1]:
            if "M" in text[2]:
                c += 700
                text = text[2]
            else:
                pass
        if "D" in text[1]:
            c += 300
            text = text[1:]
        else:
            pass
        c += 100
        text = text[1:]
        print(c, "\t text")
    else:
        pass

    if "L" in text[0]:
        if "D" in text[1]:
            c += 400
            text = text[1:]
        else:
            pass
        if "M" in text[1]:
            c += 900
            text = text[1:]
        else:
            pass
        c += 50
        text = text[1:]
        print(c,"\t text")
    else:
        pass

    if "X" in text[0]:
        if "X" in text[1]:
            if "D" in text[2]:
                c += 470
                text = text[2]
            else:
                pass
            if "M" in text[2]:
                c += 970
                text = text[2]
            else:
                pass
        if "C" in text[1]:
            c += 80
            text = text[1:]
        else:
            pass
        if "M" in text[1]:
            c += 980
            text = text[1:]
        else:
            pass
        if "D" in text[1]:
            c += 480
            text = text[1:]
        else:
            pass

        c += 10
        text = text[1:]
        print(c,"\t text")
    else:
        pass

    if "V" in text[0]:
        if "L" in text[1]:
            c += 40
            text = text[1:]
        else:
            pass
        if "C" in text[1]:
            c += 90
            text = text[1:]
        else:
            pass
        if "D" in text[1]:
            c += 490
            text = text[1:]
        else:
            pass
        if "M" in text[1]:
            c += 990
            text = text[1:]
        else:
            pass

        text = text[1:]
        c += 5
        print(c,"\t text")
    else:
        pass
    if "I" in text[0]:
        if "I" in text[1]:
            if "X" in text[2]:
                c += 6
                text = text[1:]
            else:
                pass
            if "L" in text[2]:
                c += 46
                text = text[1:]
            else:
                pass
            if "C" in text[2]:
                c += 96
                text = text[1:]
            else:
                pass
            if "D" in text[2]:
                c += 496
                text = text[1:]
            else:
                pass
            if "M" in text[2]:
                c += 996
                text = text[1:]
            else:
                pass
            text = text[1:]
            c += 1
            print(c, "\t text")
        else:
            pass
        if "V" in text[1]:
            c += 3
            text = text[1:]
        else:
            pass
        if "X" in text[1]:
            c += 8
            text = text[1:]
        else:
            pass

        if "L" in text[1]:
            c += 48
            text = text[1:]
        else:
            pass
        if "C" in text[1]:
            c += 98
            text = text[1:]
        else:
            pass
        if "D" in text[1]:
            c += 498
            text = text[1:]
        else:
            pass
        if "M" in text[1]:
            c += 998
            text = text[1:]
        else:
            pass
        text = text[1:]
        c += 1
        print(c, "\t text")

    if text == "UROBSIVEVLASY":
        print("Vypocital som ti to. Rimske", txet, "ma arabsku hodnotu", c, ".")
        quit()




print(c)
print(text)



