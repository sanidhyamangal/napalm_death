import numpy as np # for matrix maths 
import pandas as pd # for data tabels 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split

# import a data workbook 
# imunization_data = pd.ExcelFile()
# load a all india data 
all_india_data  = pd.read_excel('immunation_data.xlsx', 'All India')

# process data for the ploio_bcg_measels
labels_pbm = all_india_data.iloc[1:, -1].values

features_pbm = all_india_data.iloc[1:, [-3, -2]]

# train our rfregressor for the pbm model 
rf_pbm = RandomForestRegressor(n_estimators=100)

rf_pbm.fit(features_pbm, labels_pbm)

# data for the DT/DTP5 prediction
data_all_tdt = all_india_data.iloc[1:, [-5,-4]].values

labels_tdt = all_india_data.iloc[1:, [1]].values

svm_tdt = SVR(kernel='poly', C=1e-4)
svm_tdt.fit(data_all_tdt, labels_tdt)

# data for the prediction of any statewise performance

# load statewise data 
statewise_data = pd.read_excel("./immunation_data.xlsx", sheet_name='Statewise', header=[0,1])

# polio state data 
polio_state = statewise_data.Polio

# imputer our data for 
state_polio = Imputer(missing_values='NaN', strategy='mean', axis=0).fit_transform(polio_state)

# make a predictor 
lr_st_p = LinearRegression()

# print(polio_state.shape)

lr_st_p.fit(state_polio[:, :1], state_polio[:, 1])

state_bcg = statewise_data.BCG

# imputer our data for 
state_bcg = Imputer(missing_values='NaN', strategy='mean', axis=0).fit_transform(state_bcg)

# make a predictor 
lr_st_b = LinearRegression()

lr_st_b.fit(state_bcg[:, :2], state_bcg[:, 2])



state_bcg = statewise_data.BCG

# imputer our data for 
state_bcg = Imputer(missing_values='NaN', strategy='mean', axis=0).fit_transform(state_bcg)

# make a predictor 
lr_st_b = LinearRegression()

lr_st_b.fit(state_bcg[:, :2], state_bcg[:, 2])

# measels 
state_measels = statewise_data.Measels

# imputer our data for 
state_measels = Imputer(missing_values='NaN', strategy='mean', axis=0).fit_transform(state_measels)

# make a predictor 
lr_st_m = LinearRegression()

lr_st_m.fit(state_measels[:, :2], state_measels[:, 2])


# data for poxy vit a def.
state_1d  =  statewise_data['1st Dose']
state_25d =  statewise_data['2nd Dose to 5th Dose']
state_9d  = statewise_data['9th dose']

# make a combined dataframe for all these images
state_prox =  pd.concat([state_1d.iloc[:, -1], state_25d.iloc[:, -1], state_9d.iloc[:, -1]], axis=1)


# imputer our data for 
state_prox = Imputer(missing_values='NaN', strategy='mean', axis=0).fit_transform(state_prox)

# make a predictor 
lr_st_prox = LinearRegression()

lr_st_prox.fit(state_prox[:, :-1], state_prox[:, -1])

def predict_polio(previous_dose):
	return int(lr_st_p.predict([[previous_dose]])[0])

def predict_pbm(previous_dose):
	return rf_pbm.predict([previous_dose])[0]

def predict_prox(previous_dose):
	return lr_st_prox.predict([previous_dose])[0]

def predict_bcg_statewise(previous_dose):
	return lr_st_b.predict([previous_dose])[0]

def predict_measles_statewise(previous_dose):
	return lr_st_m.predict([previous_dose])[0]

def predict_dtp(previous_dose):
	return svm_tdt.predict([previous_dose])[0]
