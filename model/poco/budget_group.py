from dataclasses import dataclass


@dataclass
class BudgetGroup:
    """ An object representing a budget group
    
    A budget group is composed of an attribute:
        1. A name

    """
    id: str
    name: str
    budget_id: str
    
    def __init__(self, id: str, name: str, budget_id: str):
        self.id = id
        self.name = name
        self.budget_id = budget_id