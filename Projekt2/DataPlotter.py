import numpy as np
import matplotlib.pyplot as plt
import csv, sys
import unittest


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

    def __str__(self):
        return str(self.data)


class DataPlotter:  # features -> alcohol dict indicates indices for each alcohol string
    #           -> colors table are for different colors of plot
    #             -> data is raw csv data  (with one collumn of headers) for all countries
    def __init__(self, csv_handler):
        self.data = csv_handler.get_data()
        self.colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink',
                       'tab:gray', 'tab:olive', 'tab:cyan']
        self.alcohol = {'Beer': 1, 'Spirit Drinks': 2, 'Wine': 3, 'Pure Alcohol (litres)': 4}

    def show_beverage(self, bev_type="none", *args):

        if (bev_type == "none") | (len(args) < 1) | (len(args) > 10):
            print("You did not give sufficient/correct parameters to printing method,check your choice once again")
            return 1

        for country in args:
            if country not in list(map(lambda x: x[0], self.data)):
                print("There is no data about " + country + ".")

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

        plt.xticks(arguments, labels, rotation=60)
        plt.tight_layout()
        plt.title(bev_type + " Servings per person in each country")
        plt.show()
        return 0

    def top_x_countries(self, x, bev_type='none'):

        if (bev_type == 'none') | (bev_type not in self.alcohol.keys()) | (x < 1):
            print("Not correct beverage type selected: " + bev_type + "\t(Maybe check your spelling?)")
            return 1

        wanted = self.data[1:]
        wanted.sort(key=lambda x: float(x[self.alcohol.get(bev_type)]), reverse=True)
        names = []
        for index in range(0, x):
            names.append(wanted[index][0])
            index += 1

        self.show_beverage(bev_type, *names)
        return 0

    def bot_x_countries(self, x, bev_type='none'):

        if ( bev_type == 'none' ) | (bev_type not in self.alcohol.keys()) | (x < 1):
            print("Not correct beverage type selected: " + bev_type + "\t(Maybe check your spelling?)")
            return 1

        wanted = self.data[1:]
        wanted.sort(key=lambda x: float(x[self.alcohol.get(bev_type)]))
        names = []
        for index in range(0, x):
            names.append(wanted[index][0])
            index += 1

        self.show_beverage(bev_type, *names)
        return 0


if len(sys.argv) < 2:
    print("Give at least one csv file to parse")
    exit(1)

csvka = CSVhandler(sys.argv[1])
data_plot = DataPlotter(csvka)


data_plot.show_beverage("Spirit Drinks", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")
data_plot.show_beverage("Beer", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")
data_plot.show_beverage("Wine", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia", "Nibylandia")
data_plot.show_beverage("Pure Alcohol (litres)", "Albania", "Poland", "Norway", "USA", "Zimbabwe", "Etiopia")


data_plot.top_x_countries(10, "Pure Alcohol (litres)")
data_plot.bot_x_countries(10, "Beer")



class MyTests(unittest.TestCase):

    def test_names(self):
        self.assertEqual(data_plot.show_beverage("Pure Alcohol (litres)", "Albania", "Poland", "Etiopia"), 0)
        self.assertEqual(data_plot.show_beverage("Pure Alcohol (litry)"), 1)

    def test_quantity(self):
        self.assertEqual(data_plot.show_beverage("Wine"), 1)
        self.assertEqual(data_plot.show_beverage("Wine", "Poland"), 0)

    def test_top_number(self):
        self.assertEqual(data_plot.top_x_countries(-1, "Wine"), 1)
        self.assertEqual(data_plot.top_x_countries(0, "Wine"), 1)
        self.assertEqual(data_plot.top_x_countries(1, "Wine"), 0)


if __name__ == "__main__":
    unittest.main(argv=['ignore-first-arg'])
