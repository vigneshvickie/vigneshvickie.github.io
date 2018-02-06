'''Very common problem in computational programming is to determine the underlying law to which some phenomenon obeys. For learning purpose let us practice a simple variant - discovering linear dependence by two given observations (for example, how the price for some product depends on its size, weight etc.)

Linear function is defined by an equation:

for i in range(int(input())):
  a=list(map(int,input().split()))
  slope=round((a[1]-a[3])/(a[0]-a[2]))
  intercept=round(a[1]-(slope*a[0]))
  print("("+str(slope)+" "+str(intercept)+")",end=" ")
