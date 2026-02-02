
# Version 1
#celsius = float(input("Ange en temperatur i grader celsius: "))
#farenheit = 1.8 * celsius + 32
#print("Det blir ", farenheit , "grader i farenheit.")


# Version 2
val = input("Ange temperatur i Fahranheit(f) eller Celsius(c): ")
if val == "c" or val == "f":
    celsius = float(input("Skriv in temperatur i grader Celsius: "))
    fahrenheit = 1.8 * celsius + 32
    print("Det blir ", fahrenheit, "grader Fahrenheit.")
else:
    fahrenheit = float(input("Skriv in temperatur i grader Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Det blir ", celsius, "grader Celsius.")

if celsius < 10:
        print("Ta på dig vinterkläder!")
elif celsius >= 20:
        print("Packa badkläder!")