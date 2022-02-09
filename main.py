import random

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

    # main loop boolean variable
    looping = True

    # randomizer variables
    weapon1 = None
    weapon2 = None
    character = None
    map = None

    # iterator for each squad member
    i = 0

    print("Welcome to the Apex Legends Randomizer!\n")

    while(looping):
        # ask for user input
        # check if map has already been input, otherwise skip
        if map == None:
            # try statement for handling non-number answers
            try:
                # accepts floats (larger pool of correct answers), converts to ints for looping later on
                squad = int(float(input("How many in your squad? ")))
            except:
                print("Incorrect input, please try again.")
                continue
        
        # check for incorrect float inputs
        if squad > 3.0:
            print("Number over squad limit, assuming 3 players.")
            squad = 3
        elif squad < 1.0:
            print("Number under squad limit, assuming 1 player.")
            squad = 1

        # checked differently than the squad number because no translation (str->int) is necessary
        map = input("Which Map? KC, WE, O, or SP? ")

        # determine landing zone - more calculations, but clearer code
        KC_location = locations_KC[random.randint(0, len(locations_KC) - 1)]
        WE_location = locations_WE[random.randint(0, len(locations_WE) - 1)]
        O_location = locations_O[random.randint(0, len(locations_O) - 1)]
        SP_location = locations_SP[random.randint(0, len(locations_SP) - 1)]

        if map == "KC":
            print("\nKC: " + KC_location + "\n")
        elif map == "WE":
            print("\nWE: " + WE_location + "\n")
        elif map == "O":
            print("\nO: " + O_location + "\n")
        elif map == "SP":
            print("\nSP: " + SP_location + "\n")
        else:
            print("Incorrect input. Please try again.")
            continue

        # loop thrice for each squad member
        for i in range(squad):
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
        return

if __name__ == "__main__":
    main()