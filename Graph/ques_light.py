import plotly.express as px
import plotly.io as pi
import datetime
import pandas as pd
def light_ques(date, ques):
    dates = [date]
    if not len(ques):
        ques.append(0)
    p = [[date, ques[0]]]
    while (len(p) != len(ques)):
        p.append([(p[-1][0] + datetime.timedelta(days = 1)), ques[len(p) - 1]])
    df = pd.DataFrame(p)
    df.columns = ['Dates', 'Questions']
    graphs = px.line(df, x = 'Dates', y = 'Questions', template = 'plotly_white')
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
    code = pi.to_html(graphs, full_html=False, config={'displayModeBar':False}, default_height="29.5vh",
    default_width="95%")
    return code
#   fig.show()
# light_xp(datetime.date.today(), [1, 3, 42, 5, 6, 2, 9])
