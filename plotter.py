#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['Airfish', 'Seren', 'Move-ez', 'MAVERICK', 'Pandawacakra', 'The Zero Heroes', 'HKU-ARG', 'FlyLite', 'NI Aerospace', 'Waitless Technology Group']

df = pd.read_csv('video_data.csv')
time = np.arange(df['Seren'].size)
for name in names:
    print(df[name])
    plt.plot(time,df[name],'--+')

plt.show()
