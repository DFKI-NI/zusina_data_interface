import sys
import requests
import pandas as pd
import tkinter as tk
import tkfilebrowser

def Abfrage(input: str, output: str, idfeld: str, server: str, auth: str) -> bool:
    produkte = pd.read_csv(input)
    produkte["startdate"] = "none"
    produkte["enddate"] = "none"
    produkte["ecolabel"] = "none"
    produkte["ecolabel_description"] = "none"
    id_parameter = idfeld

    produkt_pd = pd.DataFrame()
    for index in range(len(produkte)):
        id = produkte.loc[index, id_parameter]

        x = requests.get("http://"+server+"/api?productid=" + str(int(id)), headers={"Authorization":"Token " + auth})
        if x.json()["count"] > 0:
            produkt_pd = pd.DataFrame.from_dict(x.json()['results'])
            produkte.at[index, "ecolabel"] = produkt_pd.ecolabel.values
            produkte.at[index, "ecolabel_description"] = produkt_pd.ecolabel_informations.values
            produkte.at[index, "startdate"] = produkt_pd.startdate.values
            produkte.at[index, "enddate"] = produkt_pd.enddate.values

    produkte.to_csv(output)

    return 1

def setinput():
    produktdatei.set(tkfilebrowser.askopenfilename())

def setoutput():
    ausgabedatei.set(tkfilebrowser.askopenfilename())

def start() -> bool:
    Abfrage(produktdatei.get(), ausgabedatei.get(), id_name.get(), server.get(), auth.get())

    return 1

if __name__ == '__main__':
    tkFenster = tk.Tk()
    tkFenster.title('ZuSiNa Client')
    tkFenster.geometry('500x250')

    produktdatei = tk.StringVar()
    ausgabedatei = tk.StringVar()
    id_name = tk.StringVar()
    server = tk.StringVar()
    auth = tk.StringVar()

    tk.Label(tkFenster, text="Produktdatei").grid(row=0, pady=5)
    tk.Label(tkFenster, text="Ausgabedatei").grid(row=1, pady=5)
    tk.Label(tkFenster, text="ID Feld").grid(row=2, pady=5)
    tk.Label(tkFenster, text="Server").grid(row=3, pady=5)
    tk.Label(tkFenster, text="Auth Token").grid(row=4, pady=5)

    tk.Entry(master=tkFenster, textvariable=produktdatei).grid(row=0, column=1)
    tk.Entry(master=tkFenster, textvariable=ausgabedatei).grid(row=1, column=1)
    tk.Entry(master=tkFenster, textvariable=id_name).grid(row=2, column=1)
    tk.Entry(master=tkFenster, textvariable=server).grid(row=3, column=1)
    tk.Entry(master=tkFenster, textvariable=auth).grid(row=4, column=1)

    tk.Button(master=tkFenster, text="Durchsuchen...", command=setinput).grid(row=0, column=2)
    tk.Button(master=tkFenster, text="Durchsuchen...", command=setoutput).grid(row=1, column=2)

    tk.Button(master=tkFenster, text="Anfrage", command=start).grid(row=5, column=2)

    tkFenster.mainloop()
