import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random
import csv

df = pd.read_csv('C:/Users/Meet Ankoliya/Python/project-15/medium_data.csv')
data = df["claps"].tolist()

population_mean = statistics.mean(data)
print(population_mean)

population_std_deviation = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    print(mean)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["claps"], show_hist = False)
    fig.show()
    
first_std_deviation_start, first_std_deviation_end = population_mean - population_std_deviation, population_mean + population_std_deviation
second_std_deviation_start, second_std_deviation_end = population_mean - (2 * population_std_deviation), population_mean + (2 * population_std_deviation)
third_std_deviation_start, third_std_deviation_end = population_mean - (3 * population_std_deviation), population_mean + (3 * population_std_deviation)
print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

mean_list2 = []
for i in range(0, 1000):
    set_of_means2 = random_set_of_mean(100)
    mean_list2.append(set_of_means2)
    
fig = ff.create_distplot([mean_list2], ["claps"], show_hist = False)
fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0, 0.17], mode="lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "Standard deviation first start"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "line", name = "Standard deviaton first end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "line", name = "Standard deviation second start"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "line", name = "Standard deviation second end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0, 0.17], mode = "line", name = "Standard deviation third start"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.17], mode = "line", name = "Standard deviation third end"))
fig.show()

df2 = pd.read_csv('C:/Users/Meet Ankoliya/Python/project-15/sample_medium_data.csv')
data2 = df2["claps"].tolist()
mean_of_sample = statistics.mean(data2)

z_score = (population_mean - mean_of_sample)/population_std_deviation
print("The z-score is :-", population_mean)