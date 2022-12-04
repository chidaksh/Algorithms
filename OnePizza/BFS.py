from parse import parseInput
import sys
import time


def GoalTest(State) -> bool:
    global start_time
    return (time.time() - start_time > 300)

def numSat(State) -> int:
    global people, numSat_runs
    Sat = []
    for person in people:
        satisfied = True
        for like in person.likes:
            if State[ingredients.index(like)] == False:
                satisfied = False
                break
        if satisfied:
            for dislike in person.dislikes:
                if State[ingredients.index(dislike)] == True:
                    satisfied = False
                    break
        if satisfied:
            Sat.append(person)

if(len(sys.argv) = 1):
    print("Usage python3 BFS.py <inputfile>")
    exit()

GMax = 

people, ingredients = parseInput(sys.argv[1])

def Beam(BeamSize, StartState):

    def MoveGen(State):
        newStates = []

        for variable in State:

            newState = State.copy()
            
            newState[State.index(variable)] = not State[State.index(variable)]

            newStates.append(newState)

        return newStates

    Explored = []
    Beam = [StartState]
    MaxState = StartState
    MaxValue = numSat(MaxState)


    while Beam:
        Frontier = []
        
        for State in Beam:

            for newState in MoveGen(State):
                
                if newState not in Explored and newState not in Frontier:

                    Frontier.append(newState)

            Explored.append(State)

            current_value = numSat(State)

            if(current_value > MaxValue):
                MaxValue = current_value
                MaxState = State
                print(MaxValue)

        Frontier = [(numSat(State), State) for State in Frontier]
     
        Frontier.sort(reverse=True)

        Frontier = [x[1] for x in Frontier]

        Beam = Frontier[0:BeamSize-1]

            




