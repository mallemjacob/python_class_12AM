# input
# 'My name is AL SWEIGART and I am 4,000 years old.'

# output
# 'Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.'


# Rule-1: If a word begins with a vowel, the word yay is added to the end of it.
# vowels = a,e,i,o,u,y

# is --> is + yay ---> isyay

# Rule-2: If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay.

# chair --> air + ch + ay --> airchay

# hi all welcome to my class



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



print('Enter a text to convert into pig Latin: ')

text = input()

final_str = ''

vowels = ['a','e','i','o','u','y']

splitted_text = text.split() # []


for word in splitted_text: # My
  
  # Last word
  if splitted_text.index(word) == len(splitted_text) - 1:
    last_char = word[-1]
    word = word[:len(word) - 1]
  
  # Decimal
  if word[0].isdecimal():
    final_str = final_str + word + ' '
  
  # Vowels
  elif word[0].lower() in vowels:
    if word.isupper() and len(word) > 1:
      final_str = final_str + word + 'YAY '
    else:
      final_str = final_str + word + 'yay '
  
  # consonants
  else:
    consonant_cluster = ''
    remaining_part = ''
    
    lower_word = word.lower() # name
    
    # name
    for i in range(len(lower_word)):
      if lower_word[i] not in vowels:
        consonant_cluster = consonant_cluster + lower_word[i]
      else:
        remaining_part = remaining_part + lower_word[i:]
        break
    
    if word.isupper():
      final_str = final_str + remaining_part.upper() + consonant_cluster.upper() + 'AY '
    elif word[0].isupper():
      final_str = final_str + (remaining_part + consonant_cluster + 'ay').capitalize() + ' '
    else:
      final_str = final_str + remaining_part + consonant_cluster + 'ay '
      

print(final_str.strip() + last_char)



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