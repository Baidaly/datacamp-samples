# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query('SELECT * FROM Album', engine)
# Equals to 
# with engine.connect() as con:
#     rs = con.execute('SELECT LastName, Title from Employee')
#     df = pd.DataFrame(rs.fetchmany(size=3)) # or rs.fetchall()
#     df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
