paragraph = """
Commentary: My walk around Singapore was a step outside my comfort zone -
and I’m all the better for it.
"""

found = {}
target = 'aeiou'
for letter in target:
  print(letter, paragraph.count(letter))
  found[letter] = paragraph.count(letter)

print(found)


# what if we change the question to for every symbol/letter you found in the
# paragraph, keep a count
