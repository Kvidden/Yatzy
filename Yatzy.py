#!/bin/python3
import random
#Copyright (c) 2023, Mikael Kvist
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 
"""
En dict för yatzy datan och skapade listor nästlade in i denna dict för att använda för olika saker.
Vissa av dessa listor får sedan variabler som man kan återkalla i andra funktioner.
Speciellt dices är mycket bra att alla räknade funktioner kan hämta ifrån denna dictionary.
"""

yatzy_data = {
    "Deltagare": [],
    "dices": [],
    "omkastning": [],
    "Slutresultat": []
}
dices = yatzy_data["dices"]
deltagare = yatzy_data["Deltagare"]

def dice():
    """
    En funktion som bara har return, denna skulle kunna byggas in i rullningen istället för att
    kalla denna funktionen såklart.
    Första skrivandet av spelet så fanns det 5st tärningar som sparade sina värden i en variabel och fungerade
    så som listan för tärningar och omkast gör fast man matade in 1 eller 0 i funktionen.
    Därför lever funktionen kvar...

    :return: random heltal mellan 1 till 6
    """
    return random.randint(1,6)

def singeltal(tal):
    """
    Sätter en variable till antalet med värdet 0 och sedan kollar vidare med en for loop som räknar upp
    varje tärning i listan av tärningar.
    Sedan är det en if sats som räknar upp antal med + 1 ifall värdet för tärningen i for loopen är
    samma som det tal som vi frågar efter.

    När for loopen är klar så kollar vi om antal är 1 eller fler och tar isf antal gånger det tal vi kollar efter.

    Denna funktionen går säker att få ihop med kortare kod så som sum() kanske men nu funkar det för tillfället.

    :param tal: tal är det tal vi skall kolla bland alla tärningar
    :return: retunerar 0 ifall inte den siffran vi kollar efter via tal inte finns, finns den så räknar vi antalet gånger
    denna siffra finns med och tar det antalet och gångrar med siffran i fråga för att retunera det värdet.
    """
    antal = 0
    for single_dice in dices:
        if single_dice == tal:
            antal += 1
    if antal >= 1:
        antal *= tal
    return antal


def pairs(check):
    """
    Har variabler för par och tvåpar som är satta till 0 för att kunna användas senare ifall inte det vi söker uppfylls.
    En variabel som håller reda på antalet gånger det finns fler än 2st av ett värde i set(dices) bland dices.
    If satsen kollar så att det finns fler än 2st av ett nr och sätter par till detta nr, plussar tvåpar med sig själv och detta nr
    samt räknar upp antalet gånger vi har haft par i bland våra tärningar.
    Varför tvåpar plusar med sig själv och par bara blir nummret är för att med set() så tas alla dubbleter bort och sorteras i ordning
    vilket gör att finns det 2st 1:or och 2st 5:or [1,1,3,5,5] så kommer paret bara ge det högsta, för det är väl ändå det värdet
    man vill ha medans tvåpar blir då 1 + 5.

    In i funktionen matas värdet av check vilket är 1 eller 2 beroende på om vi skall kolla efter 1 par eller 2 par.

    Efter for loopen är klar så kommer en if sats som kollar ifall pair_counter är 1 eller högre, samt om check är 1 så kommer
    funktionen att retunera pair * 2 vilket som i exemplet skulle ge 10.
    Varför första if satset är >= är för att även fast det finns 2 par så skall funktionen kunna räkna ut 1 par också,
    detta då 2par redan vara gjord och man behöver bara par.
    Elif är satt till att pair_counter skall vara 2 d.v.s det finns 2st par bland dices, samt att check skall vara satt till 2
    så att den inte retunerar tvåpar värde när man bara frågar efter par.
    Ifall inget av dessa stämmer så retuneras 0

    :param check: bestämmer om det skall kollas efter ettpar eller tvåpar
    :return: retunerar 0 ifall inte det finns ettpar eller tvåpar, annars par * 2 eller tvåpar * 2 beroende på vilket som söks
    """
    pair = 0
    twopairs = 0
    pair_counter = 0
    for each in set(dices):
        if dices.count(each) >= 2:
            pair_counter += 1
            pair = each
            twopairs += each
    if pair_counter >= 1 and check == 1:
        return pair * 2
    elif pair_counter == 2 and check == 2:
        return twopairs * 2
    else:
        return 0

