#!/usr/bin/env python3

#author@sagarkar10

#Description: This script will catch the latest 'Astro PIC Of the day from NASA website http://apod.nasa.gov/apod/astropix.html' and set it to your wallpaper in linux.

#Gotcha: This script is wriiten effeiciently to minimize repeated downloading of same image. (The last image downloaded from there must me 24hrs older else the script will not download new image)

#Todo: Next step is to tie this script with the network connection and make it automatic to download new image as it is updated in the said website. Or cron job it to repeat automatically.


import subprocess
import re

file_path = '/var/tmp/img.jpg' # complete path of the file

cmd_find = "find "+file_path+" ; exit 0 ;" # bash command to find file

cmd_change_wall = "gsettings set org.gnome.desktop.background picture-uri 'file:///"+file_path+"'" # command to change wallpaper

cmd_find_old = "find "+file_path+" -mtime +1 ; exit 0 ;" #find file older than a day

cmd_rm_old = "rm "+file_path #remove old file

cmd_get_website = "curl http://apod.nasa.gov/apod/astropix.html > /tmp/output.html" # download a website scource


p_find = subprocess.check_output([cmd_find],shell=True)

if p_find != b'':
	
	p_find_old = subprocess.check_output([cmd_find_old],shell=True)
	
	if p_find_old == b'':
		print("Up-to-date File Exist...")
		print("Download Done For today, Aborting...")
		
		p_change_wall = subprocess.call([cmd_change_wall],shell=True)
		
		print("Setting up wall paper:","Error" if p_change_wall else "Done")
		exit(0)
	else:
		print("Old File exist, Process Started...")
		
		p_rm_old = subprocess.call([cmd_rm_old],shell=True)
		print("Deleting Old imgae...")
else:
	print("No previos File found, Process Started...")


p_get_website = subprocess.call([cmd_get_website],shell=True)
print("getiing html from website:","Error" if p_get_website else "Done")

f = open('/tmp/output.html','r', encoding="ascii",errors="surrogateescape")
word = f.read()

img_url=re.findall('<a href="(image[^"]*)',word)
img_url = 'http://apod.nasa.gov/apod/'+img_url[0]
print(img_url)

cmd_get_img= "curl "+img_url+" > "+file_path
p_get_img = subprocess.call([cmd_get_img],shell=True)
print("downloading image from :"+img_url,"Error" if p_get_img else "Done")

p_get_img.wait()
p_change_wall = subprocess.call([cmd_change_wall],shell=True)
print("Setting up wall paper:","Error" if p_change_wall else "Done")

