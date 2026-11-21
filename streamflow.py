import numpy as np
import matplotlib.pyplot as plt
import csv


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    # open and read the CSV into a python list
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # this skips the header
        data_list = list(csv_reader)

    # use array to convert the Python list into a Numpy 2D array
    data = np.array(data_list)

    # slice the array: column 0 is the date, columns 1-5 are the five gauges
    dates = np.array(data[:, 0], dtype='datetime64')
    flows = data[:, 1:6].astype(float)  # all five gauge columns at once, as numbers
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    colors = ['orange', 'green', 'yellow', 'red', 'blue']

    # create the plot, one line per gauge (column i of flows is sites[i])
    plt.figure(figsize=(8, 5))
    for i in range(len(sites)):
        plt.plot(dates, flows[:, i], label=sites[i], color=colors[i])
    plt.title('Provo River Streamflow data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.xticks(rotation=45)

    # add legend with title as site numbers
    plt.legend(title='Site Numbers')
    plt.grid(True)
    plt.tight_layout()

    # save the figure in the project folder before showing it
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

    # show plot
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
