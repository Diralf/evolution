from typing import Tuple


class Parents:
    def __init__(self, parents):
        # type: (Tuple(Human)) -> None
        self.parents = parents

    def is_parent(self, human):
        # type: (Human) -> bool
        return human in self.parents
