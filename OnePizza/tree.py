from parse import parseInput
import sys


def main() -> None:
  people, ingredients = parseInput(sys.argv[1])

  file = open("tree.txt","w")

  people = sorted(people, key=lambda x:len(x.likes), reverse = False)
  p = 1
  n = len(people)
  current_ing = []
  cur_dislike = []
  for ing in people[0].likes:
        current_ing.append(ing)
  for ing in people[0].dislikes:
        cur_dislike.append(ing)
  
  # current_ing.append(people[0].likes)
  for i in range(n-1):
    check = 0
    for ing in people[i+1].dislikes:
      if ing in (current_ing):
        check+=1
        break

    if check == 0:
      for ing in cur_dislike:
        if ing in people[i+1].likes:
          check+=1
          break
    if check == 0:  
      p+=1
      for ing in people[i+1].likes:
        current_ing.append(ing)
      for ing in people[i+1].dislikes:
        cur_dislike.append(ing)

  print(p) 
  # print(current_ing)    
  print(len(people))
  # # print(people[0].likes)
  # for p in people:
  #   # print(len(p.likes))
  #   file.write(str(len(p.likes)))
  # # print(ingredients)
  j = current_ing[0]
  s = {j}
  for i in current_ing: 
    s.add(i)
  file = open("tree.txt","w")
  file.write(str(len(s))+' ')
  for i in s:
    file.write(i+' ')
    

if __name__ == '__main__':
  main()
# print (inp)

