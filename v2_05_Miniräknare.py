
tal_1 = int(input("Skriv in ett tal: "))
tal_2 = int(input("Skriv in ett andra tal: "))
tal_3 = int(input("Skriv in ett tredje tal: "))
summa = tal_1 + tal_2 + tal_3
print("Summan blir: " + str(summa))

if tal_1 == tal_3 == tal_2:
    print("Alla tre tal är lika.")
elif tal_1 == tal_2 or tal_2 == tal_3 or tal_1 == tal_3:
    print("Två av talen är samma.")

if tal_1 > tal_2 > tal_3 or tal_1 < tal_2 < tal_3:
    print("Det mellersta talet är: " + str(tal_2))
elif tal_3 > tal_1 > tal_2 or tal_3 < tal_1 < tal_2:
    print("Det mellersta talet är " + str(tal_1))
elif tal_1 > tal_3 > tal_2 or tal_1 < tal_3 < tal_2:
    print("Det mellersta talet är " + str(tal_3))
else:
    print("Det finns inget mellersta tal.")

if tal_2 < tal_1 > tal_3:
    print("Talet " + str(tal_1) + " är störst.")
elif tal_1 < tal_2 > tal_3:
    print("Talet " + str(tal_2) + " är störst.")
else:
    print("Talet " + str(tal_3) + " är störst.")
