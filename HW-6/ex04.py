
keychain = {0: "zero", 1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7: "seven", 8: "eight", 9:"nine", 10:"ten", 11: "eleven",
            12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15:"fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
            30: "thirty", "40": "fourty", 50 : "fifty", "60" : "sixty", 70 : "seventy", 80: "eighty", 90 : "ninety"
            }

def translation(c):
    if c not in range(0,1000):
        return("I don't know")
    try:
        return(keychain[c])
    except:
        if c < 100:
            sadge = c % 10
            c -= sadge
            return (f"{keychain[c]}-{keychain[sadge]}")
        
        sadge = c % 100
        sadge2 = sadge % 10
        try:
            return (f"{keychain[c//100]} hundred and {keychain[sadge]}")
        except:
            sadge -= sadge2
            return (f"{keychain[c//100]} hundred and {keychain[sadge]}-{keychain[sadge2]}")


print(translation(int(input())))
