import random


# 1. Wie man diese Pokerkarten modellieren koennte: (recherchierte Idee)
# Jede Karte ist eine Nummer und diese werden nach Farben und dann 
#   dementsprechend nach Zahlen sortiert

# die Farben koennte man nach num // 13 sortieren, da man dann weiss,
#   ob die Karte zb 5 // 13 = 0 - Heart, 15// 13 = 1 - Diamonds, ... rein passt

# das Symbol dann mittels num % 13, da der Rest dann ausgibt, welches Symbol es ist
#   zb. 20 % 13 = 7   --  7. Stelle ist die 9



# gleicher Anfangsaufbau wie bei Lotto
def pull_cards(amount):
    stack = list(range(0, 52))
    picked = []

    for i in range(amount):
        pos = random.randint(0, len(stack) - 1)
        card = stack.pop[pos]
        picked.append(card)

    return picked



# Anfangsgeruest von karten
def card_name():
    colors = ["hearts", "diamonds", "spades", "clubs"]
    symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10","jack", "queen", "king", "ace"]
    



# Kombinationen: Royal Flush, Straight Flush, quads, full house
#       flush, straight, three of a kind, two pairs, pair, high card

# Methoden fuer die Kombinationen
def highCard():
    pass

def pair():
    pass

def twoPair():
    pass

def threeOfAKind():
    pass

def straight():
    pass

def flush():
    pass

def fullHouse():
    pass

def quads():
    pass

def straightFlush():
    pass

def royalFlush():
    pass


# welche Kombination zutrifft
def findCombination():
    if royalFlush():
        return "royalFlush"
    elif straightFlush():
        return "straightFlush"
    elif quads():
        return "quads"
    elif fullHouse():
        return "fullHouse"
    elif flush():
        return "flush"
    elif straight():
        return "straight"
    elif threeOfAKind():
        return "threeOfAKind"
    elif twoPair():
        return "twoPair"
    elif pair():
        return "pair"
    else:
        return "highCard"



# Prozentuellen Anteil
def percent():
    # percent = count / games * 100
    pass
