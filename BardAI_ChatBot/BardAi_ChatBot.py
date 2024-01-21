import tkinter as tk
from bardapi import Bard
import os


BG_GRAY = "#ffffff"
BG_COLOR = "#101820"
TEXT_COLOR = "#FEE715"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#bardapi key 
os.environ['_BARD_API_KEY']="Use yours BardAi apikey"

def responsive_api(prompt):
    message=Bard().get_answer(prompt)["content"]
    return message

def submit_action():
    user_text = msg_entry.get("1.0", "end-1c")
    
    response = responsive_api(user_text)
    text_widget.delete("1.0", "end")  # Clear the Text widget
    text_widget.insert("end", response)
    

root = tk.Tk()
root.title("Chat Bot Project")



root.iconbitmap("chatbot.ico")
root.resizable(width=True, height=True)
root.configure(width=700, height=750, bg=BG_COLOR)

bottom_label = tk.Label(root, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)

head_label = tk.Label(root, bg="#201E20", fg="#ffffff",
                           text="Bard AI", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)

line = tk.Label(root, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)


msg_entry = tk.Text(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
msg_entry.focus()






text_widget = tk.Text(root,width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
text_widget.configure(cursor="arrow")





                             

submit_button = tk.Button(bottom_label, text="Submit",command=submit_action, font=FONT_BOLD, width=20, bg=BG_GRAY)
submit_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)





root.mainloop()