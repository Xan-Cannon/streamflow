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


# AI (Claude) helped write summarize(). What the code does:
# - Loops over each gauge (each column of flows).
# - np.max / np.min / np.mean find the max, min, and average flow in that column.
# - np.argmax gives the ROW where the max happens, so dates[row] is when it happened.
# - f-strings with widths (like :10.1f) line the numbers up into columns.
# - The same numbers are written to streamflow_summary.csv with open() and write().
def summarize(dates, flows, sites):
    """Print a table of max, date of max, min, and average flow for each gauge, and save it to streamflow_summary.csv."""
    # Excel check for gauge 10163000: MAX = 131.0 cfs, AVERAGE = 56.95 cfs (matches this program)

    header = f"{'Gauge':<10}{'Max (cfs)':>12}   {'Date of max':<18}{'Min (cfs)':>12}{'Avg (cfs)':>12}"
    print(header)

    # write the CSV header row
    out_file = open("streamflow_summary.csv", "w")
    out_file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

    for i in range(len(sites)):
        column = flows[:, i]                  # all readings for this gauge
        max_flow = np.max(column)
        min_flow = np.min(column)
        avg_flow = np.mean(column)
        max_row = np.argmax(column)           # row number of the maximum
        # turn the date into text like 2021-06-05 14:30
        max_date = str(dates[max_row]).replace("T", " ")[:16]

        # print one lined-up row to the terminal
        print(f"{sites[i]:<10}{max_flow:12.1f}   {max_date:<18}{min_flow:12.1f}{avg_flow:12.1f}")
        # save the same row to the CSV file
        out_file.write(f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.2f}\n")

    out_file.close()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
