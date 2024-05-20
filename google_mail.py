import tkinter as tk
import yagmail, csv
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Main window')
        self.protocol('WM_DELETE_WINDOW', self.quit)
        self.geometry("300x300")



        self.subject  = tk.StringVar()
        self.message  = tk.StringVar()
        self.usermail = tk.StringVar()
        self.password = tk.StringVar()

        self.usermail.set('rofik.info.bd@gmail.com')
        self.password.set('jmdr sekk dhpq vouz')
        self.subject.set('This is beautifull subject')
        self.message.set("""\
                    <html>
                    <body>
                        <p>Hi,<br>
                        This is a <b>test</b> email without an attachment sent using <a href="https://rofikit.com">Rofik IT</a>.</p>
                        <div style="text-align: center;"><img src="https://i.pinimg.com/originals/0f/a8/75/0fa875beebaae7e43eca81a6217c88b2.png" alt="..."></div>
                    </body>
                    </html>
                    """)
        fram = tk.Frame(self)
        fram.pack(fill=tk.BOTH,side=tk.TOP)
        button = tk.Button(fram, text="Send mail", command=self.sendMail, bg="#ddd", fg="black", font=("Arial", 9))
        button.pack(side=tk.TOP,padx=30, pady=30, anchor='center', fill=tk.BOTH)


    def sendMail(self):
        with open('csv.csv') as file:
            reader = csv.reader(file)
            next(reader)
            mailbox = yagmail.SMTP(
                user = self.usermail.get(), 
                password = self.password.get()
            )
            
            for (email) in reader: 
                mailbox.send(
                    to=email, 
                    subject=self.subject.get(),
                    contents=self.message.get()
                    ) 
                print('Successfully send mail to : ' + str(email[0]))
        messagebox.showinfo("Success", "All email are send successfully.")

if __name__ == '__main__':
    app = App()
    app.mainloop()
