import numpy 

#           TCS    DCS  CBS CBLS DCLS BMS  QPC  QPCL DQPC MCS
mcdo_meals = [187, 149, 87, 122, 184, 185, 185, 220, 249, 110, 200, 250, 150, 40, 300, 250]

x = numpy.mean(mcdo_meals)
print(x)  #167.8

y = numpy.median(mcdo_meals)
print(y)   #184.5 


z = numpy.std(mcdo_meals)
print(z)  #47.81380553773146
 
skewness = int(3*(x-y)/z)
print(skewness)
0