# Random password generator
import os
from string import ascii_letters, digits
from random import shuffle

length = 8
  
symbols = list(ascii_letters + digits) 
shuffle(symbols)
symbols_str = "".join(symbols) 
random_password = symbols_str[:length] 
print(random_password)
os.system("echo {0}|clip".format(random_password))