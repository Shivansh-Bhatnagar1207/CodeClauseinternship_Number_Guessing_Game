import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from random import randint


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.start_value = tk.IntVar()
        self.end_value = tk.IntVar()
        self.guess_value = tk.IntVar()

        #?configure Window
        self.title('Guess Game')
        self.geometry(f'{1100}x{580}')

        #?configure grid layout
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_rowconfigure((0,1,2,4,5,6,7,8,9),weight=1)

        #?Sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        for i in range(11):
            self.sidebar_frame.grid_rowconfigure(i, weight=1)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Guess the Number", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0,padx=20,pady=(20,5))
        self.start_label = ctk.CTkLabel(self.sidebar_frame,text='Enter Starting Range:',font=('roboto',16))
        self.start_label.grid(row=1,column=0)
        self.start = ctk.CTkEntry(self.sidebar_frame,placeholder_text="Enter Starting Range")
        self.start.insert(0,0)
        self.start.grid(row=2,column=0)
        self.end_label = ctk.CTkLabel(self.sidebar_frame,text='Enter End Range:',font=('roboto',16))
        self.end_label.grid(row=3,column=0)
        self.end=ctk.CTkEntry(self.sidebar_frame,placeholder_text="Enter End Range")
        self.end.insert(0,0)
        self.end.grid(row=4,column=0)
        self.rangebtn = ctk.CTkButton(master=self.sidebar_frame,text='Set Range',command=self.checkrange)
        self.rangebtn.grid(row=5,column=0)
        self.sidebar_frame.grid_rowconfigure(6, weight=2)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["System","Light", "Dark"],command=self.set_theme)
        self.appearance_mode_optionemenu.grid(row=8,column=0)
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.set_scale)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        
        #?main Frame

        self.Game = ctk.CTkLabel(self,text='Guess a number between the range',font=ctk.CTkFont(size=20,weight='bold'))
        self.Game.grid(row=1,column=1)
        self.ans = ctk.CTkEntry(self,placeholder_text='Enter Ans')
        self.ans.grid(row=2,column=1)
        self.ansbtn = ctk.CTkButton(self,text="Submit Answer", command=self.checkans)
        self.ansbtn.grid(row=3,column=1)

    
    def checkrange(self):
        try:
            start_int=int(self.start.get())
            end_int=int(self.end.get())
            if start_int>end_int or end_int==0:
                tk.messagebox.showerror("Invalid range", "Start value cannot be greater than end value.")
            else:
                self.start_value.set(start_int)
                self.end_value.set(end_int)
                tk.messagebox.showinfo('Range Accepted', 'Range is accepted, a random number is generated')
                global random_value
                random_value= randint(start_int,end_int)
             
        except ValueError:
            tk.messagebox.showerror("Invalid Input","Please enter Valid int values")
    def set_theme(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def set_scale(self,new_scale:str):
        new_scale_float = int(new_scale.replace("%",""))/100
        ctk.set_widget_scaling(new_scale_float)
    def checkans(self):
        sv=self.start_value.get()
        ev=self.end_value.get()
        gv=self.guess_value

        if ev==0:
            tk.messagebox.showerror("Invalid range", "Set the range first")
        else:
            try:
                ans_int = int(self.ans.get())
                if ans_int>ev:
                    tk.messagebox.showerror("Invalid Answer", "Answer value cannot be greater than end value.")
                elif ans_int<random_value:
                    tk.messagebox.showwarning('Wrong Answer',"The Answer you have guessed is too low")
                elif ans_int>random_value:
                    tk.messagebox.showwarning('Wrong Answer' ,'The Answer you have guessed is too high')
                elif ans_int==random_value:
                    tk.messagebox.showinfo("Congratulations",'You have guessed the right answer')
                    

            except ValueError:
                tk.messagebox.showerror("Invalid Input","Please enter Valid int values")

if __name__ == '__main__':
    app=App()
    app.mainloop()