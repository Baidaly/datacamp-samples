'''In this exercise, you're going to add the box_select tool to a figure and change the selected and non-selected circle glyph properties so that selected glyphs are red and non-selected glyphs are transparent blue.

You'll use the ColumnDataSource object of the Olympic Sprint dataset you made in the last exercise. It is provided to you with the name source.

After you have created the figure, be sure to experiment with the Box Select tool you added! As in previous exercises, you may have to scroll down to view the lower portion of the figure.'''

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label='Year', y_axis_label='Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle(source=source, x='Year', y='Time', selection_color='red', nonselection_alpha=0.1)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)
