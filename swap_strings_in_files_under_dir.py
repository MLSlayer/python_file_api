import re
import os
import glob

base_dir = input("Please enter the base directory to walk through")
old_s = input("Please enter the string you want to replace")
new_s = input("Please enter the replacement string")

correct_inputs=input("Do these values you correct?\nbase_directory: " + base_dir + "\nstring to replace: "
                + old_s + "\nreplacement string: " + new_s + "\nEnter in y to continue")

if correct_inputs != "y":
    exit(0)

base_dir = base_dir if base_dir[-1] == "/" else base_dir + "/"

for file in glob.iglob(base_dir + "**/*", recursive=True):
    if os.path.isdir(file):
        continue
    try :
        with open(file) as f:
            s = f.read()
        with open(file, 'w') as f:
            s = re.sub(old_s, new_s, s)
            f.write(s)
    except Exception as e:
        print("skipping file " + file + " due to Exception : " + str(e))
