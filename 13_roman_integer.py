def romanToInt(s: str) -> int:
    roman = ""
    # table = {
    #     1: "I",
    #     5: "V",
    #     10: "X",
    #     50: "L",
    #     100: "C",
    #     500: "D",
    #     1000: "M"
    # }

    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }


    num = int(s)
    for key in table.keys():
        print(key)
        continue





    # while (len(s) > 0):
    #     num = s[0]

    #     if len(s) == 4:
    #         num *


    #     num = s[0]
    #     print(num)


#print(len("3000"))
romanToInt("900")
