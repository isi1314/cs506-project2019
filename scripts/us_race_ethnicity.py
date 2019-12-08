from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
import numpy as np
import pandas as pd

from pandas import *

#reading dataset
df = pd.read_csv('../datasets/data_all_no_naics_proc_no_duplicates_owners_full_fin.csv', index_col=0)
len_df = len(df)

print (len_df)
print(df.columns)

# Configure API key authorization: api_key
configuration = openapi_client.Configuration()
configuration.api_key['X-API-KEY'] = '04f8df5b91aa6c70be88d2d3db870550'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

api_instance = openapi_client.PersonalApi(openapi_client.ApiClient(configuration))
for i in range(len_df):
# create an instance of the API class
	name_full = df.loc[i,'Contact']

	try:
	    # Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 
	    api_response = api_instance.parse_name(name_full)
	    df.loc[i,'first_name']= api_response.first_last_name.first_name
	    df.loc[i,'last_name']= api_response.first_last_name.last_name
	    api_response2 = api_instance.us_race_ethnicity(df.loc[i,'first_name'], df.loc[i,'last_name'])
	    df.loc[i,'race_ethnicity']= api_response2.race_ethnicity
	    df.loc[i,'race_ethnicity_alt']= api_response2.race_ethnicity_alt
	except ApiException as e:
	    print("Exception when calling PersonalApi->parse_name: %s\n" % e)

#save to csv
df.to_csv('../datasets/data_all_no_naics_proc_no_duplicates_owners_full_fin_names.csv')