
with open('45_data.txt','r')as file:
    data = file.read()
    new = data.replace('utilize','use')
    file_name = input("Save file as: >")     #Prompt for the output file name
    with open(f'{file_name}.txt','w') as s:  #Save output as a file
        s.write(new)
        s.close()
    file.close()