def repeated(amount):
    """
    Kollar på repiternade siffror i ett set av tärningar med en for loop och kollar så att det finns minst
    det antalet som anges i amount.
    Ifall det finns minst 3 eller 4 vilket den främst används till så sätts variablen nr till värdet på denna tärningen
    som sedan retuneras.
    Har variablen nr som är satt till 0 så att alltid 0 retuneras ifall inte triss eller fyrtal finns.

    :param amount: värdet som skall kollas om det finns minst antal av i set(dices)
    :return: retunerar värdet nr som är det tal som återkommer minst antalet gånger satt av amount
    """
    nr=0
    for each in set(dices):
        if dices.count(each) >= amount:
            nr = each
    return nr

def fullhouse():
    """
    Håller koll på om det finns 1st triss och 1st par i listan för träningarna detta genom att köra en for loop
    och kolla ifall genom köra set(dices) och kolla så att siffrorna i detta set finns med 3 gånger samt 2 gånger
    genom en dices.count(inmatad siffra ifrån for loopens set(dices))

    Finns triss och/eller par så sätts variabeln triss eller par till denna siffran och * med 3 respektive 2

    :return: om 1st triss samt 1st par finns så plussas dessa ihop och ger return på värdet
    finns ej någon av dessa retuneras värdet 0
    """
    triss=0
    par=0
    for each in set(dices):
        if dices.count(each) == 3:
            triss = each * 3
        if dices.count(each) == 2:
            par = each * 2
    if triss != 0 and par != 0:
        return triss + par
    else:
        return 0


def rullning():
    """
    Funktion som hanterar rullningen av tärningarna.
    Börjar med att kolla om listan som har värdet för tärningarna är 0, är det noll så börjar den med en for loop
    att lagra värdet av 5st tärningskast

    Ifall det finns något i listan för tärningarna så används även här en for loop för att få ut indexnummret med en range()
    och så kollar om värdet för varje index i omkastningslistan är 1 d.v.s att den skall rullas om.
    Om värdet är 1 så körs dice() funktionen som ger random tal mellan 1-6 och lagrar detta värdet på samma index fast i
    listan för tärningarna.

    :return: ingen return
    """
    if len(set(dices)) == 0:
        for each_dice in range(1, 6):
            dices.append(dice())
    else:
        for index in range(5):
            if yatzy_data["omkastning"][index] == 1:
                dices[index] = dice()
    print("Tärning 1: " + str(dices[0]) + "\nTärning 2: " + str(dices[1]) +"\nTärning 3: " + str(dices[2]) + "\nTärning 4: " + str(dices[3]) + "\nTärning 5: " + str(dices[4]) + "\n")


def dicerolls():
    """
    funktionen som håller koll på antal kast som varje användare har gjort och kollar svar ifrån funktionen stop_or_go
    där man kan välja mellan spara, kasta alla tärningar eller stanna.
    Beroende på svar så bryts loopen, ställer in alla tärningar på att rulla om eller skickar till funktionen save_what
    som beskrivs under.

    Börjar med att rensa tärningar och omkastnings listorna samt nollar räknaren för kasten, detta för att säkerhetställa
    att allt är nollat när vi går in för varje ny spelare och dess kast.
    Sedan får man kasta om såvida räknaren är under 2 och så räknar räknar upp så att stop_or_go inte kommer fram
    ifall vi kastat över 2 gånger
    Efter varje rullning så ställs omkast till 1 på alla d.v.s att alla skall kastas om man inte völjer specifikt
    i save_what funktionen

    :return: ingen return
    """
    dices.clear()
    yatzy_data["omkastning"].clear()
    rollcount=0
    while rollcount <= 2:
        rullning()
        yatzy_data["omkastning"] = [1, 1, 1, 1, 1]
        rollcount+=1
        if rollcount <= 2:
            svar = stop_or_go()
            if svar == "spara":
                save_what()
            if svar == "stopp":
                break


