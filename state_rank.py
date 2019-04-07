import pandas as pd # for datatables 
import numpy as np # for matrix maths 


# import the rank datatable 
state_rank = pd.read_excel('./state_ranking.xlsx')

# make a disease by beds factor ratio
state_rank_diseases = state_rank.iloc[:, 1:5] / state_rank.iloc[:, 1:2].values

# multiply it with mean of available services for caring
state_ranks = state_rank_diseases.mean(axis=1) * state_rank.iloc[:, 2:5].mean(axis=1)

# standardize the the ranks for the max scaller 
state_ranks /= state_ranks.max()

def get_ranking_all():
    args = state_ranks.argsort()
    return state_rank.iloc[args[::-1]].iloc[:, 0].reset_index()
    # return.iloc[1]

def get_state_plot(name):
    args = state_ranks.argsort()
    state_rank_cal = state_rank.iloc[args[::-1]].reset_index()

    return state_rank_cal[state_rank_cal['state'] == name].index

print(get_state_plot('Manipur'))
print(get_ranking_all())