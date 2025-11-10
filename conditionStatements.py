# if - else

number = 8
if number > 10:
    print("number is greater than 10")
else:
    print("number is not greater than 10")


# nested if- else
if number > 10:
    if number >12:
        print("number is greater than 12")
    else:
        print("number is not greater than 12")
else:
    if number < 5:
        print("number is less than 5")
    else:
        if number < 10:
            print("number is in between 5 and 10")
        else:
            print("number is not in between 5 and 10 also")

#Match - case statement
def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))

#Pass statement
for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)
print ("Good bye!")