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

        self.display_a = ctk.CTkLabel(master = self, text = str(self.score_a), text_font=("Helvetica", 125))
        self.display_a.grid(row = 2, column = 0)
     
        self.display_b = ctk.CTkLabel(master = self, text = str(self.score_b), text_font=("Helvetica", 125))
        self.display_b.grid(row = 2, column = 1)

        def red_2 ():
            self.score_a = self.score_a +2
            self.display_a.configure(text = str(self.score_a))
        def red_3 ():
            self.score_a = self.score_a +3
            self.display_a.configure(text = str(self.score_a))
        def red_4 ():
            self.score_a = self.score_a +4
            self.display_a.configure(text = str(self.score_a))
        def blue_2 ():
            self.score_b = self.score_b +2
            self.display_b.configure(text = str(self.score_b))
        def blue_3 ():
            self.score_b = self.score_b +3
            self.display_b.configure(text = str(self.score_b))
        def blue_4 ():
            self.score_b = self.score_b +4
            self.display_b.configure(text = str(self.score_b))
        def red_m1 ():
            self.score_a = self.score_a -1
            self.display_a.configure(text = str(self.score_a))
        def blue_m1 ():
            self.score_b = self.score_b -1
            self.display_b.configure(text = str(self.score_b))
        
        def _from_rgb(rgb):
            return "#%02x%02x%02x" % rgb 
            

        self.hourEntry=ctk.CTkEntry(master=self, width=3, text_font=("Arial",18),
        textvariable=self.hour).grid(row=1,column=4)

        self.minuteEntry= ctk.CTkEntry(master=self, width=3, text_font=("Arial",18),
                   textvariable=self.minute).grid(row=2, column=4)
  
        self.secondEntry= ctk.CTkEntry(master=self, width=3, text_font=("Arial",18),
                   textvariable=self.second).grid(row=3, column=4)

        self.redlabel = ctk.CTkLabel(master = self, text = "Red corner", text_font=("Helvetica", 35, 'bold')).grid(row = 1, column = 0, sticky = "nsew")
        self.bluelabel = ctk.CTkLabel(master = self, text = "Blue corner", text_font=("Helvetica", 35, 'bold')).grid(row = 1, column = 1, sticky = "nsew")
        print(type(self.bluelabel))
        self.red_p2_btn = ctk.CTkButton(master=self, command=red_2, height= 40, text = "+2 red",  fg_color=_from_rgb((0, 247, 0)))
        self.red_p2_btn.grid(row = 4, column = 0)
        self.red_p3_btn = ctk.CTkButton(master=self, command=red_3, height= 40,text = "+3 red", fg_color=_from_rgb((0, 247, 0)))
        self.red_p3_btn.grid(row = 5, column = 0, )
        self.red_p4_btn = ctk.CTkButton(master=self, command=red_4, height= 40,text = "+4 red", fg_color=_from_rgb((0, 247, 0)))
        self.red_p4_btn.grid(row = 6, column = 0, )
        self.red_m1_btn = ctk.CTkButton(master=self, command=red_m1, height= 40,text = "-1 red", fg_color=_from_rgb((247, 0, 0)))
        self.red_m1_btn.grid(row = 7, column = 0, )
        self.blue_p2_btn = ctk.CTkButton(master=self, command=blue_2, height= 40, text = "+2 blue", fg_color=_from_rgb((0, 247, 0)))
        self.blue_p2_btn.grid(row = 4, column = 1, )
        self.blue_p3_btn = ctk.CTkButton(master=self, command=blue_3, height= 40, text = "+3 blue", fg_color=_from_rgb((0, 247, 0)))
        self.blue_p3_btn.grid(row = 5, column = 1, )
        self.blue_p4_btn = ctk.CTkButton(master=self, command=blue_4, height= 40, text = "+4 blue", fg_color=_from_rgb((0, 247, 0)))
        self.blue_p4_btn.grid(row = 6, column = 1, )
        self.blue_m1_btn = ctk.CTkButton(master=self, command=blue_m1, height= 40,text = "-1 blue", fg_color=_from_rgb((247, 0, 0)))
        self.blue_m1_btn.grid(row = 7, column = 1, )
    
    


if __name__ == "__main__":
    app = App()
    app.mainloop()
