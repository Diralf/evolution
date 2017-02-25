
class Entity:

    valid_id = 0

    def __init__(self):
        self.id = Entity.valid_id
        Entity.valid_id += 1
