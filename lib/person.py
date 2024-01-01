#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name) -> None:
        self.name = name
        
        if not isinstance(name, str) or not (1<= len(name)<= 25):
            print("Name must be string under 25 characters.")
        return  
          
        pass
    pass
