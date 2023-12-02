
# counter = 0
# while counter <= 10:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1


# Practical Slice Email
print("*" * 73)
print(("*" * 25) + " " + "Practical Slice Email" + " " +("*" * 25) )
print("*" * 73)

theName = input('What\' your name? ').strip().capitalize()
theEmail = input('What\' your email address? ').strip()

# Here We Want to Get the Username and There Website
theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName}, your email address is {theEmail}")
print(f"Your username is {theUsername}, \nyour website is {theWebsite}")