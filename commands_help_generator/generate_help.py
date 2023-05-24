from bmio.rcon_model import (RconEvent, Command, command_entered)
from bmio import Bmio
import asyncio

app = Bmio(password='admin')

descriptions = []

def get_commands():
    '''
    Get the list of commands from the file

    Return a list of tuples:
    first element is the command itself
    second element is the command with all args
    '''
    _commands = []
    with open('commands_help_generator/commands.txt', 'r') as f:
        for line in f:
            clean_line = line.rstrip('\n')
            cmd_only = clean_line.split()[0]
            _commands.append((cmd_only, clean_line))
    return _commands

@app.handler(RconEvent.command_entered)
def description_command(command: command_entered):
    if command.ReturnText:
        # check that command was "help"
        print(command.ReturnText)

def send_command(cmd):
    app.send_command(Command.help, f'{cmd}')
    print(f'{cmd}')


async def help_commands():
    commands = get_commands()
    for command, _ in commands:
        send_command(command)
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(loop.create_task(help_commands()))


app.run()