def save_what():
    """
    En fråga som undrar vilka tärningar som skall sparas.
    Tar svaret och matar igenom en for loop som kollar om någon av siffrorna 1-5 är med, dock här som strängar
    då jag vill ha att personen skall kunna skriva 12345 1,2,3,4,5 eller 1 2 3 4 5 vilket inte går med int

    Om respektive nummer finns så kommer indexet för den tärningen i omkastningslistan ställas till 0
    vilket gör att när rullningen rullar på så kommer inte den tärningen inte få ett nytt värde.

    Sätter en variabel i början av funktionen för att minsta koden med några tecken
    :return:
    """
    omkastning = yatzy_data["omkastning"]
    print("Skriv vilken tärning som skall sparas mellan 1-5, sparas ingen rullas alla om igen så kom ihåg det.")
    spara = input()
    for val in spara:
        if val == "1":
            omkastning[0] = 0
        if val == "2":
            omkastning[1] = 0
        if val == "3":
            omkastning[2] = 0
        if val == "4":
            omkastning[3] = 0
        if val == "5":
            omkastning[4] = 0

def stop_or_go():
    """
    En simpel funktion för att fråga om man vill spara träningar, rulla eller är nöjd
    :return: beroende på vad som väljas så skickas ett svar via return som behandlas av dicerolls
    """
    print("Vill du:")
    print("1: Spara tärningar?\n2: Rulla om alla tärningar?\n3: Nöjd med kasten")
    while True:
        try:
            val = int(input())
            if val == 1:
                return "spara"
            if val == 2:
                break
            if val == 3:
                return "stopp"
            else:
                print("Svaren är endast 1,2 eller 3")
        except ValueError:
            print("Måste svara 1,2 eller 3 med siffror och inget annat...")

def add_points(player, arguments):
    """
    Skapar en lista för att kunna med en for loop dela upp argumenten ifrån funktionen add_points_where
    som skickas som en lista. När alla argument är klara så används indexen ifrån denna lista för att använda
    rätt argument på rätt ställe.

    Först är det en if sats som kollar om typen finns i övre eller undre, finns det redan d.v.s att man redan sparat
    poäng för t.ex Ettor i övre, kommer funktionen retunera ett falskt värde.
    Om däremot inget är lagrat så lagras nu poängen in för vad på rätt ställe och säger sedan till att spelareX
    har fått Xpoäng för X.

    list[0] = vart, d.v.s övre/undre
    list[1] = vad, d.v.s ettor,tvåor,triss etc
    list[2] = poäng

    Lade till lite if satser för att kolla om värdet är 0poäng och varna om så är fallet, man får då ett val
    om att ta 0 poäng eller välja om

    :param player: Här matas in vilken nuvarande spelare är så att poängen hamnar hos rätt person
    :param arguments: Här kommer en lista med argument som har retunerats ifrån funktionen add_points_where
    som förklarar vart, vad och antal poäng
    :return: Beroende på om det redan finns poäng där man vill ha poängen får vi tillbaka ett sant eller falskt värde
    som vi sedan kan använda i en while loop
    """
    kontroll = True
    list = []
    for argument in arguments:
        list.append(argument)
    grund = yatzy_data[player]["Poäng"][list[0]]
    if list[2] == 0:
        while kontroll:
            sure = input("\nDetta kommer ge " + str(list[2]) + "poäng för " + str(list[1]) + " är du säker på att du vill fortsätta? (ja/nej) ")
            if sure.upper() == "JA":
                kontroll = False
            elif sure.upper() == "NEJ":
                return False
    if grund.get(list[1]) is None:
        grund[list[1]] = list[2]
        print(yatzy_data[player]["Namn"] + " fick " + str(list[2]) + "poäng för " + str(list[1]))
        return True
    else:
        return False



