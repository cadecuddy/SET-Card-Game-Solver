import sys


class Finder:
    '''
    The Finder class is what manipulates the Cards,
    from parsing them from the system input to building
    all possible SETs of the Cards.
    '''

    # Dictonary for parsing raw card arguments
    # into easily manipulated attributes
    value_dict = {
        "blue": 0,
        "green": 1,
        "yellow": 2,
        "A": 0,
        "S": 1,
        "H": 2,
        "a": 0,
        "s": 1,
        "h": 2,
        "@": 0,
        "$": 1,
        "#": 2,
    }

    def __init__(self):
        '''
        Takes in the standard input containing the
        number of cards, as well as the cards themselves.

        It creates an array of Cards appropriately named
        "cards".
        '''
        n = int(sys.stdin.readline().rstrip())
        self.cards = [] * n
        input = sys.stdin
        for arg in input:
            card_line = arg.rstrip()
            card = self.parse_card(card_line)
            card.raw_card = card_line
            self.cards.append(card)

    def parse_card(self, raw_card):
        '''
        Assigns raw card string attribute values
        from 0-2 for each attribute (color, shading, etc)
        and constructs a Card object with the values.

        Example Card object values: (1,0,1,2)
        '''
        card_components = raw_card.split(" ")
        color = self.value_dict.get(card_components[0])
        symbol = self.value_dict.get(card_components[1][0])
        if not card_components[1][0].isalnum():
            shading = 2
        elif card_components[1][0].islower():
            shading = 0
        else:
            shading = 1
        number = len(card_components[1]) - 1

        return Card((color, symbol, shading, number))

    def find_sets(self):
        '''
        Takes O(N^2) time as opposed to the naive O(N^3)
        triple loop approach.

        Looks at 2 cards and calculates the 3rd card needed
        to complete the SET, if that card exists in the 'seen'
        dictionary, a SET has been found and is added to the
        'sets' class variable.

        SETs are represented as a tuple of Card objects.
        Card objects can be directly compared to each other
        as I've implemented hash and eq behaviors.
        '''
        seen = {}
        self.sets = []

        for idx, card in enumerate(self.cards):
            # Set the card as the key to
            # the card's index
            seen[card] = idx

        # Have index and first card for every potential set
        for i, card1 in enumerate(self.cards):
            # Have index + 1 and second card for every potential set
            for j, card2 in enumerate(self.cards[i + 1:], i + 1):
                # Find the 3rd matching card in a set of card1 and card2.
                # If the 'seen' dict has a matching Card key for the calculated 3rd card value,
                # the index value of the matching 3rd Card in the "cards" array will be set as card3.
                card3 = seen.get(card1.find_completing_card(card2))
                # Ensure card3's index is not one we have already visited, or
                # doesn't exist
                if card3 is not None and card3 > j:
                    self.sets.append((card1, card2, self.cards[card3]))

        return len(self.sets)


class Card:

    # Holds the card's intial string input
    raw_card = ""

    def __init__(self, values):
        self.values = values

    def __hash__(self):
        '''
        Allows for a much faster lookup of a possible
        third card in Finder's "seen" dictionary created
        in the find_sets() method.
        '''
        return hash(self.values)

    def __eq__(self, card):
        '''
        Equality for dictionary lookup.
        '''
        return self.values == card.values

    def __str__(self):
        '''
        Print formatting
        '''
        return self.raw_card

    def find_completing_card(self, card):
        '''
        Uses the attribute values from a Card
        and the current Card and constructs a
        Card object that represents the Card
        object needed to make a SET with the 
        2 cards.
        '''
        def calc(v0, v1):
            return (-v0-v1) % 3
        card3 = (calc(self.values[0], card.values[0]),
                 calc(self.values[1], card.values[1]),
                 calc(self.values[2], card.values[2]),
                 calc(self.values[3], card.values[3]))
        return Card(card3)


set_finder = Finder()
print(f"\n{set_finder.find_sets()} possible SETs are possible.\n")
for set in set_finder.sets:
    for card in set:
        print(card)
    print()
