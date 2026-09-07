import datetime
from dataclasses import asdict
import numpy as np
import pandas as pd
from pandas import DataFrame
import tkinter as tk
from tkinter import ttk

from NWC.accounts import bankAccount, investmentAccount


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
        tree.insert("", tk.END, values=list(row))

    root.mainloop()

    return


if __name__ == "__main__":
    rkb_accounts_df = create_rkb_accounts()
    rcp_accounts_df = create_rcp_accounts()
    shared_accounts_df = create_shared_accounts()

    all_accounts_df = pd.concat(
        [rkb_accounts_df, rcp_accounts_df, shared_accounts_df], ignore_index=True
    )
    all_accounts_df.loc["Total", "value"] = all_accounts_df["value"].sum()

    view_df_gui(all_accounts_df)
