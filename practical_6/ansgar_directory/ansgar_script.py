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
