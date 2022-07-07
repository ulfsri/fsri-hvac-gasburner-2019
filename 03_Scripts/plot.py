# ***************************** Run Notes ***************************** #
# - Experimental Plotter for 2019 Two Story Gas Burner Experiments 		#
# ********************************************************************* #

# --------------- #
# Import Packages #
# --------------- #
import os
import socket
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
# Set seaborn as default plot config
sns.set()
sns.set_style("whitegrid")
from cycler import cycler
from itertools import cycle
from pathlib import Path

# ---------------------------------- #
# Define Subdirectories & Info Files #
# ---------------------------------- #
data_dir = '../01_Data/'
event_dir = '../01_Data/Events/'
info_dir = '../02_Info/'
plot_dir = '../04_Charts/'

# Create plot dir if necessary
if not os.path.exists(plot_dir):
	os.makedirs(plot_dir)

# Read in exp info file
exp_info = pd.read_csv(f'{info_dir}Info_Gas_Burner.csv', index_col='Test_Name')

# ------------------- #
# Set Plot Parameters #
# ------------------- #

label_size = 18
tick_size = 16
line_width = 1.5
event_font = 10
font_rotation = 60
legend_font = 10
fig_width = 10
fig_height = 8

# if graphs are autoscaled set to True, else scale sets by values in exp_info file
scaled_y_axis = True

# ---------------------- #
# User-Defined Functions #
# ---------------------- #

def create_1plot_fig():
	# Define figure for the plot
	fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))

	current_palette_8 = sns.color_palette('deep', 8)
	sns.set_palette(current_palette_8)
	# sns.color_palette('Paired')
	plot_markers = cycle(['s', 'o', '^', 'd', 'h', 'p','v', '8', 'D', '*', '<', '>', 'H'])

	# Reset values for x & y limits
	x_max = 0
	y_min = 0
	y_max = 0

	return(fig, ax1, plot_markers, x_max, y_min, y_max)

def format_and_save_plot(y_lims, x_lims, secondary_axis_label, file_loc):
	# Set tick parameters
	ax1.tick_params(labelsize=tick_size, length=0, width=0)

	# Scale axes limits & labels
	ax1.set_ylim(bottom=y_lims[0], top=y_lims[1])
	ax1.set_xlim(x_lims[0],x_lims[1])
	ax1.set_xlabel('Time (s)', fontsize=label_size)

	# Secondary y-axis parameters
	if secondary_axis_label != 'None':
		ax2 = ax1.twinx()
		ax2.tick_params(labelsize=tick_size, length=0, width=0)
		ax2.set_ylabel(secondary_axis_label, fontsize=label_size)
		if secondary_axis_label == 'Temperature ($^\circ$F)':
			ax2.set_ylim([y_lims[0] * 1.8 + 32., y_lims[1] * 1.8 + 32.])
		else:
			ax2.set_ylim([secondary_axis_scale * y_lims[0],
							secondary_axis_scale * y_lims[1]])
		ax2.yaxis.grid(b=None)

	# Add vertical lines and labels for timing information (if available)
	tempevents = Events[Events.index.values > x_lims[1]].index
	Events.drop(tempevents , inplace=True)
	ax3 = ax1.twiny()
	ax3.set_xlim(x_lims[0],x_lims[1])
	ax3.set_xticks(Events.index.values)
	ax3.tick_params(axis='x', width=1, labelrotation=font_rotation, labelsize=event_font)
	ax3.set_xticklabels(Events['Event'], fontsize=event_font, ha='left')
	ax3.xaxis.grid(b=None)

	# Add legend
	handles1, labels1 = ax1.get_legend_handles_labels()
	ax1.legend(handles1, labels1, loc='best', fontsize=legend_font,
				handlelength=3, frameon=True, framealpha=0.85)

	# Clean up whitespace padding
	fig.tight_layout()
	plt.savefig(file_loc)
	plt.close()

# -------------------------------------- #
# Start Code Used to Generate Data Plots #
# -------------------------------------- #
data_file_ls = [f'{exp}.csv' for exp in exp_info.index.values.tolist()]

