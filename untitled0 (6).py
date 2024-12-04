# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16NmGMWf_6p3Ep4GT7Q5SPCNKuemur5YC
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sinus(x)', color='blue')


plt.title('Sinus Funksiyasining Grafiki')
plt.xlabel('X qiymatlari')
plt.ylabel('Y qiymatlari')

plt.grid(True)
plt.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.uniform(0, 10, 50)
y = np.random.uniform(0, 10, 50)
plt.scatter(x, y, color='blue', label='Nuqtalar')
plt.title('Tasodifiy Nuqtalar Scatter Grafiki')
plt.xlabel('X qiymatlari')
plt.ylabel('Y qiymatlari')
plt.grid(True)
plt.legend()
plt.show()