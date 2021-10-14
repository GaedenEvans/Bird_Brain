from BirdBrain import Finch
from time import sleep

bird = Finch()

print('Excercise1')
bird.setMotors(50,50)
sleep(1)
bird.stopAll()
bird.setMotors(50,-50)
sleep(1)
bird.stopAll()
