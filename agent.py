class Agent_0:
	'''
	Left : Value if left is blocked or not
	Front : Value if front is blocked or not
	Right : Value if right is blocked or not
	'''
	def __init__(self):
		self.left = 0
		self.front = 0
		self.front = 0

	def status(self):
		if self.left == 1 and self.front == 1 and self.right == 1:
			print(''' ---
					 |   |''')
		elif self.left == 1 and self.front == 1 and self.right == 0:
			print(''' ---
					 |   >''')
		elif self.left == 1 and self.front == 0 and self.right == 1:
			print('''  ^ 
					 |   |''')
		elif self.left == 0 and self.front == 1 and self.right == 1:
			print(''' ---
					 <   |''')
		elif self.left == 1 and self.front == 0 and self.right == 0:
			print('''  ^
					 |   >''')
		elif self.left == 1 and self.front == 0 and self.right == 0:
			print('''  ^
					 <   |''')
		elif self.left == 0 and self.front == 0 and self.right == 0:
			print('''  ^
					 <   >''')

#TODO : > Make a function for setting values of left, front, right
#		> Make Internal Compass functionality
#		> Make function for getting surrounding values
#		> Make movement function for traversal

agent = Agent_0()
print(agent.status(0,0,0))

