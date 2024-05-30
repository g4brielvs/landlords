from bokeh.models import ColumnDataSource, FactorRange, NumeralTickFormatter
from bokeh.plotting import figure, show, output_notebook
from bokeh.transform import factor_cmap


from bokeh.palettes import Category20_20

output_notebook()


def plot_vbar(data: dict, title: str):
    """
    Creates and displays a vertical bar chart using Bokeh.

    Parameters
    ----------
    data : dict
        A dictionary where keys are the x-axis categories and values are the y-axis values.
    title : str
        The title of the plot.
    """

    x = list(data.keys())
    y = list(data.values())

    p = figure(
        x_range=FactorRange(*x),
        title=title,
    )
    p.vbar(
        x="x",
        top="y",
        width=0.8,
        source=ColumnDataSource(data=dict(x=x, y=y)),
        fill_color=factor_cmap(
            "x",
            palette=Category20_20,
            factors=["A", "B", "C", "I"],
            start=1,
            end=2,
        ),
    )

    p.y_range.start = 0
    p.x_range.range_padding = 0.1

    p.xgrid.grid_line_color = None
    p.yaxis.formatter = NumeralTickFormatter(format="0")

    show(p)
