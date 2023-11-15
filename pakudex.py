from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        # returns number of pakuri in pakudex
        return len(self.pakuri_list)

    def get_capacity(self):
        # returns capacity
        return self.capacity

    def get_species_array(self):
        # To avoid TypeError, return empty list instead of none when there are no species.
        return [pakuri.get_species() for pakuri in self.pakuri_list] if self.pakuri_list else []

    def get_stats(self, species):
        # Returns stats list for pakuri
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        # returns none if species is not in the pakudex
        return None

    def sort_pakuri(self):
        # Sorts according to name
        self.pakuri_list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        if species in self.get_species_array():
            print(f"Error: Pakudex already contains species {species}!")
            return False
        # adds species
        if len(self.pakuri_list) < self.capacity:
            new_pakuri = Pakuri(species)
            self.pakuri_list.append(new_pakuri)
            return True
        else:
            return False

    def evolve_species(self, species):
        # evolves pakuri and checks if species is in the pakudex
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
