import plotly.express as px
import plotly.io as pi
import datetime
import pandas as pd

def light_rank(date, rank):
    dates = [date]
    p = [[date, rank[0]]]
    while (len(p) != len(rank)):
        p.append([(p[-1][0] + datetime.timedelta(days = 1)), rank[len(p) - 1]])
    df = pd.DataFrame(p)
    df.columns = ['Dates', 'Rank']
    graphs = px.area(df, x = "Dates", y = 'Rank', template = 'plotly_white')
    graphs.update_xaxes(color = '#F1884D')
    graphs.update_yaxes(color = '#F1884D')
    graphs.update_layout(xaxis_tickformat = '%d %b')
    graphs.update_layout(margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4)
    )
    # px.color_continuous_scale='#F1884D'
    code = pi.to_html(graphs, full_html=False, config={'displayModeBar': False}, default_height="29.5vh",
    default_width="95%")
    return code
#   fig.show()
# light_xp(datetime.date.today(), [1, 3, 42, 5, 6, 2, 9])
