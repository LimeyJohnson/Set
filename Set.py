totalNum = 7
totalColor = 56
totalShape = 448
totalFill = 3584

Numbers = ["1","2","","3"]
Colors = ["Red", "Purple", "","Green"]
Shapes = ["Diamond", "S-Shape", "","Board"]
Fills = ["Empty", "Striped", "","Full"]

NumbersDict = {"1":2**0, "2" : 2**1, "3":2**2}
ColorsDict = {"r":2**3, "p" : 2**4, "g":2**5}
ShapesDict = {"d":2**6, "s" : 2**7, "b":2**8}
FillsDict = {"e":2**9, "s" : 2**10, "f":2**11}
def IsSet(card1, card2, card3):
    cardsand = card1 & card2 & card3
    cardsor = card1 | card2 | card3
    #check number
    if (cardsand & totalNum) == (card1 & totalNum) or (cardsor & totalNum) == totalNum:
        if (cardsand & totalColor) == (card1 & totalColor) or (cardsor & totalColor) == totalColor:
            if (cardsand & totalShape) == (card1 & totalShape) or (cardsor & totalShape) == totalShape:
                if (cardsand & totalFill) == (card1 & totalFill) or (cardsor & totalFill) == totalFill:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False    

def ParseCard (input):
    card = 0
    if(len(input)<>4):
        print("parser error")
    input = input.lower()
    card += NumbersDict[input[0]]
    card += ColorsDict[input[1]]
    card += ShapesDict[input[2]]
    card += FillsDict[input[3]]
    return card
def CardString (card):
    output = ""
    numIndex = card & totalNum 
    output += Numbers[numIndex - 1] + " "
    
    colorIndex = (card & totalColor) >> 3
    output += Colors[colorIndex - 1] + " "
    
    shapeIndex = (card & totalShape) >> 6
    output += Shapes[shapeIndex - 1] + " "
    
    fillIndex = (card & totalFill) >> 9
    output += Fills[fillIndex - 1] + " "
    
    return output
def PrintCards(cards):
    output = ""
    for card in cards:
        output += "("+CardString(card)+") "
    print(output)

def HasSet(cards):
    length = len(cards)
    for card1Index in range(0,length - 2):
        for card2Index in range(card1Index+ 1, length -1):
            for card3Index in range(card2Index + 1, length):
                if(IsSet(cards[card1Index], cards[card2Index], cards[card3Index])):
                    PrintCards([cards[card1Index], cards[card2Index], cards[card3Index]])
                    
               



cards = []
cards.append(ParseCard("3rbs"))
cards.append(ParseCard("3pse"))
cards.append(ParseCard("1gds"))
cards.append(ParseCard("3pbf"))
cards.append(ParseCard("2psf"))
cards.append(ParseCard("2gbf"))
cards.append(ParseCard("2rbf"))
cards.append(ParseCard("3psf"))
cards.append(ParseCard("1gsf"))
cards.append(ParseCard("2gbs"))
cards.append(ParseCard("3gse"))
cards.append(ParseCard("1gdf"))


HasSet(cards)
print("done")
#PrintCards(cards)
#print(IsSet(card1, card2, card3))