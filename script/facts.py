import json

data = [

    ("My original name was Nicolas Coppola. I changed my last name after "
     "actors from my first movie resented me because I had some relatives "
     "that were very successful in the industry."),
    
    ("I chose Cage as my last name because I was inspired by the Marvel comic "
     "book superhero Luke Cage."),

    ("I once did mushrooms with my cat Louis."),

    ("When I die, I'll be buried in a nine foot tall pyramid in New Orleans."),

    ("I once had two teeth pulled for a movie. They were baby teeth, but I "
     "didn't use anesthetic so I definitely felt it."),

    ("If I don't like the way an animal has sex, I refuse to eat it."),

    ("I once had a pet octopus."),

    ("I was once stalked by a mime."),

]

if __name__ == '__main__':

    import os
    import pathlib

    # Use pathlib and os to get the path of the project folder
    FILENAME = 'facts.json'
    PROJECT_DIRECTORY = pathlib.Path(__file__).parent.parent
    DATA_FOLDER = os.path.join(PROJECT_DIRECTORY, 'data')
    JSON_FILE = os.path.join(DATA_FOLDER, FILENAME)

    # Save the dictionary as a json file
    with open(JSON_FILE, 'w') as json_file:
        json.dump(data, json_file)