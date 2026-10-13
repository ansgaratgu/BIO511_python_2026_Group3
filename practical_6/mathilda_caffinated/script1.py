#practical 6
#mathilda järkestig 13-10-26

###imports:
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as plty
import seaborn as sea
from plotnine import ggsave, ggplot, aes, geom_point, ggtitle


###load in as save oenguin data:
#sea.load_dataset("penguins") => loades in dada from pinguins
#dropna(axis=0, how="any") => drops rows containing any na value
#saves dataframe as pingu
pingu = sea.load_dataset("penguins").dropna(axis=0, how="any")
print(pingu)


###matplotlib:
#fist is x then y
mat_pingu = plt.scatter(pingu["flipper_length_mm"], pingu["body_mass_g"])
plt.title("Flipper length vs Body mass")
plt.xlabel("Flipper length(mm)")
plt.ylabel("Body mass (g)")
plt.savefig("mat_pingu.png")


###plotly

plot_pingu = plty.scatter(
    pingu,
    x="flipper_length_mm", 
    y="body_mass_g",
    title="Flipper length vs Body mass")

plot_pingu.write_html("plot_pingu.html")


hist_pingu =plty.histogram(
    pingu,
    x="bill_length_mm",
    title="Bill length distribution",
    nbins=20)

hist_pingu.write_html("hist_pingu.html")


##seaborn
sea_pingu = sea.scatterplot(
    data=pingu,
    x="flipper_length_mm", 
    y="body_mass_g",
    hue="species",
    palette="pastel")
plt.title("Flipper length vs Body mass")
sea_pingu.figure.savefig("sea_pingu.png")

###plotnine:

gg_pingu = (
    ggplot(pingu, aes(x="flipper_length_mm", y="body_mass_g")) +
    geom_point() +
    ggtitle("Flipper length vs Body mass"))
gg_pingu.save("gg_pingu")


###pandas

panda = pd.DataFrame(pingu)
short_panda = (panda[["body_mass_g", "island"]] #select bodymass and islands columns
               .groupby("island")["body_mass_g"] #group body mass by islands 
               .mean()
               .reset_index()) #island beckomes index so reset intext to mke island a regular column
print(short_panda)


plot_short_panda = plty.bar(
    short_panda,
    x="island", 
    y="body_mass_g",
    title="Mean body mass per island")

plot_short_panda.write_html("plot_short_panda.html")