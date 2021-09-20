import random

name = 'Bob'
question = input('Ask The 8 Ball a question: ')
answer = ''
random_number = random.randint(1, 11)
print(random_number)
if random_number == 1:
  answer = 'Yes - defidently.'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = "Very Doubtful."
elif random_number == 10:
  answer = 'I do not know.'
elif random_number == 11:
  answer = "sorry., system 32 has been deleted."
else:
  answer = 'Error.'

print(name + " Asks: " + question)
print("Magic 8 Ball's answer: " + answer)
