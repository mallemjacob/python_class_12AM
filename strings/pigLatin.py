# input
# 'My name is AL SWEIGART and I am 4,000 years old.'

# output
# 'Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.'


# Rule-1: If a word begins with a vowel, the word yay is added to the end of it.
# vowels = a,e,i,o,u,y

# in --> in + yay ---> inyay

# Rule-2: If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay.

# chair --> air + ch + ay --> airchay

# hi all welcome to my class

print('Enter a text to convert into pig Latin: ')

text = input()

final_str = ''

vowels = ['a','e','i','o','u','y']

splitted_text = text.split()



# for word in splitted_text: # My
#   if word[0] in vowels:
#     final_str = final_str + word + 'yay'
#   else:
#     for letter in word:
#       if letter not in vowels:
#         consonant_cluster = consonant_cluster + letter
#       else:
#         break
#     final_str = final_str + word[word.index(consonant_cluster[-1]) + 1:] + consonant_cluster + 'ay'
            

# print(final_str)        
# print(consonant_cluster)
# print(word)

# splitted_text
# ['My', 'name', 'is', 'AL', 'SWEIGART', 'and', 'I', 'am', '4,000', 'years', 'old.']


for word in splitted_text: # My
  if splitted_text.index(word) == splitted_text[len(splitted_text) - 1]:
    final_str = final_str + word[:len(word) - 1] + 'ay' + word[-1]
  if word[0].isdecimal():
    final_str = final_str + word + ' '
  elif word[0].lower() in vowels:
    if word.isupper():
      final_str = final_str + word + 'YAY '
    else:
      final_str = final_str + word + 'yay '
  else:
    consonant_cluster = ''
    remaining_part = ''
    
    lower_word = word.lower()
    
    
    for i in range(len(lower_word)):
      if lower_word[i] not in vowels:
        consonant_cluster = consonant_cluster + lower_word[i]
      else:
        remaining_part = remaining_part + lower_word[i:]
        break
    
    if word.isupper():
      final_str = final_str + remaining_part.upper() + consonant_cluster.upper() + 'AY '
    else:
      final_str = final_str + remaining_part + consonant_cluster + 'ay '
      

print(final_str)



# word = 'oldyay.'
# alpha = ''
# non_alpha = ''

# for letter in word:
#   if letter.isalpha():
#     alpha = alpha + letter
#   else:
#     non_alpha = non_alpha + letter

# print(f"Alpha: {alpha}")
# print(f"Non ALpha: {non_alpha}")