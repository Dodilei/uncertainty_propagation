from math import pi

i = True

while i:
  h = float(input("h: "))
  _h = float(input("δh: "))
  D = float(input("D: "))
  _D = float(input("δD: "))
  d = float(input("d: "))
  _d = float(input("δd: "))

  v = (1/4)*pi*(D**2 - d**2)*h
  _v = (1/4)*pi*(2*h*(D*_D + d*_d) + (D**2 - d**2)*_h)

  print(v, " +- ", _v)
  
  if input("Next? [y]/n") == "n":
    i = False
