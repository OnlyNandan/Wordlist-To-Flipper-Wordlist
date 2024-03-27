print("""
__        __                  _  _      _       _       ____                                   _               
\ \      / /  ___   _ __   __| || |    (_) ___ | |_    / ___|  ___   _ __  __   __  ___  _ __ | |_   ___  _ __ 
 \ \ /\ / /  / _ \ | '__| / _` || |    | |/ __|| __|  | |     / _ \ | '_ \ \ \ / / / _ \| '__|| __| / _ \| '__|
  \ V  V /  | (_) || |   | (_| || |___ | |\__ \| |_   | |___ | (_) || | | | \ V / |  __/| |   | |_ |  __/| |   
   \_/\_/    \___/ |_|    \__,_||_____||_||___/ \__|   \____| \___/ |_| |_|  \_/   \___||_|    \__| \___||_|   
                                                                                                               
""")

# By Nandan R
# Date: 27/03/2024
# Version 2.0

mode = input("Would you like to use the simple mode or Expert mode? (S/E): ")
print()
mode = mode.upper()
wordlist = input("Enter the wordlist Filename (.TXT): ")
if wordlist.endswith(".txt"):
    pass
else:  
    wordlist = wordlist + ".txt"
print()
output = input("Enter the output Filename (.TXT): ")
if output.endswith(".txt"):
    pass    
else: 
    output = output + ".txt"
print()
output = output.lower()


if mode == "S":

    print(f"Converting {wordlist} to {output}")
    try:
        with open(wordlist, "r") as f:
            with open(output,"w") as w:
                lines = f.readlines()
                for line in lines:
                    w.write("STRING " + line + "\n")
                    w.write("ENTER" + "\n")
    except FileNotFoundError:
        print("File Not Found")
        exit()

    except EndOfFileError:
        pass

    except Exception as e:
        print(f"An Error Occured: {e}")
        exit()

    print(f"Conversion Completed Check the output file @ {output}")

def delaymode():
    global delay, delay_time
    delay = input("Would you like to add a delay? (Y/N): ")
    delay = delay.upper()
    if delay == "Y":
        delay = True
        delay_time = input("Enter the delay time (in seconds): ")
    elif delay == "N":
        delay = False
        delay_time = 0
def duplicatemode():

    duplicate = input("Would you like to remove duplicates? (Y/N): ")
    duplicate = duplicate.upper()
    print()

    if duplicate == "Y":
        with open (wordlist, "r") as read:
            lines = read.readlines()
            lc={}
            for line in lines:
                if line in lc:
                    lc[line]+=1
                else:
                    lc[line]=1
        with open (wordlist, "w") as write:
            for line in lc:
                write.write(line)
def alternatemode():

    global case, casechoice, convert
    convert = []
    case = input("Would you like to convert the wordlist to Alternate Case? (Y/N): ")
    case = case.upper()
    if case == "Y":
        casechoice = input("Would you like to configure it (Y/N): ")
        casechoice = casechoice.upper()
        if casechoice == "Y":
            casechoice = True
            title= input("Would you like to convert the wordlist to Title Case? (Y/N): ")
            title = title.upper()
            if title == "Y":
                convert += "T"
            upper = input("Would you like to convert the wordlist to Uppercase? (Y/N): ")
            upper = upper.upper()
            if upper == "Y":
                convert += "U"
            lower = input("Would you like to convert the wordlist to Lowercase? (Y/N): ")
            lower = lower.upper()
            if lower == "Y":
                convert += "L"
        elif casechoice == "N":
            convert = ["T"]
    Converter()
def Converter():
    for i in convert:
        if i == "T":
            with open(wordlist, "r") as f:
                lines = f.readlines()
            with open(wordlist, "a") as w:
                for line in lines:
                    w.write(line.title())
            
        elif i == "U":
            with open(wordlist, "r") as f:
                lines = f.readlines()
            with open(wordlist, "a") as w:    
                for line in lines:
                    w.write(line.upper())
        elif i == "L":
            with open(wordlist, "r") as f:
            
                lines = f.readlines()
            with open(wordlist, "a") as w:    
                for line in lines:
                    w.write(line.lower())
    

if mode == "E":
    delaymode()
    alternatemode()
    duplicatemode()
        
    print()
    print(f"Converting {wordlist} to {output} with delay set to {delay}.")
    try:
        with open(wordlist, "r") as f:
            with open(output,"w") as w:
                lines = f.readlines()
                for line in lines:
                    w.write("STRING " + line + "\n")
                    w.write("ENTER" + "\n")
                    if delay:
                        w.write("DELAY " + delay_time + "\n")
    except FileNotFoundError:
        print("File Not Found")
        exit()

    except EndOfFileError:
        pass

    except Exception as e:
        print(f"An Error Occured: {e}")
        exit()

    print(f"Conversion Completed Check the output file @ {output}")

