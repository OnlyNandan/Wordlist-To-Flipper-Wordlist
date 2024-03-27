print("""
__        __                  _  _      _       _       ____                                   _               
\ \      / /  ___   _ __   __| || |    (_) ___ | |_    / ___|  ___   _ __  __   __  ___  _ __ | |_   ___  _ __ 
 \ \ /\ / /  / _ \ | '__| / _` || |    | |/ __|| __|  | |     / _ \ | '_ \ \ \ / / / _ \| '__|| __| / _ \| '__|
  \ V  V /  | (_) || |   | (_| || |___ | |\__ \| |_   | |___ | (_) || | | | \ V / |  __/| |   | |_ |  __/| |   
   \_/\_/    \___/ |_|    \__,_||_____||_||___/ \__|   \____| \___/ |_| |_|  \_/   \___||_|    \__| \___||_|   
                                                                                                               
""")

# By Nandan R
# Date: 27/03/2024
# Version 1.0

wordlist = input("Enter the wordlist Filename (.TXT): ")
output = input("Enter the output Filename (.TXT): ")
output = output.lower()
delay = input("Would you like to add a delay? (Y/N): ")
delay = delay.upper()
if delay == "Y":
    delay = True
    delay_time = input("Enter the delay time (in seconds): ")
elif delay == "N":
    delay = False
    delay_time = 0

print()
print(f"Converting {wordlist} to {output} with delay set to {delay}.")

with open(wordlist, "r") as f:
    with open(output,"w") as w:
        lines = f.readlines()
        for line in lines:
            w.write("STRING " + line + "\n")
            w.write("ENTER" + "\n")
            if delay:
                w.write("DELAY " + delay_time + "\n")
print(f"Conversion Completed Check the output file @ {output}")

