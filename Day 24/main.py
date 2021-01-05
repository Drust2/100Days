#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r".\input\letters\starting_letter.docx", "r") as template_letter:
    template = template_letter.readlines()

with open(r".\Input\Names\invited_names.txt", "r") as filen:
    names = filen.readlines()

to_replace = "[name],"
for i in names:
    current_name = i.strip()
    letter = template
    letter[0] = letter[0].replace(to_replace, current_name + ",")
    title = f"Letter_for_{current_name}"
    to_replace = current_name + ","
    with open(f".\output\ReadyToSend\{title}.txt", "a") as file:
        for i in letter:
            file.write(i)