# Week 1 Assessment – Git, Terminal and Notebook

## 1. Project Overview

This project demonstrates employee performance and salary analysis using Python, Pandas, NumPy, Matplotlib, and Jupyter Notebook.

It covers data exploration, department-wise salary analysis, city-based employee filtering, data visualization, performance measurement, Git version control, branching, merge conflict resolution, and terminal operations.

## 2. Project Structure

```text
week1-assessment/
│
├── data/
│   └── employees.csv
│
├── notebooks/
│   └── employee_analysis.ipynb
│
├── reports/
│   ├── employees_original.csv
│   └── analysis_report.md
│
├── src/
│   └── employee_analysis.py
│
├── Screenshot.png
├── .gitignore
└── README.md
```

## 3. Setup Instructions

### Step 1: Clone the Repository

```bash
# Clone the Week 1 assessment repository
git clone https://github.com/kalyanasundar66/week1-assessment.git
```

### Step 2: Navigate to the Project Directory

```bash
# Open the cloned project folder
cd week1-assessment
```

### Step 3: Install Required Libraries

```bash
# Install the libraries required for data analysis and notebooks
python -m pip install pandas numpy matplotlib notebook nbconvert
```

### Step 4: Start Jupyter Notebook

```bash
# Install 
# Launch the Jupyter Notebook server

python -m pip install notebook

python -m notebook
```

### Step 5: Open the Analysis Notebook

Open the following notebook in Jupyter:

```text
notebooks/employee_analysis.ipynb
```

Run the notebook cells sequentially to perform employee data analysis.

### Step 6: Execute the Python Script

```bash
# Run the exported Python analysis script
python src/employee_analysis.py
```

## 4. Key Findings

The employee dataset analysis produced the following findings:

1. The dataset contains **8 employees** across **4 departments**.
2. The IT department has the highest employee count, with **3 employees**.
3. Finance has the highest average salary of **INR 90,000**.
4. Chennai has **4 employees**, with an average salary of **INR 54,500**.
5. Department-wise salary analysis was performed using Pandas and visualized using Matplotlib.

## 5. Performance Measurement

Used the Jupyter Notebook `%timeit` magic command to measure the execution time of the department-wise average salary calculation.

Example:

```python
# Measure the execution time of department-wise average salary calculation
%timeit df.groupby("department")["salary"].mean()
```

This helped evaluate the execution performance of the Pandas operation.

## 6. Analysis Workflow

The project follows these steps:

1. Load employee data from the CSV file using Pandas.
2. Explore dataset dimensions, columns, and statistical summaries.
3. Calculate employee counts and average salaries by department.
4. Filter employees based on their city.
5. Measure execution time using the `%timeit` command.
6. Visualize department-wise average salaries using Matplotlib.
7. Export the analysis into a Python script and report.

## 7. Git Workflow and Version Control

The following Git operations were performed as part of the assessment:

1. Created a GitHub repository named `week1-assessment`.
2. Created and worked on the `feature/analysis` branch.
3. Completed multiple commits with descriptive commit messages.
4. Modified `README.md` on both branches to intentionally create a merge conflict.
5. Resolved the merge conflict through a Pull Request.
6. Reviewed and merged the feature branch into `main`.
7. Captured the Git commit history using `git log --oneline --graph`.

### Useful Git Commands

```bash
# Check the current working tree status
git status

# Display all local branches
git branch

# Create and switch to the feature branch
git checkout -b feature/analysis

# Stage project changes
git add .

# Commit changes with a descriptive message
git commit -m "Complete employee data analysis"

# Display commit history in graph format
git log --oneline --graph

# Push the feature branch to GitHub
git push -u origin feature/analysis
```

## 8. Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python | Programming and data analysis |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Jupyter Notebook | Interactive Python development |
| Git | Version control |
| GitHub | Repository hosting and collaboration |
| Terminal / PowerShell | Command execution and project management |

## 9. Submission Links

- **GitHub Repository:** https://github.com/kalyanasundar66/week1-assessment
- **Pull Request:** https://github.com/kalyanasundar66/week1-assessment/pull/1

## 10. Conclusion

Successfully completed the Week 1 assessment by implementing employee data analysis using Python, Pandas, NumPy, and Matplotlib.

The project also demonstrates practical experience with Git version control, terminal-based file management, Jupyter Notebook, performance measurement, feature branching, commit history, Pull Requests, and merge conflict resolution.

This assessment strengthened practical understanding of Python data analysis and collaborative software development workflows.