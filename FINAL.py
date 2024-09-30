import tkinter as tk
m = tk.Tk()

m.geometry("600x400")

songRequest = tk.StringVar()
firstName = tk.StringVar()
lastName = tk.StringVar()

def submit():
    SongRequest = songRequest
    FirstName = firstName
    LastName = lastName

    print("The requested song is: ", songRequest)
    print("The user's name is: ", firstName, lastName)

    songRequest.set("")
    firstName.set("")
    lastName.set("")
