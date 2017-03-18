"""
http://www.pygal.org/en/latest/documentation/index.html
"""
import pygal  # First import pygal


class PyGal(object):
    def bar_char(self, name, data):
        bar_chart = pygal.Bar()  # Then create a bar graph object
        bar_chart.add(name, data)  # Add some values
        bar_chart.render_in_browser()

# """
# bar_chart = pygal.Bar()
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
# bar_chart.render()
# """
