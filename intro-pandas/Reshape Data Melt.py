import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
   ds = pd.melt(report, id_vars = ['product'], var_name='quarter', value_name= 'sales' )
   return ds
