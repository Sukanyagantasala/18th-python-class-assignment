#write a program to print the grade of a student based on the marks obtained
m=int(input("enter marks"))
if m>=90 and m<=80:
  print("A grade")
elif m>=80 and m<=70:
  print("B grade")
elif m>=70 and m<=60:
  print("C grade")
elif m>=60 and m<=50:
  print("D grade")
else:
  print("Fail")
  
#write a program to print if the given year is leap or not
y=int(input("enter a number"))
if y%400==0 and y%100==0:
  print("Leap Year")
elif y%4==0 and y%100!=0:
  print("Leap year")
else:
  print("Not a leap year)
        
 #write a program to print if the given number is zero or odd or even
 n=int(input("enter a number))
 if n>0:
     print("positive")
 elif n%2==0:
     print("even")
 else:
     print("odd")
        
