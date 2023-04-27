noOfAttempts = 0
with open("ENJOYSPORT.csv", "r") as es:
    atr_list = es.readline().strip().split(",")
    for line in es:
        h = line.strip().split(",")
        if h[6] == "1" and noOfAttempts == 0:
            for line in es:
                s = line.strip().split(",")
                if s[6] == "1":
                    for i in range(len(s) - 1):
                        if h[i] != s[i]:
                            h[i] = "?"
            noOfAttempts = 1
print("Most Specific hypothesis : ", end="")
print(h)
print()
for i in range(len(h)):
    print(atr_list[i] + " : " + h[i])