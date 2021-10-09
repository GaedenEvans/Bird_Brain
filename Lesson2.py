from BirdBrain import Finch
bird = Finch()

'''
print('excercise1') 
print("Distance: ", bird.getDistance())

print('excercise2')
bird.resetEncoders()
bird.setMove('F',16,100)
print("Distance: = ", bird.getEncoder('R'))

print('excercise3')
print(float(bird.getDistance())) 

print('excerise4')
currentDistance = bird.getDistance()
print(currentDistance)
print(2*currentDistance)
print(4*currentDistance)
'''
print('excercise5')
rightSensor = bird.getLight('R')
leftSensor = bird.getLight('L')
difference = rightSensor - leftSensor
print('leftSensor = '+ str(leftSensor))
print('rightSensor = '+ str(rightSensor))
print('difference: '+ str(difference))
mean = leftSensor + rightSensor/ 2
print('mean: '+ str(mean))

