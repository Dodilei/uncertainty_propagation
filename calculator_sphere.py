i = True

while i:
  h = input("h: ")
  _h = input("δh: ")
  D = input("D: ")
  _D = input("δD: ")
  d = input("d: ")
  _d = input("δd: ")

  v = (1/6)*pi*(D**3)
  _v = (1/6)*pi*(3*(D**2)*_D)

  print(v, " +- ", _v)
  
  if input("Next? [y]/n") == "n":
    i = False
