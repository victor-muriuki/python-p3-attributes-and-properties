#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__ (self, name, breed = None) :
        self.name = name
        if not isinstance(name, str) or not (1<= len(name)<=25):
            print ("Name must be a string between 1 and 25 characters.")
            return 
        
        if breed and breed not in APPROVED_BREEDS:
            print ("Breed must be in the list of approved breeds.")
        
        else:
            self.breed = breed

       


        pass
    pass

