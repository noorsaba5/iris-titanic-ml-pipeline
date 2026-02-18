# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace contains a series of Jupyter notebooks focused on data science and Python programming exercises. The main artifacts are:
- Multiple session-based notebooks (`Session1.ipynb` to `Session8.ipynb`)
- Assignment notebooks
- A personal expense tracker notebook
- A CSV data file (`stores.csv`)

## Architecture & Data Flow
- **Notebook-centric workflow:** All code, analysis, and documentation are organized in Jupyter notebooks. Each notebook is self-contained, but may share data files (e.g., `stores.csv`).
- **Data files:** Place any shared datasets in the workspace root. Notebooks typically load data using pandas (`pd.read_csv('stores.csv')`).
- **No explicit Python modules or scripts**—all logic is in notebook cells.

## Developer Workflow
- **Edit and run code in Jupyter notebooks.**
- **Data loading:** Use pandas for reading CSVs. Example:
  ```python
  import pandas as pd
  df = pd.read_csv('stores.csv')
  ```
- **No build or test scripts** are present. Validation is manual via notebook cell execution.
- **Debugging:** Use notebook cell outputs and exception traces. There are no custom logging or error-handling frameworks.

## Project-Specific Patterns
- **Session notebooks** follow a sequential naming convention (`SessionN.ipynb`).
- **Assignments** are named with clear identifiers (e.g., `Assignment 1 - Python NOOR SABA.ipynb`).
- **Expense tracker** notebook is for personal finance analysis.
- **Data files** are referenced with relative paths from the workspace root.

## Integration Points
- **External dependencies:** Primarily pandas. Install with:
  ```python
  !pip install pandas
  ```
  (or use notebook package management tools)
- **No cross-component communication**—notebooks are independent.

## Conventions & Recommendations
- Keep all notebooks and data files in the workspace root for easy access.
- Use clear, descriptive notebook names for new work.
- Document analysis steps and results in markdown cells within notebooks.
- When adding new data, prefer CSV format and update relevant notebooks to load the new file.

## Example: Loading Data in a Notebook
```python
import pandas as pd
df = pd.read_csv('stores.csv')
df.head()
```

---
*Update this file if new workflows, dependencies, or conventions are introduced.*
