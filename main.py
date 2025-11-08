import csv

type_counter = [["ghost",0],["flying",0],["poison",0],["ground",0],["fairy",0],["dragon",0],["rock",0],["normal",0],["fighting",0],["bug",0],["dark",0],["ice",0],["psychic",0],["electric",0],["grass",0],["water",0],["fire",0],["steel",0]]
type2_counter = [["ghost",0],["flying",0],["poison",0],["ground",0],["fairy",0],["dragon",0],["rock",0],["normal",0],["fighting",0],["bug",0],["dark",0],["ice",0],["psychic",0],["electric",0],["grass",0],["water",0],["fire",0],["steel",0]]

count2ndtype = False
show2ndtype = True
includeforms = True #this way whenever a prenthese is found during processing, the form will be counted


def Addtocounter(pokemon):
    if count2ndtype :
        for i in type_counter :
            if i[0].lower() == pokemon[3].lower() :
                i[1] += 1
            if i[0].lower() == pokemon[4].lower() :
                i[1] += 1
    else :
        for i in type_counter :
            if i[0].lower() == pokemon[3].lower() :
                i[1] += 1
        for i in type2_counter:
            if i[0].lower() == pokemon[4].lower() :
                i[1] += 1

def Showcounter():
    if count2ndtype :
        for i in type_counter :
            print(i[0] + ": " + i[1])
    elif show2ndtype :
        for i in range(len(type_counter)) :
            print(str(type_counter[i][0]) + ": " + str(type_counter[i][1]) + "(+ " + str(type2_counter[i][1])+")")
    else : 
         for i in type_counter :
            print(i[0] + ": " + i[1])


def Getmonsbyname(list ="" ,separator = ""):
    splitlist = []
    res = []
    ignorenext = False
    # note that at the start : 0 = all    1 = mega    2 = Alolan form  3 = Galarian form   4 = Hisuian Form    5-9 = contextual1-5
    Formlist = ["","Mega","Alolan","Galarian","Hisuian"]
    if separator == "" :
        lastword = 0
        for i in range(len(list)) :
            if (list[i].upper() == list[i] or list[i] in ["1","2","3","4","5","6","7","8","9","0"] )and not ignorenext :
                if i != 0  :
                    splitlist+= [str(list[lastword:i])]
                    lastword = i
                    ignorenext = True
            else :
                ignorenext = False
            
            if i == len(list)-1 :
                splitlist+= [str(list[lastword:i+1])]
    else :
        splitlist = list.split(separator)
    with open('pokemon.csv', newline='') as csvfile:
        pkmnreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        newsplit = splitlist.copy()
        found = ""
        for row in pkmnreader:
            
            for i in splitlist :
                if i[0] == "0" and row[2] != "" : 
                    if row[1].lower() == i.lower()[1:] and Formlist[int(i[0])] in row[2]:
                        #print("found : "+ row[2] + " " + row[1])
                        res += [row]
                        break
                if i[0] in ["1","2","3","4"] and row[2] != "":
                    if row[1].lower() == i.lower()[1:] and Formlist[int(i[0])] in row[2]:
                        #print("found : "+ row[2])
                        res += [row]
                        found = i
                        break
                if i[0] in ["5","6","7","8","9"] and row[2] != "":
                    
                    if row[1].lower() == i.lower()[1:] :
                        #print("searching through forms")
                        res += [Getmonsbyname("0" + i[1:])[int(i[0])-5]]
                        #print("found : "+ row[2])
                        found = i
                        
                else : 
                    if row[1].lower() == i.lower() :
                        #print("found : "+ row[1])
                        res += [row]
                        found = i
                        break
            if found != "" :
                if i in splitlist : 
                   splitlist.remove(i)
                found = ""
            
    return res

def Processlistofmons(list,separator = ""):
    processed = Getmonsbyname(list,separator)
    for i in processed:
        Addtocounter(i)

    Showcounter()

list = input("liste de pokemons?")
Processlistofmons(list)

