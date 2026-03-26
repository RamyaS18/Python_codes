import random
name1=input("enter player1 name:")
name2=input("enter player2 name:")
d1=random.randint(1,25)
d2=random.randint(1,25)
s1=25
s2=25
print("_____________PLAYER1_____________")

while True:
    g1=int(input("enter ur guess:"))
    
    if(d1==g1):
       print("the guess is correct!!")
       s1=s1-1
       break
       
    elif(d1<g1):
        print("your guess is more!!")
    else:
        print("your guess is less!!")
           
        
        
print("_____________PLAYER2_____________")

while True:
    g2=int(input("enter ur guess:"))

    if(d2==g2):
      print("the guess is correct!!")
      s2=s2-1
      break
    elif(d2<g2):
        print("your guess is more!!")
    else:
        print("your guess is less!!")
        
print("_____________RESULT_____________")
        
if (s1 < s2):
    print("{} is winner".format(name1))
elif (s1 > s2):
    print("{} is winner".format(name2))
else:
    print("The match is draw")
        