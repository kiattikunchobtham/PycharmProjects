import numpy as np
import pandas as pd
import numpy as np

np.random.seed(1)
data = np.random.normal(100, 50, size=(10,))
from bayespy.nodes import GaussianARD, Gamma
mu = GaussianARD(0, 1e-6)
tau = Gamma(1e-6, 1e-6)
print(tau)
y = GaussianARD(mu, tau, plates=(10,))

y.observe(data)
from bayespy.inference import VB
Q = VB(mu, tau, y)
Q.update(repeat=20)

import bayespy.plot as bpplt
bpplt.pyplot.subplot(2, 1, 1)
bpplt.pdf(mu, np.linspace(-10, 200, num=100), color='k', name=r'\mu')
bpplt.pyplot.subplot(2, 1, 2)
bpplt.pdf(tau, np.linspace(1e-6, 1, num=100), color='k', name=r'\tau')
bpplt.pyplot.tight_layout()
bpplt.pyplot.show()