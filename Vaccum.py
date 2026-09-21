# Vacuum Cleaner Agent

def vacuum_cleaner():
    room = {
        "A": "Dirty",
        "B": "Dirty"
    }

    location = "A"

    print("Initial Room Status:", room)

    while "Dirty" in room.values():
        print("\nVacuum is at Room", location)

        if room[location] == "Dirty":
            print("Room", location, "is Dirty -> Cleaning...")
            room[location] = "Clean"
            print("Room", location, "is now Clean")

        # Move to the other room
        if location == "A":
            location = "B"
        else:
            location = "A"

    print("\nFinal Room Status:", room)
    print("All rooms are clean!")


vacuum_cleaner()