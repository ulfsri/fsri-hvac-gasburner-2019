# fsri-hvac-gasburner-2019

This repository contains the data and supporting files from 29 propane gas burner experiments conducted in a single-story ranch-style residential structure with a basement. The structure was equipped with a heating ventilation and air conditioning (HVAC) system. Experiments were conducted to assess the effects of HVAC operating status (off vs. on), the impact of fire location and fire heat release rate, and the impact of bedroom door position (open vs. closed) on heat and gas species transfer.

This project was funded through a grant from the Department of Homeland Security (DHS) Federal Emergency Management Agency's (FEMA) Assistance to Firefighters Grant (AFG) Program under the Fire Prevention and Safety Grants: Research and Development (EMW-2017-FP-00628).

## 01_Data
The data directory includes a series of sequentially numbered plain text (__.csv__) files for each experiment, each with the prefix **Gas_Burner_Experiment_**. A subdirectory, **Events**, includes a corresponding plain text file with time-stamped events that map to the data. More information on the structure of the included files and the corresponding experiments can be found here: [Data Details](01_Data/README.md) 

## 02_Info
The info directory contains a plaintext __.csv__ channel list and an info file. The channel list maps the individual channels to their respective measurement arrays. Dimensioned, instrumented floor plans can be found here: [Instrumentation Details](02_Info/README.md). The channel list files also set the channel labels and file names for graphs produced by the included scripts (03_Scripts). The info file is used to set the start and end times for graphs as well as the y-axis values for the respective measurement quantities.

## 03_Scripts
A Python script is included to produce **.pdf** graphs for each of the measurement locations for each experiment. In conjunction with Matplotlib, Seaborn is used to style the graph. If seaborn is not already installed, it can be added by the following:
```
pip install seaborn
```
If you are using the Anaconda distribution of python, it can alternatively be installed by:
```
conda install seaborn
```

## 04_Charts
The chart directories gets produced upon execution of _Plot.py_. Graphs are produced for each measurement location for each experiment. Because the graphs can be produced from files included in this repository, the graphs themselves are not files under version control. Additionally, the **04_Charts** directory is included in the __.gitignore__ file to prevent unintentional commits of the graphs.

###
For more information about the project, [Contact Us](https://fsri.org/contact-fire-safety-research-institute).
