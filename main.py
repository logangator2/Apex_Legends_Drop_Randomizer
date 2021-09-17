import random

def main():

    # weapon, character, locations list DB
    weapons = ["Flatline", "G7", "Hemlok", "R-301", "Havoc", "Prowler",
        "R-99", "Volt", "Devotion", "L-Star", "Longbow",
        "Peacekeeper", "Sentinel", "Charge Rifle", "EVA-8", "Mastiff",
        "Mozambique", "RE-45", "P2020", "Wingman", "30-30", "Boeck","Rampage", "Grenades"]
    characters = ["Bangalore", "Bloodhound", "Caustic", "Crypto", "Fuse",
        "Gibraltar", "Horizon", "Lifeline", "Loba", "Mirage", "Octane", "Pathfinder",
        "Rampart", "Revenant", "Wattson", "Wraith", "Valkyrie", "Seer"]
    locations_KC = ["Crash Site", "Artillery", "Spotted Lake", "Broken Relay", "Containment",
        "The Rig", "The Pit", "Capacitor", "Runoff", "Bunker", "Labs", "The Cage", "Airbase", 
        "Hydro Dam", "Gauntlet", "Salvage", "Market", "Repulsor", "Mirage Voyage", "Swamps",
        "Water Treatment"]
    locations_WE = ["Trials", "Skyhook", "Survey Camp", "Climatizer", "Countdown", "Epicenter", 
        "Overlook", "Lava Fissure", "Landslide", "Fragment West", "Fragment East", 
        "Staging", "Harvester", "Geyser", "Thermal Station", "Lava Siphon", 
        "Tree", "Launch Site", "Dome", "Lava City", "Big Maude"]
    locations_O = ["Docks", "Carrier", "Fight Night", "Oasis", "Estates", "Elysium", "Hydroponics"
    , "Bonsai Plaza", "Icarus", "Solar Array", "Orbital Cannon", "Grow Towers", "Gardens",
    "Rift", "Power Grid", "Turbine", "Energy Depot", "Hammond Labs"]

    # set variables ahead of time (optimization)
    weapon1 = None
    weapon2 = None
    character = None

    i = 0

    # loop thrice for each squad member
    for i in range(3):
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

    # determine landing zone
    KC_location = locations_KC[random.randint(0, len(locations_KC) - 1)]
    WE_location = locations_WE[random.randint(0, len(locations_WE) - 1)]
    O_location = locations_O[random.randint(0, len(locations_O) - 1)]

    # print landing zone
    print("\nKC: " + KC_location + "\n")
    print("\nWE: " + WE_location + "\n")
    print("\nO: " + O_location + "\n")
    return

if __name__ == "__main__":
    main()