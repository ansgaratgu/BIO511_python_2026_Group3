import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotnine import ggplot, geom_histogram, aes, geom_point, ggtitle

penguins = sns.load_dataset("penguins")

# a. remove rows with NAs, use dropna()
df_clean = pd.DataFrame.dropna(penguins)

# # check for nas in og df
# df = pd.DataFrame.isna(penguins)
# df_clean = pd.DataFrame.isna(df_clean)

# print("nas before:", penguins.isna().sum())
# print("nas after:", df_clean.isna().sum())

# b. scatterplot with matplotlib: flipper length = x, y = body mass
# add xlabel and ylabel, save plot

# x = df_clean("flipper_length_mm")
# y = df_clean("body_mass_g")

# plt.scatter(df_clean['flipper_length_mm'], df_clean['body_mass_g'])
# plt.title('Flipper length vs Body mass')
# plt.xlabel('Flipper length (mm)')
# plt.ylabel('Body mass (g)')
# plt.savefig('scatterplot_mat.png')
# plt.show()

# c. same plot with plotly, save as html
# fig2 = px.scatter(
#     df_clean, 
#     x='flipper_length_mm', 
#     y='body_mass_g',
#     title='Flipper length vs Body mass')

# fig2.write_html("/home/katerina/python_practical/practical_6/fig2.html")

# # d. plot using seaborn, color species
# sns_plot=sns.scatterplot(data=df_clean, x='flipper_length_mm', y='body_mass_g', hue='species')
# plt.title('Flipper length vs Body mass')
# plt.show()
# sns_plot.figure.savefig('sns_figure.png', dpi=300)

# # e. plotnine
# plot = (
#     ggplot(df_clean, aes(x="flipper_length_mm", y="body_mass_g"))
#     + geom_point()
#     + ggtitle("Flipper length vs Body mass")
# )
# plot.show()
# plot.save('plotnine_figure.png', width=4, height=3, dpi=300)

# # histogram
# histogram = (
#     ggplot(df_clean, aes(x="bill_length_mm"))
#     + geom_histogram()
# )
# histogram.show()
# histogram.save('plotnine_histogram.png', width=4, height=3, dpi=300)

# use pandas to group data by island
# calculate mean value of body mass per island

# grouped_df = pd.DataFrame.groupby(df_clean, by="island")
# mean_mass = grouped_df["body_mass_g"].mean()
grouped_df = df_clean.groupby("island", as_index=False)["body_mass_g"].mean()

# bar chart
bar_chart = px.bar(grouped_df, x="island", y="body_mass_g")
bar_chart.show()
#   File "/home/katerina/miniconda3/lib/python3.14/site-packages/plotly/express/_core.py", line 1380, in process_args_into_dataframe
#     raise ValueError(err_msg)
# ValueError: Value of 'x' is not the name of a column in 'data_frame'. Expected one of ['body_mass_g'] but received: island
# this is bc we get a Series with island as an index not as a column, we use False to fix that