import csv
import io
import json
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from collections import defaultdict

def test3():
    df = pd.DataFrame([
    ['France', 61083916, 'Europe'], ['Germany', 82400996, 'Europe'], ['Italy', 58147733, 'Europe'],
    ['Spain', 40448191, 'Europe'], ['United Kingdom', 60776238, 'Europe'], ['Taiwan', 23174294, 'Asia'],
    ['Japan', 127467972, 'Asia'], ['Korean', 49044790, 'Asia'], ['China', 1318683096, 'Asia']],
    columns=['country', 'pop', 'continent'])
    europe_sum = df[df['continent']=='Europe']['pop'].sum()
    asia_sum = df[df['continent']=='Asia']['pop'].sum()
    fig, ax = plt.subplots()
    size = 0.4
    ax.pie(df['pop'], labels=df['country'],
        autopct='%1.2f%%', pctdistance=0.8,
        radius=1, wedgeprops=dict(width=size, edgecolor='w'))
    ax.pie([europe_sum, asia_sum], labels=['Europe', 'Asia'], labeldistance=0.2,
        autopct='%1.2f%%', pctdistance=0.6,
        radius=1-size, wedgeprops=dict(width=size, edgecolor='w'))
    plt.title('Population')
    plt.show()
    plt.savefig("test3.png")

def test2():
    fig =go.Figure()
    fig.add_trace(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    ))
    # Update layout for tight margin
    # See https://plotly.com/python/creating-and-updating-figures/
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    #fig.show()
    fig.write_image("test2.png")

def test():
    # Make data: I have 3 groups and 7 subgroups
    status_names, graph_data = graph_feelings()
    print(status_names)
    statuses = graph_data.keys()
    emotions_size = []

    for status, senses in graph_data.items():
        for sense, emotions in senses.items():
            for emotion in emotions:
                emotions_size = [len(statuses), len(senses), len(emotions)]
                #print(emotion, sense, status)
                pass

    print(emotions_size)

    # Make data: I have 3 groups and 7 subgroups
    group_names=['groupA', 'groupB', 'groupC']
    group_size=[12,11,30]
    subgroup_names=['A.1', 'A.2', 'A.3', 'B.1', 'B.2', 'C.1', 'C.2', 'C.3', 'C.4', 'C.5']
    subgroup_size=[4,3,5,6,5,10,5,5,4,6]
    subsubgroup_names=['A1.1', 'A1.2', 'A1.3', 'B1.1', 'B1.2', 'C1.1', 'C1.2', 'C1.3', 'C1.4', 'C1.5']
    subsubgroup_size=[4,3,5,6,5,10,5,5,4,6]
    
    # Create colors
    a, b, c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
    
    # First Ring (outside)
    fig, ax = plt.subplots()
    ax.axis('equal')
    mypie, _ = ax.pie(group_size, radius=1, labels=group_names, colors=[a(0.6), b(0.6), c(0.6)] )
    plt.setp( mypie, width=0.9, edgecolor='white')
    
    # Second Ring (Inside)
    mypie2, _ = ax.pie(subgroup_size, radius=.6, labels=subgroup_names, labeldistance=0.7, colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
    plt.setp( mypie2, width=0.9, edgecolor='white')
    plt.margins(0,0)

    # Third Ring (Inside)
    mypie3, _ = ax.pie(subsubgroup_size, radius=.3, labels=subsubgroup_names, labeldistance=0.7, colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
    plt.setp( mypie3, width=0.9, edgecolor='white')
    plt.margins(0,0)

    # show it
    plt.savefig("test.png")

#def test4():

def load_csv_rows(fileloc):
    rows = []

    with io.open(fileloc, "r", encoding="utf8") as filehandle:
        #reader = csv.reader(filehandle)
        reader2 = csv.DictReader(filehandle)
        #for row in reader:
        #    rows.append(row)

    #return rows
    return reader2


def graph_feelings():
    feelings = load_csv_rows("NVC  - Feelings.csv")
    for row in feelings:
        print(row.keys())
        print(row.values())

    print(header)
    graph = defaultdict(lambda:defaultdict(list))

    for row in feelings:
        status, sense, emotion, *_ = row
        graph[status][sense].append(emotion)
        print(row)

    return header, feelings
 
if __name__ == "__main__":
    test()
    test2()
    test3()
    #print(json.dumps(graph_feelings(), indent=4))
    needs = load_csv_rows("NVC  - Needs.csv")
