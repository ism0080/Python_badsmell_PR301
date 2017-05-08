"""
http://www.pygal.org/en/latest/documentation/index.html
"""
import pygal


class PyGal(object):
    # DUPLICATED CODE SMELL
    def bar_char(self, id, dictionary):
        try:
            bar_chart = pygal.Bar(title='Employee Sales', x_title='Employee ID\'s', y_title='Sales')
            for key in dictionary:
                bar_chart.add(key, dictionary[key])  # Add some values
            bar_chart.x_labels = id
            # bar_chart.render_in_browser()
        except Exception as err:
            print("The exception is: Invalid Data", err)
