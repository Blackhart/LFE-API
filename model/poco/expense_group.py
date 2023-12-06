from dataclasses import dataclass


@dataclass
class ExpenseGroup:
    """ An object representing an expense group
    
    An expense group has 1 attribute:
        1. A name
        
    Attributes:
    
    1. Group Name
    
    The group name is defined by the user. It allows the user to easily identify the group.
    """
    id: str
    name: str
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name