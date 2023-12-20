from dataclasses import dataclass


@dataclass
class Budget:
    """ An object representing a budget
    
    A budget is composed of 1 attribute:
        1. A name

    """
    id: str
    name: str
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name