import math
import random
import os
if len(os.path.dirname(__file__)) > 0  :
    os.chdir(os.path.dirname(__file__))
def roll(a):
    s=0
    ndice=0
    if "*" in a :
        for i in range(len(a)) :
            if a[i]=="*" :
                if "d" in a[:i] :
                    return int(a[i+1:])*roll(a[:i])
                else :
                    return int(a[:i])*roll(a[i+1:])
    for i in range(len(a)) :
        if a[i]=="d" :
            ndice=int(a[:i])
            nface=int(a[i+1:])
    for i in range(ndice) :
        jet=random.randint(1,nface)
        s= s + jet
    if s==0 :
        return int(a)
    return s
def multipleroll(b):
    s=0
    y=0
    for i in range(len(b)):
        if b[i]=="+" :
            r=roll(b[y:i])
            s=s+r            
            y=i
    r=roll(b[y:])
    s=s+r
    return s

file = open("fdpmodele.svg","r",encoding="utf-8") #importation du modèle svg
svg = file.read()
file.close
print ("Combien de caractéristiques ?"); #nombre de caractéristiques
while True:
    try:
        c =int(input())
        break
    except ValueError:
        print("Veuillez saisir un nombre entier")
i = 1;
listcarac= ["nom", "race","sexe"] 
while i<= c: # nommage des caractéristiques
    print ("Quel est le nom de la caractéristique", i, "?");
    caracn= input();
    num = str(i)
    carac= "carac " + num
    posc = svg.find(carac)
    listcarac.append (caracn);
    i = i+1;
    if posc > 0: #écriture des noms des caractéristiques dans le svg
        svg = svg[:posc]+ caracn+svg[posc+7:]
if c<7: # ajustement de la taille du tableau et suppression des colonnes inutiles
    i= 7
    width = (29.889563*7)/c
    écart = width-29.889563
    while i > c: #suppression des colonnes inutiles
        num = str(i)
        supc = 'id="carac'+ num+ '"'
        pos= svg.find(supc)
        sups = 'id="stat' + num+ '"'
        poss = svg.find(sups)
        supctxt= 'id="car' + num
        supstxt = 'id="sta' + num
        posctxt = svg.find(supctxt)
        posstxt = svg.find(supstxt)
        rectctxt= svg[posctxt-393:posctxt+338]
        rectstxt= svg[posstxt-395:posstxt+335]
        poss = poss-37
        rects = svg[poss:poss+313]
        pos = pos-35
        posf = pos+312
        rectc= svg[pos:posf]
        svg = svg.replace(rectc,"" )
        svg = svg.replace(rects,"")
        svg = svg.replace(rectctxt,"")
        svg = svg.replace(rectstxt,"")
        i= i-1
    i= 1
    while i<=c : #ajustement de la taille des colonnes
        num = str(i)
        supc = 'id="carac'+ num+ '"'
        pos = svg.find(supc)
        x = float(svg[pos+166:pos+175])
        xnew = x + (i-1)*écart
        suptxt='id="sta'+ num
        postxt = svg.find(suptxt)
        xtxt = float(svg[postxt+99:postxt+108])
        xtxtnew= xtxt+ (i-1)*écart
        svg = svg.replace(str(x),str(xnew))
        svg = svg.replace(str(xtxt), str(xtxtnew))
        i= i+1
    width = str(width)
    svg = svg.replace("29.889563", width)
print ("Comment sont tirées les caractéristique ? (ex:1d6+3)"); #selection de la manière de tirer les caractéristiques
tirage = str(input());
while True:
    try :
        multipleroll(tirage)
        break
    except:
        print("Veuillez donner un lancer de dès valide")
        tirage = input()
print ("Combien de personnages vont être crées ?") #séléction du nombre de personnage
while True:
    try:
        personbr=int(input())
        break
    except ValueError:
        print("Veuillez saisir un nombre entier")
l= 0
listeperso = []
mode=""
print("Comment voulez-vous que les noms, races, sexe soit choisi ? (m pour manuel, a pour aléatoire, p pour procédural")
mode = input()
while mode != "m" and mode != "a" and mode != "p":
    print("Veuillez saisir m ou a ou p")
    mode = input()
