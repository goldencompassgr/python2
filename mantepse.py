import random
secret_numper=random.randint(1,1000)
guesses=0
found=False
a=raw_input("Skeftika enan arithmo, mporeis na ton mantepseis ? (N/O) ")
while not (a=="N" or a=="n" or a=="O" or a=="o"):
    a=raw_input("Skeftika enan arithmo, mporeis na ton mantepseis ? (N/O) ")
if a=="N" or a=="n":
    print "o kwdikos sou:" '912',secret_numper,'890'
    while not found and guesses < 10:
        guess=input("Mantepse ton arithmo (1-1000): ")
        guesses=guesses+1
        if guess==secret_numper:
            found=True
        else:
            if guess < secret_numper:
                print "O arithmos sou einai mikroteros."
            else:
                print "O arithmos sou einai megaluteros."
    if found == True:
        print "Mpavo to vrikes me ",guesses," prospathies"
    else:
        print "Dustuxws den ton vrikes."
    print "o Arithmos htan o: ",secret_numper
else:
    print "Se eixa gia exipno."
