from math import pi

i = True

while i:
  print("\nDescribe your measures: \n")
  D = float(input("D: "))
  _D = float(input("δD: "))

  v = (1/6)*pi*(D**3)
  _v = (1/6)*pi*(3*(D**2)*_D)

  print(v, " +- ", _v)
  
  if input("Next? [y]/n\n") == "n":
    i = False
