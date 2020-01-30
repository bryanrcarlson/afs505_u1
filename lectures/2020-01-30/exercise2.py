from sys import argv

def print_txt_stats(argv):
    script, filePath = argv
    fileHandler = open(filePath, 'r')
    #print(fileHandler.read())
    char_count = 0
    word_count = 0
    line_count = 0

    line = fileHandler.readline()
    while line:
        char_count += len(line)
        word_count += len(line.split(" "))
        line_count += 1

        line = fileHandler.readline()

    print(f"{char_count} {word_count} {line_count}")


print_txt_stats(argv)