import numpy as np
import matplotlib.pyplot as plt
import csv, sys


class CSVhandler:  # usage -> this gets data from given csv path in constructor
    # features -> you can add them when you want to add another file to analysis
    def __init__(self, filename):
        try:
            with open(filename, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                self.data = []
                for line in csv_reader:
                    self.data.append(line)

        except IOError:
            print("Error opening CSV file")
            exit(1)

    def get_data(self):
        return self.data

    def __add__(self, other):
        self.data += other.data


class DataPlotter:

    def __init__(self, csv_handler):
        self.data = csv_handler.get_data()
        self.colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink',
                       'tab:gray', 'tab:olive', 'tab:cyan']
        self.alcohol = {'Beer': 1, 'Spirit Drinks': 2, 'Wine': 3, 'Pure Alcohol (litres)': 4}

    def show_beverage(self, bev_type="none", *args):
        if (bev_type == "none") | (len(args) < 1):
            print("You did not give sufficient parameters to printing method")
            return

        plotted = list(filter(lambda x: x[0] in args, self.data))
        plotted.sort(key=lambda x: float(x[self.alcohol.get(bev_type)]))

        labels = list(map(lambda x: x[0], plotted))
        values = list(map(lambda x: float(x[self.alcohol.get(bev_type)]) if (bev_type == 'Pure Alcohol (litres)')
        else int(x[self.alcohol.get(bev_type)]),
                          plotted))
        arguments = np.arange(1, len(labels) + 1, 1)

        bar_list = plt.bar(arguments, values, align='center')
        i = 0
        for bar in bar_list:
            bar.set_color(self.colors[i % len(self.colors)])
            i += 1

        ax = plt.gca()
        ax.grid(True, axis='y')
        ax.set_axisbelow(True)
        ax.autoscale(enable=True, axis='both')

        for index, value in enumerate(values):
            ax.text(index + 1, value * 1.05, str(value), ha='center')

        plt.xticks(arguments, labels, rotation=90)
        plt.tight_layout()
        plt.title(bev_type + " Servings per person in each country")
        plt.show()
        return

    def top_x_countries(self, x, bev_type='none'):
        wanted = self.data[1:]
        wanted.sort(key=lambda x: float(x[self.alcohol.get(bev_type)]), reverse=True)
        names = []
        for index in range(0, x):
            names.append(wanted[index][0])
            index += 1

        self.show_beverage(bev_type, *names)
        return


data_plot = DataPlotter(CSVhandler(sys.argv[1]))

data_plot.show_beverage("Spirit Drinks", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")
data_plot.show_beverage("Beer", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")
data_plot.show_beverage("Wine", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")
data_plot.show_beverage("Pure Alcohol (litres)", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")


data_plot.top_x_countries(10, "Wine")
