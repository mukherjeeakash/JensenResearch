import matplotlib.pyplot as plt
import re

readFile = open("C:\College\Research\S_Mutans_Analysis\S.Mutans.txt", "r")
genomeFile = readFile.read()
readFile.close

lines = genomeFile.split('\n')
genome = ''

for i in lines:
    genome += i
unique20 = []
unique19 = []
nonUnique20 = []
nonUnique19 = []

def complement(s):
    result = ""
    for i in s:
        if i == "T":
            result+="A"
        elif i == "A":
            result+="T"
        elif i == "C":
            result+="G"
        elif i == "G":
            result+="C"
    return result

def countUniques(num):
    unique = {}
    nonUnique = {}
    total = 0
    for i in range(len(genome)):
        if genome[i:i+2] == "TA":
            if (i+2 - num) >= 0:
                total += 1
                if genome[i+2 - num:i+2] in nonUnique:
                    pass
                elif genome[i+2 - num:i+2] in unique:
                    if i+2-num != unique[genome[i+2 - num:i+2]][0]:
                        nonUnique[genome[i+2 - num:i+2]] = i+2 - num
                        unique.pop(genome[i+2 - num:i+2])
                if complement(genome[i+2 - num:i+2]) in nonUnique:
                    pass
                elif complement(genome[i+2 - num:i+2]) in unique:
                    if i+2-num != unique[complement(genome[i+2 - num:i+2])][0]:
                        nonUnique[complement(genome[i+2 - num:i+2])] = i+2 - num
                        unique.pop(complement(genome[i+2 - num:i+2]))
                else:
                    unique[genome[i+2 - num:i+2]] = [i+2-num, "r"]
                    unique[complement(genome[i+2 - num:i+2])] = [i+2-num, "r"]
            if (i+ num - 1 < len(genome)):
                total += 1
                if genome[i:i+num] in nonUnique:
                    pass
                elif genome[i:i+num] in unique:
                    if i != unique[genome[i:i+num]]:
                        nonUnique[genome[i:i+num]] = i
                        unique.pop(genome[i:i+num])
                if complement(genome[i:i+num]) in nonUnique:
                    pass
                elif complement(genome[i:i+num]) in unique:
                    if i != unique[complement(genome[i:i+num])]:
                        nonUnique[complement(genome[i:i+num])] = i
                        unique.pop(complement(genome[i:i+num]))
                else:
                    unique[genome[i:i+num]] = [i, "f"]
                    unique[complement(genome[i:i+num])] = [i, "f"]
    if (num == 20):
        unique20.append(unique)
        nonUnique20.append(nonUnique)
    if (num == 19):
        unique19.append(unique)
        nonUnique19.append(nonUnique)
    return ((len(unique))/(total*2))

plotData = []
for i in range(3, 21):
    plotData.append(countUniques(i))

plt.plot([i for i in range(3,21)], plotData, color = "Orange")
plt.title("Percent uniqueness vs. Length of TA Recognition Site Length")
plt.xlabel("Length of TA Recognition Site Length")
plt.ylabel("Percent uniqueness")
plt.axvline(x = 15, color = "Blue")
plt.show()
print(plotData)

# print(len(unique19[0]))
# print(len(unique20[0]))
# map20 = {}
# for i in unique19[0]:
#     if unique19[0][i][1] == "r":
#         if not (("C" + i) in unique20[0] or ("A" + i) in unique20[0] or ("T" + i) in unique20[0] or ("G" + i) in unique20[0]):
#             print(unique19[0][i])
#         elif ("C" + i) in unique20[0]:
#             if "C"+i in map20:
#                 print("C"+i)
#                 break
#             map20["C"+i] = 0
#         elif ("T" + i) in unique20[0]:
#             if "T"+i in map20:
#                 print("T"+i)
#                 break
#             map20["T"+i] = 0
#         elif ("A" + i) in unique20[0]:
#             if "A"+i in map20:
#                 print("A"+i)
#                 break
#             map20["A"+i] = 0
#         elif ("G" + i) in unique20[0]:
#             if "G"+i in map20:
#                 print("G"+i)
#                 break
#             map20["G"+i] = 0
#     else:
#         if  not ((i + "C") in unique20[0] or (i + "A") in unique20[0] or (i + "T") in unique20[0] or (i + "G") in unique20[0]):
#             print(unique19[0][i])
#             break
#         elif (i + "C") in unique20[0]:
#             if i+"C" in map20:
#                 print(i+"C")
#                 break
#             map20[i+"C"] = 0
#         elif (i + "T") in unique20[0]:
#             if i+"T" in map20:
#                 print(i+"T")
#                 break
#             map20[i+"T"] = 0
#         elif (i + "A") in unique20[0]:
#             if i+"A" in map20:
#                 print(i+"A")
#                 break
#             map20[i+"A"] = 0
#         elif (i + "G") in unique20[0]:
#             if i+"G" in map20:
#                 print(i+"G")
#                 break
#             map20[i+"G"] = 0
# 
# print("TAAGAAAGTCAACGGCATT" in unique19[0])
# print("AAGAAAGTCAACGGCATTA" in unique19[0])
# 
# print([m.start() for m in re.finditer('(?=AAGAAAGTCAACGGCATTA)', genome)])

# splice = genome[1150806:1150826]
# print(splice)
# print(splice[:19])
# print([m.start() for m in re.finditer(splice[:19], genome)])
# 
# print(splice[:] in unique20[0])
# 
# def countUniques2(num):
#     patterns = []
#     total = 0
#     unique = 0
#     for i in range(len(genome)):
#         if genome[i:i+2] == "TA":
#             if (i+2 - num) >= 0:
#                 total += 1
#                 patterns.append(genome[i+2 - num:i+2])
#             if (i+ num - 1 < len(genome)):
#                 total += 1
#                 patterns.append(genome[i:i+num])
#     for i in patterns:
#         if (len([m.start() for m in re.finditer(i, genome)]) == 1):
#             unique+=1
#     return ((unique)/total)
# 
# for i in range(3, 21):
#     plotData.append(countUniques2(i))
# 
# plt.plot([i for i in range(3,21)], plotData, color = "Orange")
# plt.title("Percent uniqueness vs. Length of TA Recognition Site Length")
# plt.xlabel("Length of TA Recognition Site Length")
# plt.ylabel("Percent uniqueness")
# plt.axvline(x = 15, color = "Blue")
# plt.show()
# print(plotData)