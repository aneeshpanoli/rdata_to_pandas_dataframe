# Rdata_to_pandas_dataframe
Converts expression data in RData format to pandas dataframe to work in python enviornment

# Usage
```python
from rdata_to_pandas_dataframe import convert  
r2df = convert.Initialize()  
url_name = "http://bowtie-bio.sourceforge.net/recount/ExpressionSets/bodymap_eset.RData"  
r2df.download_rdata(url_name, "body_map_eset.RData")  

eset = r2df.load_rdata_as_eset(file)  
r2df.get_table_names(eset)  
pdata_df = r2df.get_pd_dataframe(eset, 'pData') # phenotype data
fdata_df = r2df.get_pd_dataframe(eset, 'fData') # feature data
edata_df = r2df.get_pd_dataframe(eset, 'exprs') # expression data
```

# Requirements
seaborn  
rpy2  
urllib  
pandas  
numpy  
