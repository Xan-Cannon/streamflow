import numpy as np
import matplotlib.pyplot as plt
import csv

# open and read the CSV into to make python list
with open('June-2021-Provo-River-Streamflow-Rates.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # this skips the header
    data_list = list(csv_reader)

# use array to convert the Python list into a Numpy 2D
data = np.array(data_list)

# slice the array
x = data[:, 0]
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

x_dates = np.array(x, dtype='datetime64')

# create the plot
plt.figure(figsize=(8, 5))
plt.plot(x_dates, y_1, label='10163000', color='orange')
plt.plot(x_dates, y_2, label='10155200', color='green')
plt.plot(x_dates, y_3, label='10155500', color='yellow')
plt.plot(x_dates, y_4, label='10154200', color='red')
plt.plot(x_dates, y_5, label='10155000', color='blue')
plt.title('Provo River Streamflow data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.xticks(rotation=45)

# add legend with title as site numbers
plt.legend(title='Site Numbers')
plt.grid(True)
plt.tight_layout()

# show plot
plt.show()
