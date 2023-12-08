from dataclasses import dataclass


@dataclass
class BudgetCategory:
    """ An object representing a budget category
    
    A budget category is composed of 2 attributes:
        1. A name
        2. The budget group ID it is linked to

    """
    id: str
    name: str
    budget_group_id: str
    
    def __init__(self, id: str, name: str, budget_group_id: str):
        self.id = id
        self.name = name
        self.budget_group_id = budget_group_id