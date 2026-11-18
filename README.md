# Week 1 Assessment - Git, Terminal and Notebook

## Project Overview
Employee Performance Analysis using Python, Pandas, NumPy, Matplotlib and Jupyter Notebook.

## Project Structure
- data/ - Employee CSV dataset
- notebooks/ - Jupyter analysis notebook
- reports/ - Original employee dataset
- src/ - Exported Python analysis script

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/kalyanasundar66/week1-assessment.git

2. Navigate to the project:
   cd week1-assessment

3. Install required libraries:
   pip install pandas numpy matplotlib notebook nbconvert

4. Start Jupyter:
   python -m notebook

5. Open notebooks/employee_analysis.ipynb.

## Key Findings

1. The dataset contains 8 employees across 4 departments.
2. The IT department has the highest employee count with 3 employees.
3. Finance has the highest average salary of INR 90,000.
4. Chennai has 4 employees with an average salary of INR 54,500.
5. Department-wise salary analysis was performed using Pandas and visualized using Matplotlib.

## Performance Measurement
Used the Jupyter %timeit magic command to measure execution time.

## Technologies Used
Python, Pandas, NumPy, Matplotlib, Jupyter Notebook, Git and GitHub.

## Analysis Workflow

1. Load employee data from the CSV file using Pandas.
2. Explore dataset dimensions, columns and statistical summaries.
3. Calculate employee counts and average salaries by department.
4. Filter employees based on city.
5. Measure execution time using `%timeit`.
6. Visualize average department salaries using Matplotlib.