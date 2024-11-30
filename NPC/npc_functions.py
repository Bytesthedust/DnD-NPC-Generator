#source of generator functions
from random import choice, choices, seed
from npcdbs import*

def generateRace():
    """Returns a string in form of (subrace race) or race and image"""
    result = ""
    race = choice(list(raceDict.keys())) #returns a random race from dict

    #image = getImage(race) #returns an image of the selected race
    if raceDict.get(race) != None: #check if race has a subrace
        result = choice(raceDict.get(race)) + " " + race
    else:
        result = race

    return result

def generateRelationStatus():
    """Returns an NPC marital status"""
    status = choice(relationship)
    return status

def generateOrientation():
    """Returns an NPC orientation"""
    ori = choice(orientation)
    return ori

def generateAge():
    """Returns NPC age group"""
    age = choice(agegroup)
    return age

def generateBackground():
    """Returns a string of subrace race"""
    background = choice(list(profDict.keys())) #returns a random background
    result = choice(profDict.get(background))
    return result


def generatePersonality():
    """Returns a string with three personality traits"""
    #Opens and reads a text file containing personality traits
    personalityFile = open("python\\NPC\\textFiles\\personalityList.txt", "r")
    personalityLines = personalityFile.readlines()

    #empty list to contain traits
    personalityTraits = []

    for i in personalityLines:
        personalityTraits.append(i.rstrip())

    personalityFile.close()


    #The choices function will return a list containing three random traits
    perList = choices(personalityTraits, k=3)

    persona_format = "{}, {}, {}".format(perList[0], perList[1], perList[2])
    return persona_format

def generateName():
    """returns a name as a string"""
    #opens file containing first names
    firstNameFile = open("python\\NPC\\textFiles\\nameList.txt")
    firstNameLines = firstNameFile.readlines()
    firstName = choice(firstNameLines).strip() #randomly chooses a name and removes whitespace
    firstNameFile.close()

    #opens file containing surnames
    surnameFile = open("python\\NPC\\textFiles\\surname.txt")
    surnameLines = surnameFile.readlines()
    surname = choice(surnameLines).strip()
    surnameFile.close()

    name = "{} {}".format(firstName, surname) #formatting the final name
    return name

def generateGender():
    """Returns a string representing gender"""
    return choice(["M", "F"])

def generateAll():
    generated_data = {
        "Name": generateName(),
        "Race": generateRace(),
        "Gender": generateGender(),
        "Personality": generatePersonality(),
        "Background": generateBackground(),
        "Relationship Status": generateRelationStatus(),
        "Orientation": generateOrientation(),
        "Age Group": generateAge()
        # Add more attributes as needed
    }
    return generated_data
