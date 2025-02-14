import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Reported Cases dataset
file_path_cases = './vibrio_vulnifius_DataExtracted_KM - ReportedCases.csv'  # Adjust this path to your file location

cases_data = pd.read_csv(file_path_cases)

# Setting plot style for seaborn
sns.set(style="whitegrid")

# Yearly, Monthly, and Seasonal Distribution of Cases
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.countplot(x='Year.M', data=cases_data, palette='viridis')
plt.title('Yearly Distribution of Cases')
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
sns.countplot(x='Month.M', data=cases_data, palette='viridis', order=['January', 'February', 'March', 'April', 'May', 'June', 
                                                                     'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('Monthly Distribution of Cases')
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
sns.countplot(x='Season.M', data=cases_data, palette='viridis', order=['Winter', 'Spring', 'Summer', 'Fall'])
plt.title('Seasonal Distribution of Cases')
plt.tight_layout()
plt.show()

# Distribution of Cases by County and Coastal vs Non-Coastal Areas
plt.figure(figsize=(15, 5))
sns.countplot(x='County', data=cases_data, palette='viridis')
plt.title('Distribution of Cases by County')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(7, 5))
sns.countplot(x='Coastal', data=cases_data, palette='viridis')
plt.title('Cases in Coastal vs Non-Coastal Areas')
plt.show()

# Yearly, Monthly, and Seasonal Deaths
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.barplot(x='Year.M', y='Deaths.M1', data=cases_data, palette='viridis', estimator=sum)
plt.title('Yearly Deaths due to V. vulnificus')
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
sns.barplot(x='Month.M', y='Deaths.M1', data=cases_data, palette='viridis', order=['January', 'February', 'March', 'April', 'May', 'June', 
                                                                                 'July', 'August', 'September', 'October', 'November', 'December'], estimator=sum)
plt.title('Monthly Deaths due to V. vulnificus')
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
sns.barplot(x='Season.M', y='Deaths.M1', data=cases_data, palette='viridis', order=['Winter', 'Spring', 'Summer', 'Fall'], estimator=sum)
plt.title('Seasonal Deaths due to V. vulnificus')
plt.tight_layout()
plt.show()

# Relationship between Cases and Deaths
plt.figure(figsize=(7, 5))
sns.scatterplot(x='Cases.M1', y='Deaths.M1', data=cases_data)
plt.title('Relationship between Cases and Deaths')
plt.xlabel('Number of Cases')
plt.ylabel('Number of Deaths')
plt.show()

# Distribution of Cases and Deaths by NOAA Station
plt.figure(figsize=(15, 7))
sns.countplot(x='NOAA_Stat', data=cases_data, palette='viridis')
plt.title('Distribution of Cases by NOAA Station')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15, 7))
sns.barplot(x='NOAA_Stat', y='Deaths.M1', data=cases_data, palette='viridis', estimator=sum)
plt.title('Total Deaths by NOAA Station')
plt.xticks(rotation=90)
plt.show()
