'''Flow control statemnts
1.Decision making/conditional
   1.if


2.Iterative statemnts(Loops)




types of if
1.simple if
    if condition:
        statements'''

age=int(input("give your age"))
if age>60:
    print("you are eligible for travel allowance")

'''
2.if else

   if condition:
    statement1
   else:
     statements2'''


age=int(input("give your age"))
if age>60:
    print("you are eligible for travel allowance")
else:
    print("you are not eligible")


'''
3.if  elif  else

  if condition1:
      st1
  elif condition2:
       st2
  elif condition 3:
       st3
  else:
    statement'''

m1=45
m2=36
m3=12
total=m1+m2+m3
if total>=250:
    print("A")
elif total>=200 and total<250:
    print("B")
elif total>=150 and total<200:
    print("C")
else:
    print("Failed")

    



'''

4.Multiple if

   if cond1:
       if cond2:
          st1
       else:
          st2
   else:
      if condition3:
         st3
      elif cond4:
          st4
      else:
        st5  '''

m1=45
m2=36
m3=12
total=m1+m2+m3
if total>=250:
    print("A")
elif total>=200 and total<250:
    print("B")
elif total>=150 and total<200:
    print("C")
else:
    print("Failed")

    

    


