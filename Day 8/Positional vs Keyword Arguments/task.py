# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}?")

greet_with("William","UK")
greet_with("Jack Bauer","Italy")
greet_with(location="US",name="John")