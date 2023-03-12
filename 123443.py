N=1000
print "Skepsou enan arithmo apo to 1 ews to ",N
guesses=0
found=False
first=1
last=N
while not found and guesses < 10:
    mid=(first+last)/2
    answer=raw_input("Einai o arithmos o "+str(mid)+" ? (N/O) ")
    guesses=guesses+1
    if answer=="N":
        found=True
    else:
        answer=raw_input("Einai mikroteros tou "+str(mid)+"? ")
    if answer=="N":
        last=mid-1
    else:
         first=mid+1
if found:
    print "Kerdisa!!! To vrika me ",guesses," prospathies"
else:
    print "Kerdises"
