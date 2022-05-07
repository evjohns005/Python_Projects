# #Part 1

# import datetime

# todays_date = datetime.datetime.now()
# print("Today is: ", todays_date)

# current_time = datetime.datetime.now().time()
# print("Time: ", current_time)


#Part 2
peom_string = 'Tiny little secrets \nGet buried in the dirt, \nAnd if they were dug up, \nSomeone would probably get hurt.'
print(peom_string)

poem_file = open('poem.txt', 'w')
poem_file.write(peom_string)
poem_file.close()

peom_file = open('poem.txt', 'r')
for line in peom_file:
    print(line, end = ' ')
peom_file.close()