def add_points_where():
    """
    Har en dictionary med nesta dictionaries som har en lista i sig med kommandona som körs beroende på vad man väljer.
    Key är nummer som motsvarar vad man vill lagra sina kast som, värdet på dessa är en dictionary som har key vilket
    säger i text vad som skall lagras. Varje värde för denna key är en lista som säger om det är övre eller undre som skall
    lagras, vad som skall lagras och värdet.

    Valde en lista som value där då jag kan ta och hämta hela denna listan ifrån dictionaryt och sedan köra in hela
    den i return, och kan således ta emot hela listan in i funktionen för att lägga till poängen där jag behöver
    all denna information.
    :return: retunerar listan som finns i dictionaryn
    """
    placering = {
        1: {"Ettor": ["Övre", "Ettor", singeltal(1)]},
        2: {"Tvåor": ["Övre", "Tvåor", singeltal(2)]},
        3: {"Treor": ["Övre", "Treor", singeltal(3)]},
        4: {"Fyror": ["Övre", "Fyror", singeltal(4)]},
        5: {"Femmor": ["Övre", "Femmor", singeltal(5)]},
        6: {"Sexor": ["Övre", "Sexor", singeltal(6)]},
        7: {"Ettpar": ["Undre", "Ettpar", pairs(1)]},
        8: {"Tvåpar": ["Undre", "Tvåpar", pairs(2)]},
        9: {"Triss": ["Undre", "Triss", repeated(3) * 3]},
        10: {"Frytal": ["Undre", "Fyrtal", repeated(4) * 4]},
        11: {"Lilla stegen": ["Undre", "Lilla stegen", 15 if tuple(sorted(dices)) == (1, 2, 3, 4, 5) else 0]},
        12: {"Stora stegen": ["Undre", "Stora stegen", 20 if tuple(sorted(dices)) == (2, 3, 4, 5, 6) else 0]},
        13: {"Kåk": ["Undre", "Kåk", fullhouse()]},
        14: {"Yatzy": ["Undre", "Yatzy", 50 if len(set(dices)) == 1 else 0]},
        15: {"Chance": ["Undre", "Chance", sum(dices)]},
    }
    """
    Här hämtar jag ut nummer (key) och värde ( value ) ifrån placerings dictionaryn genom .items()
    Då jag tagit ut varje del kan jag i denna for loopen skriva ut vilket nummer, d.v.s key för varje rad
    och samtidigt ta värdet ifrån samma rad.
    Här är det dock så att värdet är ju en ny dictinary, så för att bara få ut första delen d.v.s keyn
    så använder jag mig av .keys() på värdet för att således bara hämta ut keyn d.v.s texten.
    ex:
    Skriv 1 för Ettor - 1 är ju key i första och värdet är ju en dict med "Ettor": [lista med skit]
    så genom att ta och använda mig av .keys så tar ju bara key ifrån dict 2 d.v.s "Ettor" i detta fallet.
    """
    for nummer, värde in placering.items():
        print("Skriv " + str(nummer) + " för " + str(*värde.keys()))
    while True:
        try:
            val = int(input("Nummer: "))
            if val not in range(1,16):
                print("Måste vara med nummer mellan 1 till 15")
            else:
                break
        except ValueError:
            print("Måste ange siffor mellan 1 till 15")
    return placering.get(val).values()


def calculate_part(part):
    """
    Tar emot om det är övre eller undre dictionaryn som skall räknas ihop, sedan med for loopen
    så loppas hela övre eller undra igenom och genom att ta typ, poäng så skiljer jag av i for loopen
    mellan key : value och i detta fallet tar jag bara värdet för varje key och lägger ihop

    :param part: tar emot om det är övre eller undre delen som skall räknas ut i yatzy delen
    :return: räknar ihop summan av övre eller undre beroende på vad som matas in i funktionen
    """
    tot = 0
    for typ, poäng in part.items():
        tot += poäng
    return tot

