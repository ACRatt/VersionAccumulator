class Organization:
    def __init__(self, name, buildPacks):
        self.name = name
        self.buildPacks = buildPacks
    
def getOrgByName(list, target):
    for index, i in enumerate(list):
        if i.name == target:
            return index
    return -1

def getPackByName(org, packName):
    for pack in org.buildPacks:
        if pack[0] == packName:
            return pack
    return -1

def printResults(envName, env):
    print(envName + " Records:")
    for org in env:
        buildList = []
        for pack in org.buildPacks:
            buildList.append(pack[0] + ": " + str(pack[1]))
        print(org.name + " uses: " + ', '.join(buildList) + "\n")