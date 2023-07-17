from datetime import datetime


class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, pet_name):
        self.__name = pet_name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    print("Programmer: Dat Vo ")
    print("Lab 18.1 ", datetime.now())

    my_pet = Pet()

    name = input("\nEnter your name: ")

    pet_name = input("Enter the name of the pet: ")
    my_pet.set_name(pet_name)

    animal_type = input("Enter the type of animal: ")
    my_pet.set_animal_type(animal_type)

    age = int(input("Enter the age of your pet: "))
    my_pet.set_age(age)

    print(f"\n{name}, here is the data about your pet: ")
    print("\nPet Name:", my_pet.get_name())
    print("Animal Type:", my_pet.get_type())
    print("Age of pet:", my_pet.get_age())


if __name__ == "__main__":
    main()
