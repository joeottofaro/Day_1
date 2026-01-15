# Band Name Generator
from time import sleep

print("Welcome to the Band Name Generator!!!")

# Grab users info
users_city = input("What City did you grow up in ? \n")
users_pet_name = input("What was your pets name growing up ? \n")

# Builds Suspense
print("Your Band Name is.... \n")
sleep(2)

print(users_city + " " + users_pet_name)
