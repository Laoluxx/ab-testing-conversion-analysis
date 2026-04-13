# 1. Load the library
import pandas as pd
import os
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

# 2. Load the actual file 
import pandas as pd
df = pd.read_csv(r"C:\Users\user\Downloads\project_folder\AB_testing_analysis\Data\marketing_AB.csv")
df.head()

#3. Dataset shape and structure 
df.shape
df.info()

#4. Check for missing values
df.isnull().sum()

df['test group'].unique()
df['converted'].unique()

df.duplicated(subset='user id').sum()
df = df.drop_duplicates(subset='user id')

df['converted'] = df['converted'].astype(int)

df.columns
df.columns = df.columns.str.strip().str.lower()
df.columns

#5. Group the data 
grouped = df.groupby('test group')['converted']

total_users = grouped.count()
total_users

total_conversions = grouped.sum()
total_conversions

conversion_rate = total_conversions / total_users
conversion_rate

#6. Summary
summary = pd.DataFrame({
    'Total Users': total_users,
    'Conversions': total_conversions,
    'Conversion Rate': conversion_rate
})

summary

#7. Visualization
import os

os.makedirs("visuals", exist_ok=True)

summary['Conversion Rate (%)'] = summary['Conversion Rate'] * 100

summary['Conversion Rate (%)'].plot(kind='bar')

plt.title('Conversion Rate by Test Group')
plt.xlabel('Test Group')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=0)

plt.tight_layout()

# Save the plot
plt.savefig("visuals/conversion_rate_by_group.png")

plt.show()

conversions = summary['Conversions'].values
users = summary['Total Users'].values

z_stat, p_value = proportions_ztest(count=conversions, nobs=users)

print("Z-statistic:", z_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Result: Reject the null hypothesis (Significant difference)")
else:
    print("Result: Fail to reject the null hypothesis (No significant difference)")

