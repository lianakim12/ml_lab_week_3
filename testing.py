import pandas as pd  # For data manipulation and analysis
college_df = pd.read_csv('/workspaces/ml_lab_week_3/data/cc_institution_details.csv')
job_df = pd.read_csv('/workspaces/ml_lab_week_3/data/Placement_Data_Full_Class.csv')
print(college_df.info())