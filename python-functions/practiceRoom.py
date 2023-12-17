
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
# print("*" * 100)
# print(" Calculating Person Age with Time Units ".center(100, "#"))
# print("*" * 100)

# age = int(input("Enter your age: ").strip())
# print("NOTE! You can enter the unit or the first letter of the unit you wish to ".center(100, "#"))
# unit = input("Enter the unit you wish (months, weeks, days, hours, minutes, seconds, or first letter of each unit): ").strip()

# # Getting the unit values
# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# if unit == "months" or unit == "m":
#     print(f"You have chosen {unit}")
#     print(f"You have lived for {months:,} months.")
# elif unit == "weeks" or unit == "w":
#     print(f"You have chosen {unit}")
#     print(f"You have lived for {weeks:,} weeks.")
# elif unit == "days" or unit == "d":
#     print(f"You have chosen {unit}")
#     print(f"You have lived for {days:,} days.")
# elif unit == "hours" or unit == "h":
#     print(f"You have chosen {unit}")
#     print(f"You have lived for {hours:,} hours.")
# elif unit == "minutes" or unit == "mi":
#     print(f"You have chosen {unit}")
#     print(f"You have lived for {minutes:,} minutes.")
# elif unit == "seconds" or unit == "s":
#     print(f"You have chosen {unit}")
#     print(f"You have lived for {seconds:,} seconds.")
# else:
#     print("Invalid unit entered. Please enter a valid unit.")

#################################################
############# Calculating Person Age with Time Unites Advanced ############
#################################################
# print("*" * 100)
# print(" Practicle Membership Control ".center(100, "#"))
# print("*" * 100)

# # List contain the Admins
# admins = ["Kejgon","James","Laa","Kimo","Bumana"]

# #login Input
# name = input("Enter your username: ").strip().capitalize()

#checks if username is in the Admins list

# if name in admins:

#     print(f"Hello {name}, Welcome back.\n\n")
#     option = input("Do you want to Update / 'U' or Delete / 'D' your username? ").strip().capitalize()

#     if option == "Update" or option == "U":
#         newUsername = input("Please enter your new username? ").strip().capitalize()
#         admins[admins.index(name)] = newUsername
#         print(f"Your username was updated successfully to : {newUsername}")
#         print(admins)

#     elif option == "Delete" or option == "D":
#         admins.remove(name)
#         print(f"Your username was deleted successfully")
#         print(admins)

#     else:
#         print("invalid option")

# else:
#     print("You'r not admin or invalid username")
#     status = input("You want to be Added? Yes / Y or No / N?").strip().capitalize()
#     if status == "Yes" or status == "Y":
#         admins.append(name)
#         print("You have been added successfully.")
#         print(admins)
#     elif status == "No" or status == "N":
#         print("Come back later.")


#################################################
############# Loop => While Practice ############
############# Simple Bookmark Manager ############
#################################################
# print("*" * 100)
# print(" Simple Bookmark Manager ".center(100, "#"))
# print(("*" * 100) + "\n")

# bookmarksList = []

# #Maximum websites allowed in the bookmarks list
# maxBookmarks = 5

# while maxBookmarks > 0:
#     websites = input("Ente yout website without http:// ")
#     bookmarksList.append(f"http://{websites.strip().lower()}")
#     print(bookmarksList)

#     # Decrease One number from the number of bookmarksList
#     maxBookmarks -= 1
#     # Display a messege after the adding a website in the bookmarks list
#     print(f"Website added, {maxBookmarks} spots left.")

# else:
#     print("The bookmarks is full")

# count = 0
# for bookmark in bookmarksList:
#     print(f"# {count + 1} - {bookmark}")
#     count += 1


#################################################
############# Loop => While Practice ############
############# Simple Password Guess ############
#################################################
# print("*" * 100)
# print(" Simple Password Guess ".center(100, "#"))
# print(("*" * 100) + "\n")

# attempt = 3
# password = '123@.com'
# pasInput = input("Enter your password: ").strip()

# while password != pasInput:
#     print(f"Wrong password, you\'ve left with {attempt} attempts")
#     pasInput = input("Enter your password: ").strip()
#     attempt -= 1


#     if attempt == 0:
#         print(f"All your attempts are done.")
#         break

# else:
#     print(f"Correct password")


# #################################################
# ############# Function Packing, Unpacking Arguments Trainings ############
# #################################################
# print("*" * 100)
# print(" Function Packing, Unpacking Arguments Trainings ".center(100, "#"))
# print(("*" * 100) + "\n")

# mySkillsLevels = {
#     "front_End": ["HTML", "CSS", "JavaScripts"],
# }

# softSkill = ("Problem Solving", "Communication Skill", "Project Management")

# def skills_ShowCase(name, *soft_skill, **myskills_level):
#     print(f"Hi {name}, welcome to your skills showcase")
#     print("Your soft skills are :")

#     for softK in soft_skill:
#         print(f" - {softK}")

#     for mslevel_key, levelValue in myskills_level.items():
#         print(f"{mslevel_key} skills are:")
#         for level in levelValue:
#             print(f"  - {level}")



# skills_ShowCase("kejgon", *softSkill, **mySkillsLevels)



# #################################################
# ############# Function Recusion ############
# #################################################
# print("*" * 100)
# print(" Function Recusion  ".center(100, "#"))
# print(("*" * 100) + "\n") 

# # CLEAR WORD FUNCTION

# word = "WWWorlldd"

# def clear_word(word):

#     if len(word) == 1:
#         return word

#     if word[0] == word[1]:

#         print(f"Print before the condition {word}")

#         return clear_word(word[1:])

#     print(f"Print Before Return {word}")

#     return word[0] + clear_word(word[1:])

# print(clear_word(word))        




#################################################
############# Function Recusion ############
#################################################
# print("*" * 100)
# print(" Function Recusion  ".center(100, "#"))
# print(("*" * 100) + "\n") 


import json


phone = {
    "name": "iPhone",
    "model": 15
}

convToJson = json.dumps(phone)

print(f"This is Json data: {(convToJson)} ")
print(f"This is Json a Dictionary: {phone} ")
print(type(convToJson))
print(dir(json))