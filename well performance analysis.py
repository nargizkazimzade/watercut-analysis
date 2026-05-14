import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Set global font family
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Cambria']

# =========================
# WELL X
# =========================

# read excel file
well_x = pd.read_excel("WELL_X.xlsx")

# rename columns so they are easier to work with
well_x.columns = ["date", "oil", "water", "watercut"]

# convert date column to datetime
well_x["date"] = pd.to_datetime(well_x["date"], format="%B %Y")

# plot oil and water for well x
plt.plot(well_x["date"], well_x["oil"], color="green", label="Oil production")
plt.plot(well_x["date"], well_x["water"], color="royalblue", label="Water production")

plt.title("Well X Production Data")
plt.xlabel("Date")
plt.ylabel("Production rate (t/day)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# water cut
plt.plot(well_x["date"], well_x["watercut"], color="steelblue", label="Water cut")

# trend line for water cut

# keep only rows where watercut exists
valid = well_x["watercut"].notna()

# x and y must have same length
x = np.arange(valid.sum())

y = well_x.loc[valid, "watercut"]

# calculate coefficients
coefficients = np.polyfit(x, y, 1)

# create mathematical trend function
trend_function = np.poly1d(coefficients)

# plot trendline
plt.plot(
    well_x.loc[valid, "date"],
    trend_function(x),
    color="dimgray",
    linestyle="--",
    label="Water cut trendline"
)

plt.title("Well X Water Cut")
plt.xlabel("Date")
plt.ylabel("Water cut (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# =========================
# WELL Y
# =========================

well_y = pd.read_excel("WELL_Y.xlsx")
well_y.columns = ["date", "oil", "water", "watercut"]
well_y["date"] = pd.to_datetime(well_y["date"], format="%B %Y")

plt.plot(well_y["date"], well_y["oil"], color="green", label="Oil production")
plt.plot(well_y["date"], well_y["water"], color="royalblue", label="Water production")

plt.title("Well Y Production Data")
plt.xlabel("Date")
plt.ylabel("Production rate (t/day)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# x axis formatting
plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.show()

# water cut
plt.plot(well_y["date"], well_y["watercut"], color="steelblue", label="Water cut")

# trend line for water cut

# keep only rows where watercut exists
valid = well_y["watercut"].notna()

# x and y must have same length
x = np.arange(valid.sum())

y = well_y.loc[valid, "watercut"]

# calculate coefficients
coefficients = np.polyfit(x, y, 1)

# create mathematical trend function
trend_function = np.poly1d(coefficients)

# plot trendline
plt.plot(
    well_y.loc[valid, "date"],
    trend_function(x),
    color="dimgray",
    linestyle="--",
    label="Water cut trendline"
)

plt.title("Well Y Water Cut")
plt.xlabel("Date")
plt.ylabel("Water cut (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# x axis formatting
plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.show()


# =========================
# WELL Z
# =========================

well_z = pd.read_excel("WELL_Z.xlsx")
well_z.columns = ["date", "oil", "water", "watercut"]
well_z["date"] = pd.to_datetime(well_z["date"], format="%B %Y")

plt.plot(well_z["date"], well_z["oil"], color="green", label="Oil production")
plt.plot(well_z["date"], well_z["water"], color="royalblue", label="Water production")

plt.title("Well Z Production Data")
plt.xlabel("Date")
plt.ylabel("Production rate (t/day)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# water cut
plt.plot(well_z["date"], well_z["watercut"], color="steelblue", label="Water cut")

# trend line for water cut

# keep only rows where watercut exists
valid = well_z["watercut"].notna()

# x and y must have same length
x = np.arange(valid.sum())

y = well_z.loc[valid, "watercut"]

# calculate coefficients
coefficients = np.polyfit(x, y, 1)

# create mathematical trend function
trend_function = np.poly1d(coefficients)

# plot trendline
plt.plot(
    well_z.loc[valid, "date"],
    trend_function(x),
    color="dimgray",
    linestyle="--",
    label="Water cut trendline"
)

plt.title("Well Z Water Cut")
plt.xlabel("Date")
plt.ylabel("Water cut (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# =========================
# COMPARATIVE WATER CUT GRAPH
# =========================

plt.plot(well_x["date"], well_x["watercut"], color = "deeppink", label="Well X")
plt.plot(well_y["date"], well_y["watercut"], color = "plum", label="Well Y")
plt.plot(well_z["date"], well_z["watercut"], color = "turquoise", label="Well Z")

plt.title("Comparative Water Cut Trends")
plt.xlabel("Date")
plt.ylabel("Water cut (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# x axis formatting
plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.show()