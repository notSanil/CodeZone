import datetime
import matplotlib.pyplot as plt 
import mpld3
import pandas as pd
import numpy as np
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
plt.switch_backend('agg')


def select_even(seq, num):
    length = float(len(seq))
    res = []
    for i in range(num):
        res.append(seq[int(np.ceil(i * length / num))])
    return res


def questions_graph(ques, date):
    """
    Generates graph for number of questions solved per day, takes as input a list of questions solved each
    day
    """
    dates = [date]
    print(len(dates), len(ques))
    while not (len(dates) >= len(ques)):
        
        dates.append(date + datetime.timedelta(days= len(dates)))
    print(dates)
    a = plt.stackplot(dates, ques, colors=['#001333'])

    ticks = select_even(dates, min(5, len(dates)))
    
    plt.xlabel("Date", color='#F1884D')
    plt.xticks(ticks)
    print(ticks)
    plt.title("Questions solved per day")
    plt.grid(True, color='#EFF3FF')# set graph grid color and control its pres
    ax = plt.axes()
    ax.set_facecolor('white') #set graph bg-color
    b = a[0].figure
    b.set_figwidth((screensize[0] * 0.3 * 1)/100.0)
    b.set_figheight((screensize[1] * 0.54 * 0.5)/100.0)
    
    code = mpld3.fig_to_html(b)
    
    return code


def rank_graph(rank, date):
    """
    Generates the graph for the rank change per day, takes as input the rank list
    """
    dates_ = [date]
    while not (len(dates_) >= len(rank)):
        dates_.append(date + datetime.timedelta(days= len(dates_)))    
    
    a = plt.plot(dates_, rank, color = '#F1884D', linewidth = 5)
    plt.xlabel("Date")
    plt.title("Rank Change")
    ticks = select_even(dates_, min(5, len(dates_)))
    plt.xticks(ticks)
    plt.grid(True, color='#EFF3FF')
    
    ax = plt.axes()
    ax.set_facecolor('white')
    b = a[0].figure
    b.set_figwidth((screensize[0] * 0.3 * 1)/100.0)
    b.set_figheight((screensize[1] * 0.54 * 0.5)/100.0)
    
    code = mpld3.fig_to_html(b)
    print(code)
    
    return code


def xp_graph(xp, date):
    """
    Generates the graph for the xp change
    """
    dates_ = [date]
    while not (len(dates_) >= len(xp)):
        dates_.append(date + datetime.timedelta(days = len(dates_)))
    dates_ = np.array(dates_)
    df = pd.DataFrame(xp)
    fig, ax = plt.subplots()
    ticks = select_even(dates_, min(5, len(dates_)))
    plt.xticks(ticks)
    plt.title("XP change per day")
    ax.grid(True, alpha=0.3, color='#EFF3FF')
    for key, val in df.iteritems():
        l, = ax.plot(dates_, val.values, color='#001333', linewidth = 5)
        # ax.legend()
        ax.set_xlabel("Date")
        ax.fill_between(dates_,
                        val.values * .5, val.values * 1.5,
                        color='#F1884D', alpha=.4)
        ax.set_facecolor('white')
    # b = a[0].figure
    fig.set_figwidth((screensize[0] * 0.3 * 1)/100.0)
    fig.set_figheight((screensize[1] * 0.54 * 0.5)/100.0)
    
    code = mpld3.fig_to_html(fig)
    return code
