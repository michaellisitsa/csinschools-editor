# CSinSchools Editor

This repo has a semi-compatible implementation of the [csinschools.io](csinschools.io) custom Skulpt Python Editor, that runs on regular CPython.
For some version (unclear if this is the latest) of the [csinschools.io](csinschools.io) editor, see https://github.com/Nick-Lamanna907/nicksSkulptEdits
A minimal list of implementations are added so most Intro To Coding scripts will run without modification.

# How to Use:

- Create virtual environment. `python3 -m venv venv`
- Run `pip install -e .` [why?](https://stackoverflow.com/a/50194143/12462631)
- Add `from csinsc import *` to any file to have a [csinschools-ey](csinschools.io) python environment.

# Set up Formatter & VS Code

- You can install `black` via provided requirements.txt.
- If using VS Code:
  - Set your default formatter to black for this workspace.
  - Install extension [Regex Replace on Save](https://marketplace.visualstudio.com/items?itemName=CryptoCooLby.vscode-regex-replace-on-save&ssr=false#overviewto) to prevent `label .xxx` and `goto .xxx` having whitespace stripped off ` # fmt: skip`.

# ENVIRONMENT

The environment in [csinschools](csinschools.io) has a few specific differences to a standard Python environment.

# Modules

## `csinsc`

Some Skulpt Builtins are re-implemented into the `csinsc` package. This isn't consistent with [csinschools](csinschools.io), but ensures the code can be mutually run:

- `goto` added per [Kenny2github/goto](https://github.com/Kenny2github/goto) into the csinsc module. Consistent to [https://entrian.com/goto/](https://entrian.com/goto/).
  - csinsc appears to use a looser version that allows goto within loops.
  - "black-formatter" doesn't like the space between in `label .here` so an override comment is used in examples.
- `clear()` function added. CSINSC uses an implementation inside [Skulpt](https://github.com/skulpt/skulpt) builtins.

Modifications to the `csinsc` modules:

- `Colour`, `Highlight` & `Style` keywords use different ANSI colour codes see [https://xdevs.com/guide/color_serial/](https://xdevs.com/guide/color_serial/). Mac / VS code doesn't seem to support the ones built into csinsc custom Skulpt build.
