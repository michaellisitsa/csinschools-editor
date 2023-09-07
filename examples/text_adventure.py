from csinsc import *
from time import sleep

print(
    "You are on a pirate ship led by Pirate Red hat\n\
Standing on the deck, you hear a loud noise from the wheelhouse\n"
)
label .ship_deck  # fmt: skip
print(
    "[W] Go to wheelhouse\n\
[C] Go to crew quarters."
)
deck_choice = input("> ")
if deck_choice == "W" or deck_choice == "w" or deck_choice == "Go to wheelhouse":
    goto .wheelhouse  # fmt: skip
elif deck_choice == "C" or deck_choice == "c" or deck_choice == "Go to crew quarters":
    goto .crew_quarters  # fmt: skip
else:
    print("Invalid Option: " + deck_choice)
    goto .ship_deck  # fmt: skip

label .wheelhouse  # fmt: skip
print("Wheelhouse Not Implemented.")
goto .game_over  # fmt: skip

label .crew_quarters  # fmt: skip
print("Crew Quarters Not Implemented.")
goto .game_over  # fmt: skip

label .game_over  # fmt: skip
