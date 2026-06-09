radius = 6
PI = 22/7

volume_without_math_lib = (4/3)*PI*radius*radius*radius

import math
volume_with_math_lib = (4/3)*math.pi*math.pow(radius,3)

print(volume_without_math_lib)
print(volume_with_math_lib)