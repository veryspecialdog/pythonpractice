phonebook ={'ann':6575,'bob':8982,'job':2598,'zoe':1225}
print(phonebook['bob'])

phonebook1 = {'ann':6575,'bob':8982,'job':2598,'zoe':1225,'ann':6585}
phonebook2 ={'john':9876,'mike':5603,'stan':6898,'eric':7898}

phonebook1.update(phonebook2)
print(phonebook1)

phonebook1 = {'ann':6575,'bob':8982,'joe':2598,'zoe':1225,'ann':6585}
del phonebook1['ann']
print(phonebook1)

print('ann' in phonebook1)

print(phonebook1.keys())

print('stan' in phonebook1.keys())

print(phonebook1.values())
phonebook1

phonebook1.items()
print(('stan',6898) in phonebook1.items())