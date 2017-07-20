#things done before the program
#wget -r --no-parent .html website-address


import os
import glob
import re
os.system("wget -r --no-parent .html www.example.com")

#start_path='/home/aashan/c/webscrapping-website/lums.edu.pk/'
start_path='.'
#start_path="https://aashan007.github.io/"
for path,dirs,files in os.walk(start_path):
	for filename in files:
		#print os.path.join(path,filename)
		fpath=os.path.join(path,filename)
		email_list=[]
		with open(fpath) as f:
			text=f.read()						# reading the separate file
			match=re.findall(r'[\w\.-]+@[\w\.-]+\.\w+',text)   #email extractor
			scrapped_list=list(match)
			if(len(match)==0):
				continue				#removing the null list
			else:
				#str1 = ' '.join(match)

				email_list=email_list+scrapped_list
				#email_list.append(match)#listing all the files which has an email id
		print email_list
		

		#f=open("fpath","r")
		#print f.read()
		#f.close()
