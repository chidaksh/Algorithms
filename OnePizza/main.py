from parse import parseInput, Person
import sys

def main() -> None:
    people, ingredients = parseInput(sys.argv[1])
    print(len(people))
    print(len(ingredients))
    # ingredient1 = ingredients[0]
    # ingredient2 = ingredients[1]

    # only1 = []
    # only2 = []
    # both = []

    # for person in people:
    #     if (ingredient1 in person.likes or ingredient1 not in person.dislikes) and (ingredient2 in person.likes or ingredient2 not in person.dislikes):
    #         both.append(person)
    #     if ingredient1 in person.likes or ingredient1 not in person.dislikes:
    #         only1.append(person)
    #     if ingredient2 in person.likes or ingredient2 not in person.dislikes:
    #         only2.append(person)

    # print(len(only1), len(only2), len(both))
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <input file>")
        exit()
    main()