from csinsc import *

box = {
    "top_left": "┌",
    "top_right": "┐",
    "bot_left": "└",
    "bot_right": "┘",
    "bot": "─",
    "top": "─",
    "left": "│",
    "right": "│",
}

vertical_mode = True
max_box_height = 1
max_box_width = 2
keypress = None
label .here  # fmt: skip
clear()
print(
    "Keep pressing [ENTER] to grow vertically! Or [Space + Enter] to switch direction of growth"
)
if keypress in [" "]:
    vertical_mode = not vertical_mode

if vertical_mode:
    max_box_height += 1
if not vertical_mode:
    max_box_width += 1

goto .print_top_border_START  # fmt: skip
label .print_top_border_END  # fmt: skip

box_height = 1
label .side_borders_loop  # fmt: skip
if box_height < max_box_height:
    goto .print_side_borders_START  # fmt: skip
    label .print_side_borders_END  # fmt: skip
    box_height += 1
    goto .side_borders_loop  # fmt: skip

goto .print_bot_border_START  # fmt: skip
label .print_bot_border_END  # fmt: skip
keypress = input("↓↓↓" if vertical_mode else "→→→")
goto .here  # fmt: skip


"""Functions"""


label .print_top_border_START  # fmt: skip
top_border = box["top_left"]
for i in range(max_box_width):
    top_border += box["top"]
top_border += box["top_right"]
print(top_border)
goto .print_top_border_END  # fmt: skip

label .print_bot_border_START  # fmt: skip
bot_border = box["bot_left"]
for i in range(max_box_width):
    bot_border += box["bot"]
bot_border += box["bot_right"]
print(bot_border)
goto .print_bot_border_END  # fmt: skip

label .print_side_borders_START  # fmt: skip
side_borders = box["left"]
for i in range(max_box_width):
    side_borders += " "
side_borders += box["right"]
print(side_borders)
goto .print_side_borders_END  # fmt: skip
