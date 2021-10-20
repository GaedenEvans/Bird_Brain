from BirdBrain import Finch
from time import sleep

bird = Finch()
'''
print('Excercise1')
bird.setMotors(50,50)
sleep(1)
bird.stopAll()
bird.setMotors(50,-50)
sleep(1)
bird.stopAll()

print('Excercise2')
left = int(input("Amount of speed left motor (0-100)?"))
right = int(input("Amount of speed right motor (0-100)?"))
bird.setMotors(left,right)
sleep(3)
bird.stopAll()

print('Excercise3')
bird.setMotors(50,0)
sleep(1)
bird.setMotors(0,50)
sleep(4)
bird.setMotors(50,0)
sleep(4)
bird.stopAll()

print('Excercise4')
color = input("Please enter a letter: ")
if (color == 'g'):
    bird.setBeak(0,100,0)
else:
    print('Sorry, that is not my favorite letter!')
sleep(1)
bird.stopAll()

print('Excercise5')
letter = input("Please enter a letter r or l: ! ")
if(letter == 'r'):
               bird.setMove('F',10,100)
               bird.setTurn('R',90,100)
else:
    bird.setMove('F',10,100)
    bird.setTurn('L',90,100)
sleep(1)
bird.stopAll()

print('Excercise6')
userResponse = input('Please enter a speed (-100 to 100): ')
speed = int(userResponse)
if (speed >= -100) and (speed <= 100):
    bird.setMotors(speed,speed)
    sleep(1)
    bird.stop()
else:
    print(" That speed is not valid! ")
'''
print('Excercise7')
right = input('Please enter a speed for the right wheel (0 to 50): ')
speed2 = int(right)
left = input('Please enter a speed for the left wheel (0 to 50): ')
speed = int(left)
if (speed == 0 - 50) and (speed2 == 0 - 50):
    bird.setMotors(speed,speed2 + speed2)
    sleep(1)
    bird.stop()
else:
    print(" That speed is not valid! ")





























    



