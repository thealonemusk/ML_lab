spc_hyp = []
gen_hyp = []
linesRead = 1
atr_values = {0: ["Sunny", "Rainy"], 1:["Warm", "Cold"], 2:["Normal", "High"], 4:["Warm", "Cool"], 5:["Same", "Change"]}
with open("ENJOYSPORT.csv") as es:
    atr_list = es.readline().strip().split(",")
    for line in es:
        linesRead = linesRead + 1
        s = line.strip().split(",")

        # For enjoysport is 1
        if s[6] == "1":
            if len(spc_hyp) == 0:
                spc_hyp = s
                spc_hyp.pop(6)
            else:
                for i in range(len(spc_hyp)):
                    if s[i] != spc_hyp[i]:
                        spc_hyp[i] = "?"

            if len(gen_hyp) != 0:
                for val in gen_hyp:
                    for i in range(len(s)-1):
                        if val[i] != "?" and val[i] != s[i]:
                            gen_hyp.remove(val)
                            break

        # For enjoysport is 0
        elif s[6] == "0":
            if len(gen_hyp) == 0:
                for key, value in atr_values.items():
                    temp = []
                    if s[key] == value[0]:
                        for i in range(len(s)-1):
                            if i == key:
                                temp.append(value[1])
                            else:
                                temp.append("?")
                    else:
                        for i in range(len(s)-1):
                            if i == key:
                                temp.append(value[0])
                            else:
                                temp.append("?")
                    gen_hyp.append(temp)


            elif len(gen_hyp) != 0:
                cnst = 0
                for val in gen_hyp:
                    for i in range(len(s)-1):
                        if val[i] != "?" and val[i] != s[i]:
                            cnst = 1
                    if cnst == 0:
                        for key, value in atr_values.items():
                            temp = val
                            if val[key] == "?" and s[key] == value[0]:
                                temp[key] = value[1]
                                gen_hyp.append(temp)
                            elif val[key] == "?" and s[key] == value[1]:
                                temp[key] = value[0]
                                gen_hyp.append(temp)
                        gen_hyp.remove(val)

            with open("ENJOYSPORT.csv") as cc:
                for i in range(linesRead):
                    l = cc.readline().strip().split(",")
                    for val in gen_hyp:
                        if l[6] == "1":
                            for j in range(len(l) - 1):
                                if val[j] != "?" and val[j] != l[j]:
                                    gen_hyp.remove(val)
                                    break

                        elif l[6] == "0":
                            for j in range(len(l) - 1):
                                if val[j] != "?" and val[j] == l[j]:
                                    gen_hyp.remove(val)
                                    break

print(f"Specific Hypothesis : {spc_hyp}\n")
print(f"General Hypothesis : {gen_hyp}\n")
hyp_set = []
for val in gen_hyp:
    for i in range(len(spc_hyp)):
        temp = val.copy()
        if temp[i] != spc_hyp[i]:
            temp[i] = spc_hyp[i]
            hyp_set.append(temp)

all_hyp = []
for hyp in hyp_set:
    if hyp not in all_hyp:
        all_hyp.append(hyp)
print(f"All hypothesis :")
for hyp in all_hyp:
    print(hyp)