
mylist = []
for x in range (6):
    number = random.sample(1, 60)


    mylist.append(number)
    mylist.sort()

if x == 3:
    import random
    from playsound import playsound
    import multiprocessing
    p = multiprocessing.Process(target=playsound, args=('stimela.mp3',))



print(mylist)
