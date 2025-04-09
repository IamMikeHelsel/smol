import customtkinter as ctk

def test_customtkinter():
    try:
        app = ctk.CTk()
        app.title("CustomTkinter Test")
        label = ctk.CTkLabel(app, text="If you see this, CustomTkinter works!")
        label.pack(pady=20, padx=20)
        app.mainloop()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_customtkinter()
