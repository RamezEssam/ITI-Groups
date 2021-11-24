# importing required libraries
import csv
import random

# reading csv file
with open('./list.csv', newline='') as f:
    reader = csv.reader(f)
    namesList = list(reader)

# putting all the names in one list
allNames = []
for element in namesList:
    allNames.append(element[0])

# splitting groups
membersPerGroup = 4
allGroups = {}
groupNum = 1
while len(allNames) > 0:
    group = []
    for i in range(min(membersPerGroup, len(allNames))):
        group.append(allNames.pop(random.randrange(0, len(allNames))))
    allGroups[f'Group {groupNum}'] = group
    groupNum += 1

# assigning remaining group members
allGroups[f'Group {random.randint(1, 8)}'].append(allGroups['Group 10'].pop())
allGroups[f'Group {random.randint(1, 8)}'].append(allGroups['Group 10'].pop())
allGroups.pop('Group 10')

# writing results in a csv file
with open('./groups.csv', 'w') as f:
    writer = csv.writer(f)
    for key, value in allGroups.items():
        writer.writerow([key, value])
