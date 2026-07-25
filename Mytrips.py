import tkinter as tk
from tkinter import messagebox

bookings = [

    {
        "customer": "Rahul",
        "phone": "9876543210",
        "destination": "Goa",
        "date": "20-08-2026",
        "travellers": "2",
        "amount": 12000,
        "status": "Confirmed"
    }

]


class MyTripsPage:


    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "My Trips"
        )

        self.root.geometry(
            "700x500"
        )

        self.root.configure(
            bg="#e6f2ff"
        )


        self.create_ui()

        self.root.mainloop()


    def open_reviews(self):

        self.root.destroy()

        from reviews import ReviewsPage

        ReviewsPage()

    def create_ui(self):


        title = tk.Label(
            self.root,
            text="My Bookings",
            font=("Arial",20,"bold"),
            bg="#007acc",
            fg="white",
            pady=15
        )

        title.pack(fill="x")



        self.listbox = tk.Listbox(
            self.root,
            width=80,
            height=12,
            font=("Arial",12)
        )

        self.listbox.pack(
            pady=30
        )


        self.display_bookings()



        button_frame = tk.Frame(
            self.root,
            bg="#e6f2ff"
        )

        button_frame.pack()



        tk.Button(
            button_frame,
            text="Cancel Booking",
            bg="red",
            fg="white",
            width=18,
            command=self.cancel_booking
        ).grid(
            row=0,
            column=0,
            padx=10
        )



        tk.Button(
            button_frame,
            text="Refresh",
            bg="green",
            fg="white",
            width=18,
            command=self.display_bookings
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Button(
            button_frame,
            text="Give Review",
            bg="blue",
            fg="white",
            width=18,
            command=self.open_reviews
        ).grid(
            row=0,
            column=2,
            padx=10
        )


    def display_bookings(self):

        self.listbox.delete(
            0,
            tk.END
        )


        if len(bookings) == 0:

            self.listbox.insert(
                tk.END,
                "No bookings available"
            )

            return



        for index, booking in enumerate(bookings):

            details = (

                f"{index+1}. "
                f"{booking['destination']} | "
                f"Date: {booking['date']} | "
                f"Travellers: {booking['travellers']} | "
                f"Amount: ₹{booking['amount']} | "
                f"Status: {booking['status']}"

            )


            self.listbox.insert(
                tk.END,
                details
            )


    def cancel_booking(self):


        selected = self.listbox.curselection()


        if not selected:

            messagebox.showerror(
                "Error",
                "Select a booking first"
            )

            return



        index = selected[0]


        bookings[index]["status"] = "Cancelled"



        messagebox.showinfo(
            "Cancelled",
            "Booking cancelled successfully"
        )


        self.display_bookings()

if __name__ == "__main__":

    MyTripsPage()