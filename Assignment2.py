# Yusuf Emir Cömert - 2220765023 - Assignment 2
patient_information = []
names = []                                                                              #Names will be in this list

def read():
    global input_file
    input_file = open("doctors_aid_inputs.txt", 'r')                                    #For reading the text file

def create(a):
    newPatient = a[7:].split(", ")                                                      #create has 6 characters and we have space thats why it starts from 7.
    patient_information.append(newPatient)
    save_output(str("Patient " + newPatient[0] + " is recorded."))

def save_output(text):
    output_file.writelines((text))
    output_file.writelines(('\n'))

def findPatient(command):                                                               #This is the main function and does the most job
    actualCommand = command.split()[0]                                                  #I was going to name it command but I already used command name so I called it actualCommand
    name = command.split()[1]                                                           #Index 0 is create,probability,list exc. thats why I used 1.
    for find in range(len(patient_information)):
        if name in patient_information[find]:
            probability(command, find)
            recommendation(command, find)
            remove(command, find)
            break
        else:
            pass

    else:
        save_output((actualCommand.capitalize(), " for ", name, " cannot be calculated due to absence."))

def remove(command, find):
    if command.startswith("remove "):
        save_output(("Patient " + patient_information[find][0] + " is removed."))
        patient_information.pop(find)                                                   #Pop's job is to remove some informations.

def calculate(find):
    global risk
    global actualRisk
    incidence, total = (patient_information[find][3]).split("/")                        #For splitting the denominator and nominator.
    incidence = float(incidence)                                                        #It looks like string to python thats why I needed to turn it to float.
    total = float(total)
    accuracy = float(patient_information[find][1])
    predicted = (total - incidence) * (1 - accuracy) + incidence                        #Calculating the probability.
    risk = incidence / predicted
    actualRisk = round(100 * risk, 2)                                                   #actualRisk = Probability

def probability(command, find):
    if command.startswith("probability "):
        calculate(find)
        save_output(("Patient " + patient_information[find][0] + " has a probability of " + str(actualRisk) + "% of having " + patient_information[find][2].lower() + "."))
    else:
        pass

def recommendation(command, find):
    if command.startswith("recommendation "):
        calculate(find)
        if risk < float(patient_information[find][-1]):                                 #If risk < probability, treatment risk is much/less that's why program will suggest or not suggest to take the treatment.
            save_output(("System suggests " + patient_information[find][0] + " NOT to have the treatment."))
        else:
            save_output(("System suggests " + patient_information[find][0] + " to have the treatment."))

def list():                 #Creating the table
    save_output(("\n{:<15}{:<15}{:<20}{:<15}{:<20}{:<5}".format("Patient", "Diagnosis", "Disease", "Disease", "Treatment", "Treatment")))
    save_output(("{:<15}{:<15}{:<20}{:<15}{:<20}{:<5}".format("Name", "Accuracy", "Name", "Incidence", "Name", "Risk")))
    save_output(("{:<94}".format(94*"-",)))

    for info in range(len(patient_information)):
        save_output(("{:<15}{:<15}{:<20}{:<15}{:<20}{:<5}".format(patient_information[info][0], patient_information[info][1],patient_information[info][2], patient_information[info][3], patient_information[info][4], patient_information[info][5])))

read()
output_file = open('doctors_aid_outputs.txt', 'w')                                       #This command is for writing output file
                                                                                         #I wrote it here because defining it global
while True:
    line = input_file.readlines()
    for say in range(len(line)):
        if line[say].startswith("create "):
            create(line[say])
        elif line[say].startswith("list"):
            list()
        else:
            findPatient(line[say])
    if not line:
        break