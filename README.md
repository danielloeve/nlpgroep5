<<<<<<< HEAD
# Information Extraction - Groep 5

Groep 5
- Bai Jie Cao
- Daniël Loeve
- Jonas Boekema
- Tim van Rijsewijk

Als groep 5 hebben we gekozen voor Information Extraction. Met deze technologie willen we automatisch bepaalde informatie verkrijgen van een bepaald onderwerp uit een tekstbron.


Create a python function to achieve : Upon user input of his/her name the function should give number of letters in the name, arrange name in alphabetical order(A-Z), and middle 3 character of middle name.
# assumption -The middle name is just one word. 
# Supress Warnings

import warnings
warnings.filterwarnings('ignore')
#Read the input name
txt = input()
Poonam yadav yadav
print("Length of input string :" , len(txt))
words = [word.lower() for word in txt.split()]
words.sort()
print("\n")

#############################################################################

print("The sorted words are:")
for word in words:
   print(word , end = ' ' )
print("\n")

#############################################################################

li = list(txt.split(" ")) 
if len(li) < 3:
    print ("no middle name")
else:
    mid = lambda s: s[int(len(li[1])/2) - 1:int(len(li[1])/2) + 2]
    print ("The middle three characters of the middle name :" ,mid(li[1]))
Length of input string : 18


The sorted words are:
poonam yadav yadav 

The middle three characters of the middle name : ada
Problem statement 2
#Build python code to extract names of individual from Municipal Corporation of Greater Mumbai from Page 2 of this pdf 
#(http://www.udri.org/pdf/02%20working%20paper%201.pdf) 
pip install PyPDF2
Requirement already satisfied: PyPDF2 in c:\users\ajay\anaconda3\lib\site-packages (1.26.0)
Note: you may need to restart the kernel to use updated packages.
pip install textract
Requirement already satisfied: textract in c:\users\ajay\anaconda3\lib\site-packages (1.6.3)
Requirement already satisfied: python-pptx==0.6.18 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (0.6.18)
Requirement already satisfied: SpeechRecognition==3.8.1 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (3.8.1)
Requirement already satisfied: pdfminer.six==20181108 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (20181108)
Requirement already satisfied: chardet==3.0.4 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (3.0.4)
Requirement already satisfied: argcomplete==1.10.0 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (1.10.0)
Requirement already satisfied: xlrd==1.2.0 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (1.2.0)
Requirement already satisfied: EbookLib==0.17.1 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (0.17.1)
Requirement already satisfied: beautifulsoup4==4.8.0 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (4.8.0)
Requirement already satisfied: six==1.12.0 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (1.12.0)
Requirement already satisfied: extract-msg==0.23.1 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (0.23.1)
Requirement already satisfied: docx2txt==0.8 in c:\users\ajay\anaconda3\lib\site-packages (from textract) (0.8)
Requirement already satisfied: lxml>=3.1.0 in c:\users\ajay\anaconda3\lib\site-packages (from python-pptx==0.6.18->textract) (4.4.1)
Requirement already satisfied: Pillow>=3.3.2 in c:\users\ajay\anaconda3\lib\site-packages (from python-pptx==0.6.18->textract) (6.2.0)
Requirement already satisfied: XlsxWriter>=0.5.7 in c:\users\ajay\anaconda3\lib\site-packages (from python-pptx==0.6.18->textract) (1.2.1)
Requirement already satisfied: pycryptodome in c:\users\ajay\anaconda3\lib\site-packages (from pdfminer.six==20181108->textract) (3.9.9)
Requirement already satisfied: sortedcontainers in c:\users\ajay\anaconda3\lib\site-packages (from pdfminer.six==20181108->textract) (2.1.0)
Requirement already satisfied: soupsieve>=1.2 in c:\users\ajay\anaconda3\lib\site-packages (from beautifulsoup4==4.8.0->textract) (1.9.3)
Requirement already satisfied: imapclient==2.1.0 in c:\users\ajay\anaconda3\lib\site-packages (from extract-msg==0.23.1->textract) (2.1.0)
Requirement already satisfied: olefile==0.46 in c:\users\ajay\anaconda3\lib\site-packages (from extract-msg==0.23.1->textract) (0.46)
Requirement already satisfied: tzlocal==1.5.1 in c:\users\ajay\anaconda3\lib\site-packages (from extract-msg==0.23.1->textract) (1.5.1)
Requirement already satisfied: pytz in c:\users\ajay\anaconda3\lib\site-packages (from tzlocal==1.5.1->extract-msg==0.23.1->textract) (2019.3)
Note: you may need to restart the kernel to use updated packages.
pip install nltk
Requirement already satisfied: nltk in c:\users\ajay\anaconda3\lib\site-packages (3.4.5)
Requirement already satisfied: six in c:\users\ajay\anaconda3\lib\site-packages (from nltk) (1.12.0)
Note: you may need to restart the kernel to use updated packages.
import PyPDF2, urllib.request , nltk , textract
from io import BytesIO
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')  
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\AJAY\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
True
#Reading the PDF
wFile = urllib.request.urlopen('http://www.udri.org/pdf/02%20working%20paper%201.pdf')
pdfreader = PyPDF2.pdf.PdfFileReader(BytesIO(wFile.read()) )
#extracting page 2 of the docuemnt
pageObj = pdfreader.getPage(2)
page2 = pageObj.extractText()
#Cleaning the text
punctuations = ['(',')',';',':','[',']',',','...','.']
tokens = word_tokenize(page2)
stop_words = stopwords.words('english')
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

name_list = list()
check =  ['Mr.', 'Mrs.', 'Ms.']
for idx, token in enumerate(tokens):
    if token.startswith(tuple(check)) and idx < (len(tokens)-1):
        name = token + tokens[idx+1] + ' ' +  tokens[idx+2]
        name_list.append(name)

print(name_list)
['Mr.Jagdish Talreja', 'Mr.Dinesh Naik', 'Mr.Hiren Daftardar', 'Ms.Anita Naik', 'Mr.Prasad Gharat']
#Extra code
#extracting page 1 of the docuemnt
pageObj = pdfreader.getPage(1)
page2 = pageObj.extractText()
#Cleaning the text
punctuations = ['(',')',';',':','[',']',',','...','.']
tokens = word_tokenize(page2)
stop_words = stopwords.words('english')
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

name_list = list()
check =  ['Mr.', 'Mrs.', 'Ms.']
for idx, token in enumerate(tokens):
    if token.startswith(tuple(check)) and idx < (len(tokens)-1):
        name = token + tokens[idx+1] + ' ' +  tokens[idx+2]
        name_list.append(name)

print(name_list)
['Mr.Subodh Kumar', 'Mr.Rajeev Kuknoor', 'Mr.Sudhir Ghate', 'Mr.A.G. Marathe', 'Mr.R.Balachandran ,', 'Mr.V.K Phatak', 'Mr.A.NKale ,', 'Mr.A.SJainFormer Dy', 'Mr.Jagdish Talreja', 'Mr.Dinesh Naik', 'Mr.Hiren Daftardar', 'Ms.Anita Naik', 'Mr.Prasad Gharat']
wFile.close()
 
>>>>>>> 99b8d04076bb5820d42528101ea0d824224e2eb8
