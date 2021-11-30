import plotly.graph_objects as go
import plotly.io as pi
import datetime
def light_xp(date, xp):
    dates = [date]
    if not len(xp):
        xp.append(0)

    while (len(dates) != len(xp)):
        dates.append(dates[-1] + datetime.timedelta(days = 1))
    xp_rev = dates[::-1]
    xp_upper = [i * 1.5 for i in xp]
    xp_lower = [i * 0.5 for i in xp]
    xp_lower.reverse()
    xp_upper += xp_lower
    fig = go.Figure()
    fig = go.Figure()
    # fig.template = 'plotly_white'
        # print(x)
    fig.add_trace(go.Scatter(
        x=dates+xp_rev,
        # y= (y1 + [1]*10) + (y1 + [-1]*10),
        y = xp_upper,
        fill='toself',
        fillcolor='#F1884D',
        line_color='rgba(255,255,255,0)',
        showlegend=False,
        name='Fair',
    ))
    fig.add_trace(go.Scatter(
        x=dates, y=xp,
        line_color='blue',
        # showlegend=False,
        # template = 'plotly_white',
        name='XP',
    ))
    fig.update_layout(template = 'plotly_white')
    fig.update_xaxes(color = '#F1884D')
    fig.update_yaxes(color = '#F1884D')
    fig.update_layout(xaxis_tickformat = '%d %b')
    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4)
    )
    code = pi.to_html(fig, full_html=False, config={'displayModeBar': False}, default_height="29.5vh",
    default_width="95%")
    return code
#   fig.show()
# light_xp(datetime.date.today(), [1, 3, 42, 5, 6, 2, 9])
