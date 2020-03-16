from math import pi

i = True

while i:
  h = int(input("h: "))
  _h = int(input("δh: "))
  D = int(input("D: "))
  _D = int(input("δD: "))
  d = int(input("d: "))
  _d = int(input("δd: "))

  v = (1/4)*pi*(D**2 - d**2)*h
  _v = (1/4)*pi*(2*h*(D*_D + d*_d) + (D**2 - d**2)*_h)

  print(v, " +- ", _v)
  
  if input("Next? [y]/n") == "n":
    i = False
