############################################################
# Abstract:
#       - The purpose of this script is to be run as is,
#         with no arguments to sort customer files
#         into their proper folders
############################################################

import os
import shutil

DEBUG_MODE = 2
# 0 = ERROR
# 1 = WARNING
# 2 = INFO

# Global variables
insurance_companies = ["Geico", "MMG", "Progressive", "Statefarm", "Vermont Mutual", "Allstate", "American Family", 
                       "General Liberty Insurance", "Trumbull Hartford"]

def print_debug(msg, mode):
    if mode <= DEBUG_MODE:
        if mode == 0:
            print("=== ERROR ======", msg)
        if mode == 1:
            print("=== WARNING ====", msg)
        if mode == 2:
            print("=== INFO =======", msg)

def main():
    for item in os.listdir():
        if item not in insurance_companies:
            # Only care about folders that aren't the insurance company folders
            for insurance_company in insurance_companies:
                if insurance_company.lower() == "trumbull hartford":
                    for token in insurance_company.lower().split():
                        if token in item.lower():
                            print_debug("Found " + item + " not in the correct folder...", 2)
                            shutil.move(item, insurance_company)
                            print_debug("Moving " + item + " into " + insurance_company + " folder...", 2)
                elif insurance_company.lower() in item.lower():
                    # If an insurance company name is found in the folder name,
                    # put it into that folder
                    print_debug("Found " + item + " not in the correct folder...", 2)
                    shutil.move(item, insurance_company)
                    print_debug("Moving " + item + " into " + insurance_company + " folder...", 2)
    return

if __name__ == "__main__":
    main()