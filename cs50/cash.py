while True:
   try:
       x = float(input("Change: "))
       if x < 0:
           continue
   except:
       continue
   else:
       break
count = 0
while True:
    x = round(x,2)
    if x >= 0.25:
        x = x - 0.25
        count += 1
    elif x < 0.25 and x >= 0.10:
        x = x - 0.10
        count += 1
    elif x < 0.10 and x >= 0.05:
        x = x - 0.05
        count += 1
    elif x < 0.05 and x >= 0.01:
        x = x - 0.01
        count += 1
    elif x < 0.01:
        break

print(count)
