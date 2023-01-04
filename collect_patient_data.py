# import Libraries
import numpy as np
import pandas as pd
import os
from collections import Counter

# define path
aff_path = 'resize/AFF'
control_path = 'resize/CONTROL'

# collect all file names based on class
affListing = os.listdir(aff_path)
controlListing = os.listdir(control_path)

# define classes
classes = ['AFF', 'CONTROL']

# collect all AFF file names in a list
affFileNames = []
for item in affListing:
    if ".png" in item:
        affFileNames.append(item)

print(f'Total AFF files: {len(affFileNames)}')

# collect all control file names in a list
controlFileNames = []
for item in controlListing:
    if ".png" in item:
        controlFileNames.append(item)

print(f'Total Control files: {len(controlFileNames)}')


# create df
# AFF
affNamesShort = [i.split('_') for i in affFileNames]
affPatientNum = [l[:2] for l in affNamesShort]
affPatientNum = ['_'.join(l) for l in affPatientNum]
affPatientImageCount = Counter(affPatientNum)

affDF = pd.DataFrame.from_dict(affPatientImageCount, orient='index').reset_index()
affDF.columns = ['patientNumber', 'imageCount']
affDF['class'] = 'AFF'


# CONTROL
controlNamesShort = [i.split('_') for i in controlFileNames]
controlPatientNum = [l[:2] for l in controlNamesShort]
controlPatientNum = ['_'.join(l) for l in controlPatientNum]
controlPatientImageCount = Counter(controlPatientNum)

controlDF = pd.DataFrame.from_dict(controlPatientImageCount, orient='index').reset_index()
controlDF.columns = ['patientNumber', 'imageCount']
controlDF['class'] = 'CONTROL'


# Final DF
finalDF = pd.concat([affDF, controlDF], axis=0)
print(finalDF.sample(6))


# Export data to CSV
os.makedirs('data', exist_ok=True)  
finalDF.to_csv('data/patientPNGImageCount.csv')