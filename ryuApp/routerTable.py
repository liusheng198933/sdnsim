class RouterTable: 

	def __init__(self):
		self.route = {}
		for i in range(1, 17):
			self.route.setdefault(i, {})

		for i in range(1, 30):
			self.route[1][i] = i
			self.route[2][i] = 17
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4


		for i in range(30, 46):
			self.route[1][i] = 30
			self.route[2][i] = i-29
			self.route[3][i] = 16
			self.route[4][i] = 15
			self.route[5][i] = 7
			self.route[6][i] = 7
			self.route[7][i] = 27
			self.route[8][i] = 26
			self.route[9][i] = 13
			self.route[10][i] = 13
			self.route[11][i] = 13
			self.route[12][i] = 13
			self.route[13][i] = 8
			self.route[14][i] = 8
			self.route[15][i] = 52
			self.route[16][i] = 5

		for i in range(46, 60):
			self.route[1][i] = 31
			self.route[2][i] = 18
			self.route[3][i] = i-45
			self.route[4][i] = 16
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4
	
		for i in range(60, 73):
			self.route[1][i] = 32
			self.route[2][i] = 19
			self.route[3][i] = 17
			self.route[4][i] = i-59
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(73, 78):
			self.route[1][i] = 33
			self.route[2][i] = 20
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = i-72
			self.route[6][i] = 8
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4


		for i in range(78, 83):
			self.route[1][i] = 34
			self.route[2][i] = 21
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 8
			self.route[6][i] = i-77
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(83, 108):
			self.route[1][i] = 35
			self.route[2][i] = 22
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = i-82
			self.route[8][i] = 27
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(108, 132):
			self.route[1][i] = 36
			self.route[2][i] = 23
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 28
			self.route[8][i] = i-107
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(132, 143):
			self.route[1][i] = 37
			self.route[2][i] = 24
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = i-131
			self.route[10][i] = 14
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(143, 154):
			self.route[1][i] = 38
			self.route[2][i] = 25
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 14
			self.route[10][i] = i-142
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(154, 165):
			self.route[1][i] = 39
			self.route[2][i] = 26
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = i-153
			self.route[12][i] = 14
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(165, 176):
			self.route[1][i] = 40
			self.route[2][i] = 27
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 14
			self.route[12][i] = i-164
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(176, 182):
			self.route[1][i] = 41
			self.route[2][i] = 28
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = i-175
			self.route[14][i] = 9
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(182, 188):
			self.route[1][i] = 42
			self.route[2][i] = 29
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 9
			self.route[14][i] = i-181
			self.route[15][i] = 51
			self.route[16][i] = 4

		for i in range(188, 238):
			self.route[1][i] = 43
			self.route[2][i] = 30
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = i-187
			self.route[16][i] = 6

		for i in range(238, 241):
			self.route[1][i] = 44
			self.route[2][i] = 31
			self.route[3][i] = 15
			self.route[4][i] = 14
			self.route[5][i] = 6
			self.route[6][i] = 6
			self.route[7][i] = 26
			self.route[8][i] = 25
			self.route[9][i] = 12
			self.route[10][i] = 12
			self.route[11][i] = 12
			self.route[12][i] = 12
			self.route[13][i] = 7
			self.route[14][i] = 7
			self.route[15][i] = 53
			self.route[16][i] = i-237

	def get_route(self):
		return self.route
