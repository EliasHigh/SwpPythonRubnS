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
        card = stack.pop(pos)
        picked.append(card)

    return picked


# wie viele Symbole kommen genau amount mal vor
# zb amount = 2 und Ergebnis 1 -> ein Paar
def sameSymbols(cards, amount):
    counter = {}
    for symbol in range(13):
        counter[symbol] = 0

    for card in cards:
        counter[card % 13] = counter[card % 13] + 1

    result = 0
    for symbol in counter:
        if counter[symbol] == amount:
            result = result + 1
    return result


# Methoden fuer die Kombinationen
def pair(cards):
    return sameSymbols(cards, 2) == 1

def twoPair(cards):
    return sameSymbols(cards, 2) == 2

def threeOfAKind(cards):
    return sameSymbols(cards, 3) == 1

def quads(cards):
    return sameSymbols(cards, 4) == 1

def fullHouse(cards):
    return threeOfAKind(cards) and pair(cards)

def flush(cards):
    for card in cards:
        if card // 13 != cards[0] // 13:
            return False
    return True

def straight(cards):
    symbols = []
    for card in cards:
        symbols.append(card % 13)
    symbols = sorted(symbols)

    # Ass unten (A 2 3 4 5) wird hier nicht gezaehlt
    for i in range(4):
        if symbols[i] + 1 != symbols[i + 1]:
            return False
    return True


# welche Kombination zutrifft (von oben nach unten)
def findCombination(cards):
    if straight(cards) and flush(cards):
        return "straightFlush"
    elif quads(cards):
        return "quads"
    elif fullHouse(cards):
        return "fullHouse"
    elif flush(cards):
        return "flush"
    elif straight(cards):
        return "straight"
    elif threeOfAKind(cards):
        return "threeOfAKind"
    elif twoPair(cards):
        return "twoPair"
    elif pair(cards):
        return "pair"
    else:
        return "highCard"


# wie viele_ziehungen bei Lotto
def manyGames(games):
    statistic = {"straightFlush": 0, "quads": 0, "fullHouse": 0,
                 "flush": 0, "straight": 0, "threeOfAKind": 0,
                 "twoPair": 0, "pair": 0, "highCard": 0}

    for i in range(games):
        cards = pull_cards(5)
        combination = findCombination(cards)
        statistic[combination] = statistic[combination] + 1

    return statistic


# Prozentuellen Anteil
# echte Werte (Wikipedia): straightFlush 0.0015, quads 0.024,
#   fullHouse 0.14, flush 0.2, straight 0.39, threeOfAKind 2.11,
#   twoPair 4.75, pair 42.26, highCard 50.12
def percent(statistic, games):
    for combination in statistic:
        print(combination, statistic[combination] / games * 100, "%")


def main():
    games = 100000
    statistic = manyGames(games)
    print(statistic)
    percent(statistic, games)


main()
