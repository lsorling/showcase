import random

def generate():
  generated = ""
  for count in range(10):
    y = random.choice('01234567890~!@#$%^&*(abcdefghijklmnopqrstuvwxyz')
    #print(y)
    generated = generated + y
  #print(generated)
  return generated


print(generate())
