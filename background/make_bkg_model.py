import numpy 
import os
import uproot
import math
import pandas
import root_pandas
from hep_ml import reweight
import matplotlib
matplotlib.use('agg') # backend for remote server
import time
from matplotlib import pyplot as plt
# import pickle

def draw_comparison_plots(original, target, variables, original_weights, tag, norm=True):
    
    thedir = 'plots/'
    if not os.path.isdir(thedir):
        os.system("mkdir %s" % thedir)

    #Normalize or not?
    if norm is True:
      # hist_settings = {'bins': 10, 'density': True, 'alpha': 0.5}
      hist_settings = {'bins': 10, 'alpha': 0.5}
    
    else:
      # hist_settings = {'bins': 10, 'density': None, 'alpha': 0.5}
      hist_settings = {'bins': 10, 'alpha': 0.5}
    
    #Create figure on matplotlib
    matplotlib.rcParams.update({'font.size': 35})
    plt.figure(figsize=[80, 60], dpi=50)
    
    # ksresults = []
    # i = 0
    for idx, column in enumerate(variables, 1):
        xlim = numpy.percentile(numpy.hstack([target[column]]), [0.01, 99.99])
        plt.subplot(4, 3, idx)
        plt.hist (original[column], label='Bkg. Model',      weights = original_weights, range = xlim, **hist_settings)
        plt.hist (target[column],   label='4 btag (Target)',                             range = xlim, **hist_settings)
        plt.legend(loc = 'best')
        plt.title(column, fontsize = 40)
        # ks =  ks_2samp_weighted(original[column], target[column], weights1=original_weights, weights2=numpy.ones(len(target), dtype=float))
        # ksresults.append(ks)
        # i += 1
    plt.savefig("plots/distr_%s.pdf" % tag)
    # return ksresults 

# import argparse
starttime = time.time()
## read input parameters
## add the column that defines the mHH chi2 (for the AR and VR)
## AR, VR : position of the selection
## SR, CR : circle and ring
region_type = 'AR'

inputfile  = '../analysis/objects_data_BTagCSV_Run2016_ALL.root'
outputfile_3b = 'data_3btag_with_weights_%s.root' % region_type
outputfile_4b = 'data_4btag.root'

## read input file
print "... running on dataset", inputfile, 'reading the bbbbTree'
arrs      = uproot.open(inputfile)['bbbbTree']
print "... read", len(arrs), "events from the input, now converting to a dataframe"
dataset   = arrs.pandas.df()
#dataset   = arrs.pandas.df(entrystop = 10000000) # not all entries - only for debug!
# note : this step can be sped up by limiting the branches converted:L
# dataset   = arrs.pandas.df(['H*_b*_pt', 'H*_b*_eta', 'HH_*'])

print "... conversion done, here is the dataset"
print dataset.head(10)
print dataset.tail(10)


print "... selecting the analysis regions"
# AR
if region_type == 'AR':
    col_chi = numpy.sqrt( (dataset['H1_m']-120)*(dataset['H1_m']-120)+(dataset['H2_m']-110)*(dataset['H2_m']-110))
    print "   -The analysis region will be used"
elif region_type == 'VR':
    col_chi = numpy.sqrt( (dataset['H1_m']-205)*(dataset['H1_m']-205)+(dataset['H2_m']-190)*(dataset['H2_m']-190))
    print "   -The validation region will be used"
else:
    raise RuntimeError("region not recognised")

dataset['chi'] = col_chi

## split the dataset in the AR and VR parts, SR and CR
dataset_SR = dataset.loc[dataset['chi'] < 30]
dataset_CR = dataset.loc[(dataset['chi'] >= 30) & (dataset['chi'] < 60)]

## split the datasets in 3 btag and 4 btag
dataset_SR_3b = dataset_SR.loc[dataset_SR['n_btag'] == 3]
dataset_SR_4b = dataset_SR.loc[dataset_SR['n_btag'] >= 4]

dataset_CR_3b = dataset_CR.loc[dataset_CR['n_btag'] == 3]
dataset_CR_4b = dataset_CR.loc[dataset_CR['n_btag'] >= 4]

# summary
print '---- Region (%s) ---' % region_type
print '...  SR = %10i      ( 3b : %10i, 4b : %10i ): ' % (len(dataset_SR), len(dataset_SR_3b), len(dataset_SR_4b))
print '...  CR = %10i      ( 3b : %10i, 4b : %10i ): ' % (len(dataset_CR), len(dataset_CR_3b), len(dataset_CR_4b))

## run the reweighting method

transfer_factor = 1.*len(dataset_CR_4b.index)/len(dataset_CR_3b.index)
print '---> transfer factor 3b > 4b is', transfer_factor

