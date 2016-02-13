__author__ = 'Cyph3r (Matthew Gakowski)'
__copyright__ = "Copyright 2016, Prime Finder"
__credits__ = ["Matthew Gakowski"]
__license__ = "GPL v3.0"
__version__ = "1.0"
__maintainer__ = "Matthew Gakowski"
__email__ = "mgakowski@gmail.com"
__status__ = "Production"

import math
 
f = str(input("Filename?"))
text_file = open(f+".txt", "w")
n = int(input("Limit? "))  # Limit Number
x = int(input("Start? "))  # Starting Number
a = int(math.sqrt(x))+1  # Working number
 
while x != n:
 
    if x % a != 0:  # Not equal divide
        if a != 1:  # Check if (a) not at bottom of list
            a -= 1
        if a == 1:  # Check if (a) is at bottom of list
            text_file.write(str(x)+"\n")
            print(str(x)+" is Prime!")
            x += 1
 
    if x % a == 0:  # If Equal divide, skip
        x += 1
        a = int(math.sqrt(x))+1
text_file.close()
