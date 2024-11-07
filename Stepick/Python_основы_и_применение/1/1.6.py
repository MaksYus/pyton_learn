classes = {}

for _ in range(int(input())):
    row = input().split(' ')
    classes[row[0]] = [row[0]]
    if len(row) != 1:
        parents = row[2::]
        for parent in parents:
            if parent in classes:
                classes[row[0]].extend(classes[parent])
            else:
                classes[row[0]].append(parent)

        for key in classes:
            if key == row[0]:
                classes[key] = list(set(classes[key]))
                continue
            if row[0] in classes[key]:
                classes[key].remove(row[0])
                classes[key].extend(classes[row[0]])
                classes[key] = list(set(classes[key]))

for _ in range(int(input())):
    row = input().split(' ')
    if row[0] in classes[row[1]]:
        print('Yes')
    else:
        print('No')
