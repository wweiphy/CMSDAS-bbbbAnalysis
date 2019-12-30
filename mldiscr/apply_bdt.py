import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import uproot
from sklearn.metrics import roc_curve, auc
import matplotlib
from matplotlib import pyplot as plt
import pickle

infile   = open('bdt_training.pkl', 'rb')
in_data   = pickle.load(infile)
infile.close()

print '... opened model, dict contains: ', in_data
model         = in_data['model']
vars_training = in_data['vars']

#### do things here