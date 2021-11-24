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
allGroups = []
groupNum = 0
while len(allNames) > 0:
    group = [f'Group {groupNum}:']
    for i in range(min(membersPerGroup, len(allNames))):
        group.append(allNames.pop(random.randrange(0, len(allNames))))
    allGroups.append(group)
    groupNum += 1

# writing results in a csv file
with open('./groups.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(allGroups)
