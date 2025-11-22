import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt

def fetch_employee_info(source_url):
    try:
        result = requests.get(source_url)
        result.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    soup = BeautifulSoup(result.text, "html.parser")
    data_table = soup.find("table")

    if data_table is None:
        print("No table found in the HTML content.")
        return []

    employee_list = []
    table_rows = data_table.select("tr")[1:]

    for row in table_rows:
        columns = row.find_all("td")
        if len(columns) == 4:
            employee = [cell.get_text(strip=True) for cell in columns]
            employee_list.append(employee)

    return employee_list

def export_to_csv(records, filename="employees.csv"):
    if not records:
        print("No employee records to export.")
        return

    with open(filename, mode="w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Employee Name", "Job Title", "Department", "Email Address"])
        csv_writer.writerows(records)

    print(f"Export complete: {filename}")

def generate_report(records):
    if not records:
        print("No data available for analysis.")
        return

    df = pd.DataFrame(records, columns=["Employee Name", "Job Title", "Department", "Email Address"])

    dept_distribution = df["Department"].value_counts()
    title_distribution = df["Job Title"].value_counts()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    dept_distribution.plot(kind="bar", ax=ax1, color="cornflowerblue", edgecolor="black")
    ax1.set_title("Employees by Department")
    ax1.set_xlabel("Department")
    ax1.set_ylabel("Count")
    ax1.tick_params(axis='x', rotation=45)

    title_distribution.plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax2)
    ax2.set_title("Distribution by Job Title")
    ax2.set_ylabel("")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    target_url = "http://darkmind.uk/SCRAPESITE/employees.html"
    employees = fetch_employee_info(target_url)

    export_to_csv(employees)
    generate_report(employees)
