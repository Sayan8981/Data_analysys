
#Code #1: Scatter Markers
#To create scatter circle markers, circle() method is used.

from bokeh.plotting import figure,output_notebook, show


class plotting_design:

    def plotting(self):
        #output_notebook(notebook_type=txt)
        plot=figure(plot_width=400,plot_height=400)
        x=[1,3,6,7]
        y=[4,7,5,2]
        plot.circle(x,y,size=10,color="navy",alpha=1)
        plot.legend.click_policy='hide'
        show(plot)

plotting_design().plotting()