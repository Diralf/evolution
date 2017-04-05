class Level:
    def __init__(self, options):
        self.init_func = options.init
        self.update_func = options.update
        self.draw_func = options.draw

    def init(self):
        self.init_func()

    def update(self, delta):
        self.update_func(delta)

    def draw(self, surface):
        self.draw_func(surface)