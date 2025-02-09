wether=(1,0,1,0,1,0,0,1)
sunny=0
rainy=0
for  i in range(0,8) :
    if (wether[i]==0):
        sunny+=1
    else:    
        rainy+=1
if sunny>rainy:
    print("Weather is good")
else:
    print("Weather is bad")    
