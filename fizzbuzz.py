def fizzbuzz():
    for i in range(1,101):
        if not i % 3 == 0:
            print('fizz')
        elif not i % 5 == 0:
            print('buzz')
        else:
            print(i)

