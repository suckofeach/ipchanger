import tkinter as tk
from tkinter import ttk
import os
import subprocess

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        #Setting the window
        self.master.geometry("600x800")
        self.master.title("DHCP to Manual")

        #Parsing harware ports
        #rawPorts = os.system("networksetup -listallhardwareports")
        #print(rawPorts)

        #Running tk
        self.create_widgets()


    # Create Widgets function
    def create_widgets(self):
        #Button1
        self.button_dhcp = ttk.Button(self)
        self.button_dhcp.configure(text="DHCP")
        self.button_dhcp.configure(command = self.setDhcp) #do not forget to add self!
        self.button_dhcp.pack()

        #Button2
        self.button_man = ttk.Button(self)
        self.button_man.configure(text="192.168.1.88")
        self.button_man.configure(command = self.setManual) #do not forget to add self!
        self.button_man.pack()

        #Collecting device data
        self.output = subprocess.check_output("networksetup -listallhardwareports".split())

        #Label
        self.label_hello = ttk.Label(self)
        self.label_hello.configure(text=self.output)
        self.label_hello.pack()

        #Entry
        #self.name = tk.StringVar()
        #self.entry_name = ttk.Entry(self)
        #self.entry_name.configure(textvariable = self.name)
        #self.entry_name.pack()

        #Label2
        #self.label_name = ttk.Label(self)
        #self.label_name.configure(text = 'Please input something in Entry')
        #self.label_name.pack()

    # Event Callback Function
    def setDhcp(self):
        #print("Hello, World")  # on python console
        #self.label_hello.configure(text="I Have been Clicked!")
        #print(self.name.get())
        #self.label_name.configure(text=self.name.get())
        os.system('networksetup -setdhcp "Wi-Fi"')

    def setManual(self):
        #print("Hello, World")  # on python console
        #self.label_hello.configure(text="I Have been Clicked!")
        #print(self.name.get())
        #self.label_name.configure(text=self.name.get())
        os.system('networksetup -setmanual "Wi-Fi" 192.168.1.88 255.255.255.0 192.168.1.1')



def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit class inheritance!
    app.mainloop()


if __name__ == "__main__":
    main()