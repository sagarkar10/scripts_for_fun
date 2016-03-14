### Description: 
This script will catch the latest 'Astro PIC Of the day from NASA website http://apod.nasa.gov/apod/astropix.html' and set it to your wallpaper in linux.

### Gotcha:
This script is wriiten effeiciently to minimize repeated downloading of same image. (The last image downloaded from there must me 24hrs older else the script will not download new image)

### Todo:
Next step is to tie this script with the network connection and make it automatic to download new image as it is updated in the said website. Or cron job it to repeat automatically.

### Use:
Just download the script and make it executable in your machine with proper permission. (eg: $ sudo chmod +x wallchange.py)

And then Run (eg: $ ./wallchange.py)

If you have changed the file before 24 hrs and still want to download again and sync the wallpaper with the website, just delete the img.jpg the file from the file_path (/var/tmp by default or your new path) and rerun the script.

The Script download the file in the /var/tmp directory in the name of img.jpg.
And its over written everytime (not for wallpaper collection :p).

If you want to change the location makesure you tweak the script variable 'file_path'


For any kind HUGS or BUGS feel free to contact me at sagarkar10@gmail.com
