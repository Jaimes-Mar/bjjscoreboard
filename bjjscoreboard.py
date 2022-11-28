import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700X800")
        self.title("BJJ scoreboard")
        self.minsize(300, 200)

        self.score_a = 0
        self.score_b = 0

        self.hour=ctk.StringVar()
        self.minute=ctk.StringVar()
        self.second=ctk.StringVar()

        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.hourEntry=ctk.CTkEntry(master=self, width=3, text_font=("Arial",18),
        textvariable=self.hour).grid(row=1,column=4)

        self.minuteEntry= ctk.CTkEntry(master=self, width=3, text_font=("Arial",18),
                   textvariable=self.minute).grid(row=2, column=4)
  
        self.secondEntry= ctk.CTkEntry(master=self, width=3, text_font=("Arial",18),
                   textvariable=self.second).grid(row=3, column=4)

        self.redlabel = ctk.CTkLabel(master = self, text = "Red corner", text_font=("Helvetica", 35, 'bold')).grid(row = 1, column = 0, sticky = "nsew")
        self.redlabel = ctk.CTkLabel(master = self, text = "Blue corner", text_font=("Helvetica", 35, 'bold')).grid(row = 1, column = 1, sticky = "nsew")

        self.display_a = ctk.CTkLabel(master = self, text = str(self.score_a), text_font=("Helvetica", 125)).grid(row = 2, column = 0)
     
        self.display_b = ctk.CTkLabel(master = self, text = str(self.score_b), text_font=("Helvetica", 125)).grid(row = 2, column = 1)
       
        self.red_p2_btn = ctk.CTkButton(master=self, text = "+2 red", height = 4,bg_color='PeachPuff1').grid(row = 3, column = 0, sticky = "nsew")
    
    


if __name__ == "__main__":
    app = App()
    app.mainloop()
