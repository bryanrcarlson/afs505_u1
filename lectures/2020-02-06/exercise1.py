# BioSample, Experiment, Run, time, Organism, tissue, genotype
# split "genotype" col into: subspecies, abbreviation, IRGC_Number, species
# save as new file

from sys import argv

def parse_line(line):
    values = line.split("\t")

    # Azuenca (AZ; IRGC#328, Japonica)
    variety = values[8].split(" ")[0]
    abbrev = values[8].split(" ")[1].replace("(","").replace(";","")
    subspecies = values[8].split(",")[1].replace(")","")
    irgc = values[8].split("#")[1].split(",")[0]

    obs = {
        "BioSample": values[0].strip(),
        "Experiment": values[1].strip(),
        "Run": values[5].strip(),
        "Time": values[9].strip(),
        "Organism": values[23].strip(),
        "Tissue": values[28].strip(),
        "Variety": variety.strip(),
        "Abbreviation": abbrev.strip(),
        "Subspecies": subspecies.strip(),
        "IRGC_Num": irgc.strip()
    }

    return(obs)

def write_data(data):
    outFileHandler = open("output.txt", mode = "a")
    outFileHandler.write("BioSample\tExperiment\tRun\tTime\tOrganism\tTissue\tVariety\tAbbreviation\tSubspecies\tIRGC_Num\n")
    for obs in data:
        line = obs["BioSample"] + "\t" + obs["Experiment"] + "\t" + obs["Run"] + "\t" + obs["Time"] + "\t" + obs["Organism"] + "\t" + obs["Tissue"] + "\t" + obs["Variety"] + "\t" + obs["Abbreviation"] + "\t" + obs["Subspecies"] + "\t" + obs["IRGC_Num"] + "\n"
        outFileHandler.write(line)
    
    outFileHandler.close()

def main(argv):
    script, filePath = argv
    print(filePath)

    fileHandler = open(filePath)

    # skip first line
    fileHandler.readline()

    data = []
    line = fileHandler.readline()
    while line:
        data.append(parse_line(line))
        line = fileHandler.readline()

    fileHandler.close()
    write_data(data)

    

if __name__ == "__main__":
    main(argv)