''' Given a temperature, print:

"Hot" if above 35
"Warm" if between 20 and 35
"Cold" if below 20'''


def temparature_mesurement(temp):
    if temp > 35: print("Hot")
    elif temp >=20 and temp <=35:print("Warm")
    else: print("Cold")
temparature_mesurement(int(input("Enter the temparature in celcius: ")))