import numpy as np
from bokeh.io import output_notebook
output_notebook()
from bokeh.layouts import gridplot, row, widgetbox
from bokeh.plotting import figure,  show
from bokeh.models import Label
from sklearn.metrics import mean_squared_error

def lm_plot(x_train,y_train,x_test,y_test,lm_model):

    x = np.linspace(min(x_train),max(x_train),len(y_train))
    i=0
    y=lm_model.intercept_
    y_pred=lm_model.intercept_
    while i<len(lm_model.coef_):
        y+=lm_model.coef_[i]*x**(i+1)
        y_pred+=lm_model.coef_[i]*x_test**(i+1)
        i+=1
    mse=np.around(mean_squared_error(y_test, y_pred),decimals=2)

    plot = figure(title="Model Validation",x_axis_label=x_train.name, y_axis_label=y_train.name,
                 plot_width=450, plot_height=350)
    plot.circle(x_train, y_train, size=3, fill_alpha=0.6,color="#bdbdbd")
    plot.line(x,y, line_width=3, line_alpha=0.8, line_color="#fdbb84")
    
    plot.circle(x_test, y_test, size=4, fill_alpha=0.8,color="#de2d26")

    citation = Label(x=30, y=200, x_units='screen', y_units='screen',
                 text='MSE = '+mse.astype(str))
    
    plot.add_layout(citation)
    show(plot)

