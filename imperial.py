#imperial.py
#this will convert a float into a 
class Imperial():
	def __init__(self, str_dimension, foot="", inch="", fraction=""): 
		self.foot = foot
		self.inch = inch
		self.fraction = fraction
		self.str_dimension = str_dimension

		self.nominator = 0
		self.denominator = 0
		self.seperator = ""
		self.f_measurement_inches = 0

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
		dirty_str_rip = self.str_dimension
		str_rip = dirty_str_rip.replace(" ", "")
		rip_f = self.fraction

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
		
		def rip_fract(fract_str):
			if "/" not in fract_str:
				return
			
			parts = fract_str.split("/")
			self.nominator = float(parts[0])
			self.denominator = float(parts[1])
		
		if self.fraction != "":
			rip_fract(self.fraction)
			if self.denominator != 0:
				f_fract = self.nominator / self.denominator
			else:
				f_fract = 0
		else:
			f_fract = 0
		
		if self.foot != "":
			f_foot = float(self.foot)
		else:
			f_foot = 0
		
		if self.inch != "":
			f_inch = float(self.inch)
		else:
			f_inch = 0

		self.f_measurement_inches = (f_foot * 12) + f_inch + f_fract

		print(f"\nFoot: {self.foot}\nInch: {self.inch}\nFraction: {self.fraction}\n")	
		print(f"Measurement in inches: {self.f_measurement_inches}")


	# takes the kb input and feeds back tape measure values
	# the input is a string, and is converted into architectural
	def convert_to_arch():
		str_dimension 
		pass 

