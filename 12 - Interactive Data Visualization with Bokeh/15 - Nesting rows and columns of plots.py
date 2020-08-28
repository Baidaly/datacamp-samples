'''You can create nested layouts of plots by combining row and column layouts. In this exercise, you'll make a 3-plot layout in two rows using the auto-mpg data set. Three plots have been created for you of average mpg vs year (avg_mpg), mpg vs hp (mpg_hp), and mpg vs weight (mpg_weight).

Your job is to use the row() and column() functions to make a two-row layout where the first row will have only the average mpg vs year plot and the second row will have mpg vs hp and mpg vs weight plots as columns.

By using the sizing_mode argument, you can scale the widths to fill the whole figure.'''

# Import column and row from bokeh.layouts
from bokeh.layouts import column, row

# Make a row layout that will be used as the second row: row2
row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a column layout that includes the above row layout: layout
layout = column([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)