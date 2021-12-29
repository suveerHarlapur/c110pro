import statistics,plotly.figure_factory as ff,pandas as pd,random;
data = pd.read_csv("medium_data.csv")
df = data["reading_time"].tolist()
popmean = statistics.mean(df)
print("population mean:",popmean)
fig = ff.create_distplot([df],['rawdata'],show_hist=False)
fig.show()
def random_set_of_mean():
    dataset = []
    for i in range(0,30):
        random_index = random.randint(0,len(df)-1)
        random_value = df[random_index]
        dataset.append(random_value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
def setup():
    for i in range(0,100):
        meanvalue = random_set_of_mean()
        mean_list.append(meanvalue)
    samplemean = statistics.mean(mean_list)
    print("sample mean is :",samplemean)

def figure():
    fig = ff.create_distplot([mean_list],["mean list"],show_hist=False)
    fig.show()

setup()
figure()