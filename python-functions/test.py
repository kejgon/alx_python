
# counter = 0
# while counter <= 10:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1

##################################################
# ############# Practical Slice Email ############
##################################################
# print("*" * 73)
# print(("*" * 25) + " " + "Practical Slice Email" + " " +("*" * 25) )
# print("*" * 73)

# theName = input('What\' your name? ').strip().capitalize()
# theEmail = input('What\' your email address? ').strip()

# # Here We Want to Get the Username and There Website
# theUsername = theEmail[:theEmail.index("@")]
# theWebsite = theEmail[theEmail.index("@") + 1:]

# print(f"Hello {theName}, your email address is {theEmail}")
# print(f"Your username is {theUsername}, \nyour website is {theWebsite}")


# ##################################################
# # ############# Your Age Full Details ############
# ##################################################
# print("*" * 73)
# print(("*" * 25) + " " + "Your Age Full Details" + " " +("*" * 25) )
# print("*" * 73)

# getAge = int(input("Enter your age: ").strip())

# # Get the from Different Units
# months = getAge * 12
# weeks = months * 4
# days = getAge * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# print(f"You\' lived for :")
# print(f"Months : {months}")
# print(f"Weeks : {weeks:,}")
# print(f"Days : {days:,}")
# print(f"Hours : {hours:,}")
# print(f"Minutes : {minutes:,}")
# print(f"Seconds : {seconds:,}")


##################################################
# ############# Make Decision ############
##################################################
# print("*" * 73)
# print(("*" * 25) + " " + "Make Decision" + " " +("*" * 25) )
# print("*" * 73)

# uName = "Kejgon James"
# uCountry = "South Korea"
# cName = "Python"
# cPrice = 100

# if uCountry == "South Sudan":
#     print(f"Hi {uName}, because you're from {uCountry}!")
#     print(f"The course \'{cName}\' Price is : ${cPrice - 95}.")

# elif uCountry == "US":
#     print(f"Hi {uName}, because you're from {uCountry}!")
#     print(f"The course \'{cName}\' Price is : ${cPrice - 10}.")

# else:
#     print(f"Hi {uName}, because you're from {uCountry}!")
#     print(f"The course \'{cName}\' Price is : ${cPrice - 50}.")

#################################################
############# Ternary Condition ############
#################################################
# print("*" * 73)
# print(("*" * 25) + " " + "Ternary Condition" + " " +("*" * 25) )
# print("*" * 73)

# age = 17
# adultMovies = 18

# print("Movie is not good for you" if age < adultMovies else "Movie is good for you")


#################################################
############# Calculating Person Age with Time Unites Advanced ############
#################################################
print("*" * 100)
print(" Calculating Person Age with Time Units ".center(100, "#"))
print("*" * 100)

age = int(input("Enter your age: ").strip())
print("NOTE! You can enter the unit or the first letter of the unit you wish to ".center(100, "#"))
unit = input("Enter the unit you wish (months, weeks, days, hours, minutes, seconds, or first letter of each unit): ").strip()

# Getting the unit values
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if unit == "months" or unit == "m":
    print(f"You have chosen {unit}")
    print(f"You have lived for {months:,} months.")
elif unit == "weeks" or unit == "w":
    print(f"You have chosen {unit}")
    print(f"You have lived for {weeks:,} weeks.")
elif unit == "days" or unit == "d":
    print(f"You have chosen {unit}")
    print(f"You have lived for {days:,} days.")
elif unit == "hours" or unit == "h":
    print(f"You have chosen {unit}")
    print(f"You have lived for {hours:,} hours.")
elif unit == "minutes" or unit == "mi":
    print(f"You have chosen {unit}")
    print(f"You have lived for {minutes:,} minutes.")
elif unit == "seconds" or unit == "s":
    print(f"You have chosen {unit}")
    print(f"You have lived for {seconds:,} seconds.")
else:
    print("Invalid unit entered. Please enter a valid unit.")

