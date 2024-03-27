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

elif mode == "E":
    delay = input("Would you like to add a delay? (Y/N): ")
    delay = delay.upper()
    duplicate = input("Would you like to remove duplicates? (Y/N): ")
    duplicate = duplicate.upper()
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
                
    if delay == "Y":
        delay = True
        delay_time = input("Enter the delay time (in seconds): ")
    elif delay == "N":
        delay = False
        delay_time = 0

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