def calculate_tot():
    """
    Funktion för att med en for loop bläddra igenom deltagarna i deltagar listan och räkna ihop övre och undra poängen
    för varje deltagare, spara dessa i en lista och sedan kolla av om övre poängen är över 63 eller ej.

    :return: inget att retunera
    """
    for player in deltagare:
        """
        Lite variabler för att korta ner koden senare, kanske blir svårare att läsa genom att variabler med variabler
        i sig skapar nya variabler. Men detta är för att koden skall bli kortare när själva frågan efter speciella
        listor i dictonaryn skall bli kortare och enklare att se.
        """
        grund = yatzy_data[player]["Poäng"]
        total = grund["Total"]
        övre = grund["Övre"]
        undre = grund["Undre"]
        namn = yatzy_data[player].get("Namn")
        """
        skickar in övre eller undre dictionaryn i calc part funktionen för att få en summa som sedan lagras
        i en lista i dictionaryn, detta då jag bara behöver ett nummer lagrat och då jag manuellt sätter vart
        summan skall ligga behöver jag bara veta att index 0 är övre, index 1 är undre och index 2 är bonus
        """
        total[0] = (calculate_part(övre))
        total[1] = (calculate_part(undre))
        """
        Kollar ifall index 0 vilket är den övre delen 1-6 är över 63poäng, är det så kommer man få en bonus
        på 50 poäng som lagras på index 2
        """
        if total[0] >= 63:
            total[2] = 50
            print("Grattis " + namn + ", du fick en bonus på 50poäng för att ha nått över 63poäng på övre delen!")
        print(namn + " fick totalt " + str(sum(total)) + " poäng.")
        """
        gjorde om resultatet till en lista för att lagra först poäng och sedan namn
        detta gör att jag enklare kan använda sorted med reverse=True för att sortera
        efter poängen och sedan skriva ut
        """
        yatzy_data["Slutresultat"].append((sum(total), namn))


def startmeny():
    """
    Startmeny för spelet vilket välkommnar och sedan frågar efter antal spelare.
    Skapar sedan varje spelare och lagrar dess namn i yatzy_data dictionaryn samt dictionarys för poängen etc.
    Detta görs med en for loop med en range som tar in svaret för antalspelare samt lägger in p1, p2 osv i listan
    Deltagare som återanvänds vid tillfällen senare.

    Efter användaren är skapad så läggs namnet till i välkomst text för att hälsa alla deltagarna välkommna.
    Sist så sätts info om vem som är spelare_nu, denna är till för att hålla koll på vem som kastar tärningarna.

    :return: ingen return
    """
    print("Välkommen till Yatzy!")
    print("Hur många spelare önskas?\n1?\n2?\n3?\n4?")
    while True:
        try:
            antalspelare=int(input())
            if antalspelare >= 0 and antalspelare <= 4:
                break
            else:
                print("Måste vara 1 eller fler spelare och inte fler än 4st, ange antalet spelare igen: ")
        except ValueError:
            print("Det var inte en siffra som angavs, ange en siffra mellan 1-4 för antalet deltagare.")

    welcome = "Nu kör vi!"
    for nr in range(1, antalspelare + 1 ):
        namn = input("Namn på spelare nr: " + str(nr) + " ")
        player = "p" + str(nr) # skapar en variabel player av p + nummer ifrån loopen
        deltagare.append(player) ## lägger till varje spelar i en lista för att kunna hoppa mellan dem
        ## lägger till spelare som p1, p2 osv och skapar 1 dict i dem för namn samt poängen som har egen dict i value
        yatzy_data[player] = {"Namn": namn,
                              "Poäng": {
                                  "Övre": {},
                                  "Undre": {},
                                  "Total": [0, 0, 0],
                              }
                            }
        # ett välkomst meddelande som byggs upp och printas
        welcome += "\nSpelare " + str(nr) + ": " + namn
    print(welcome)



