import time
from parse import parseInput
import sys
import itertools

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

    # print(f"NumSat runs: {numSat_runs}")
    # numSat_runs += 1
    return len(Sat)

# def Beam(BeamSize, StartState):
#     global Clauses, goalState

#     def MoveGen(State):
#         newStates = []

#         for variable in State:

#             newState = State.copy()
            
#             newState[State.index(variable)] = not State[State.index(variable)]

#             newStates.append(newState)

#         return newStates

#     Explored = []
#     Beam = [StartState]

#     goalFound = False

#     while Beam and not goalFound:
#         Frontier = []
        
#         for State in Beam:

#             if GoalTest(State):
#                 goalState = State
#                 goalFound = True
#                 Explored.append(goalState)
#                 break

#             for newState in MoveGen(State):
                
#                 if newState not in Explored and newState not in Frontier:

#                     Frontier.append(newState)

#             Explored.append(State)
     
#         Frontier.sort(reverse=True, key=numSat)

#         Frontier = [state[1] for state in Frontier]

#         Beam = Frontier[0:BeamSize-1]

#     if goalFound:
#         print("Goal state found!")
#         print(goalState)
#         print(f"Number of Explored States: {len(Explored)}")
#     else:
#         print("No goal state found!")

    
def VND(StartState):
    global Clauses, goalState
    density = 1

    def MoveGen(State):
        nonlocal density

        def MoveGenDensity(State, density):

            for comb in itertools.combinations(list(range(NumIng)), density):

                newState = State.copy()
                
                for index in comb:
                    newState[index] = not newState[index]
                    
                if newStates not in Explored:
                    newStates.append(newState)

            return newStates

        newStates = []

        # while not newStates and density <= NumIng:
        #     newStates = MoveGenDensity(State, density)
        #     density += 1
        newStates = MoveGenDensity(State, density)
     
        return newStates

    Explored = []
    goalFound = False
    currState = StartState
    bestState = StartState

    while currState:

        Frontier = MoveGen(currState)

        Frontier = [(numSat(state),state) for state in Frontier if state not in Explored]

        Frontier.sort(reverse=True)

        Frontier = [state[1] for state in Frontier]

        Explored.append(currState)

        print(numSat(currState), numSat(bestState))
        if numSat(currState) > numSat(bestState):
            bestState = currState
            print(f"New best states found: {numSat(bestState)}")

        if Frontier:
            currState = Frontier[0]
        else:
            currState = None

    # if goalFound:
    #     print("Goal state found!")
    #     print(goalState)
    #     print(f"Number of Explored States: {len(Explored)}")
    # else:
    #     print("No goal state found!")
    print(bestState)
    print(f"Number of satisfied customers: {numSat(bestState)}")
    print(f"Number of Explored States: {len(Explored)}")

    return bestState

# def Tabu(StartState, Tenure):
#     global Clauses, goalState

#     CurrentTenure = [0] * NumIng

#     def MoveGen(State):
#         TenureDict = {}
#         newStates = []
#         nonlocal CurrentTenure

#         CurrentTenure = [max(var-1, 0) for var in CurrentTenure]
            

#         for variable in State:
        
#             if (CurrentTenure[State.index(variable)]):
#                 continue

#             newState = State.copy()
            
#             newState[State.index(variable)] = not State[State.index(variable)]

#             # key = str(newState)
#             # value = 'asdf'

#             value = CurrentTenure.copy()

#             # if(CurrentTenure[State.index(variable)] == 0):

#             value[State.index(variable)] = Tenure


#             TenureDict[str(newState)] =  value
            
#             newStates.append(newState)

#         return newStates, TenureDict

#     Explored = []
#     goalFound = False
#     nextState = StartState

#     while nextState and not goalFound and len(Explored) < 5000:
#         if GoalTest(nextState):
#             goalState = nextState
#             goalFound = True
#             Explored.append(goalState)
#             break

#         Frontier, TenureDict = MoveGen(nextState)

#         Frontier = [(numSat(state),state) for state in Frontier]

#         Frontier.sort(reverse=True)

#         Explored.append(nextState)

#         if Frontier:
#             nextState = Frontier[0]
#             CurrentTenure = TenureDict[str(Frontier[0])]
#         else:
#             nextState = None

#     if goalFound:
#         print("Goal state found!")
#         print(goalState)
#         print(f"Number of Explored States: {len(Explored)}")
#     else:
#         print("No goal state found!")    

if __name__ == "__main__":
    numSat_runs = 0
    start_time = time.time()
    people, ingredients = parseInput(sys.argv[1])
    NumIng = len(ingredients)

    tree_txt = open("tree.txt", "r")
    for line in tree_txt:
        ing = line.strip("\n").split(" ")[1:-1]
    StartState = [False] * NumIng
    for ingredient in ing:
        StartState[ingredients.index(ingredient)] = True
    bestState = VND(StartState)

    outputFile = open("output.txt", 'w')
    
    outputFile.write(f"{sum(bestState)} ")
    for ingredient in ingredients:
        if bestState[ingredients.index(ingredient)]:
            outputFile.write(f"{ingredient} ")