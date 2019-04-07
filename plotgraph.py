import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import csv

dataset = pd.read_csv('mydata.csv')
	
def disease_death():
	X = dataset.iloc[:, :-1]
	y_one = dataset.iloc[:, [1,2,3,4]]

	#diseases line graph
	plt.xlabel('Years')
	plt.ylabel('Deaths due to disease')
	plt.plot( y_one, linewidth=2.0)
	plt.savefig('static/linechart.png')

def disease_pie(y):
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	labels = 'Malaria Deaths',	'Diarrhoeal Deaths',	'Respiratory Deaths', 'viral fever deaths'

	sizes = disease_values(y)
	explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.savefig('static/foo.png')

def disease_values(year):
	x = dataset[dataset['Year']==year].iloc[:, 1:5].values
	return x.ravel()

def medicine_pie(y):

	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	labels = 'Malaria Deaths',	'Diarrhoeal Deaths',	'Respiratory Deaths', 'viral fever deaths'

	sizes = medicine_values(y)
	explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.savefig('static/medi.png')

def medicine_values(year):
	x = dataset[dataset['Year']==year].iloc[:, 5:9].values
	return x.ravel()