#!/usr/bin/env python
# coding: utf-8

# By--Bl4cKc34sEr


from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import json, requests, urllib.request, tkinter as tk

def CreateWidgets():
    urlLabel = Label(root, text="Instagram Username : ", background = "deepskyblue3")
    urlLabel.grid(row=0, column=0, padx=5, pady=5)

    root.urlEntry = Entry(root, width=30, textvariable=insta_id)
    root.urlEntry.grid(row=0, column=1,columnspan=2, pady=5)

    dwldBTN = Button(root, text="Download Image", command=i_Downloader, highlightbackground = "green")
    dwldBTN.grid(row=0, column=3, padx=5, pady=5)

    root.resultLabel = Label(root, textvariable=dwldtxt, background = "tan4")
    root.resultLabel.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
    root.resultLabel.config(font=("Courier", 25))

    root.previewLabel = Label(root, text="Profile Picture Preview : ", background = "tan4")
    root.previewLabel.grid(row=3, column=0, padx=5, pady=5)

    root.dpLabel = Label(root, background = "tan4")
    root.dpLabel.grid(row=4, column=1, columnspan=2,padx=1, pady=1)


def i_Downloader():
    download_path = "Desktop"
    insta_username = insta_id.get()
    insta_url = "https://www.instagram.com/"+insta_username
    insta_response =  requests.get(insta_url)
    soup = BeautifulSoup(insta_response.text, 'html.parser')
    script = soup.find('script', text=re.compile('window._sharedData'))
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
    data = json.loads(page_json)
    dp_url = data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    dp_name = download_path+insta_username+'.jpg'
    urllib.request.urlretrieve(dp_url, dp_name)
    dp_image = Image.open(dp_name)
    dp_image = dp_image.resize((500, 500), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(dp_image)
    root.dpLabel.config(image=image)
    root.dpLabel.photo = image
    dwldtxt.set('Profile Picture Successfully Downloaded')

root = tk.Tk()

root.geometry("1024x1600")
root.title("instaProfile--Downloader")
root.config(background = "tan4")

insta_id = StringVar()
dwldtxt = StringVar()

CreateWidgets()

root.mainloop()


# In[ ]:




