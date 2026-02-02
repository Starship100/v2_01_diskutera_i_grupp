


print("Match: Tottenham vs Liverpool")
tottenham_goals = int(input("Hur många mål gjorde Tottenham? "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool? "))

if tottenham_goals == liverpool_goals:
    print("Det blev oavgjort!")
elif tottenham_goals > liverpool_goals:
    differ = tottenham_goals - liverpool_goals
    print("Tottenham vann med ", differ ," mål!")
elif tottenham_goals < liverpool_goals:
    differ = liverpool_goals - tottenham_goals
    print("Liverpool vann med ", differ ," mål!")