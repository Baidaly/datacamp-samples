'''
Setup the Engine and MetaData

In this exercise, your job is to create an engine to the database that will be used in this chapter. Then, you need to initialize its metadata.

Recall how you did this in Chapter 1 by leveraging create_engine() and MetaData.
'''
# Import create_engine, MetaData
from sqlalchemy import (create_engine, MetaData)

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()
