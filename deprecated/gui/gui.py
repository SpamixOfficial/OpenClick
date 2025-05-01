import customtkinter

def on_press_gui():
    print("Constant Started")

def stop_press_gui():
    print("Constant Stopped")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)
        self.title("OpenClick GUI Edition")
        self.geometry("400x150")

        customtkinter.CTkButton(self, text="Start constant (F2)", command=on_press_gui).grid(row=0, column=0, padx=20, pady=20)
        customtkinter.CTkButton(self, text="Stop constant (F2)", command=stop_press_gui).grid(row=0, column=1, padx=20, pady=20)

        
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()