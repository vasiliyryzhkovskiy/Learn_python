import random

words_bank = (
   'автострада', 'бензин', 'инопланетянин', 'самолет',
   'библиотека', 'шайба', 'олимпиада', 'весна',
)


secret_word = random.choice(words_bank)

print(secret_word)

gamer_word = ['*'] * len(secret_word)


print(gamer_word)
print(''.join(gamer_word))