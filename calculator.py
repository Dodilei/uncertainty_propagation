i = True

while i:
  h = input("h: ")
  _h = input("δh: ")
  D = input("D: ")
  _D = input("δD: ")
  d = input("d: ")
  _d = input("δd: ")

  v = (1/4)*pi*(D**2 - d**2)*h
  _v = (1/4)*pi*(2*h*(D*_D + d*_d) + (D**2 - d**2)*_h)

  print(v, " +- ", _v)
  
  if input("Next? [y]/n") == "n":
    i = False
