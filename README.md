This is a collection of different rcon scripts

# Scripts

## tournament.py

Script that allows some commands used during tournaments. All commands must
start with `!` (e.g. `!pause`).
- Allow to use `pause`, `unpause`, `restartround`, `restartmap`
- Add 2 custom commands: `help` and `map`.
    - `help` displays the available commands
    - `map` is used to change map (e.g. `!map throne`). Possible values are:
        - arena
        - city
        - desert
        - desertcity
        - factory
        - fields
        - fields_two
        - lake
        - mines
        - railroad
        - rooftops
        - sewers
        - snow
        - throne
        - tutorial
        - warehouse
        - water

## scavenger.py

Script to start the scavenger gamemode.

If Player A kills Player B, he automatically "steals" Player B loadout.
