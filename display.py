"""
http://www.pygal.org/en/latest/documentation/index.html
"""
import pygal


class PyGal(object):
    def bar_char(self, id, name, data, name2=None, data2=None):
        try:
            bar_chart = pygal.Bar()  # Then create a bar graph object
            bar_chart.add(name, data)  # Add some values
            bar_chart.title = "The Employee Sales"
            bar_chart.x_labels = id
            if name2 is not None:
                bar_chart.add(name2, data2)
                bar_chart.title = "The Employee Sales vs The Employee Salary"
                bar_chart.x_labels = id
            bar_chart.render_in_browser()
        except Exception as err:
            print("The exception is: Invalid Data", err)
