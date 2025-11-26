#data types list
int_a=1
float_b=12.5
str_c='python'
bool_d= True
list_e=[1,2,3,45,13]

#addition
def fun_add():
    a=13
    b=7
    print(a+b)
fun_add()

#mark statemaent
def fun():
    mark= int(input("Enter The Total Marks:"))
    if mark>=50 and mark<=60:
        print("Grade is C")
    elif mark>=70 and mark<=80:
        print("Grade is B")
    elif mark>=80 and mark<=90:
        print("Grade is A")
    elif mark>=90 and mark<=100:
        print("Grade is O")
    else:
        print("Below Average")
fun()

#Palindrome
def Palin(p):
    return p == p[::-1]  
Text= str (input("Enter a String:"))
if Palin(Text):
    print (" is Palindrome")
else:
    print("Not a Plaindrome")     


#Subraction
def fun_Sub():
    A=int(input("Enter The No:"))
    B=int(input("Enter The No:"))
    print("ANS IS:",A-B)
fun_Sub()