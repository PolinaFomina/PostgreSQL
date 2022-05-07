import json

def getName(line):

    name = line[0].replace(',', '')

    while len(name) != 0 and name[-1] == ' ':
        name = name[0:-1]

    while len(name) != 0 and name[0] == ' ':
        name = name[1:]

    name = name.replace('\"', '')
    name = name.replace('\\', '')
    return name

def getTitle(line):

    title = []
    index = 0

    while index < len(line) and line[index] == ' ':
        index = index + 1

    while index < len(line) and line[index] != '(':
        title.append(line[index])
        index = index + 1

    while len(title) != 0 and title[-1] == ' ':
        title = title[0:-1]

    seriesName = ""
    if len(title) != 0 and title[0] == '\"' and title[-1] == '\"':
        seriesName = getSeriesName(line)

    title = ''.join(title)
    seriesName = ''.join(seriesName)
    if seriesName != "":
        title = title + " " + seriesName
    title = title.replace('\"', '')
    title = title.replace('\\', '')

    return title

def getSeriesName(line):

    name = []
    index = 0

    while index < len(line) and line[index] != '{':
        index = index + 1

    while index < len(line) and line[index] != '}':
        name.append(line[index])
        index = index + 1

    if index < len(line) and line[index] == '}':
        name.append(line[index])

    name = ''.join(name)
    return name

def getYear(line):

    year = []
    index = 0

    while index < len(line) - 1 and (line[index] != '('
                                     or (line[index] == '(' and not line[index + 1].isdigit())):
        index = index + 1

    index = index + 1
    while index < len(line) and line[index] != ')':
        year.append(line[index])
        index = index + 1

    year = ''.join(year)
    return year

def getCharacterName(line):

    name = []
    index = 0

    while index < len(line) and line[index] != '[':
        index = index + 1

    index = index + 1
    if index < len(line):
        while index < len(line) and line[index] != ']':
            name.append(line[index])
            index = index + 1

    name = ''.join(name)
    name = name.replace('\"', '')
    name = name.replace('\\', '')
    return name

datasetActors = open("/Users/polinafomina/Documents/Study/PyCharm/SUBD/actors.txt", "r", encoding = "ISO-8859-1")
datasetActresses = open("/Users/polinafomina/Documents/Study/PyCharm/SUBD/actors.txt", "r", encoding = "ISO-8859-1")
dataset = open("/Users/polinafomina/Documents/Study/PyCharm/SUBD/dataset.txt", "w", encoding="UTF-8")

j = 0
jsonString = ""
roles = []
actor = []

for line in datasetActors:

    name_ = ""
    title_ = ""
    year_ = ""
    characterName_ = ""

    line = line.rstrip("\n")
    array = line.split("\t")

    name_ = getName(array)

    index_ = 1

    while index_ < len(array) and array[index_] == '':
        index_ = index_ + 1

    if index_ < len(array):
        title_ = getTitle(array[index_])
        year_ = getYear(array[index_])
        characterName_ = getCharacterName(array[index_])

    if name_ != "" and title_ != "" and year_ != "":
        if jsonString != "":
            print(jsonString)
            dataset.write(jsonString + '\n')
            j = j + 1
            jsonString = ""
            roles = []
        role1 = {'title': title_, 'year': year_, 'character': characterName_}
        roles.append(role1)
        actor = {'id': j, 'primaryName': name_, 'roles': roles}
        jsonString = json.dumps(actor)
    elif name_ == "" and title_ != "" and year_ != "":
        role2 = {'title': title_, 'year': year_, 'character': characterName_}
        roles.append(role2)
        actor["roles"] = roles
        jsonString = json.dumps(actor)


for line in datasetActresses:

    name_ = ""
    title_ = ""
    year_ = ""
    characterName_ = ""

    line = line.rstrip("\n")
    array = line.split("\t")

    name_ = getName(array)

    index_ = 1

    while index_ < len(array) and array[index_] == '':
        index_ = index_ + 1

    if index_ < len(array):
        title_ = getTitle(array[index_])
        year_ = getYear(array[index_])
        characterName_ = getCharacterName(array[index_])

    if name_ != "" and title_ != "" and year_ != "":
        if jsonString != "":
            print(jsonString)
            dataset.write(jsonString + '\n')
            j = j + 1
            jsonString = ""
            roles = []
        role1 = {'title': title_, 'year': year_, 'character': characterName_}
        roles.append(role1)
        actor = {'id': j, 'primaryName': name_, 'roles': roles}
        jsonString = json.dumps(actor)
    elif name_ == "" and title_ != "" and year_ != "":
        role2 = {'title': title_, 'year': year_, 'character': characterName_}
        roles.append(role2)
        actor["roles"] = roles
        jsonString = json.dumps(actor)
