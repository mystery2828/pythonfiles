import random
usn_is = ["1JS16IS022","1JS17IS001","1JS17IS005","1JS17IS007",
       "1JS17IS010","1JS17IS011","1JS17IS016","1JS17IS017","1JS17IS018","1JS17IS019","1JS17IS020","1JS17IS021",
       "1JS17IS022","1JS17IS023","1JS17IS024","1JS17IS026","1JS17IS028","1JS17IS029","1JS17IS030","1JS17IS031",
       "1JS17IS032","1JS17IS035","1JS17IS036","1JS17IS040","1JS17IS041","1JS17IS043","1JS17IS046","1JS17IS050",
       "1JS17IS051","1JS17IS058","1JS17IS059","1JS17IS061","1JS17IS062","1JS17IS067","1JS17IS071","1JS17IS077",
       "1JS17IS079","1JS17IS080","1JS17IS084","1JS17IS085","1JS17IS088","1JS15IS093","1JS16IS064"]
usn_ec = ["1JS17EC002",
       "1JS17EC003","1JS17EC008","1JS17EC016","1JS17EC021","1JS17EC025","1JS17EC028","1JS17EC032","1JS17EC035",
       "1JS17EC051","1JS17EC069","1JS17EC071","1JS17EC079","1JS17EC080","1JS17EC082","1JS17EC083","1JS17EC085",
       "1JS17EC095","1JS17EC096","1JS17EC102","1JS17EC115","1JS17EC120","1JS17EC122","1JS17EC125","1JS17IM004"]
print(len(usn_ec))
print(len(usn_is))
x_is=[]
x_ec=[]
all_is = []
all_ec = []
project_is=["Tic-Tac-Toe","Monkey-Bananas","8-Puzzle","Magic-Square","Missionaries and cannibals","Cryptarithmatic","Bridge","Block World Problem","Tower of Honal","Chess","Travelling Salesman","8 Queens"]
project_ec=["Tic-Tac-Toe","Monkey-Bananas","8-Puzzle","Magic-Square","Missionaries and cannibals","Cryptarithmatic","Bridge","Block World Problem","Tower of Honal","Chess","Travelling Salesman","8 Queens"]
def letsdoitis(usn_is,x_is,project_is,all_is):
    for j in range(len(usn_is)):
        if len(usn_is)>3:
            for i in range(4):
                w = len(usn_is) - 1
                y = random.randint(0, w)
                x_is.append(usn_is[y])
                all_is.append(usn_is[y])
                usn_is.remove(usn_is[y])
            if len(project_is)>0:
                q = len(project_is) - 1
                z = random.randint(0, q)
                z1 = project_is[z]
                project_is.remove(project_is[z])
                print(x_is, end='')
                print("=> %s" %z1)
                print("\n")
                del x_is[:]
def letsdoitec(usn_ec,x_ec,project_ec,all_ec):
    for j in range(len(usn_ec)):
        if len(usn_ec)>3:
            for i in range(4):
                w = len(usn_ec) - 1
                y = random.randint(0, w)
                x_ec.append(usn_ec[y])
                all_ec.append(usn_ec[y])
                usn_ec.remove(usn_ec[y])
            if len(project_ec)>0:
                q = len(project_ec) - 1
                z = random.randint(0, q)
                z1 = project_ec[z]
                project_ec.remove(project_ec[z])
                print(x_ec, end='')
                print("=> %s" %z1)
                print("\n")
                del x_ec[:]
letsdoitis(usn_is,x_is,project_is,all_is)
letsdoitec(usn_ec,x_ec,project_ec,all_ec)