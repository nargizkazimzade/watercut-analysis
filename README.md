# watercut-analysis
This is the oil and water production plus water cut analysis on three wells I have done for my internship report
# Well Performance Decline Through Water Cut Dynamics

### Bibiheybat Oilfield Case Study

This repository contains the Python workflow and processed datasets used for the bachelor's internship report:

**"Evaluation of Well Performance Decline Through Water Cut Dynamics in a Mature Onshore Field: A Case Study of Bibiheybat Oilfield"**

The project focuses on analyzing production behavior and water cut trends of three wells with different ages located in the Bibiheybat oilfield, Azerbaijan.

---

# Project Objective

The purpose of this project is to:

* analyze long-term oil and water production behavior,
* calculate weighted monthly average production data,
* evaluate water cut dynamics,
* compare production decline trends between wells of different ages,
* visualize production performance using Python.

The selected wells represent:

* a young well,
* a middle-aged well,
* and a mature well.

---

# Workflow

The analysis workflow includes:

1. Digitizing handwritten production journals into Excel format
2. Cleaning and preprocessing production data
3. Calculating weighted monthly averages
4. Calculating water cut values
5. Handling inactive periods and inconsistent historical records
6. Visualizing production and water cut trends
7. Generating comparative graphs and trendlines

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Excel

---

# Repository Structure

```text
├── data/
│   ├── well_x.xlsx
│   ├── well_y.xlsx
│   └── well_z.xlsx
│
├── figures/
│   ├── well_x_watercut.png
│   ├── well_y_watercut.png
│   ├── well_z_watercut.png
│   └── comparative_watercut.png
│
├── well_performance_analysis.py
└── README.md
```

---

# Notes About the Dataset

* Original well names were anonymized for confidentiality reasons.
* Historical field records were obtained from handwritten production journals.
* Some historical intervals contained inconsistencies in water production reporting.
* Reliable quantitative water cut analysis begins:

  * 2024 for Well X
  * 2000 for Well Y
  * 2010 for Well Z

Inactive periods caused by workovers, perforation operations, pump failures, and well interventions were preserved as gaps in the analysis rather than artificially interpolated.

---

# Example Analysis Outputs

The repository includes:

* oil production graphs,
* water production graphs,
* water cut graphs,
* polynomial trendline visualizations,
* comparative water cut analysis between wells.

---

# Author

Nargiz Kazimzade
UFAZ — Petroleum Engineering / Reservoir Geology
2026
