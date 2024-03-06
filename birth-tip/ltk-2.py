import tkinter as tk

class Index(tk.Tk):  # Parent class
    def __init__(self):
        super().__init__()
        self.title("Index Window")
        self.geometry("400x300")
        self.index_frame = tk.Frame(self)
        self.subindex_frame = tk.Frame(self)
        self.show_index()  # Show index frame by default

    def show_index(self):
        self.subindex_frame.pack_forget()
        self.index_frame.pack(fill="both", expand=True)

    def show_subindex(self):
        self.index_frame.pack_forget()
        self.subindex_frame.pack(fill="both", expand=True)

class SubIndex(Index):  # Subclass inheriting from Index
    def __init__(self):
        super().__init__()  # Calls the constructor of the parent class
        self.title("SubIndex Window")
        # Additional initialization specific to SubIndex can be added here

# Example usage
if __name__ == "__main__":
    index_app = Index()  # Create an instance of Index
    subindex_app = SubIndex()  # Create an instance of SubIndex
    index_app.mainloop()  # Start the mainloop for Index
    # subindex_app.mainloop()  # You can also start the mainloop for SubIndex if needed