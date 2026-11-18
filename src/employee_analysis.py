#!/usr/bin/env python
# coding: utf-8

# # Employee Performance Analysis
# 
# ## Week 1 Assessment - Git, Terminal and Notebook
# 
# ### Objective
# Analyze employee salary and department data using Python, Pandas and Matplotlib.
# 
# ### Dataset
# The dataset contains 8 employees with the following columns:
# - Employee ID
# - Name
# - Department
# - Salary
# - City

# In[2]:


# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load employee dataset
df = pd.read_csv("../data/employees.csv")

# Display first five records
df.head()


# In[3]:


# Check dataset dimensions
print("Dataset Shape:", df.shape)

# Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check data types and missing values
print("\nDataset Information:")
df.info()

# Generate statistical summary
print("\nStatistical Summary:")
df.describe()


# ## df.shape – displays rows and columns.
# 
# ## df.columns – displays column names.
# 
# ## df.info() – shows data types and non-null counts.
# 
# ## df.describe() – calculates salary and other numerical statistics.

# In[6]:


# Count employees in each department
department_count = df["department"].value_counts()

print("Employee Count by Department:")
print(department_count)

# Calculate average salary by department
department_salary = df.groupby("department")["salary"].mean()

print("\nAverage Salary by Department:")
print(department_salary)


# In[7]:


# Filter employees from Chennai
chennai_employees = df[df["city"] == "Chennai"]

print("Employees from Chennai:")
display(chennai_employees)

# Count Chennai employees
print("\nTotal Chennai Employees:", len(chennai_employees))

# Calculate average salary in Chennai
print(
    "Average Chennai Salary:",
    chennai_employees["salary"].mean()
)


# In[9]:


# Measure execution time of department-wise salary calculation

get_ipython().run_line_magic('timeit', 'df.groupby("department")["salary"].mean()')


# In[11]:


# Calculate average salary by department
department_salary = df.groupby("department")["salary"].mean()

# Create bar chart
plt.figure(figsize=(8, 5))
department_salary.plot(kind="bar")

# Add chart title and labels
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")

# Display values on bars
for index, value in enumerate(department_salary):
    plt.text(index, value, f"{value:.0f}", ha="center", va="bottom")

plt.tight_layout()
plt.show()


# ## Key Findings
# 
# 1. The dataset contains 8 employees across 4 departments.
# 2. The IT department has the highest employee count with 3 employees.
# 3. The Finance department has the highest average salary of INR 90,000.
# 4. Chennai has 4 employees with an average salary of INR 54,500.
# 5. Department-wise salary analysis was performed using Pandas and visualized using Matplotlib.
# 
# ## Performance Measurement
# 
# The `%timeit` magic command was used to measure the execution time of department-wise salary calculation.
# 
# ## Conclusion
# 
# This analysis demonstrates employee data exploration, department-wise salary comparison, city-based filtering, execution-time measurement, and data visualization using Python.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:

# Final analysis summary
print("\n========== FINAL ANALYSIS SUMMARY ==========")
print("Total Employees:", len(df))
print("Total Departments:", df["department"].nunique())
print("Chennai Employees:", len(chennai_employees))
print("Average Chennai Salary:", chennai_employees["salary"].mean())
print("============================================")



