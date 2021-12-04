# SET Card Game Solver

This Python project was made to find all possible sets given an arbitrary (81 or less) amount of SET cards.

#

## What classifies as a 'set' in SET?

### Cards in the game SET have 4 characteristics:

(_Italic values represent the possible characteristic values in my program._)

- Color
  - _blue, yellow, green_
- Symbol
  - _A, S, H_
- Shading (of the symbols)
  - _lowercase, uppercase, symbol-case (_@, $, #_)_
- Number (of symbols)
  - _number of times the symbol on a card appears_
    \
    &nbsp;

### Finding a valid set:

3 cards for a set if and only if for each of the 4 characteristics, **the cards either share the same value or all have different values**.
\
\
Example Set & Explanation:

blue @@@, yellow @@, green @

- Color: all **different** colors (blue, yellow, green)
- Symbol: all **same** symbols (A)
- Shading: all **same** shading (symbol case)
- Number: all **different** number of symbols (3, 2, 1)

#

## How to Run

Open a new bash terminal in the script directory, and run any standard input from a test file using the syntax below:

    cat 15_cards.txt | python.exe set_game.py

New/custom card inputs can be ran as well, provided the formatting from the 2 examples is followed.

#