# ## here are the variables that the reweighting will used
variables = ['H1_m', 'H2_m', 'H1_b1_pt', 'H1_b2_pt', 'H2_b1_pt', 'H2_b2_pt', 'HH_m']

# create the weights (dummy 1 for the target, transfer factor for the origin)
# origin : 3b
# target : 4b

origin = dataset_CR_3b[variables]
target = dataset_CR_4b[variables]

weights_origin = numpy.ones(dtype='float64', shape=len(origin))
weights_origin = numpy.multiply(weights_origin, transfer_factor)

weights_target = numpy.ones(dtype='float64', shape=len(target))

## now train the BDT reweighter
print '... starting the reweighting'
rnd_seed = 123456
numpy.random.seed(rnd_seed) # the seed is set through numpy arrays
reweighter_base = reweight.GBReweighter      (n_estimators=50, learning_rate=0.1, max_depth=2, min_samples_leaf=20, gb_args={'subsample': 0.6} )
reweighter      = reweight.FoldingReweighter (reweighter_base, random_state = rnd_seed, n_folds = 2, verbose = False)
reweighter.fit(origin, target, weights_origin, weights_target)

print '... reweighting fit done'
ws      = reweighter.predict_weights (origin, weights_origin, lambda x: numpy.mean(x, axis=0) )
weights = numpy.multiply(ws, transfer_factor)
factor  = float( float(len(target.index)) / weights.sum()  ) 

print " == Summary of the reweighting =="
print " ================================"
print "  - The transfer factor                                                 = ", transfer_factor
print "  - The sum of target weights                                           = ", weights_target.sum(),"+/-",math.sqrt(numpy.square(weights_target).sum() )
print "  - The sum of model weights (before reweighting)                       = ", weights_origin.sum(),"+/-",math.sqrt(numpy.square(weights_origin).sum() )
print "  - The sum of model weights (after reweighting, before renorm. factor) = ", weights.sum(),"+/-",math.sqrt(numpy.square(weights).sum() )
print "  - The renormalization factor                                          = ", factor
print "  - The sum of model weights (after renormalization factor)             = ", weights.sum()*factor

weights = numpy.multiply(weights, factor)

### make some plots to compare
print "... making comparison plots for vars", variables
draw_comparison_plots(origin, target, variables, weights_origin,  tag="CR_pre_rew")
draw_comparison_plots(origin, target, variables, weights,         tag="CR_post_rew")

## verify the goodness of the reweighting with a KS test
# def ks_measurement(variables, ks_noweight, ks_weight):
#     print "  ** Runninng KS-test on each variable to define the bdt-reweighter paramaters:"
#     mean = 0
#     for i in range(0, len(variables) ):
#         ratio = ks_weight[i] / ks_noweight[i] 
#         print "   **KS distance ratio in %s (after/before) = (%0.3f/%0.3f)  = %0.3f"%(variables[i], ks_weight[i], ks_noweight[i], ratio)
#         mean += ratio 
#     print "  ** The average KS distance ratio = %0.3f"%(mean/len(variables))
# ks_measurement(variables, ksresult_original, ksresult_model)

## now save the reweighter to an output pkl file

print "... preparing 4b/3b output datasets "
dataset_4b  = dataset.loc[dataset['n_btag'] >= 4].copy() ## just select events with 4 btag, independently on the chi2. Need to copy as this will be a new, output dataset
dataset_3b  = dataset.loc[dataset['n_btag'] == 3].copy() ## just select events with 3 btag, independently on the chi2. Need to copy as this will be a new, output dataset
del dataset 

print "... now saving 4 b tag data only to the output file: ", outputfile_4b
dataset_4b.to_root(outputfile_4b, key='bbbbTree')

print "... now saving 3 b tag events with the background modelling weights to the output file: ", outputfile_3b
dataset_3b_subset = dataset_3b[variables]
weights_3b        = numpy.ones(dtype='float64', shape=len(dataset_3b_subset))
weights_3b        = numpy.multiply(weights_3b, transfer_factor)
## NB: the absolute normalisation of weights_3b has not impact on the returned modelling weights
bkg_model_w       = reweighter.predict_weights (dataset_3b_subset, weights_3b, lambda x: numpy.mean(x, axis=0) )
bkg_model_w       = numpy.multiply(bkg_model_w, transfer_factor)
bkg_model_w       = numpy.multiply(bkg_model_w, factor)
# do not drop index --> branch __index__ in the output will be my entry number of the original file
dataset_3b['bkg_model_w'] = bkg_model_w
dataset_3b.to_root(outputfile_3b, key='bbbbTree')

print "... done! running background model script took %.1f seconds"%(time.time() - starttime)