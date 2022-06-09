from os.path import dirname, join
import datetime

import pandas as pd
import matplotlib.pyplot as plt

total_time = 0


def make_pie_chart(filename):
    global total_time
    data = pd.read_csv(join(dirname(__file__), filename), dtype=object).rename({'Time spent seconds': 'time'}, axis=1)
    data['time'] = data['time'].astype(int)
    total_time = data.iloc[-1]['time']/3600
    data.dropna(subset=['Author'], inplace=True)
    data['time'] = data.groupby('Author')['time'].transform('sum')
    data.drop_duplicates(['Author'], inplace=True)
    data = data[['Author', 'time']]

    data['time'] = data['time'].apply(lambda x: int(x)/3600)

    plt.figure()
    plt.bar(height=data['time'], x=data['Author'])
    plt.title('Heures travaillées par personne')
    plt.savefig(join(dirname(__file__), f'pie_chart_{datetime.datetime.now().date()}.png'), format='png')

def slice_value(x):
    return f'{(x/100)*total_time:.2f}h ({x:.2f}%)'


make_pie_chart('worklogs_backup.csv')