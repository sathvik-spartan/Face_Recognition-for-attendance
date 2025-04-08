import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from datetime import datetime
from report_utils import send_report_email

CSV_FILE = "attendance.csv"

class ReportViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Report Viewer")

        self.df = pd.read_csv(CSV_FILE)
        self.filtered_df = self.df.copy()

        self.build_gui()

    def build_gui(self):
        # Filters
        filter_frame = ttk.Frame(self.root)
        filter_frame.pack(pady=10)

        ttk.Label(filter_frame, text="Filter by Name:").grid(row=0, column=0)
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(filter_frame, textvariable=self.name_var)
        name_entry.grid(row=0, column=1)

        ttk.Label(filter_frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=2)
        self.start_date_var = tk.StringVar()
        start_entry = ttk.Entry(filter_frame, textvariable=self.start_date_var)
        start_entry.grid(row=0, column=3)

        ttk.Label(filter_frame, text="End Date (YYYY-MM-DD):").grid(row=0, column=4)
        self.end_date_var = tk.StringVar()
        end_entry = ttk.Entry(filter_frame, textvariable=self.end_date_var)
        end_entry.grid(row=0, column=5)

        filter_btn = ttk.Button(filter_frame, text="Apply Filters", command=self.apply_filters)
        filter_btn.grid(row=0, column=6, padx=5)

        reset_btn = ttk.Button(filter_frame, text="Reset", command=self.reset_filters)
        reset_btn.grid(row=0, column=7, padx=5)

        # Treeview Table
        self.tree = ttk.Treeview(self.root, columns=("Name", "Date", "Time", "Snapshot"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.populate_treeview(self.df)

        # Actions
        action_frame = ttk.Frame(self.root)
        action_frame.pack(pady=10)

        ttk.Button(action_frame, text="📤 Export to Excel", command=self.export_excel).grid(row=0, column=0, padx=5)
        ttk.Button(action_frame, text="📊 Show Chart", command=self.show_chart).grid(row=0, column=1, padx=5)
        ttk.Button(action_frame, text="✉️ Email Report", command=self.email_report).grid(row=0, column=2, padx=5)

    def apply_filters(self):
        df = self.df.copy()
        name = self.name_var.get().strip().lower()
        if name:
            df = df[df["Name"].str.lower().str.contains(name)]

        try:
            start = datetime.strptime(self.start_date_var.get(), "%Y-%m-%d")
            df = df[df["Date"] >= start.strftime("%Y-%m-%d")]
        except:
            pass

        try:
            end = datetime.strptime(self.end_date_var.get(), "%Y-%m-%d")
            df = df[df["Date"] <= end.strftime("%Y-%m-%d")]
        except:
            pass

        self.filtered_df = df
        self.populate_treeview(df)

    def reset_filters(self):
        self.name_var.set("")
        self.start_date_var.set("")
        self.end_date_var.set("")
        self.filtered_df = self.df.copy()
        self.populate_treeview(self.df)

    def populate_treeview(self, df):
        self.tree.delete(*self.tree.get_children())
        for _, row in df.iterrows():
            self.tree.insert("", tk.END, values=list(row))

    def export_excel(self):
        if self.filtered_df.empty:
            tk.messagebox.showinfo("No Data", "Nothing to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.filtered_df.to_excel(file_path, index=False)
            tk.messagebox.showinfo("Exported", f"Report saved to:\n{file_path}")

    def show_chart(self):
        if self.filtered_df.empty:
            tk.messagebox.showinfo("No Data", "No data to plot.")
            return

        count_by_name = self.filtered_df["Name"].value_counts()
        count_by_name.plot(kind='bar', title="Attendance Count", color='skyblue')
        plt.xlabel("Name")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()

    def email_report(self):
        if self.filtered_df.empty:
            tk.messagebox.showinfo("No Data", "Nothing to email.")
            return

        recipient = tk.simpledialog.askstring("Recipient", "Enter email address:")
        if recipient:
            try:
                send_report_email(recipient, self.filtered_df)
                tk.messagebox.showinfo("Email Sent", f"Report emailed to: {recipient}")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to send email:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReportViewer(root)
    root.mainloop()
