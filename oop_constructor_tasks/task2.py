'''
Task 2: Create a class named vehicle, based on number of wheels, Presence of engine
and presense of sterring wheel assign weather its a car, motorbike and cycle (bike) 
do it with constructor
'''

class Vehicle:
    def __init__(self, num_wheels, has_engine, has_steering_wheel):
        self.num_wheel_var = num_wheels
        self.has_engine_var= has_engine
        self.has_steering_wheel_var = has_steering_wheel
        print(f'Metadata: \n wheels: {self.num_wheel_var}\n engine: {self.has_engine_var}\nsteering wheel: {self.has_steering_wheel_var}')
        print('=='*25)

    def classify(self):

        if self.num_wheel_var == 4 and self.has_engine_var==True and self.has_steering_wheel_var==True:
            return "car"
        elif self.num_wheel_var == 2 and self.has_engine_var==True and self.has_steering_wheel_var==False:
            return "motorbike"
        elif self.num_wheel_var == 2 and  self.has_engine_var==False and self.has_steering_wheel_var==False:
            return "cycle"
        else:
            return "unlnown"



vehicle1 = Vehicle(4, True, True)
print(vehicle1.classify())

vehicle2 = Vehicle(2, True, False)
print(vehicle2.classify())

vehicle3 = Vehicle(2, False, False)
print(vehicle3.classify())



