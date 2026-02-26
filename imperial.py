#imperial.py
#this will convert a float into a 


class Imperial():
	def __init__(self, str_dimension): #feet, inch, fract,
		'''
		self.feet = feet
		self.inch = inch
		self.fract = fract
		'''
		self.str_dimension = str_dimension

	# Check if inputs were arch or float
	def input_check(self):
		if "'" in self.str_dimension or '"' in self.str_dimension or "/" in self.str_dimension:
			return self.convert_from_arch(str_dimension)
		else: 
			self.str_to_float(str_dimension)

	def str_to_float(self):
		pass

	# takes str input and returns a float 
	def convert_from_arch(self, str_dimension):
		dirty_str_rip = self.str_dimension
		str_rip = dirty_str_rip.strip(" ")
		feet = ""
		inch = ""
		fraction = ""
		seperator = ""

		for pos in reversed(str_rip):
			seperator += pos
			if pos == '"':
				if "/" in seperator:
					fraction = seperator.replace('"', "")		
				seperator = ""
			if pos == "'":
				inch = seperator.replace("'", "")
				seperator = ""
			else:
				feet = seperator
				seperator = ""
		print(f"Feet: {feet}\nInch: {inch}\nFraction: {fraction}")
		return(feet, inch, fraction)

		# take (feet) numbers before "'" and turn them to inches


		# take (inces) numbers and add them to 
		float_dimension  = float(self.str_dimension)
		


	# takes the kb input and feeds back tape measure values
	# the input is a string, and is converted into architectural
	def convert_to_arch(self):
		str_dimension 
		pass