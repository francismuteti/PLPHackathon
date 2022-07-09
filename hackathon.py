
# Bus Fare Challenge – Task One (Day 1)
import datetime
x=datetime.datetime.today()
q=x.strftime("%A")[0:3]
date=x.strftime("%Y-%m-%d")
if x.weekday() < 5:
    print ('Date:',date)
    print ('Day:',q)
    print ('Fare:',100)
elif q=='Sat':
    print ('Date:',date)
    print ('Day:',q)
    print ('Fare:',60)
else:
    print ('Date:',date)
    print ('Day:',q)
    print ('Fare:',80)

# Sales Tax Challenge – Task Two (Day 1)
square_foot=int(input("Enter total square feet of the wall "))
paint_price=int(input("Enter price of the paint per gallon "))
def construction():
  paint_required=(square_foot*1)/115
  labor_required=(square_foot*8)/115
  labor_cost=labor_required*20
  cost_of_Paint=paint_required*paint_price
  total_cost=cost_of_Paint+labor_cost
  print('Paint required:',paint_required,'Gallons')
  print('Labor Required;',labor_required,'Hours')
  print('cost of paint:$',cost_of_Paint)
  print('laborcost:$',labor_cost)
  print('Total Cost:$',total_cost)

construction()



# Personality test program - Task One (Day 2)
books=int(input("Enter the number of books you bought"))
if books<=0:
  print("Oops No Points Awarded!")
elif books==1:
  print("Bravo! 6 Points Awarded!!")
elif books==2:
  print("Bravo! 16 Points Awarded!!")
elif books==3:
  print("Bravo! 32 Points Awarded!!")
elif books>=4:
  print("Bravo! 60 Points Awarded!!")
# Challenge - Task Two (Day 2)
careers=['Doctor','Accountant','Software engineer','Lawyer']
career_advices=['score well in biology','get and A in business studies and mathematics','have passion for computers and enroll at PLP','Pass your History classes']
career_questions=['What subject do you like most? ','What subject do you score the highest? ','What subject exits you most? ']
for question in career_questions:
  user_input=input(question)
for i in career_advices:
  possible_outcome=i.split()
  if user_input in possible_outcome:
    print("true")
    if user_input=='biology':
      print('Venture into Doctry')
  else:
    print('invalid') 

# Door lock system Challenge – Task One (Day 3)


import datetime

password="1234@gmail"
door_command=""
door_command_open="open"
door_command_close="close"
door_command_quit="quit"
door_command_invalid="invalid"
door_command_open_count=0
door_command_close_count=0
door_command_quit_count=0
door_command_invalid_count=0
door_command_open_date=""
door_command_close_date=""
password_attempts=0

entered_password=input("Enter password to unlock: ")
while entered_password !=password:
  print("invalid password")
  entered_password=input("Enter password to unlock: ")
else:
  while door_command != door_command_quit:
    door_command=input("Type a command ")
    if door_command == door_command_open:
      door_command_open_count+=1
      if door_command_open_count==1:
        door_command_open_date=str(datetime.datetime.now())
        print("The door is now open")
        print("Door was opened at ",door_command_open_date)
      else:
        print("The door is already open")
    elif door_command == door_command_close:
      door_command_close_count+=1
      if door_command_close_count==1:
        door_command_close_date=str(datetime.datetime.now())
        print("The door is now closed")
        print("Door was Closed at ",door_command_close_date)
      else:
          print("The door is already closed")
    elif door_command == door_command_quit:
      door_command_close_quit+=1
      print("Thank you for your time")
      break
    else:
      print("invalid input")
# Day 3: Challenge Task Two (Day 3)


fat_grams_consumed=int(input("Enter the number of fat grams you consume: "))
carbohydrate_grams_consumed=int(input("Enter the number of carbohydrate grams you consume: "))

def calories():
  Calories_from_fats_fat_grams=fat_grams_consumed*9
  Calories_from_carbs_carb_grams= carbohydrate_grams_consumed*4
  print("Calories from carbs carb grams; ",Calories_from_fats_fat_grams)
  print("Calories from fats fat grams; ",  Calories_from_carbs_carb_grams)

calories()
