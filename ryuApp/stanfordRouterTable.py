class StanfordRouterTable: 

	def __init__(self):
		self.route = {}
		for i in range(1, 17):
			self.route.setdefault(i, {})

		for i in range(1, 30):
			self.route[1][i] = i
			self.route[2][i] = 17
			self.route[3][i] = 15
			

		for i in range(30, 46):
			self.route[1][i] = 30
			self.route[2][i] = i-29
			self.route[3][i] = 16
			
		for i in range(46, 60):
			self.route[1][i] = 31
			self.route[2][i] = 18
			self.route[3][i] = i-45
			
	

	def get_route(self):
		return self.route
