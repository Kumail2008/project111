import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data],["Reading Time"],show_hist = False)
fig.show()

#part two
def random_set_of_mean(counter):
  dataSet = []
  for i in range(0,counter):
    randomIndex = random.randint(0,len(data)-1)
    value = data[randomIndex]
    dataSet.append(value)
  mean = statistics.mean(dataSet)
  return(mean)

mean_list = []
for i in range(0,100):
  setOfMeans = random_set_of_mean(30)
  mean_list.append(setOfMeans)   

standard_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean of sampling distribution",mean)
print("Standard deviation of sampling distribution",standard_deviation)

fig = ff.create_distplot([mean_list],["Reading Time"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = "lines",name = "MEAN"))


#part 3
mean = statistics.mean(data)
stdevation = statistics.stdev(data)
print("Mean of the population: ",mean)
print("Standard deviation is: ",stdevation)

stdevation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean of sampling distribution",mean)
print("Standard deviation of sampling distribution",ation)




FirststdevStart,FirststdevEnd = mean - stdevation,mean + stdevation
SecondstdevStart,SecondstdevEnd = mean - (stdevation*2),mean + (stdevation*2)
ThirdstdevStart,ThirdstdevEnd = mean - (stdevation*3),mean + (stdevation*3)




print("stdev1",FirststdevStart,FirststdevEnd)
print("stdev2",SecondstdevStart,SecondstdevEnd)
print("stdev3",ThirdstdevStart,ThirdstdevEnd)

fig = ff.create_distplot([mean_list],["Reading Time"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "MEAN"))

fig.add_trace(go.Scatter(x=[FirststdevStart,FirststdevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[FirststdevEnd, FirststdevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[SecondstdevStart, SecondstdevStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[SecondstdevEnd, SecondstdevEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[ThirdstdevStart,ThirdstdevStart], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[ThirdstdevEnd,ThirdstdevEnd], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


