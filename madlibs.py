import random as rd
import pyttsx3

def say(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('rate', 150)
    
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    
def splt(tab):
    for i in range(len(tab)):
        tab[i] = tab[i].split(";")
    return tab

nom = open("nouns.txt", encoding='utf-8').read().split("\n")
nom = splt(nom)

nom_fem = []
nom_mas = []
for i in range(len(nom)-1):
    if nom[i][1] == "fem":
        nom_fem.append(nom[i])
    elif nom[i][1] == "mas":
        nom_mas.append(nom[i])
verbes = open("verbs.txt", encoding='utf-8').read().split("\n")
verbes = splt(verbes)
verbe=[]
for i in range(len(verbes)):
    if len(verbes[i]) == 3 and verbes[i][2]=="3sg":
        verbe.append(verbes[i])
        

adj = open("adjectives.txt", encoding='utf-8').read().split("\n")
adj = splt(adj)

adj_fem = []
adj_mas = []
for i in range(len(adj)-1):
    if adj[i][1] == "fem":
        adj_fem.append(adj[i])
    elif adj[i][1] == "mas":
        adj_mas.append(adj[i])
conj = open("conjunctions.txt", encoding='utf-8').read().split("\n")
conj = splt(conj)

deter = open("determiners.txt", encoding='utf-8').read().split("\n")
deter = splt(deter)
        
adv = open("adverbs.txt", encoding='utf-8').read().split("\n")
adv = splt(adv)

prep = open("prepositions.txt", encoding='utf-8').read().split("\n")
prep = splt(prep)

pronoun = open("pronouns.txt", encoding='utf-8').read().split("\n")
pronoun = splt(pronoun)


def nom(noms):
    return noms[rd.randint(0,len(noms)-1)]

determinant = deter[rd.randint(0,len(deter)-1)]
for i in range(3) :
    if determinant[1] == "mas":
        say(determinant[0]+" "+nom(nom_mas)[0]+" "+nom(adj_mas)[0]+" "+verbe[rd.randint(0,len(verbe)-1)][0]+" "+adv[rd.randint(0,len(adv)-1)][0]+"\n"+conj[rd.randint(0,len(conj)-1)][0]+" "+determinant[0]+" "+nom(nom_mas)[0]+" "+nom(adj_mas)[0]+" "+verbe[rd.randint(0,len(verbe)-1)][0]+" "+adv[rd.randint(0,len(adv)-1)][0])
    else:
        say(determinant[0]+" "+nom(nom_fem)[0]+" "+nom(adj_fem)[0]+" "+verbe[rd.randint(0,len(verbe)-1)][0]+" "+adv[rd.randint(0,len(adv)-1)][0]+"\n"+conj[rd.randint(0,len(conj)-1)][0]+" "+determinant[0]+" "+nom(nom_fem)[0]+" "+nom(adj_fem)[0]+" "+verbe[rd.randint(0,len(verbe)-1)][0]+" "+adv[rd.randint(0,len(adv)-1)][0])
        
