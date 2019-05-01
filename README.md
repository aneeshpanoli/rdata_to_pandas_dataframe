# Rdata_to_pandas_dataframe
Convert expression data in RData format to pandas dataframe

# Usage
```python
from rdata_to_pandas_dataframe import convert  
r2df = convert.Initialize()  
url_name = "http://bowtie-bio.sourceforge.net/recount/ExpressionSets/bodymap_eset.RData"  
r2df.download_rdata(url_name, "body_map_eset.RData")  
```

# Requirements
seaborn  
rpy2  
urllib  
pandas  
numpy  
