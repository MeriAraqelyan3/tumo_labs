import random

user_input = (input("Enter '1', '2', '3' to select a template if you don't decided enter 'r' for random choice: "))


def template_1():
    number = (input("Input a number: "))
    measure_of_time = input("Measure of time: ")
    mode_of_transportation = input("Input mode of transportation: ")
    adjective = input("Input adjective (feeling): ")
    adjective_2 = input("Input adjective again (feeling): ")
    noun = input("Input noun: ")
    color = input("Input a color: ")
    part_of_body = input("Input part of body: ")
    number_2 = input("Input a number again: ")
    noun_2 = input("Input a noun again: ")
    noun_3 = input("Input a noun again: ")
    part_of_body_2 = input("Input a part of body again: ")
    verb = input("Input a verb: ")
    noun_4 = input("Input a noun again: ")
    adjective_3 = input("Input adjective again (feeling): ")
    silly_word = input("Input a silly word: ")

    return f'''
    It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. 
    The hospital is a/an {adjective} place, there are a lot of {adjective_2} {noun} here. 
    There are nurses here who have {color} {part_of_body}. If someone wants to come into my room I told them 
    that they have to (verb) first. I’ve decorated my room with {number_2} {noun_2}. Today I talked to a doctor and 
    they were wearing a {noun_3} on their {part_of_body_2}. I heard that all doctors {verb} {noun_4} every day for 
    breakfast. The most {adjective_3} thing about being in the hospital is the {silly_word} {noun} ! 
         '''


def template_2():
    person_name = input("Input person name: ")
    noun = input("Input noun: ")
    adjective = input("Input adjective (feeling): ")
    adjective_2 = input("Input adjective again (feeling): ")
    verb_2 = input("Input na verb again: ")
    verb = input("Input verb (ending in ing): ")
    adverb = input("Input adverb (ending in ly: ")
    measure_of_time = input("Input measure of time: ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    number = input("input number: ")
    silly_word = input("Input silly word: ")
    noun_2 = input("Input noun again: ")

    return f'''
    This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag,
    and {noun}. I am so {adjective} to {verb} in a tent. I am {adjective_2} we might see a(n)
    {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb_2}. I
    have heard that the {color} lake is great for {verb}. Then we will {adverb} hike
    through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring
    it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun_2} around the campfire!!
          '''


def template_3():
    person_name = input("Input person name: ")
    adjective = input("Input adjective (feeling): ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    place = input("Input a place: ")
    adjective_2 = input("Input adjective again (feeling): ")
    magical_creature = input("Input magical creature (plural): ")
    adjective_3 = input("Input adjective again (feeling): ")
    magical_creature_2 = input("Input magical creature again (plural): ")
    room_in_a_house = input("Input room in a house: ")
    noun = input("Input noun: ")
    noun_2 = input("Input noun again: ")
    noun_3 = input("Input noun again (plural): ")
    adjective_4 = input("Input adjective again (feeling): ")
    noun_4 = input("Input noun again (plural): ")
    number = input("Input a number: ")
    measure_of_time = input("Input measure of time: ")
    verb = input("Input verb (ending in ing): ")
    adjective_5 = input("Input adjective again (feeling): ")
    noun_5 = input("Input noun again (plural): ")

    return f'''
    Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I
    found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective_2}
    {magical_creature} and {adjective_3} {magical_creature_2} here! In the {room_in_a_house} there is a pool full
    of {noun}. I fall asleep each night on a {noun_2} of {noun_3} and dream of {adjective_4} {noun_4}. It
    feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the
    only way to get here now is {verb} on a {adjective_5} {noun_5}!!
         '''


def choices(choice):
    if choice == '1':
        print(template_1())
    elif choice == '2':
        print(template_2())
    elif choice == '3':
        print(template_3())


templates = [template_1, template_2, template_3]

choices(user_input)

if user_input == "r":
    a_lst = ['1', '2', '3']
    a = random.choice(a_lst)
    choices(a)