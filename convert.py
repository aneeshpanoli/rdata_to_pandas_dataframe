#!/usr/bin/env python

"""Convert an expression dataset from biological experiment to pandas dataframe"""

__author__      = "Aneesh Panoli"
__copyright__   = "MIT License"


import seaborn as sns
import rpy2
from rpy2.robjects import pandas2ri
from rpy2.robjects import r
import rpy2.robjects as robjects
import urllib.request as ur
import pandas as pd
from rpy2.robjects.packages import importr
import numpy as np

#supresses RRuntime import warnings
import warnings
from rpy2.rinterface import RRuntimeWarning
warnings.filterwarnings("ignore", category=RRuntimeWarning)



# do the following _only the first time_, to install the package Biobase
print("Loading R packages...")
base = importr('base')
base.source("http://www.bioconductor.org/biocLite.R")
biocinstaller = importr("BiocInstaller")
# biocinstaller.biocLite("IRanges", "suppressUpdates=TRUE")
biocinstaller.biocLite("Biobase",  suppressUpdates=True)

# load the installed package "Biobase"
biobase = importr("Biobase")
print("R package loading complete!")
#activate converter
pandas2ri.activate()



class Initialize:
  
  def __init__(self):

    self.R = robjects.r
  
  def download_rdata(self, url_name, dataset_name = 'R_data_set.RData'):
    ur.urlretrieve(url_name, dataset_name)
    print("Download complete! File saved as  {}".format(dataset_name))
    return dataset_name
  
  def load_rdata_as_eset(self, file_name):
    '''loads and returns RData to the R environment
    as an eSet'''
    data = self.R['load'](file_name)
    eset_name = data[0]
    return self.R[eset_name]
  
  def get_table_names(self, eset_name):
    '''returns table names in the eset'''
    print(tuple(eset_name.slots.keys()))
    
  def get_pd_dataframe(self, eset_name, fn_name):
    '''
      table names will give you hints on which function to use
      look up the package docs for fn_names
    '''
#     data = eset_name.slots[table_name]
    r_frame = self.R[fn_name](eset_name) #fn_name is a function from biobase package
    r_to_pd_frame = pandas2ri.ri2py(r_frame)
    return pd.DataFrame(data=r_to_pd_frame)
    
  
    
  
