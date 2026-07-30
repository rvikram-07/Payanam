import tkinter as tk
from tkinter import messagebox
from datetime import datetime

bookings = []

selected_package = {
    "destination": "Goa",
    "price": 12000
}

class BookingPage:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Tourist Booking - Booking Details"
        )

        self.root.geometry(
            "500x550"
        )

        self.root.configure(
            bg="#e6f2ff"
        )

        self.create_ui()

        self.root.mainloop()

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="Complete Your Booking",
            font=("Arial",20,"bold"),
            bg="#007acc",
            fg="white",
            pady=15
        )
        title.pack(
            fill="x"
        )
        frame=tk.Frame(
            self.root,
            bg="white",
            padx=30,
            pady=30
        )
        frame.pack(
            pady=30
        )
        tk.Label(
            frame,
            text="Name",
            bg="white"
        ).grid(
            row=0,
            column=0,
            pady=10
        )
        self.name=tk.Entry(frame)
        self.name.grid(
            row=0,
            column=1
        )
        tk.Label(
            frame,
            text="Phone",
            bg="white"
        ).grid(
            row=1,
            column=0,
            pady=10
        )
        self.phone=tk.Entry(frame)
        self.phone.grid(
            row=1,
            column=1
        )
        tk.Label(
            frame,
            text="Travel Date",
            bg="white"
        ).grid(
            row=2,
            column=0,
            pady=10
        )
        self.date=tk.Entry(frame)
        self.date.grid(
            row=2,
            column=1
        )
        tk.Label(
            frame,
            text="Travellers",
            bg="white"
        ).grid(
            row=3,
            column=0,
            pady=10
        )

        self.people=tk.Entry(frame)
        self.people.grid(
            row=3,
            column=1
        )
        tk.Label(
            frame,
            text="Package",
            bg="white"
        ).grid(
            row=4,
            column=0,
            pady=10
        )
        self.package_label=tk.Label(
            frame,
            text=selected_package["destination"],
            bg="white"
        )
        self.package_label.grid(
            row=4,
            column=1
        )
        tk.Label(
            frame,
            text="Price",
            bg="white"
        ).grid(
            row=5,
            column=0,
            pady=10
        )
        self.price_label=tk.Label(
            frame,
            text=f"₹{selected_package['price']}",
            bg="white"
        )
        self.price_label.grid(
            row=5,
            column=1
        )
        tk.Button(
            self.root,
            text="Confirm Booking",
            bg="green",
            fg="white",
            width=20,
            command=self.confirm_booking
        ).pack(
            pady=20
        )

    def confirm_booking(self):

        name=self.name.get()

        phone=self.phone.get()

        date=self.date.get()

        people=self.people.get()

        if (
            name=="" or
            phone=="" or
            date=="" or
            people==""
        ):

            messagebox.showerror(
                "Error",
                "Fill all details"
            )

            return

        booking={

            "customer":name,

            "phone":phone,

            "date":date,

            "travellers":people,

            "destination":selected_package["destination"],

            "amount":selected_package["price"],

            "status":"Confirmed"

        }

        bookings.append(
            booking
        )

        messagebox.showinfo(
            "Success",
            "Booking Confirmed Succesfully"
        )

        self.root.destroy()

        from Mytrips import MyTripsPage

        MyTripsPage()

if __name__=="__main__":

    BookingPage()