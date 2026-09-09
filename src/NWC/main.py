import datetime
from dataclasses import asdict
import numpy as np
import numbers
import pandas as pd
from pandas import DataFrame
import tkinter as tk
from tkinter import ttk

from NWC.accounts import bankAccount, investmentAccount
from NWC.incomes import salary, inheritance
from NWC.debts import studentLoans, carLoan


# --- Functions to create bank and investment accounts ---
def create_rkb_accounts() -> DataFrame:
    pnc_checking = bankAccount(
        institution="PNC",
        type="checking",
        owner="RKB",
        value=5495.09,
        interest_percent=0.0,
        last_updated=datetime.datetime(2026, 7, 14),
    )

    discover_savings = bankAccount(
        institution="Discover (Capital One)",
        type="savings",
        owner="RKB",
        value=19441,
        interest_percent=3.09,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    roth_ira = investmentAccount(
        institution="Fidelity",
        type="IRA",
        tax_advantage="Roth",
        owner="RKB",
        value=55915.06,
        principal=36188.76,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    trad_401k = investmentAccount(
        institution="Voya",
        type="401k",
        tax_advantage="Traditional",
        owner="RKB",
        value=10043.84,
        principal=0.0,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    roth_401k = investmentAccount(
        institution="Voya",
        type="401k",
        tax_advantage="Roth",
        owner="RKB",
        value=10461.92,
        principal=0.0,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    hsa_cash = investmentAccount(
        institution="MoneyWise",
        type="HSA",
        tax_advantage="Triple",
        owner="RKB",
        value=2165.47,
        principal=2165.47,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    hsa_invest = investmentAccount(
        institution="MoneyWise",
        type="HSA",
        tax_advantage="Triple",
        owner="RKB",
        value=2298.79,
        principal=0.0,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    brokerage = investmentAccount(
        institution="Fidelity",
        type="Brokerage",
        tax_advantage="None",
        owner="RKB",
        value=50552.46,
        principal=30623.96,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    accounts_list = [
        pnc_checking,
        discover_savings,
        roth_ira,
        trad_401k,
        roth_401k,
        hsa_cash,
        hsa_invest,
        brokerage,
    ]
    df = pd.DataFrame([asdict(account) for account in accounts_list])
    columns = [
        "institution",
        "type",
        "tax_advantage",
        "owner",
        "value",
        "principal",
        "interest_percent",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_rcp_accounts() -> DataFrame:
    checking = bankAccount(
        institution="PNC",
        type="checking",
        owner="RCP",
        value=0.0,
        interest_percent=0.0,
        last_updated=datetime.datetime(2026, 9, 7),
    )

    savings = bankAccount(
        institution="Discover (Capital One)",
        type="savings",
        owner="RCP",
        value=0.0,
        interest_percent=0.0,
        last_updated=datetime.datetime(2026, 9, 7),
    )

    roth_ira = investmentAccount(
        institution="SEI",
        type="IRA",
        tax_advantage="Roth",
        owner="RCP",
        value=8621.17,
        principal=0.0,
        last_updated=datetime.datetime(2026, 7, 29),
    )

    trad_403b = investmentAccount(
        institution="Voya",
        type="401k",
        tax_advantage="Traditional",
        owner="RCP",
        value=0.0,
        principal=0.0,
        last_updated=datetime.datetime(2026, 9, 7),
    )

    roth_403b = investmentAccount(
        institution="Voya",
        type="401k",
        tax_advantage="Roth",
        owner="RCP",
        value=0.0,
        principal=0.0,
        last_updated=datetime.datetime(2026, 9, 7),
    )

    accounts_list = [checking, savings, roth_ira, trad_403b, roth_403b]
    df = pd.DataFrame([asdict(account) for account in accounts_list])
    columns = [
        "institution",
        "type",
        "tax_advantage",
        "owner",
        "value",
        "principal",
        "interest_percent",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_shared_accounts() -> DataFrame:
    cap1_checking = bankAccount(
        institution="Capital One",
        type="checking",
        owner="Shared",
        value=15263.0,
        interest_percent=0.1,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    cap1_savings = bankAccount(
        institution="Capital One",
        type="savings",
        owner="Shared",
        value=21307.0,
        interest_percent=3.0,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    marcus_savings = bankAccount(
        institution="Marcus",
        type="savings",
        owner="Shared",
        value=51436.39,
        interest_percent=3.4,
        last_updated=datetime.datetime(2026, 6, 30),
    )

    accounts_list = [
        cap1_checking,
        cap1_savings,
        marcus_savings,
    ]
    df = pd.DataFrame([asdict(account) for account in accounts_list])
    df["tax_advantage"] = "NaN"
    df["principal"] = "NaN"
    columns = [
        "institution",
        "type",
        "tax_advantage",
        "owner",
        "value",
        "principal",
        "interest_percent",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_accounts_df() -> DataFrame:
    rkb_accounts_df = create_rkb_accounts()
    rcp_accounts_df = create_rcp_accounts()
    shared_accounts_df = create_shared_accounts()

    all_accounts_df = pd.concat(
        [rkb_accounts_df, rcp_accounts_df, shared_accounts_df], ignore_index=True
    )
    all_accounts_df.loc["Total", "institution"] = "TOTAL"
    all_accounts_df.loc["Total", "value"] = all_accounts_df["value"].sum()

    return all_accounts_df


# --- Functions to create salary and inheritance incomes ---
def create_rkb_incomes() -> DataFrame:

    hl_yearly_salary = 110_000
    hunterlab_salary = salary(
        institution="HunterLab",
        owner="RKB",
        monthly_value=hl_yearly_salary / 12,
        yearly_value=hl_yearly_salary,
        last_updated=datetime.datetime(2026, 9, 8),
    )

    inher_monthly = 2_450
    rkb_inheritance = inheritance(
        institution="Inheritance",
        owner="RKB",
        monthly_value=inher_monthly,
        yearly_value=inher_monthly * 12,
        last_updated=datetime.datetime(2026, 9, 8),
    )

    incomes_list = [
        hunterlab_salary,
        rkb_inheritance,
    ]
    df = pd.DataFrame([asdict(income) for income in incomes_list])
    columns = [
        "institution",
        "owner",
        "monthly_value",
        "yearly_value",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_rcp_incomes() -> DataFrame:

    trinity_yearly_salary = 80_000
    trinity_salary = salary(
        institution="Trinity Washington",
        owner="RCP",
        monthly_value=trinity_yearly_salary / 12,
        yearly_value=trinity_yearly_salary,
        last_updated=datetime.datetime(2026, 9, 8),
    )

    incomes_list = [
        trinity_salary,
    ]
    df = pd.DataFrame([asdict(income) for income in incomes_list])
    columns = [
        "institution",
        "owner",
        "monthly_value",
        "yearly_value",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_shared_incomes() -> DataFrame:

    incomes_list = []
    df = pd.DataFrame([asdict(income) for income in incomes_list])
    columns = [
        "institution",
        "owner",
        "monthly_value",
        "yearly_value",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_incomes_df() -> DataFrame:
    rkb_incomes_df = create_rkb_incomes()
    rcp_incomes_df = create_rcp_incomes()
    # shared_incomes_df = create_shared_incomes()

    all_incomes_df = pd.concat([rkb_incomes_df, rcp_incomes_df], ignore_index=True)
    all_incomes_df.loc["Total", "institution"] = "TOTAL"
    all_incomes_df.loc["Total", "monthly_value"] = all_incomes_df["monthly_value"].sum()
    all_incomes_df.loc["Total", "yearly_value"] = all_incomes_df["yearly_value"].sum()

    return all_incomes_df


# --- Functions to create debts ---
def create_rkb_debts() -> DataFrame:

    student_monthly_value = 293
    months_remaining = 72
    rkb_studentLoans = studentLoans(
        institution="Nelnet",
        owner="RKB",
        monthly_value=student_monthly_value,
        yearly_value=student_monthly_value * 12,
        remaining_total=student_monthly_value * months_remaining,
        months_remaining=months_remaining,
        last_updated=datetime.datetime(2026, 9, 8),
    )

    incomes_list = [
        rkb_studentLoans,
    ]
    df = pd.DataFrame([asdict(income) for income in incomes_list])
    columns = [
        "institution",
        "owner",
        "monthly_value",
        "yearly_value",
        "remaining_total",
        "months_remaining",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_rcp_debts() -> DataFrame:

    incomes_list = []
    df = pd.DataFrame([asdict(income) for income in incomes_list])
    columns = [
        "institution",
        "owner",
        "monthly_value",
        "yearly_value",
        "remaining_total",
        "months_remaining",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_shared_debts() -> DataFrame:

    incomes_list = []
    df = pd.DataFrame([asdict(income) for income in incomes_list])
    columns = [
        "institution",
        "owner",
        "monthly_value",
        "yearly_value",
        "remaining_total",
        "months_remaining",
        "last_updated",
    ]
    df = df[columns]

    return df


def create_debts_df() -> DataFrame:
    rkb_debts_df = create_rkb_debts()
    # rcp_debts_df = create_rcp_debts()
    # shared_debts_df = create_shared_debts()

    all_debts_df = pd.concat([rkb_debts_df], ignore_index=True)
    all_debts_df.loc["Total", "institution"] = "TOTAL"
    all_debts_df.loc["Total", "monthly_value"] = all_debts_df["monthly_value"].sum()
    all_debts_df.loc["Total", "yearly_value"] = all_debts_df["yearly_value"].sum()
    all_debts_df.loc["Total", "remaining_total"] = all_debts_df["remaining_total"].sum()

    return all_debts_df


# --- Function to create a gui table to view a dataframe ---
def view_df_gui(dataframe):
    """
    Pops up a clean, native desktop table window.
    Completely immune to numpy.float64 type errors.
    """
    root = tk.Tk()
    root.title("DataFrame Inspector")
    root.geometry("800x500")

    # Add a scrollbar container
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Setup native Treeview table
    # Columns must be strings for Tkinter config mapping
    columns = [str(col) for col in dataframe.columns]
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Configure scrollbars
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Grid positioning for standard table layout
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Format table headers
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    # Insert data rows (automatically handles floats smoothly)
    for _, row in dataframe.iterrows():
        # Convert values to list for safe rendering
        values = [
            f"{value:.2f}" if isinstance(value, numbers.Real) else value
            for value in row
        ]
        tree.insert("", tk.END, values=values)

    root.mainloop()

    return


if __name__ == "__main__":

    all_accounts_df = create_accounts_df()
    all_incomes_df = create_incomes_df()
    all_debts_df = create_debts_df()

    # view_df_gui(all_accounts_df)
    # view_df_gui(all_incomes_df)
    # view_df_gui(all_debts_df)

    combined_net_worth = (
        all_accounts_df.loc["Total", "value"]
        - all_debts_df.loc["Total", "remaining_total"]
    )
    print(f"Combined net worth = {combined_net_worth}")
