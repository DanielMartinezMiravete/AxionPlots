import matplotlib.pyplot as plt
import matplotlib as mpl
from XPlotter import BasePlot, ExPltItem
from database import *
from classes import *

class Background:
    ListOfPlotTypes = {'large_panorama', 'panorama', 'LSWexps', 'haloscopes', 'haloscopes_zoom',
                       'haloscopes_radeszoom', 'helioscopes'}

    def __init__(self, plottype="large_panorama"):
        # print(projections, showplot, saveplot)

        if plottype not in self.ListOfPlotTypes:
            print('ERROR: ' + plottype + ' not a known plot type')
            exit()

        figx = 6.5
        figy = 5
        ymin = 1e-18
        ymax = 1e-4
        xmin = 1e-11
        xmax = 1e9
        ticksopt_x = 'dense'
        ticksopt_y = 'normal'
        labelx = '$m_a$ (eV)'
        labely = r'$|g_{a\gamma}|$ (GeV$^{-1}$)'

        if plottype == "panorama":
            figx = 6.5
            figy = 6
            ymin = 1e-17
            ymax = 1e-6
            xmin = 1e-9
            xmax = 10
            ticksopt_x = 'normal'
            ticksopt_y = 'normal'

        if plottype == "helioscopes":
            figx = 8
            figy = 6
            ymin = 1e-13
            ymax = 1e-8
            xmin = 1e-11
            xmax = 1
            ticksopt_x = 'normal'
            ticksopt_y = 'normal'

        if plottype == "LSWexps":
            figx = 6.5
            figy = 5
            ymin = 1e-13
            ymax = 1e-6
            xmin = 1e-10
            xmax = 1e-2
            ticksopt_x = 'normal'
            ticksopt_y = 'normal'

        if plottype in ["haloscopes", "haloscopes_zoom", "haloscopes_radeszoom"]:
            figx = 8
            figy = 5
            ymin = 1e-1
            ymax = 1e3
            xmin = 1e-9
            xmax = 1
            if plottype in ["haloscopes_zoom"]:
                xmin = 3e-7
                xmax = 3e-2
            if plottype in ["haloscopes_radeszoom"]:
                xmin = 3.4e-5
                xmax = 4.5e-5
            ticksopt_x = 'normal'
            ticksopt_y = 'normal'
            labely = r'$|C_{a\gamma}|\tilde{\rho}_a^{1/2}$'

        self.axplot = BasePlot(xlab=labelx, ylab=labely,
                               figsizex=figx, figsizey=figy,
                               y_min=ymin, y_max=ymax,
                               x_min=xmin, x_max=xmax,
                               ticksopt_x=ticksopt_x, ticksopt_y=ticksopt_y)
        