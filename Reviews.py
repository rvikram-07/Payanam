import tkinter as tk
from tkinter import messagebox

reviews = [

    {
        "user": "Rahul",
        "rating": 5,
        "comment": "Wonderful experience"
    }

]

class ReviewsPage:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Tourist Reviews"
        )

        self.root.geometry(
            "600x500"
        )

        self.root.configure(
            bg="#e6f2ff"
        )

        self.create_ui()

        self.root.mainloop()

    def create_ui(self):
        title = tk.Label(
            self.root,
            text="Reviews & Ratings",
            font=("Arial",20,"bold"),
            bg="#007acc",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

        frame = tk.Frame(
            self.root,
            bg="white",
            padx=20,
            pady=20
        )

        frame.pack(
            pady=20
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

        self.name_entry = tk.Entry(
            frame
        )

        self.name_entry.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Rating (1-5)",
            bg="white"
        ).grid(
            row=1,
            column=0,
            pady=10
        )


        self.rating_entry = tk.Entry(
            frame
        )

        self.rating_entry.grid(
            row=1,
            column=1
        )

        tk.Label(
            frame,
            text="Review",
            bg="white"
        ).grid(
            row=2,
            column=0,
            pady=10
        )


        self.comment_entry = tk.Entry(
            frame,
            width=30
        )

        self.comment_entry.grid(
            row=2,
            column=1
        )

        tk.Button(
            frame,
            text="Submit Review",
            bg="green",
            fg="white",
            command=self.add_review
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=15
        )

        self.review_list = tk.Listbox(
            self.root,
            width=70,
            height=10
        )

        self.review_list.pack(
            pady=20
        )


        self.display_reviews()

    def add_review(self):

        name = self.name_entry.get()

        rating = self.rating_entry.get()

        comment = self.comment_entry.get()

        if (
            name == ""
            or rating == ""
            or comment == ""
        ):

            messagebox.showerror(
                "Error",
                "Fill all fields"
            )

            return

        try:

            rating = int(rating)

            if rating < 1 or rating > 5:

                raise ValueError

        except:

            messagebox.showerror(
                "Error",
                "Rating must be between 1 to 10"
            )

            return

        reviews.append(

            {
                "user": name,
                "rating": rating,
                "comment": comment
            }

        )

        messagebox.showinfo(
            "Success",
            "Review Added"
        )

        self.display_reviews()

    def display_reviews(self):

        self.review_list.delete(
            0,
            tk.END
        )

        for review in reviews:

            data = (

                f"{review['user']} | "
                f"Rating: {review['rating']} ⭐ | "
                f"{review['comment']}"

            )

            self.review_list.insert(
                tk.END,
                data
            )

        if len(reviews) > 0:

            total = 0

            for review in reviews:

                total += review["rating"]

            average = total / len(reviews)

            self.review_list.insert(
                tk.END,
                "-------------------------"
            )

            self.review_list.insert(
                tk.END,
                f"Average Rating: {average:.1f}"
            )

if __name__ == "__main__":

    ReviewsPage()