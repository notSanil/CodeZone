import plotly.express as px
import plotly.io as pi
import datetime
import pandas as pd
def dark_ques(date, ques):
    dates = [date]
    p = [[date, ques[0]]]
    while (len(dates) != len(ques)):
        p.append([(p[-1][0] + datetime.timedelta(days = 1)), ques[len(p) - 1]])
    df = pd.DataFrame(p)
    df.columns = ['Dates', 'Rank']
    graphs = px.line(df, x = 'Dates', y = 'Rank', template = 'plotly_dark')
    # px.color_continuous_scale='#F1884D'
    code = pi.to_html(graphs)
    return code
#   fig.show()
# light_xp(datetime.date.today(), [1, 3, 42, 5, 6, 2, 9])