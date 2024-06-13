import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header=True)
speed = taxi[:, 7]/(taxi[:, 8]/3600)

#Mean speed
mean_speed = speed.mean()
print("This is the mean speed: ", mean_speed)

#rides in february
rides_feb = taxi[taxi[:,1] == 2,1]
print("These are the total # of rides in february: ",rides_feb.shape[0])

#Tips greater than 50
print("Tips greater than $50: ", taxi[taxi[:, -3] > 50, -3].shape[0])

#Number of drops to JFK airport
print("# of drops to JFK airport: ", taxi[taxi[:, 6] == 2,6].shape[0])