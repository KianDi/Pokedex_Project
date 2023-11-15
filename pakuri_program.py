from pakudex import Pakudex


def display_menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")


def list_pakuri(pakudex):
    # first check size
    if pakudex.get_size() > 0:
        print("Pakuri In Pakudex:")
        # displays pakuri
        for i, species in enumerate(pakudex.get_species_array(), start=1):
            print(f"{i}. {species}")
    else:
        print("No Pakuri in Pakudex yet!")


def show_pakuri(pakudex):
    species = input("Enter the name of the species to display: ")
    stats = pakudex.get_stats(species)
    # displays the stats of pakuri
    if stats:
        print(f"Species: {species}")
        print(f"Attack: {stats[0]}")
        print(f"Defense: {stats[1]}")
        print(f"Speed: {stats[2]}")
    else:
        # if inputted pakuri does not exist in pakudex
        print("Error: No such Pakuri!")


def add_pakuri(pakudex):
    # check capacity first before prompting user to add species
    if pakudex.get_size() < pakudex.get_capacity():
        species = input("Enter the name of the species to add: ")
        if species in pakudex.get_species_array():
            # checks if pakuri is already in the pakudex
            print(f"Error: Pakudex already contains this species!")
        else:
            pakudex.add_pakuri(species)
            print(f"Pakuri species {species} successfully added!")
    else:
        print("Error: Pakudex is full!")


def evolve_pakuri(pakudex):
    species = input("Enter the name of the species to evolve: ")
    # calls the evolve_species method from Pakudex class
    if pakudex.evolve_species(species):
        print(f"{species} has evolved!")
    else:
        print("Error: No such Pakuri!")


def sort_pakuri(pakudex):
    # sorts the pakuri using the sort method
    pakudex.sort_pakuri()
    print("Pakuri have been sorted!")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity > 0:
                break
            else:
                print("Please enter a valid size.")

        # accounts for inputs such as ???
        except ValueError:
            print("Please enter a valid size.")
    pakudex = Pakudex(capacity)

    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    while True:
        display_menu()

        choice = input("What would you like to do? ")

        if choice == "1":
            list_pakuri(pakudex)
        elif choice == "2":
            show_pakuri(pakudex)
        elif choice == "3":
            add_pakuri(pakudex)
        elif choice == "4":
            evolve_pakuri(pakudex)
        elif choice == "5":
            sort_pakuri(pakudex)
        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")


if __name__ == '__main__':
    main()
