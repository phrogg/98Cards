from random import randint
import os

decks = [0,0,100,100]
playersCards = [0,0,0,0,0,0,0,0]
cardsInGame = [0]
debug = False

def main():
    while True:
        if playersTurn():
            break
    pass

def printPlayground():
    print('Cards remaining:'+str(98-(len(cardsInGame)+len(playersCards))))
    print(decks)
    print(playersCards)

def initPlayground():
    for i in range(len(playersCards)):
        if playersCards[i] == 0:
            playersCards[i] = drawACard()

def drawACard():
    drawedCard = 0
    while drawedCard in cardsInGame:
        drawedCard = randint(1,98)

    cardsInGame.append(drawedCard)
    return drawedCard

def isCardInPlayerField(card):
    if debug:
        return True
    if int(card) in playersCards:
        return True
    return False

def deckExists(deck):
    if int(deck) not in [0,1,2,3]:
        print('Your chosen Deck is not there.')
    return False

def removeCardPlayerfield(card):
    for i in range(len(playersCards)):
        if int(card) == playersCards[i]:
            playersCards[i] = drawACard()

def card2Deck(card,deck):
    card = int(card)
    deck = int(deck)

    if deck < 2:
        if card <= decks[deck] and not card+10 == decks[deck]:
            print('The card must be higher than the decks top card, or exactly ten lower..')
            return False
        else:
            decks[deck] = card
    else:
        if card >= decks[deck] and not card-10 == decks[deck]:
            print('The card must be lower than the decks top card, or exactly ten higher.')
            return False
        else:
            decks[deck] = card
    removeCardPlayerfield(card)

def playersTurn():
    global debug
    printPlayground()
    chosenCard = input('CARD Number:')
    if " " in str(chosenCard):
        chosenCard = chosenCard.split(" ")
        chosenDeck = int(chosenCard[1])
        chosenCard = int(chosenCard[0])
    if "giveMe:" in str(chosenCard):
        chosenCard = int(str(chosenCard).replace("giveMe:",""))
        debug = True
    if isCardInPlayerField(chosenCard):
        #if chosenDeck == None: 
        chosenDeck = input('Put it on deck 0,1 2,3?:')
        if not deckExists(chosenDeck):
            return False
        card2Deck(chosenCard,chosenDeck)
    else:
        print('Your chosen Card is not in the field.')
        return False
    os.system("cls")

initPlayground()
main()