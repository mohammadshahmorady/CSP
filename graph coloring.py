from timeit import default_timer


def backtrack(domains, constraints, cities, FW, MRV):
    Min = 9999999
    min_index = -1
    for i in range(len(domains)):  # minimum remaining value
        if len(domains[i]) == 0:
            return False, []
        if cities[i] == -1 and len(domains[i]) < Min:
            Min = len(domains[i])
            min_index = i
            if MRV == 'n':
                break

    if min_index == -1:
        return True, cities

    for i in domains[min_index]:
        newDomains = Domains.copy()
        newDomains[min_index] = [i]
        cities[min_index] = i
        if FW == 'y':
            for j in range(len(constraints[min_index])):  # forward checking
                if constraints[min_index][j] == '1' and (i in newDomains[j]):
                    newDomains[j].remove(i)
        else:
            flag = False
            for j in range(len(constraints[min_index])):  # check if chosen value satisfies the constraints
                if constraints[min_index][j] == '1' and cities[j] == i:
                    flag = True
                    break
            if flag:
                continue

        isAns, Cities = backtrack(newDomains, constraints, cities, FW, MRV)
        if isAns:
            return True, Cities

    return False, []


Input = open("input.txt", "r")
Colors = Input.readline().split(",")
Colors[-1] = Colors[-1][:-1]
Map = Input.read().split("\n")
Input.close()

Domains = []
for _ in range(len(Map)):
    Domains.append(list(range(len(Colors))))

forward_check = input("Do you want forward checking? (y/n): ")
mrv = input("Do you want to apply minimum remaining value? (y/n): ")
t = default_timer()
ans, colors = backtrack(Domains, Map, [-1] * len(Domains), forward_check, mrv)
time = default_timer() - t

Output = open("output.txt", "w")
if ans:
    Output.write("YES," + str(round(time * 1000, 2)) + "ms")
    for c in range(len(colors)):
        Output.write("\n" + str(c) + ":" + Colors[colors[c]])
else:
    Output.write("NO," + str(round(time * 1000, 2)) + "ms")

Output.write("\nForward Checking : " + forward_check + "\nMinimum remaining value : " + mrv)

Output.close()
