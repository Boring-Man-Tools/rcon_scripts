import random

from time import sleep
from bmio.rcon_model import (RconEvent,
    RconRequest,
    Command,
    command_entered,
    log_message,
    player_death,
    chat_message
)
from bmio import Bmio

# Create a Bmio
app = Bmio(password='baguette_admin')


maps = [
    'maps\\stock\\arctic',
    'maps\\stock\\arena',
    'maps\\stock\\city',
    'maps\\stock\\desert',
    'maps\\stock\\factory',
    'maps\\stock\\desertcity',
    'maps\\stock\\fields',
    'maps\\stock\\fields_two',
    'maps\\stock\\lake',
    'maps\\stock\\mines',
    'maps\\stock\\railroad',
    'maps\\stock\\rooftops',
    'maps\\stock\\sewers',
    'maps\\stock\\snow',
    'maps\\stock\\tutorial',
    'maps\\stock\\throne',
    'maps\\stock\\warehouse',
    'maps\\stock\\water',
]

commands_allowed = [
        'pause',
        'unpause',
        'restartmap',
        'restartround',
]

# Register a handler
@app.handler(RconEvent.log_message)
def do_something(some_data: log_message):
    '''Print into the console whenever something is written to the logs'''
    print(some_data.Message)



# Send a command: Send a message when they die.
@app.handler(RconEvent.player_death)
def player_spawn(death_info: player_death):
    '''Send a random message!'''
    app.send_command(Command.say, random.choice([
        'Try harder!',
        'You have died',
        'Be careful next time',
        'Get back up and keep trying',
        'Try again',
        'Uh Oh',
        'Whoa',
        'Wow',
        'Dont give up!',
    ]))

@app.handler(RconEvent.chat_message)
def remote_admin(chat: chat_message):
    if chat.Message.startswith('!') and not chat.Message != "!help" and not chat.Message.startswith("!map"):
        full_cmd = chat.Message[1:]
        cmd = full_cmd.split(" ")[0]
        if cmd in commands_allowed:
            app.send_request(full_cmd, RconRequest.command)
        else:
            app.send_command(Command.say, 'Not a possible command. !help')

@app.handler(RconEvent.chat_message)
def help_commands_allowed(chat: chat_message):
    if chat.Message == '!help':
        text = 'Valid commands:' + ','.join(commands_allowed)
        text += ', map'
        app.send_command(Command.say, text)

@app.handler(RconEvent.chat_message)
def change_map(chat: chat_message):
    if chat.Message == '!map':
        app.send_command(Command.say, 'Use with: arena, city, desert, factory, desertcity, fields, fields_two, lake, mines, railroad, rooftops, sewers, snow, tutorial, throne, warehouse, water')
    elif chat.Message.startswith('!map '):
        _map = chat.Message[5:]
        map_filepath = f"maps\\stock\\{_map}"
        app.send_command(Command.changemap, map_filepath)

@app.handler(RconEvent.command_entered)
def command_response(command: command_entered):
    if command.ReturnText:
        app.send_command(Command.say, f'{command.ReturnText} [{command.Command}]')
