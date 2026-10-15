#### import modules
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as ply

#### a
# load penguins dataset
peng = sns.load_dataset("penguins")
# print(peng)

#### b
# plot scatterplot x=flipper length, y=body mass, title, xlabel, ylabel, save plot
def plot_matplotlib(input):
    plt.scatter(input['flipper_length_mm'], input['body_mass_g'])
    plt.title('Flipper length vs Body mass')
    plt.xlabel('Flipper length (mm)')
    plt.ylabel('Body mass (g)')
    # how to save a matplotlib
    plt.savefig('plot1_figure.png', dpi = 300)

# first_plot = plot_matplotlib(peng)

#### c
def plot_plotly(input):
    plotly_fig = ply.scatter(
        input, 
        x = "flipper_length_mm",
        y = "body_mass_g",
        title = "Flipper length vs Body mass")
    plotly_fig.show()
    # save as .html
    plotly_fig.write_html('plotly_image_interactive.html')

# second_plot = plot_plotly(peng)

#### d
def plot_seaborn(input):
    sns_plot = sns.scatterplot(input[['flipper_length_mm', 'body_mass_g']], x = 'flipper_length_mm', y = 'body_mass_g') #???????????????????????????????????????????????????????????????????????
    plt.title('Flipper length vs Body mass')
    sns_plot.label(x = "Flipper length (mm)", y = "Body mass (g)", color = "") # I dunno how to do this
    # save
    sns_plot.figure.savefig('seaborn_figure.png', dpi = 300)

# third_plot = plot_seaborn(peng)

#### e
from plotnine import ggplot, aes, geom_point, facet_wrap, ggtitle, geom_histogram


# plot = (
#     ggplot(peng, aes(x = "flipper_length_mm", y = "body_mass_g"))
#     + geom_point()
#     + ggtitle("Flipper length vs Body mass")
# )
# show the plot in a seperate little window
# also shows exis position on mouse
# plot.show()

# save
# plot.save("plotnine_figure.png", width = 4, height = 3, dpi = 300)

#### histogram
# plot = (ggplot(peng, aes(x = "bill_length_mm", fill = "species"))
#         + geom_histogram()
#         + ggtitle("Bill length sorted by species")
#         # separate by species
#         + facet_wrap("species")
#         )

# plot.show()

#### island
import pandas as pd
# group by island using pandas
df = pd.DataFrame(peng)
# print(df)

# make a series with means for the islands and round to one decimal point
means = df.groupby("island")["body_mass_g"].mean().round(1)

# save means to df
# .map makes it add the value for each island row thingy
df["mean_body_mass_g"] = df["island"].map(means)
print(df)

# create a bar plot where each bar represents mean bd mass for one island
from plotnine import geom_bar
plot = (
    ggplot(df, aes(x = "island", y = "mean_body_mass_g"))
    + geom_bar(stat = "summary") # stat = "summary" makes it not add upp all mean values
)

plot.show()