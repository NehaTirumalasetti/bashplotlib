#scratch.py
from bashplotlib.scatterplot import plot_scatter

x_coords = [-10,20,30]
y_coords = [-10,20,30]
width = 10
char = 'x'
color = 'default'
title = 'My Test Graph'
title_align = 'c'
ytitle = 'My y axis'
xtitle = 'My x axis'

plot_scatter(
    None,
    x_coords,
    y_coords,
    width,
    char,
    color,
    title,
    title_align,
    xtitle,
    ytitle)
