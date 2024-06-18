class Agent_0:
	'''
	Left : Value if left is blocked or not
	Front : Value if front is blocked or not
	Right : Value if right is blocked or not
	'''
	def __init__(self):
		self.left = 0
		self.front = 1
		self.right = 0
		self.current_loc = (7,10)
		self.direction = "N"

	def status(self):
		sides = ("left","front","right")
		vision = (self.left,self.front,self.right)
		options = {"left":"<","front":"^","right":">"}
 
		moves_rn = [options[sides[i]] for i in range(len(vision)) if vision[i] == 0]
		print(moves_rn)

	def move_forward(self):
		if self.direction == "N":
			self.current_loc = tuple(map(sum, zip(self.current_loc, (1,0))))
			print(self.current_loc)
		elif self.direction == "S":
			self.current_loc = tuple(map(sum, zip(self.current_loc, (-1,0))))
		elif self.direction == "E":
			self.current_loc = tuple(map(sum, zip(self.current_loc, (0,1))))
		elif self.direction == "W":
			self.current_loc = tuple(map(sum, zip(self.current_loc, (0,-1))))

	def turn(self,side):
		print(self.direction)
		current = ("N","E","S","W")
		right = ("E","S","W","N")
		left = ("W","N","E","S")
		right_dir = dict(zip(current,right))
		left_dir = dict(zip(current,left))

		if side == "Right":
			self.direction = right_dir[self.direction]
		elif side == "Left":
			self.direction = left_dir[self.direction]



#TODO : > 

agent = Agent_0()
agent.status()
agent.move_forward()
agent.move_forward()
agent.turn("Right")

