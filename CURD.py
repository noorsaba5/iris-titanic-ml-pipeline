{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "view-in-github"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/noorsaba5/Analysing-Data/blob/main/Untitled4.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4a6262d1"
      },
      "source": [
        "Let's create the foundational structure for the expense tracker. This will include a list to store our expenses and functions for the core CRUD (Create, Read, Update, Delete) operations, as well as a main menu to navigate these features."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "32a5db32"
      },
      "outputs": [],
      "source": [
        "expenses = []\n",
        "\n",
        "def add_expense():\n",
        "    \"\"\"Adds a new expense to the tracker.\"\"\"\n",
        "    print(\"\\n--- Add Expense ---\")\n",
        "    date = input(\"Enter date (YYYY-MM-DD): \")\n",
        "    category = input(\"Enter category: \")\n",
        "    try:\n",
        "        amount = float(input(\"Enter amount: \"))\n",
        "    except ValueError:\n",
        "        print(\"Invalid amount. Please enter a number.\")\n",
        "        return\n",
        "    description = input(\"Enter description: \")\n",
        "\n",
        "    expense = {\n",
        "        'date': date,\n",
        "        'category': category,\n",
        "        'amount': amount,\n",
        "        'description': description\n",
        "    }\n",
        "    expenses.append(expense)\n",
        "    print(f\"✅ Expense added: {description} | {category} | ${amount:.2f}\")\n",
        "\n",
        "def view_expenses():\n",
        "    \"\"\"Displays all recorded expenses.\"\"\"\n",
        "    print(\"\\n--- View Expenses ---\")\n",
        "    if not expenses:\n",
        "        print(\"No expenses recorded yet.\")\n",
        "        return\n",
        "\n",
        "    for i, expense in enumerate(expenses):\n",
        "        print(f\"{i+1}. Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}\")\n",
        "\n",
        "def update_expense():\n",
        "    \"\"\"Updates an existing expense based on its index.\"\"\"\n",
        "    print(\"\\n--- Update Expense ---\")\n",
        "    if not expenses:\n",
        "        print(\"No expenses to update.\")\n",
        "        return\n",
        "\n",
        "    view_expenses()\n",
        "    try:\n",
        "        index = int(input(\"Enter the number of the expense to update: \")) - 1\n",
        "        if not (0 <= index < len(expenses)):\n",
        "            print(\"Invalid expense number.\")\n",
        "            return\n",
        "    except ValueError:\n",
        "        print(\"Invalid input. Please enter a number.\")\n",
        "        return\n",
        "\n",
        "    expense = expenses[index]\n",
        "    print(f\"Updating expense: {expense['description']} (${expense['amount']:.2f})\")\n",
        "\n",
        "    new_date = input(f\"Enter new date (YYYY-MM-DD) (current: {expense['date']}): \")\n",
        "    new_category = input(f\"Enter new category (current: {expense['category']}): \")\n",
        "    new_amount_str = input(f\"Enter new amount (current: {expense['amount']:.2f}): \")\n",
        "    new_description = input(f\"Enter new description (current: {expense['description']}): \")\n",
        "\n",
        "    if new_date: expense['date'] = new_date\n",
        "    if new_category: expense['category'] = new_category\n",
        "    if new_description: expense['description'] = new_description\n",
        "    if new_amount_str:\n",
        "        try:\n",
        "            expense['amount'] = float(new_amount_str)\n",
        "        except ValueError:\n",
        "            print(\"Invalid amount. Amount not updated.\")\n",
        "\n",
        "    print(\"✅ Expense updated successfully!\")\n",
        "\n",
        "def delete_expense():\n",
        "    \"\"\"Deletes an expense based on its index.\"\"\"\n",
        "    print(\"\\n--- Delete Expense ---\")\n",
        "    if not expenses:\n",
        "        print(\"No expenses to delete.\")\n",
        "        return\n",
        "\n",
        "    view_expenses()\n",
        "    try:\n",
        "        index = int(input(\"Enter the number of the expense to delete: \")) - 1\n",
        "        if not (0 <= index < len(expenses)):\n",
        "            print(\"Invalid expense number.\")\n",
        "            return\n",
        "    except ValueError:\n",
        "        print(\"Invalid input. Please enter a number.\")\n",
        "        return\n",
        "\n",
        "    deleted_expense = expenses.pop(index)\n",
        "    print(f\"✅ Expense deleted: {deleted_expense['description']} | ${deleted_expense['amount']:.2f}\")\n",
        "\n",
        "def main_menu():\n",
        "    \"\"\"Displays the main menu and handles user choices.\"\"\"\n",
        "    while True:\n",
        "        print(\"\\n===== Personal Expense Tracker =====\")\n",
        "        print(\"1. Add Expense\")\n",
        "        print(\"2. View Expenses\")\n",
        "        print(\"3. Update Expense\")\n",
        "        print(\"4. Delete Expense\")\n",
        "        print(\"5. Exit\")\n",
        "\n",
        "        choice = input(\"Enter your choice: \")\n",
        "\n",
        "        if choice == '1':\n",
        "            add_expense()\n",
        "        elif choice == '2':\n",
        "            view_expenses()\n",
        "        elif choice == '3':\n",
        "            update_expense()\n",
        "        elif choice == '4':\n",
        "            delete_expense()\n",
        "        elif choice == '5':\n",
        "            print(\"Exiting Expense Tracker. Goodbye!\")\n",
        "            break\n",
        "        else:\n",
        "            print(\"Invalid choice. Please try again.\")\n",
        "\n",
        "# To run the tracker, uncomment the line below:\n",
        "# main_menu()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None
,
      "metadata": {
        "id": "apfG-VhhaeGt"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "authorship_tag": "ABX9TyPWfs3tCylKYjjp1MoekaET",
      "include_colab_link": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
