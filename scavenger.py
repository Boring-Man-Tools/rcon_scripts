from bmio.rcon_model import (RconEvent, RconRequest, Command, player_death,
                             player_spawn)

from bmio import Bmio

app = Bmio(password='admin')

loadouts = {}
names = {}

# A player spawns.
@app.handler(RconEvent.player_spawn)
def player_spawn(data):
    # save loadout of player and their name
    player = data.PlayerID
    names[player] = data.Name
    loadouts[player] = {
            "primary": data.Weap1,
            "secondary": data.Weap2,
            "grenade": data.Equip,
            "dualwield": data.OffWeap
    }

# A player dies, give the killer the loadout of the killed.
@app.handler(RconEvent.player_death)
def give_weapon(data):
    dead = data.VictimID
    killer = data.KillerID

    if killer not in names or dead not in loadouts:
        print(f'Missing {killer} name or missing {dead} loadout')
        return

    loadout = loadouts[dead]

    app.send_command(Command.forceweap, names[killer], loadout["primary"].value,
                     loadout["secondary"].value, loadout["grenade"].value,
                     loadout["dualwield"].value)


app.run()
