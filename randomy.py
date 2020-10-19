import numpy as np

nsteps = 100
nwalks = 500
draws = np.random.randint(0, 2, size =(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum(axis=1) # sums over 'rows'
print(steps)
print(walk)
#print(walk.min())
#print(walk.max())
#print(np.abs((walk) >= 10).argmax())  #True/False czy spelnia ten warunek >=10; True is a max value


