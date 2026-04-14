from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import prompt
from rich.table import Table
from rich.console import Console
import os

console = Console()
bindings = KeyBindings()

@bindings.add("up")
def _(event):
    event.app.exit(result='up')
@bindings.add("down")
def _(event):
    event.app.exit(result='down')
@bindings.add("enter")
def _(event):
    event.app.exit(result='enter')

ROWS = [
    ["Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690"],
    ["May 25, 2018", "Solo: A Star Wars Story", "$393,151,347"],
    ["Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889"],
    ["Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889"]
]
idx = 0 
while True:        
    table = Table(title="Star Wars Movies", show_lines=True)

    table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Box Office", justify="right", style="green")
    
    for index, r in enumerate(ROWS):
        if index == idx:
            """ Define style here """
            STYLE = "bold on #0f172a"
            row = r
        else:
            STYLE = ''
        table.add_row(*(r), style=STYLE)

    console.print(table)            
    
    option = prompt(key_bindings=bindings)
    if option == 'up': 
        if idx > 0:
            idx -= 1
        else:
            idx = 0
    elif option == 'down': 
        if idx < len(ROWS) -1:
            idx += 1
        else:
            idx = len(ROWS) - 1 
    elif option == 'enter': 
        console.print(f"You chose {row}")
        break
    os.system('clear') if os.name != 'nt' else os.system('cls')