import json
import os
from cgitb import text
from pydoc import pager
from tkinter import font
from turtle import width
from fpdf import FPDF

# Find JSON file
CurrentDirectory = os.getcwd()
print(CurrentDirectory)
jsonFile = "%s/%s" % (CurrentDirectory, "Personal Information.json")
jsonData = {}

# Read JSON file and store in jsonData
with open(jsonFile) as data_file:
    jsonData = json.load(data_file)

# Set JSON Data # personal details
FullName1 = jsonData["NAME1"]
FullName2 = jsonData["NAME2"]
FullName3 = jsonData["NAME3"]
Course = jsonData["Course"]

PersonalProfile1 = jsonData["Personal Profile1"]
PersonalProfile2 = jsonData["Personal Profile2"]
PersonalProfile3 = jsonData["Personal Profile3"]
PersonalProfile4 = jsonData["Personal Profile4"]

MobileNumber = jsonData["Mobile"]
GmailEmail = jsonData["Gmail"]
FullAddress1 = jsonData["Address1"]
FullAddress2 = jsonData["Address2"]

SaA1 = jsonData["Skills and Abilities1"]
SaA2 = jsonData["Skills and Abilities2"]
SaA3A = jsonData["Skills and Abilities3A"]
SaA3B = jsonData["Skills and Abilities3B"]
SaA4 = jsonData["Skills and Abilities4"]
SaA5 = jsonData["Skills and Abilities5"]
SaA6 = jsonData["Skills and Abilities6"]
SaA7 = jsonData["Skills and Abilities7"]

FacebookAccount = jsonData["Facebook"]
InstagramAccount = jsonData["Instagram"]
TwitterAccount = jsonData["Twitter"]
GitHubAccount = jsonData["Github"]

SchoolSHS = jsonData["School SHS"]
StrandSHS1 = jsonData["Strand SHS1"]
StrandSHS2 = jsonData["Strand SHS2"]
SHSDescription1 = jsonData["SHS Description1"]
SHSDescription2 = jsonData["SHS Description2"]
SHSAchievement1 = jsonData["SHS Achievement1"]
SHSAchievement2 = jsonData["SHS Achievement2"]
SHSAchievement3 = jsonData["SHS Achievement3"]

SchoolJHS1 = jsonData["School JHS1"]
SchoolJHS2 = jsonData["School JHS2"]
JHSDescription1 = jsonData["JHS Description1"]
JHSDescription2 = jsonData["JHS Description2"]
JHSAchievement1 = jsonData["JHS Achievement1"]
JHSAchievement2 = jsonData["JHS Achievement2"]
JHSAchievement3 = jsonData["JHS Achievement3"]




# create FPDF object
pdf = FPDF ('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
pdf.add_font('Montserrat', '', 
            r'C:\Users\JED\Desktop\Jed Esguerra\1st Year\1st Semester\Programming Logic and Design\Assignments\Assignment 9\Font\static\Montserrat-Regular.ttf',
            uni=1)

pdf.add_font('Montserrat', 'B', 
            r'C:\Users\JED\Desktop\Jed Esguerra\1st Year\1st Semester\Programming Logic and Design\Assignments\Assignment 9\Font\static\Montserrat-Bold.ttf',
            uni=1)


pdf.set_text_color(0,0,0)
pdf.set_fill_color(220,220,220)
pdf.set_font('Montserrat', 'B', 35)
pdf.cell(0,249, "", fill=1)
pdf.ln(3)
pdf.cell(0, 15, "                    " + FullName1, ln=1, fill=1)
pdf.cell(0, 15, "                    " + FullName2, ln=1, fill=1)
pdf.cell(0, 15, "                    " + FullName3, ln=1, fill=1)
pdf.ln(3)
pdf.set_font('Montserrat', '', 15)
pdf.cell(0, 12, "                                                   " + Course, ln=1, fill=1)
pdf.image('Picture.jpg', 10, 10, 0, 60)
pdf.ln(10)


pdf.set_font('Montserrat', 'B', 14)
pdf.cell(50, 10, 'PERSONAL PROFILE                                     SOCIAL ACCOUNTS', ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(0, 7, PersonalProfile1 + "                           Facebook:      " + FacebookAccount, ln=1, align='L', fill=0)
pdf.cell(0, 5, PersonalProfile2 + "                          Instagram:     " + InstagramAccount, ln=1, align='L', fill=0)
pdf.cell(0, 7, PersonalProfile3 + "                                     Twitter:           " + TwitterAccount, ln=1, align='L', fill=0)
pdf.cell(0, 5, PersonalProfile4 + "                                                                                           GitHub:          " + GitHubAccount, ln=1, align='L', fill=0)
pdf.ln(10)


pdf.set_font('Montserrat', 'B', 14)
pdf.cell(50, 10, 'CONTACT DETAILS                                        ACADEMIC PROFILE', ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 7,'Mobile: ' + MobileNumber, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', 'B', 11)
pdf.cell(0, 7, SchoolSHS, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 5, 'Gmail: ' + GmailEmail, ln=0, align='L', fill=0)
pdf.cell(0, 5, StrandSHS1, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 7, 'Address: ' + FullAddress1, ln=0, align='L', fill=0)
pdf.cell(0, 5, StrandSHS2, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 5, FullAddress2, ln=0, align='L', fill=0)
pdf.cell(0, 5, SHSDescription1, ln=1, align='L', fill=0)
pdf.cell(138, 7, SHSDescription2, ln=1, align='R', fill=0)
pdf.set_font('Montserrat', '', 8)
pdf.cell(180, 5, SHSAchievement1, ln=1, align='R', fill=0)
pdf.cell(162, 3, SHSAchievement2, ln=1, align='R', fill=0)
pdf.cell(148, 5, SHSAchievement3, ln=1, align='R', fill=0)


pdf.ln(5)
pdf.set_font('Montserrat', 'B', 14)
pdf.cell(50, 10, 'SKILLS AND ABILITIES', ln=0, align='L', fill=0)
pdf.set_font('Montserrat', 'B', 11)
pdf.cell(0, 10, "                                                   " + SchoolJHS1, ln=1, align='L', fill=0)


pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 7, SaA1, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', 'B', 11)
pdf.cell(0, 7, " " + SchoolJHS2, ln=1, align='L', fill=0)


pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 5, SaA2, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', '', 11)
pdf.cell(0, 7, " " + JHSDescription1, ln=1, align='L', fill=0)


pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 7, SaA3A, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', '', 10)
pdf.cell(0, 7, " " + JHSDescription2, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 5, SaA3B, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', '', 9)
pdf.cell(0, 7, " " + JHSAchievement1, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 7, SaA4, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', '', 9)
pdf.cell(0, 7, " " + JHSAchievement2, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 5, SaA5, ln=0, align='L', fill=0)
pdf.set_font('Montserrat', '', 9)
pdf.cell(0, 5, " " + JHSAchievement3, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(105, 7, SaA6, ln=1, align='L', fill=0)

pdf.set_font('Montserrat', '', 10)
pdf.cell(0, 5, SaA7, ln=1, align='L', fill=0)

pdf.output('ESGUERRA-EDGAR.pdf')
