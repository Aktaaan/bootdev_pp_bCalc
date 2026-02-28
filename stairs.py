#stairs.py


# Calculate the depth and height of the middle stairs, leaving the top and
# bottom stairs to eat the rounding size for good measurement
import math
from fractions import Fraction

class Stairs():
    def __init__(self, f_rise, f_run, f_height, f_depth, f_tread):
        self.f_rise = f_rise
        self.f_run = f_run
        self.f_height = f_height
        self.f_depth = f_depth
        self.f_tread = f_tread

        self.bottom_stair = 0.0
        self.top_stair = 0.0
        self.common_stair = 0.0

    def calc_stairs(self, f_rise, f_run, f_height, f_depth, f_tread):
        #get number of steps
        float_of_steps = f_rise / (f_height - f_tread)
        truncated_numstp = math.trunc(float_of_steps)
        number_of_steps = truncated_numstp
        
        size_of_steps = f_rise / number_of_steps

        sos_inch = math.trunc(size_of_steps)
        sos_remainder = size_of_steps - sos_inch
        sos_sxtnth = Stairs.to_sixteenths(sos_remainder)

        #turn step depth into measurement 
        dep_inch = math.trunc(f_depth)
        dep_remainder = f_depth - dep_inch
        dep_sxtnth = Stairs.to_sixteenths(dep_remainder)
        
        #calc lenth of run
        len_of_run = f_depth * number_of_steps
        lor_inch_all = math.trunc(len_of_run)
        lor_remainder = len_of_run - lor_inch_all
        lor_sxtnth = Stairs.to_sixteenths(lor_remainder)
                # inches and feet
        lor_foot_dirty = lor_inch_all / 12
        lor_foot = math.trunc(lor_foot_dirty)
        lor_inches = lor_inch_all - (lor_foot * 12)

        print(f'Rise: {f_rise}"')
        print(f"Number of steps: {number_of_steps}")
        print(f'Height of steps: {sos_inch}" {sos_sxtnth}')
        print(f'Depth of steps: {dep_inch}" {dep_sxtnth}') # this is incomplete
        print(f"""Length of run: {lor_foot}' {lor_inches}" {lor_sxtnth}""")

    def inch_to_feet(inches):
        #this would be just as much work
        return (feet, inches)

    def to_sixteenths(decimal):
        sixteenth = round(decimal * 16)
        return Fraction(sixteenth, 16)