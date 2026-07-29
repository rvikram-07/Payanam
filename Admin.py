import tkinter as tk
from tkinter import messagebox

packages = [
    {
        "id": 1,
        "destination": "Goa",
        "price": 12000
    },

    {
        "id": 2,
        "destination": "Ooty",
        "price": 6500
    },

    {
        "id": 3,
        "destination": "Manali",
        "price": 15000
    }
]

bookings = [

    {
        "customer": "Rahul",
        "destination": "Goa",
        "status": "Confirmed"
    }

]

class AdminDashboard:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Admin Dashboard"
        )

        self.root.geometry(
            "700x550"
        )

        self.root.configure(
            bg="#e6f2ff"
        )


        self.create_ui()

        self.root.mainloop()

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="Admin Dashboard",
            font=("Arial",22,"bold"),
            bg="#007acc",
            fg="white",
            pady=15
        )

        title.pack(
            fill="x"
        )

        button_frame=tk.Frame(
            self.root,
            bg="#e6f2ff"
        )

        button_frame.pack(
            pady=20
        )

        tk.Button(
            button_frame,
            text="View Packages",
            width=20,
            bg="green",
            fg="white",
            command=self.view_packages
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Add Package",
            width=20,
            bg="blue",
            fg="white",
            command=self.add_package_window
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Delete Package",
            width=20,
            bg="red",
            fg="white",
            command=self.delete_package
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        tk.Button(
            button_frame,
            text="View Bookings",
            width=20,
            bg="purple",
            fg="white",
            command=self.view_bookings
        ).grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        self.listbox=tk.Listbox(
            self.root,
            width=70,
            height=15,
            font=("Arial",12)
        )

        self.listbox.pack(
            pady=20
        )

    def view_packages(self):

        self.listbox.delete(
            0,
            tk.END
        )

        for package in packages:

            self.listbox.insert(

                tk.END,

                f"{package['id']} - "
                f"{package['destination']} "
                f"- ₹{package['price']}"

            )

    def add_package_window(self):

        window=tk.Toplevel()

        window.title(
            "Add Package"
        )

        window.geometry(
            "350x300"
        )

        tk.Label(
            window,
            text="Destination"
        ).pack(pady=5)


        destination=tk.Entry(
            window
        )

        destination.pack()

        tk.Label(
            window,
            text="Price"
        ).pack(pady=5)

        price=tk.Entry(
            window
        )

        price.pack()

        def save():

            if destination.get()=="" or price.get()=="":

                messagebox.showerror(
                    "Error",
                    "Fill all details"
                )

                return

            packages.append(

                {
                    "id":len(packages)+1,

                    "destination":destination.get(),

                    "price":int(price.get())

                }

            )

            messagebox.showinfo(
                "Success",
                "Package Added"
            )

            window.destroy()

        tk.Button(
            window,
            text="Save",
            bg="green",
            fg="white",
            command=save
        ).pack(
            pady=20
        )

    def delete_package(self):

        selected=self.listbox.curselection()

        if not selected:

            messagebox.showerror(
                "Error",
                "Select package"
            )

            return

        index=selected[0]

        packages.pop(index)

        messagebox.showinfo(
            "Deleted",
            "Package removed"
        )

        self.view_packages()

    def view_bookings(self):

        self.listbox.delete(
            0,
            tk.END
        )

        for booking in bookings:

            self.listbox.insert(

                tk.END,

                f"{booking['customer']} | "
                f"{booking['destination']} | "
                f"{booking['status']}"

            )

if __name__=="__main__":

    AdminDashboard()