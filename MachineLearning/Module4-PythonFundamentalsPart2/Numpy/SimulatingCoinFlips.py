# A simply program to simulate coin flips and gain an introduction to the numpy library

import numpy
# n represents the number of flips per test
# p represents the probability (for 0.5, probability of a success is 50%)
# Size repesents the number of times the experiment is run
# Outputs the number of successes in 100 flips, 500 times
print(numpy.random.binomial(n = 100, p = 0.5, size = 500))
