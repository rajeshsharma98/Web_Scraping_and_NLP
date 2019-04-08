import re
import os
from bs4 import BeautifulSoup
import requests
# from summary import use
import summary

class color:
# to make text colored or any other format: this do not work for a text file
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class working:
    def general(self,):
        #getting url
        self.url="https://en.wikipedia.org/wiki/Main_page"
        name=input("Enter the topic: ")
        post_data = {"search": name}
        #getting page of required topic
        self.req = requests.get(self.url, params=post_data)
        self.content = self.req.content
        #applying beautiful soup ( html parsing)
        self.soup = BeautifulSoup(self.content,"html.parser")
        self.all_h=self.soup.find_all("span",{"class":"mw-headline"})
        self.all_h=self.all_h[:-5]

    def writing(self):
        file = open("info.txt","a")

        first_h=self.soup.find_all("h1",{"class":"firstHeading"})
        for h in first_h:
            file.write(h.text+"\n"+"X----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----X"+"\n\n")
        """ to print the intro under heading of the topic still remaining"""
        for h in self.all_h:
             # file.write(color.BOLD+h.text+color.END)  ## to make text bold using class color
             file.write(h.text)
             file.write("\n")
             file.write(h.find_next("p").text+"\n")

        file.close()
        file = open("info.txt","r")
        filer=open("infon.txt","w")
        #to remove "[any_number]" from text
        for i in file:
            filer.write(re.sub("[\(\[].*?[\)\]]", "", i))

        print("information fetched")
        file.close()
        os.remove("info.txt")

    def short(self):
         file_sum = open("sum.txt","w")
         first_s=self.soup.find_all("h1",{"class":"firstHeading"})

         for h in first_s:
             file_sum.write(h.text+"\n"+"X----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----XX----X"+"\n\n")
         """ to print the intro under heading of the topic still remaining"""

         for h in self.all_h:
              # file.write(color.BOLD+h.text+color.END)  ## to make text bold
              file_sum.write("\n"+h.text)
              file_sum.write("\n")
              file_sum.write(summary.use.fun(h.find_next("p").text))
              file_sum.write("\n")

         file_sum.close()
         filesr_sum = open("sum.txt","r")
         filer_sum=open("summary.txt","w")
         #to remove "[any_number]" from text
         for i in filesr_sum:
              filer_sum.write(re.sub("[\(\[].*?[\)\]]", "", i))
         print("summary created")
         filer_sum.close()
         os.remove("sum.txt")

def main():
    w=working()
    w.general()
    print("1.Information")
    print("2.Summary")
    a=int(input())
    print("\n")
    if a==1:
        w.writing()
    if a==2:
        w.short()


main()
