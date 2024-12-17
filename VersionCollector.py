import csv
import Organization
from Organization import Organization as Org

ap01 = "ap01-anon.csv"
vp01 = "vp01-anon.csv"

def process_environment(env):

    rows = []
    orgs = []

    with open(vp01, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        next(csvreader)

        for row in csvreader:
            if not any (org.name == row[1] for org in orgs):
                orgs.append(Org(row[1], [])) 
            else:
                org = orgs[Organization.getOrgByName(orgs, row[1])]
                if(row[4] == ''):
                    if not any (pack[0] == "unknown" for pack in org.buildPacks):
                        org.buildPacks.append(["unknown", 1])
                    else:
                        pack = Organization.getPackByName(org, "unknown")
                    pack[1] = pack[1] + 1
                elif not any (pack[0] == row[4] for pack in org.buildPacks):
                    org.buildPacks.append([row[4], 1])
                else:
                    pack = Organization.getPackByName(org, row[4])
                    pack[1] = pack[1] + 1
                    
            rows.append(row)
        

        csvfile.close()
    return orgs

ap01Orgs = process_environment(ap01)
vp01Orgs = process_environment(vp01)

Organization.printResults("ap01", ap01Orgs)
Organization.printResults("vp01", vp01Orgs)