"""
Code written by Maxwell Logan
Referenced code from https://www.pythontutorial.net/tkinter/ tutorials
"""

import random
import tkinter as tk

# weapon, character, locations makeshift list DB
weapons = ["Flatline", "G7", "Hemlok", "R-301", "Havoc", "Prowler",
        "R-99", "Alternator", "Devotion", "L-Star", "Longbow",
        "Peacekeeper", "Sentinel", "Charge Rifle", "EVA-8", "Mastiff",
        "Mozambique", "RE-45", "P2020", "Wingman", "30-30", "Boeck",
        "C.A.R. SMG", "Rampage", "Grenades"]
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
        "Hammond Labs", "Phase Driver", "Terminal"]
locations_SP = ["North Pad", "The Wall", "Highpoint", "Lightning Rod", "Checkpoint", 
        "Cascade Falls", "Command Center", "Thunder Watch", "Storm Center", "The Mill", "Cenote Cave", 
        "Barometer", "Antenna", "Launch Pad", "Ship Fall", "Gale Station", "Fish Farms"]

# main program
def main():

    # root window for tkinter
    root = tk.Tk()
    root.title("Apex Legends Drop Randomizer")

    # # grid layout for the input frame
    # frame = tk.Frame(root)
    # frame.columnconfigure(0, weight=1)
    # frame.columnconfigure(0, weight=3)

    # welcome message
    message = tk.Label(root, text="Welcome to the Unofficial Apex Legends Drop Randomizer!")
    message.pack()

    # squad size radio selection widget
    selected = tk.StringVar()
    r1 = tk.Radiobutton(root, text='1', value='Value 1', variable=selected)
    r2 = tk.Radiobutton(root, text='2', value='Value 2', variable=selected)
    r3 = tk.Radiobutton(root, text='3', value='value 3', variable=selected)
    r1.pack()
    r2.pack()
    r3.pack()

    # map radio selection widget
    selected2 = tk.StringVar()
    r4 = tk.Radiobutton(root, text="King's Canyon", value='Value 1', variable=selected2)
    r5 = tk.Radiobutton(root, text="World's Edge", value='Value 2', variable=selected2)
    r6 = tk.Radiobutton(root, text='Olympus', value='value 3', variable=selected2)
    r7 = tk.Radiobutton(root, text='Storm Point', value='value 3', variable=selected2)
    r4.pack()
    r5.pack()
    r6.pack()
    r7.pack()

    # randomize button
    randomize = tk.Button(root, text="Randomize!", command=lambda: randomize(selected, selected2))
    randomize.pack()

    # exit button
    exit = tk.Button(text="Quit", command=root.destroy)
    exit.pack()

    # final tkinter loop
    root.mainloop()
    return

def randomize(squad_size, map_name):
    """
    randomize - core function for the drop randomizer
    **args:
        squad_size - number of teammates on user's squad, including themselves
        map_name - name of the map that the game is being played on
    """

    # randomizer variables
    weapon1 = None
    weapon2 = None
    character = None
    map = None

    # iterator for each squad member
    i = 0

    if map_name == "KC":
        KC_location = locations_KC[random.randint(0, len(locations_KC) - 1)]
        # FIXME: Need to add the location to the output
    elif map_name == "WE":
        WE_location = locations_WE[random.randint(0, len(locations_WE) - 1)]
    elif map_name == "O":
        O_location = locations_O[random.randint(0, len(locations_O) - 1)]
    elif map_name == "SP":
        SP_location = locations_SP[random.randint(0, len(locations_SP) - 1)]

    # loop thrice for each squad member
    for i in range(squad_size):
        # determine weapons
        weapon1 = weapons[random.randint(0, len(weapons) - 1)]
        weapon2 = weapons[random.randint(0, len(weapons) - 1)]
        # determine characters
        character = characters[random.randint(0, len(characters) - 1)]
        # print formatting
        print()
        print(character, " - ", weapon1, ",", weapon2)
        print()
        # removes characters already picked
        characters.remove(character)

        # FIXME: Need to do some formatting here, add to output

    return

if __name__ == "__main__":
    main()