# Loop through test data files & create plots
for f in data_file_ls:

	# Read in data for experiment, rename time column to timestamp
	data_df = pd.read_csv(f'{data_dir}{f}')
	data_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
	data_df = data_df.set_index('Time')

	if Path(f'{data_dir}{f[:-4]}_Event.csv').is_file():
		Events = pd.read_csv(f'{data_dir}{f[:-4]}_Event.csv')

	# Get test name from file
	test_name = f[:-4]
	print (f'--- Loaded data file for {test_name} ---')

	# Read in channel list file & create list of sensor groups
	channel_list = pd.read_csv(f"{info_dir}{exp_info.at[test_name, 'Channel List']}", index_col='Channel_Name')
	channel_groups = channel_list.groupby('Chart')

	# Read in experiment event file
	# Create index column of time relative to ignition in exp_data
	Events = pd.read_csv(f'{event_dir}{f[:-4]}_Events.csv')
	Events = Events.set_index('Time')

	# Set dir name for experiment's plots
	save_dir = plot_dir + test_name + '/'
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)

	# Set list of channels to skip from info file
	skip_groups = [g for g in exp_info.loc[test_name, 'Excluded_Groups'].split('|')]
	skip_channels = [c for c in exp_info.loc[test_name, 'Excluded_Channels'].split('|')]

	# Loop through channel groups & generate plot of channel data
	for group in channel_groups.groups:

		if any([substring == group for substring in skip_groups]):
			continue
		print ('  Plotting ' + group.replace('_',' '))

		# Create figure for plot(s)
		fig, ax1, plot_markers, x_max, y_min, y_max = create_1plot_fig()

		# Plot each channel within group
		for channel in channel_groups.get_group(group).index.values:

			if any([substring == channel for substring in skip_channels]):
				continue

			# Set secondary axis default to None, get data type from channel list
			secondary_axis_label = 'None'
			data_type = channel_list.loc[channel,'Type']

			# Set plot parameters based on data type
			if data_type == 'Temperature':

				# Set y-axis labels
				ax1.set_ylabel('Temperature ($^\circ$C)', fontsize=label_size)
				secondary_axis_label = 'Temperature ($^\circ$F)'
				y_max_set = exp_info['Y Scale TC'][test_name]

			elif data_type == 'Velocity':

				# Set y-axis labels & scale
				ax1.set_ylabel('Velocity (m/s)', fontsize=label_size)
				secondary_axis_label = 'Velocity (mph)'
				secondary_axis_scale = 2.23694
				y_max_set = exp_info['Y Scale BDP'][test_name]

			elif data_type == 'HRR':

				ax1.set_ylabel('HRR (kW)', fontsize=label_size)
				y_max_set = exp_info['Y Scale HRR'][test_name]

			elif data_type == 'Volume_Percent':

				# Set y-axis properties
				ax1.set_ylabel('Concentration (% vol)', fontsize=label_size)
				y_max_set = exp_info['Y Scale GAS'][test_name]

			elif data_type == 'Vapor_Volume_Percent':

				# Set y-axis properties
				ax1.set_ylabel('Concentration (% vol)', fontsize=label_size)
				y_max_set = exp_info['Y Scale GAS'][test_name]

			elif data_type == 'Pressure':

				ax1.set_ylabel('Pressure (Pa)', fontsize=label_size)
				secondary_axis_label = 'Pressure (psi)'
				secondary_axis_scale = 0.000145038
				y_max_set = exp_info['Y Scale PRESSURE'][test_name]

			# Plot channel data
			ax1.plot(data_df.index, data_df[channel], lw=line_width,
				marker=next(plot_markers), markevery=30, mew=3, mec='none', ms=7, 
				label=channel_list.loc[channel, 'Channel_Label'])

			# Determine x bounds for current data & update max of chart if necessary
			x_min = exp_info['Start_Time'][test_name]
			x_end = exp_info['End_Time'][test_name]
			if x_end > x_max:
				x_max = x_end

			# Auto set graphs by dataframe values or user specified 
			if scaled_y_axis:
				if min(data_df[channel]) - abs(min(data_df[channel]) * .1) < y_min:
					y_min = min(data_df[channel]) - abs(min(data_df[channel]) * .1)

				if max(data_df[channel]) * 1.1 > y_max:
					y_max = max(data_df[channel]) * 1.1
			else:
				y_max = y_max_set
				if data_type == 'Velocity' or data_type == 'Pressure':
					y_min = -1*y_max
				else:
					y_min = 0

		# Add vertical lines for event labels; label to y axis
		[ax1.axvline(_x, color='0.25', lw=1) for _x in Events.index.values if _x >= 0 and _x <= x_max]

		# Set save directory and call plotting function
		save_dir = f'{plot_dir}{test_name}/'
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)

		format_and_save_plot([y_min, y_max], [x_min, x_max], secondary_axis_label, f'{save_dir}{group}.pdf')
