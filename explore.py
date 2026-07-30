import tkinter as tk
from tkinter import messagebox

packages = [

    {
        "id": 1,
        "destination": "Goa",
        "duration": "4 Days / 3 Nights",
        "price": 12000,
        "rating": 4.8
    },

    {
        "id": 2,
        "destination": "Ooty",
        "duration": "3 Days / 2 Nights",
        "price": 16500,
        "rating": 4.5
    },

    {
        "id": 3,
        "destination": "Manali",
        "duration": "5 Days / 4 Nights",
        "price": 15000,
        "rating": 4.9
    },

    {
        "id": 4,
        "destination": "Kerala",
        "duration": "6 Days / 5 Nights",
        "price": 9000,
        "rating": 4.6
    }

]

selected_package = None

class ExplorePage:


    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Explore Destinations"
        )

        self.root.geometry(
            "700x500"
        )

        self.root.configure(
            bg="#e6f2ff"
        )


        self.create_ui()

        self.root.mainloop()


    def create_ui(self):


        title = tk.Label(
            self.root,
            text="Explore Packages",
            font=("Arial",20,"bold"),
            bg="#007acc",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

        search_frame=tk.Frame(
            self.root,
            bg="#e6f2ff"
        )

        search_frame.pack(
            pady=15
        )


        tk.Label(
            search_frame,
            text="Search Destination:",
            bg="#e6f2ff",
            font=("Arial",12)
        ).pack(side="left")


        self.search_entry=tk.Entry(
            search_frame,
            width=25
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        tk.Button(
            search_frame,
            text="Search",
            command=self.search
        ).pack(
            side="left"
        )

        self.listbox=tk.Listbox(
            self.root,
            width=70,
            height=12,
            font=("Arial",12)
        )

        self.listbox.pack(
            pady=20
        )

        self.show_packages()

        tk.Button(
            self.root,
            text="Book Now",
            bg="green",
            fg="white",
            width=20,
            command=self.book
        ).pack()

    def show_packages(self):

        self.listbox.delete(0,tk.END)

        for package in packages:

            data = (
                f"{package['id']}. "
                f"{package['destination']} | "
                f"{package['duration']} | "
                f"₹{package['price']} | "
                f"Rating {package['rating']}"
            )


            self.listbox.insert(
                tk.END,
                data
            )

    def search(self):

        keyword = self.search_entry.get().lower()


        self.listbox.delete(
            0,
            tk.END
        )


        for package in packages:

            if keyword in package["destination"].lower():

                self.listbox.insert(
                    tk.END,
                    f"{package['destination']} | ₹{package['price']}"
                )


    def book(self):

        global selected_package


        choice=self.listbox.curselection()


        if not choice:

            messagebox.showerror(
                "Error",
                "Select a package first"
            )

            return

        index=choice[0]

        selected_package=packages[index]

        messagebox.showinfo(
            "Selected",
            f"You selected {selected_package['destination']}"
        )

        self.root.destroy()

        from booking import BookingPage

        BookingPage()


if __name__=="__main__":

    ExplorePage()