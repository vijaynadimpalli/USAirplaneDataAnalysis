def floatconversion(data):
 floatcol=[X for X in data.dtypes.index if data.dtypes[X]=='float64']
 for col in floatcol:
  data.loc[:,col]=pd.to_numeric(data.loc[:,col],downcast='float')
 return data 
 
 
def intconversion(data):
 intcol=[X for X in data.dtypes.index if data.dtypes[X]=='int64']
 for col in intcol:
  data.loc[:,col]=pd.to_numeric(data.loc[:,col],downcast='integer')
 return data 
 
def catconversion(data):
 catcol=[X for X in data.dtypes.index if data.dtypes[X]=='object']
 for col in catcol:
  num_unique_values = len(data[col].unique())
  num_total_values = len(data[col])
  if num_unique_values / num_total_values < 0.5:
    data.loc[:,col] = data[col].astype('category')
  else:
    data.loc[:,col] = data[col]
 return data 
 
 
def dtypeconversion(data):
 floatconversion(data)
 intconversion(data)
 catconversion(data)
 return data 
 
 
def main(df):
    df=dtypeconversion(df) #df is your dataframe which needs dtype conversion.
    colnames = dtypes.index
    types = [i.name for i in df.dtypes.values]
    column_types = dict(zip(colnames, types))
    print(types)
    return column_types
