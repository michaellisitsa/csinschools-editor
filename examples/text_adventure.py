from csinsc import *
from time import sleep

print(
    "You are on a pirate ship led by Pirate Red hat\n\
Standing on the deck, you hear a loud noise from the wheelhouse"
)
label .deck  # fmt: skip
print(
    "[W] Go to wheelhouse\n\
[C] Go to crew quarters."
)
deck_choice = input("> ")
if deck_choice == "W" or deck_choice == "w" or deck_choice == "Go to wheelhouse":
    goto .wheelhouse_corridor  # fmt: skip
elif deck_choice == "C" or deck_choice == "c" or deck_choice == "Go to crew quarters":
    goto .crew_quarters  # fmt: skip
else:
    print("Invalid Option: " + deck_choice)
    goto .deck  # fmt: skip

label .wheelhouse_corridor  # fmt: skip
print(
    "\nWalking up to the door of the wheelhouse, you notice there is no light coming from under the door.\n\
There is a torch in the crow's nest on top of the ship mast. Do you get it?\n\
[Y] Yes\n\
[N] No"
)
corridor_choice = input("> ")
if corridor_choice == "Y" or corridor_choice == "y" or corridor_choice == "Yes":
    goto .wheelhouse  # fmt: skip
elif corridor_choice == "N" or corridor_choice == "n" or corridor_choice == "No":
    goto .crows_nest  # fmt: skip
else:
    print("Invalid Option: " + corridor_choice)
    goto .wheelhouse_corridor  # fmt: skip

label .crew_quarters  # fmt: skip
print("Your fellow crewmates accuse you of cowardice and walk you back on deck.")
goto .deck  # fmt: skip

label .wheelhouse  # fmt: skip
print("wheelhouse Not Implemented.")
goto .game_over  # fmt: skip

label .crows_nest  # fmt: skip
print("crows_nest Not Implemented.")
goto .game_over  # fmt: skip

label .game_over  # fmt: skip