def spelet():
    """
    Funktion sköter hela spelet.
    Börjar med att köra startmeny funktion för att bestämma hur många spelare och sätta upp datan för alla spelare.
    Sedan stätts antalet rundor vilket kommer vara 15 då det är 15st poänggivande saker i yatzy att göra.
    En while loop håller koll på detta och varje gång loopen körs så räknar variablen tot_rounds upp.

    Innanför denna while loopen finns en for loop som loopar igenom alla deltagare i deltagare listan och hämtar
    namnet på denna deltagare för att sedan köra vidare till dicerolls funktionen som tar hand om varje deltagares
    kast för den omgången.

    När vederbörnade deltagare är klar med sina kast så skapas en while loop som kollar med en if sats att funktionen
    add_points retunerar True, som vi gick igenom i den funktionen så retuneras True endast om deltagaren inte har poäng
    satta där deltagaren vill sätta poängen.
    Retunerar add_points False så kickar except in och säger att poäng finns redan och add_points funktionen körs igen.

    Till add_points funktionen skickas player med vilket säger till funktionen vilken spelare som spelare just nu som
    hämtades ifrån deltagare listan.
    Sedan skickas det in en lista in i add_points efter player argumentet, denna listan är vad som retuneras av
    add_points_where funktionen som förklaras ovan, * framför betyder att listan som kommer ut skall packas ut.
    Om inte detta göras så kommer det med lite information om dictionaryn etc vilket vi inte vill ha med och
    add_points_where funktionen förstår inte riktigt vad den den skall göra.

    När poängen är inlagda så tackas nuvarande spelare fär dess tur och säger till att det är dags för nästa spelare och
    loopen startar om igen.


    När while loopen är slut så skrivs det ut att spelet är slut och att resultaten skall räknas ihop.
    Nu körs funktionen calculate_tot som räknar ut poängen för varje deltagare och sparar dessa, vilket beskrivs ovan.
    När allt är ihop räknat för varje deltagare så hämtas denna lista och sorteras med sorted() funktionen efter vem som
    har högst poängn och detta genom att ta en reverse=True för att få det i rätt ordning d.v.s högst till lägst.

    För att skriva ut vem som vann spelet och vart de andra deltagarna kom så används här en for loop som använder sig
    av en range genom att räkna antalet deltagare i deltagarlistan med len(deltagare).
    Detta körs för att säkerhetställa att t.ex inte deltagare 3 och 4 skall skrivas ut och ge fel om dessa inte var med
    i denna omgången av spelet.
    Innanför denna for loopen ligger if statement med elif som kommer om deltagare på index 0, 1 ,2 eller 3 finns med i
    resultat listan, och skriver då ut namn och poäng på denna person och vilken placering vederbörande hade


    :return: inget att retunera
    """
    startmeny()
    tot_rounds = 0
    while tot_rounds < 15: #skall vara 15 om annat står här är det fel och för testsyfte
        tot_rounds += 1
        for player in deltagare:
            namn = yatzy_data[player].get("Namn")
            input("Tryck enter för att att påbörja omgången")
            print("\n" + namn + " kastar\n")
            dicerolls()
            while True:
                try:
                    if add_points(player, *add_points_where()):
                        break
                    else:
                        print("Välj annan post, antigen ångrade du dig eller så fanns det redan poäng där")
                except:
                    print("Fel val, gör om")
            print("Tack " + namn + ", dags för nästa spelare\n")
    print("Då var spelet slut, resultaten räknas ut och presenteras:\n")
    calculate_tot()
    resultat = sorted(yatzy_data["Slutresultat"], reverse=True)
    for index in range(len(deltagare)):
        if index == 0:
            print("Grattis " + resultat[index][1] + ", du vann med " + str(resultat[index][0]) + "poäng")
        elif index == 1:
            print("Bra kämpat " + resultat[index][1] + " du kom dessvärre 2a med " + str(resultat[index][0]) + "poäng")
        elif index == 2:
            print("Bra kämpat " + resultat[index][1] + " du kom dessvärre 3a med " + str(resultat[index][0]) + "poäng")
        elif index == 3:
            print("Bra kämpat " + resultat[index][1] + " du kom dessvärre 4a med " + str(resultat[index][0]) + "poäng")
        else:
            print("Något gick åt helvete minst sagt, detta skall inte kunna synas ;D")
            exit(2)


if __name__ == "__main__":
    spelet()
    exit(0)