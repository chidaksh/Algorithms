class Person():
    def __init__(self, likes, dislikes):

        self.likes = likes
        self.dislikes = dislikes

def parseInput(filename: str) -> tuple[list, list]:
    file = open(filename, "r")
    people = []
    ingredients = set()

    for index, line in enumerate(file):
        if index == 0:
            num_of_people = int(line.strip("\n"))
        elif index%2 == 1:
            likes = line.strip("\n").split(" ")[1:]
            for like in likes:
                ingredients.add(like)
        else:
            dislikes = line.strip("\n").split(" ")[1:]
            for dislike in dislikes:
                ingredients.add(dislike)
            people.append(Person(likes, dislikes))

    return people, list(ingredients)