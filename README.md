# Week 1 Assessment - Git, Terminal and Notebook

## Project Overview

This project delivers an employee performance and salary analysis using Python, Pandas, NumPy, Matplotlib, and Jupyter Notebook.

It demonstrates data exploration, department-wise salary analysis, city-based employee filtering, data visualization, Git version control, and terminal operations.

## Project Structure

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

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/kalyanasundar66/week1-assessment.git
```

### 2. Navigate to the project

```bash
cd week1-assessment
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib notebook nbconvert
```

### 4. Start Jupyter Notebook

```bash
python -m notebook
```

### 5. Open the analysis notebook

Open `notebooks/employee_analysis.ipynb` and run the notebook cells.

### 6. Run the exported Python script

```bash
python src/employee_analysis.py
```

## Key Findings

1. The dataset contains **8 employees** across **4 departments**.
2. The IT department has the highest employee count, with **3 employees**.
3. Finance has the highest average salary of **INR 90,000**.
4. Chennai has **4 employees** with an average salary of **INR 54,500**.
5. Department-wise salary analysis was performed using Pandas and visualized using Matplotlib.

## Performance Measurement

Used the Jupyter `%timeit` magic command to measure the execution time of the department-wise average salary calculation.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git and GitHub

## Analysis Workflow

1. Load employee data from the CSV file using Pandas.
2. Explore dataset dimensions, columns, and statistical summaries.
3. Calculate employee counts and average salaries by department.
4. Filter employees based on city.
5. Measure execution time using `%timeit`.
6. Visualize average department salaries using Matplotlib.

## Git Workflow

- Created a GitHub repository named `week1-assessment`.
- Created and worked on the `feature/analysis` branch.
- Completed multiple small commits with descriptive messages.
- Modified README.md on both branches to create a deliberate merge conflict.
- Resolved the conflict through a Pull Request.
- Merged the feature branch into `main`.
- Captured the Git commit history using `git log --oneline --graph`.

## Submission Links

- **GitHub Repository:** https://github.com/kalyanasundar66/week1-assessment
- **Pull Request:** https://github.com/kalyanasundar66/week1-assessment/pull/1

## Conclusion

This project demonstrates practical experience with Git version control, terminal-based file management, Jupyter Notebook, Python data analysis, performance measurement, data visualization, and project documentation.