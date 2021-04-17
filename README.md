# EXIF_date_to_title
Very minimalistic python TK GUI  
to rename image files based on EXIF creation date and custom label

Renames image files to label + file creation date + count 
Creation date is read if EXIF data is available  
Otherwise get_exif_date returns nullstring  
> Example 1: img_140015.jpg -> label_2021_01_02_1_.jpg  
> Example 2: scann_15.jpg -> label.jpg  

![GUI](https://github.com/xngst/EXIF_date_to_title/blob/master/img/exif_2_title.png)