while l < personbr :
    fdp = svg;
    perso = [];
    if mode == "m" : #mode manuel
        print ("Quel est le nom du personnage n°",l+1,"?");
        nom = input();
        print ("Quel est la race du personnage n°",l+1,"?");
        race = input();
        print("Quel est le sexe du personnage n°",l+1,"?");
        sexe = input();
        sexe = "sexe : " + sexe
    if mode == "p": #mode procédural (seul le nom est choisi aléatoirement)
        import os
        i = 0
        liste = os.listdir()
        ftxt=[]
        while i< len(liste):
            if "listenom" in liste[i] and".txt" in liste[i]:
                ftxt.append(liste[i])
            i= i+1
        i= 0
        listrace= []
        while i<len(ftxt):
            race = ftxt[i]
            race = race[9:-5]
            if race not in listrace:
                listrace.append(race)
            i= i+1
        race =""
        print("Quel est la race de ton personnage ? (parmi " ,', '.join(listrace),")")
        race = input()
        while race not in listrace:
            print("Veuillez selectionnez une race valide");
            race = input()   
        print("le personnage est de quel sexe ? (0 pour neutre, 1 pour homme, 2 pour femme):",);
        sexe =input()
        fname = "listenom " + race + sexe +".txt";
        while fname not in ftxt:
            print("ce sexe n'existe pas pour cette race ou alors n'est pas dans le dossier du programme");
            sexe = input();
            fname = "listenom " + race + sexe +".txt";
        file = open(fname,"r", encoding="utf-8");
        txt = file.readlines();
        maxr = len(txt)-1;
        rnum= random.randint(0, maxr);
        nom = txt[rnum];
        nom = nom.rstrip();
        sexecon = ["N","M","F"]
        sexe = "sexe : " + sexecon[int(sexe)]
    if mode == "a": #mode automatique (purement aléatoire)
        import os
        i = 0
        liste = os.listdir()
        ftxt=[]
        while i< len(liste):
            if "listenom" in liste[i] and".txt" in liste[i]:
                ftxt.append(liste[i])
            i= i+1
        i= 0
        maxnbr= len(ftxt)-1
        filenbr = random.randint(0, maxnbr)
        fname = ftxt[filenbr]
        race = fname[9:-5]
        sexe = int(fname[-5])
        file = open(fname,"r", encoding="utf-8");
        txt = file.readlines();
        maxr = len(txt)-1;
        rnum= random.randint(0, maxr);
        nom = txt[rnum];
        nom = nom.rstrip()
        sexecon = ["N","M","F"]
        sexe = "sexe : " + sexecon[sexe]
    perso.append(nom);
    perso.append(race);
    perso.append(sexe);
    fdp = fdp.replace("nom",nom);
    fdp = fdp.replace("race :",race);
    fdp = fdp.replace("sexe :",sexe);
    i = 1;
    b = 0;
    while i <= c: # tirage des caractéristiques
        i = i+1;
        score = int(multipleroll(tirage));
        perso.append(score);
        num = str(i-1);
        stat = "stat " + num;
        posc = fdp.find(stat);
        if posc >0 : # ajout du tirage obtenu sur le svg
            comp = str(score);
            fdp = fdp[:posc]+ comp + fdp[posc+6:];
    fnom = "fdp_" + nom + ".svg";
    file = open(fnom, "w+", encoding="utf-8");
    file.write(fdp);
    file.close
    print (perso);
    i = 0;
    l= l+1;
    ligneperso = "";
    while b <= c+2: # pour permettre l'export de plusieurs personnage
        t=str(perso[b])
        ligneperso = ligneperso + "," + t ;
        b= b+1;
    ligneperso = ligneperso[1:];
    listeperso.append(ligneperso) 
print("Voulez-vous exporter en csv (tableur) ? (y pour dire oui)");
reponse = input();
if reponse == "y": #export en csv
    import csv
    with open('jdr.csv', 'w', newline='',encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',)
        fieldnames = []
        while i <= c+2:
            fieldnames.append (listcarac[i]) ;
            i = i+1;
        headwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        headwriter.writeheader()
        personnage =""
        n = 0
        while n < personbr:
            personnage = listeperso[n]
            personnage = personnage.replace('"','')
            writer.writerow([personnage]);
            n = n+1
