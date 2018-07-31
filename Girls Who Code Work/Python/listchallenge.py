from random import *

appetizers = ['salad','soup','bread']
main = ['pasta','pizza','meat']
desserts = ['cake','ice cream','milkshake']

response = input('Would you like something to eat?(Y/N)')
while response !='N':
    if response == 'Y':
        aRandomIndex = randint(0, len(appetizers)-1)
        print(appetizers[aRandomIndex])

        aRandomIndex = randint(0, len(main)-1)
        print(main[aRandomIndex])

        aRandomIndex = randint(0, len(desserts)-1)
        print(desserts[aRandomIndex])
        response = input('Another meal?(Y/N)')
    else:
        print('{} is an invalid input.'.format(response))
        response = input('Try again?(Y/N)')
else:
    exit()
