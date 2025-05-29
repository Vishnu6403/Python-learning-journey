#operators
''' symbols which perform actions

1.Arithematic operators
   arithematic
   + Addition
   - Subtraction
   * multiplication
   /  division
   ** power  a**2 a**10
   // floor division
   % modulo reminder
   '''

a=int(input("Enter a value for a"))
b=int(input("Enter a value for b"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)


''' Relational operators

>,<,>=,<=,==,!=
a==5  a!=5'''
print(a==b)
print(a<=b)

''' Assignment operators
=
a=5
a=a+2   a+=2,-=,*='''
print(a)
a+=4
print(a)
a-=2
print(a)
a*=5
print(a)
a/=3
print(a)

''' Logical operators
c1 and c2   total>80 and maths>80
c1 or  c2   total>80 or maths>90
c1        '''
a=int(input("a"))
b=int(input("b"))

print(a>4 and b>2)
print(a>4 or b>2)

