from visual_entity import *


class MoveableEntity(VisualEntity):

	def __init__(self, body):
		VisualEntity.__init__(self, body)
		direction = Point(0, 0)
		speed = 0
		vspeed = 0
		hspeed = 0

	def move(self, dx, dy):
		self.body.figure.move(dx, dy)

	def set_speed(self, speed):
		self.speed = speed
		self.hspeed = direction.x * speed
		self.vspeed = direction.y * speed
