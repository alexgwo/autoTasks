#This code organises your .xlsx files by month based on its names.

import os

# customize your path here
path = r"C:\Users\Python\Desktop\Folder"

file_list = os.listdir(path)

for file_i in file_list:
	if ".xlsx" in file_i:
		if "Jan" in file_i:
			# move file to "January" folder
			os.rename(f"Move/{file_i}", f"Move/Jan/{file_i}")
		if "Feb" in file_i:
			# move file to "February" folder
			os.rename(f"Move/{file_i}", f"Move/Feb/{file_i}")
		if "Mar" in file_i:
			# move file to "March" folder
			os.rename(f"Move/{file_i}", f"Move/Mar/{file_i}")
		if "Apr" in file_i:
			# move file to "April" folder
			os.rename(f"Move/{file_i}", f"Move/Apr/{file_i}")
		if "May" in file_i:
			# move file to "May" folder
			os.rename(f"Move/{file_i}", f"Move/May/{file_i}")
		if "Jun" in file_i:
			# move file to "June" folder
			os.rename(f"Move/{file_i}", f"Move/Jun/{file_i}")
		if "Jul" in file_i:
			# move file to "Jul" folder
			os.rename(f"Move/{file_i}", f"Move/Jul/{file_i}")
		if "Aug" in file_i:
			# move file to "August" folder
			os.rename(f"Move/{file_i}", f"Move/Aug/{file_i}")
		if "Sept" in file_i:
			# move file to "September" folder
			os.rename(f"Move/{file_i}", f"Move/Sep/{file_i}")
		if "Oct" in file_i:
			# move file to "October" folder
			os.rename(f"Move/{file_i}", f"Move/Oct/{file_i}")
		if "Nov" in file_i:
			# move file to "November" folder
			os.rename(f"Move/{file_i}", f"Move/Nov/{file_i}")
		if "Dec" in file_i:
			# move file to "December" folder
			os.rename(f"Move/{file_i}", f"Move/Dec/{file_i}")


