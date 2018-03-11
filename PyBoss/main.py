import pandas as pd

csv_path="employee_data1.csv"
empData= pd.read_csv(csv_path, encoding="utf-8")
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
empData["SSN"]= "***-**-"+empData["SSN"].str[-4:]
empData["DOB"] = empData["DOB"].str.replace("-","/")
empData["DOB"]= empData["DOB"].str[-5:]+"/"+empData["DOB"].str[:4]
empData[["Name","Last Name"]]= empData.Name.str.split(" ",expand=True)
empData["State"] = empData["State"].map(us_state_abbrev)
empClean = empData.rename(columns={"Name":"First Name",})

empNew = empClean[["Emp ID","First Name","Last Name","DOB","SSN","State"]]
empNew.to_csv("Converted_Employee_Data.csv", index=False, header=True)
empNew.head()