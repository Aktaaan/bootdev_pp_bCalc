#imperial.py
#this will convert a float into a 
class Imperial():
	def __init__(self, str_dimension, foot="", inch="", fraction=""): 
		self.foot = foot
		self.inch = inch
		self.fraction = fraction
		self.seperator = ""

	# Check if inputs were arch or float
	def input_check(self):
		if "'" in self.str_dimension or '"' in self.str_dimension or "/" in self.str_dimension:
			return self.convert_from_arch(str_dimension)
		else: 
			self.str_to_float(str_dimension)

	def str_to_float():
		pass

		# takes str input and returns a float 
	def convert_from_arch(self, str_dimension):
		dirty_str_rip = str_dimension
		str_rip = dirty_str_rip.replace(" ", "")

		def rip_n_shred(str_rip):
			if not str_rip:
				if self.seperator:
					self.fraction = self.seperator
					self.seperator = ""
				return

			char = str_rip[0]

			if str_rip[0] == "'":
				self.foot = self.seperator
				self.seperator = ""
			elif str_rip[0] == '"':
				self.inch = self.seperator
				self.seperator = ""
			else:
				self.seperator += char
				
			return rip_n_shred(str_rip[1:])

		rip_n_shred(str_rip)	
		print(f"\nFoot: {self.foot}\nInch: {self.inch}\nFraction: {self.fraction}\n")
		


	# takes the kb input and feeds back tape measure values
	# the input is a string, and is converted into architectural
	def convert_to_arch():
		str_dimension 
		pass 

