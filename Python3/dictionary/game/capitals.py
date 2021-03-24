lookup = {
'Japan':'Tokyo',
'USA':'Washington DC',
'Singapore': 'Singapore',
'Thailand': 'Bangkok',
'China': 'Beijing',
'Russia': 'Moscow',
'Nigeria': 'Abuja',
'Malaysia': 'Kuala Lumpur',
'South Korea': 'Seoul',
'Indonesia': 'Jakarta'}

#1 tip
countries = list(lookup.keys())
#print(countries)

#2 tip
import random
selected = random.sample(countries, 5)
#print(selected)


score = 0
print("In this game, you are going to answer 5 questions.")
for count in range(5):
  select = selected[count]
  question = "What is the capital of " + select + "? "
  reply = input(question)
  expected = lookup[select]
  if reply.lower() == expected.lower():
    score = score + 1

print('Game Over')
print('Your score is', score, '/5')
if score == 5:
  print('Well Done!')
