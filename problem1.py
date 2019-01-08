import time
import random
print('-'*65)
print('Magic Eight Ball')
print()

question = input ('What is your question?')
print('Shaking!')
time.sleep(1)
print('...thinking...')
time.sleep(1)
print('...thinking...')
time.sleep(1)

choice = random.randint(1,6)

if choice == 1:
	print('No you will not.')
elif choice == 2:
	print('You most certainly will.')
elif choice == 3:
	print('How are you still on this question?')
elif choice == 4:
	print('Please move on to a new question!')
elif choice == 5:
	print('I BEG YOU TO ASK ME SOMETHING ELSE OR I WILL MALFUNCTION!')
else:
	print('I am not here. Please leave me a message after the beep. BEEEEEEEP!')

print('-'*65)