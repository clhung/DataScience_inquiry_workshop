import numpy as np
from bokeh.io import output_notebook
output_notebook()
from bokeh.layouts import gridplot, row, widgetbox
from bokeh.models import CustomJS, Slider
from bokeh.models import Label, LabelSet
from bokeh.plotting import figure, output_file, show, ColumnDataSource

def lm1_interactive(x_p,y_p):

    x = np.linspace(min(x_p),max(x_p),len(y_p))
    y = x
    res =y-y_p
    rmse = x

    source = ColumnDataSource(data=dict(x=x, y=y, x_p=x_p, y_p=y_p, res=res, rmse=rmse))

    plot = figure(title="Model 1", x_axis_label=x_p.name, y_axis_label=y_p.name,
                 plot_width=450, plot_height=350)

    plot.circle(x_p, y_p, size=3, fill_alpha=0.6)
    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6, line_color="#636363")

    resplot = figure(title="Residual", x_axis_label=x_p.name, y_axis_label='Prediction - Data',
                    plot_width=450, plot_height=250)
    resplot.circle('x_p','res', source=source, color="#fdbb84",size=4, fill_alpha=0.6)
    resplot.line([min(x_p),max(x_p)],[0,0], line_width=3, line_alpha=0.8, line_dash="dashed", line_color="#bdbdbd")
    

    callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var a = intercept.value;
        var b = slope.value;
        var x = data['x'];
        var y = data['y'];
        var res = data['res'];
        var x_p = data['x_p'];
        var y_p = data['y_p'];
        for (var i = 0; i < x.length; i++) {
            y[i] = a + b*x[i];
            res[i] = a + b*x_p[i] - y_p[i];
        }
        source.change.emit();
    """)

    intercept_slider = Slider(start=-50, end=50, value=0, step=.01,
                        title="Intercept (a)", callback=callback)
    callback.args["intercept"] = intercept_slider

    slope_slider = Slider(start=-10, end=10, value=1, step=.01,
                         title="Slope (b)", callback=callback)
    callback.args["slope"] = slope_slider


    layout = gridplot([
        [plot,
        widgetbox(intercept_slider, slope_slider)],
        [resplot,None]]
    )

    # show the results
    show(layout)

