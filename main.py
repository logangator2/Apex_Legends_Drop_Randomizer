"""
Code written by Maxwell Logan
Referenced code from https://www.pythontutorial.net/tkinter/ tutorials
"""

from email import message
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# weapon, character, locations makeshift list DB
weapons = ["Flatline", "Rampage", "Hemlok", "R-301", "Havoc", "Prowler",
        "R-99", "Alternator", "Devotion", "L-Star", "Longbow",
        "Peacekeeper", "Sentinel", "Charge Rifle", "EVA-8", "C.A.R.",
        "Mozambique", "RE-45", "P2020", "Wingman", "30-30", "Boeck",
        "Grenades"]
vault_weapons = ["Kraber", "G7", "Mastiff", "Volt"]
characters = ["Bangalore", "Bloodhound", "Caustic", "Crypto", "Fuse", "Gibraltar", 
        "Horizon", "Lifeline", "Loba", "Mirage", "Octane", "Pathfinder",
        "Rampart", "Revenant", "Wattson", "Wraith", "Valkyrie", "Seer", 
        "Ash", "Mad Maggie"]
locations_KC = ["Crash Site", "Artillery", "Spotted Lake", "Broken Relay", "Containment",
        "The Rig", "The Pit", "Capacitor", "Runoff", "Bunker", "Labs",
        "The Cage", "Airbase", "Hydro Dam", "Gauntlet", "Salvage", "Market", 
        "Repulsor", "Mirage Voyage", "Swamps", "Water Treatment"]
locations_WE = ["Trials", "Skyhook", "Survey Camp", "Climatizer", "Countdown",
        "Epicenter", "Overlook", "Lava Fissure", "Landslide", "Fragment West", "Fragment East", 
        "Staging", "Harvester", "Geyser", "Thermal Station", "Lava Siphon", "Tree", 
        "Launch Site", "Dome", "Lava City", "Big Maude"]
locations_O = ["Docks", "Carrier", "Fight Night", "Oasis", "Estates",
        "Elysium", "Hydroponics", "Bonsai Plaza", "Icarus", "Solar Array", "Orbital Cannon",
        "Grow Towers", "Gardens", "Rift", "Power Grid", "Turbine", "Energy Depot", 
        "Hammond Labs", "Phase Driver", "Terminal", "Lifeline's Clinic"]
locations_SP = ["North Pad", "The Wall", "Highpoint", "Lightning Rod", "Checkpoint", 
        "Cascade Falls", "Command Center", "Thunder Watch", "Storm Center", "The Mill", "Cenote Cave", 
        "Barometer", "Antenna", "Launch Pad", "Ship Fall", "Gale Station", "Fish Farms",
        "Downed Beast"]

# root window for tkinter
root = tk.Tk()
root.title("Apex Legends Drop Randomizer")

# main program
def main():

    # grid layout for the input frame
    frame = ttk.Frame(root)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    # welcome message
    message = ttk.Label(root, 
        text="Welcome to the Unofficial Apex Legends Drop Randomizer!").grid(column=1, row=0)

    # squad selection label
    squadnum = ttk.Label(root, text="How many people in your squad?").grid(column=0, row=1)

    # squad size radio selection widget
    selected = tk.StringVar()
    r1 = ttk.Radiobutton(root, text='1', value=1, variable=selected).grid(column=0, row=2)
    r2 = ttk.Radiobutton(root, text='2', value=2, variable=selected).grid(column=0, row=3)
    r3 = ttk.Radiobutton(root, text='3', value=3, variable=selected).grid(column=0, row=4)

    # map selection label
    maps = ttk.Label(root, text="Which map are you playing on?").grid(column=2, row=1)

    # map radio selection widget
    selected2 = tk.StringVar()
    r4 = ttk.Radiobutton(root, 
        text="King's Canyon", value="King's Canyon", variable=selected2).grid(column=2, row=2)
    r5 = ttk.Radiobutton(root, 
        text="World's Edge", value="World's Edge", variable=selected2).grid(column=2, row=3)
    r6 = ttk.Radiobutton(root, 
        text='Olympus', value='Olympus', variable=selected2).grid(column=2, row=4)
    r7 = ttk.Radiobutton(root, 
        text='Storm Point', value='Storm Point', variable=selected2).grid(column=2, row=5)

    # use care package weapons checkbox
    selected3 = tk.StringVar()
    c1 = ttk.Checkbutton(root, 
        text="Include Care Package Weapons?",variable=selected3, onvalue=1, offvalue=0, 
        command=lambda: set_weapons()).grid(column=1, row=6)
    
    # randomize button
    randomizer = ttk.Button(root, 
        text="Randomize!", 
        command=lambda: randomize(int(selected.get()), selected2.get())).grid(column=1, row=7)

    # exit button
    exit = ttk.Button(text="Quit", command=root.destroy).grid(column=1, row=10)

    # final tkinter loop
    root.mainloop()
    return

def randomize(squad_size, map_name):
    """
    randomize - core function for the drop randomizer
    **args:
        squad_size - str number of teammates on user's squad, including themselves
        map_name - name of the map that the game is being played on
    """

    # randomizer variables
    weapon1 = None
    weapon2 = None
    character = None
    character_str = None
    drop_location = None
    output_str = ""

    # copy character list for fresh list every time randomization is called
    char_list = characters.copy()

    # iterator for each squad member
    i = 0

    # determine drop location for selected map
    if map_name == "King's Canyon":
        drop_location = "King's Canyon Drop Location:\n" + " " + locations_KC[random.randint(0, len(locations_KC) - 1)]
    elif map_name == "World's Edge":
        drop_location = "World's Edge Drop Location:\n" + " " + locations_WE[random.randint(0, len(locations_WE) - 1)]
    elif map_name == "Olympus":
        drop_location = "Olympus Drop Location:\n" + " " + locations_O[random.randint(0, len(locations_O) - 1)]
    elif map_name == "Storm Point":
        drop_location = "Storm Point Drop Location:\n" + " " + locations_SP[random.randint(0, len(locations_SP) - 1)]

    # add drop location to output_str
    output_str += drop_location + "\n"

    # loop thrice for each squad member
    for i in range(squad_size):
        # determine weapons
        weapon1 = weapons[random.randint(0, len(weapons) - 1)]
        weapon2 = weapons[random.randint(0, len(weapons) - 1)]
        # determine characters
        character = char_list[random.randint(0, len(char_list) - 1)]
        # formatting
        character_str = "\n" + character + " - " + weapon1 + ", " + weapon2 + "\n"
        # removes characters already picked
        char_list.remove(character)
        # add character_str to output message
        output_str += character_str

    # testing only
    # print(output_str)

    # display outbut in tkinter messagebox
    tk.messagebox.showinfo(title="Randomization", message=output_str)

    return

def set_weapons():
    global weapons
    if vault_weapons[0] not in weapons:
        weapons = weapons + vault_weapons
    else:
        for i in weapons:
            for j in vault_weapons:
                if i == j:
                    weapons.remove(i)
    return

if __name__ == "__main__":
    main()