import datetime
import matplotlib.pyplot as plt 
import mpld3
import pandas as pd
import numpy as np
def generate_html_for_graph_questions(ques, date):
    
    dates = [date]
    while (len(dates) != len(ques)):
        dates.append(date + datetime.timedelta(days= 1))
    
    a = plt.stackplot(dates, ques, colors=['#001333'])
    
    plt.xlabel("Date")
    plt.ylabel("Number of questions solved")
    plt.title("Questions solved per day")
    plt.grid(True, color='#EFF3FF')# set graph grid color and control its pres
    ax = plt.axes()
    ax.set_facecolor('white') #set graph bg-color
    b = a[0].figure
    # b.set_figwidth(10)
    # b.set_figheight(10)
    
    code = mpld3.fig_to_html(b)
    
    return code


def generate_html_for_graph_rank(rank, date):
    
    dates_ = [date]
    while (len(dates_) != len(rank)):
        dates_.append(date + datetime.timedelta(days= 1))
    
    
    a = plt.plot(dates_, rank, color = '#F1884D', linewidth = 5)
    plt.xlabel("Date")
    plt.ylabel("Rank in leaderboard")
    
    plt.grid(True, color='#EFF3FF')
    ax = plt.axes()
    ax.set_facecolor('white')
    b = a[0].figure
    # b.set_figwidth(10)
    # b.set_figheight(10)
    
    code = mpld3.fig_to_html(b)
    
    return code


def generate_html_for_graph_xp(xp, date):
    
    dates_ = [date]
    while (len(dates_) != len(xp)):
        dates_.append(dates_[-1] + datetime.timedelta(days = 1))
    dates_ = np.array(dates_)
    df = pd.DataFrame(xp)
    fig, ax = plt.subplots()
    ax.grid(True, alpha=0.3, color='#EFF3FF')
    for key, val in df.iteritems():
        l, = ax.plot(dates_, val.values, color='#001333', linewidth = 5)
        # ax.legend()
        ax.set_xlabel("Date")
        ax.set_ylabel("XP")
        ax.fill_between(dates_,
                        val.values * .5, val.values * 1.5,
                        color='#F1884D', alpha=.4)
        ax.set_facecolor('white')
    # b = a[0].figure
    # fig.set_figwidth(10)
    # fig.set_figheight(10)
    
    code = mpld3.fig_to_html(fig)
    # print(code)
    return code
# generate_html_for_graph_questions([5, 2, 4, 5, 2, 9, 0, 1], datetime.date.today())

