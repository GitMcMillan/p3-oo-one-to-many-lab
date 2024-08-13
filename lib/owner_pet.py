class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} must be in PET_TYPES")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
        

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
         return [pet for pet in Pet.all if pet.owner == self]
            
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} must be an instance of Pet class")
        
        pet.owner = self

    def get_sorted_pets(self):
        pets_list = self.pets()
        sorted_pets = sorted(pets_list, key=lambda pet: pet.name)
        return sorted_pets