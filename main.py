from tkinter import messagebox

res = messagebox.askquestion('Message title', 'Message ask content')
res = messagebox.askyesno('Message title', 'Message y/n content')
res = messagebox.askyesnocancel('Message title', 'Message y/n/cancel content')
res = messagebox.askokcancel('Message title', 'Message ok/cancel content')
res = messagebox.askretrycancel('Message title', 'Message retry/cancel content')