import tkinter as tk
from tkinter import messagebox

users = [
    {
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "admin123",
        "role": "admin"
    }
]

current_user = None

class LoginPage:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Tourist Booking System - Login")
        self.root.geometry("500x450")
        self.root.configure(bg="#e6f2ff")
        self.root.resizable(False, False)

        self.create_ui()

        self.root.mainloop()


    def create_ui(self):

        title = tk.Label(
            self.root,
            text="Tourist Booking System",
            font=("Arial",20,"bold"),
            bg="#007acc",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

        frame = tk.Frame(
            self.root,
            bg="white",
            padx=30,
            pady=30
        )

        frame.place(
            x=70,
            y=120
        )

        tk.Label(
            frame,
            text="Email",
            bg="white"
        ).grid(row=0,column=0,pady=10)


        self.email_entry = tk.Entry(
            frame,
            width=30
        )

        self.email_entry.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Password",
            bg="white"
        ).grid(row=1,column=0,pady=10)


        self.password_entry = tk.Entry(
            frame,
            width=30,
            show="*"
        )

        self.password_entry.grid(
            row=1,
            column=1
        )

        tk.Button(
            frame,
            text="Login",
            width=15,
            bg="#007acc",
            fg="white",
            command=self.login
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=20
        )

        tk.Button(
            frame,
            text="Register",
            width=15,
            bg="green",
            fg="white",
            command=self.register_window
        ).grid(
            row=3,
            column=0,
            columnspan=2
        )

    def login(self):

        global current_user


        email = self.email_entry.get()

        password = self.password_entry.get()


        if email == "" or password == "":

            messagebox.showerror(
                "Error",
                "Enter all fields"
            )

            return

        for user in users:

            if (
                user["email"] == email
                and
                user["password"] == password
            ):

                current_user = user


                messagebox.showinfo(
                    "Success",
                    "Login Successful"
                )


                self.root.destroy()


                if user["role"] == "admin":

                    from Admin import AdminDashboard

                    AdminDashboard()


                else:

                    from explore import ExplorePage

                    ExplorePage()


                return

        messagebox.showerror(
            "Failed",
            "Invalid Login Details"
        )

    def register_window(self):

        RegisterPage()

class RegisterPage:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title(
            "Tourist Registration"
        )

        self.window.geometry(
            "400x400"
        )

        self.window.configure(
            bg="#e6f2ff"
        )

        self.create_ui()

    def create_ui(self):

        frame=tk.Frame(
            self.window,
            bg="white",
            padx=25,
            pady=25
        )

        frame.pack(pady=40)

        tk.Label(
            frame,
            text="Name",
            bg="white"
        ).grid(row=0,column=0,pady=10)


        self.name=tk.Entry(frame)

        self.name.grid(row=0,column=1)

        tk.Label(
            frame,
            text="Email",
            bg="white"
        ).grid(row=1,column=0,pady=10)


        self.email=tk.Entry(frame)

        self.email.grid(row=1,column=1)

        tk.Label(
            frame,
            text="Password",
            bg="white"
        ).grid(row=2,column=0,pady=10)


        self.password=tk.Entry(
            frame,
            show="*"
        )

        self.password.grid(row=2,column=1)

        tk.Button(
            frame,
            text="Create Account",
            bg="green",
            fg="white",
            command=self.register
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )

    def register(self):


        name=self.name.get()

        email=self.email.get()

        password=self.password.get()



        if name=="" or email=="" or password=="":

            messagebox.showerror(
                "Error",
                "Fill all fields"
            )

            return



        for user in users:

            if user["email"]==email:

                messagebox.showerror(
                    "Error",
                    "Email already exists"
                )

                return

        users.append(
            {
                "name":name,
                "email":email,
                "password":password,
                "role":"tourist"
            }
        )

        messagebox.showinfo(
            "Success",
            "Registration Completed"
        )

        self.window.destroy()

if __name__ == "__main__":

    LoginPage()