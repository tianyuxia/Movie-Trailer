import urllib

def read_text(file_name):
    quote_file = open(file_name)
    content = quote_file.read()
    quote_file.close()
    return content

def check_profanity(input_text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + input_text)
    output = connection.read()
    connection.close()
    if(output == "true"):
        print("Profanity Alert")
    elif(output == "false"):
        print("No Curse Word Found")
    else:
        print("Could not scan document properly")

file_name = "C:\Users\Tianyu Xia\Desktop\Udacity\Udacity-FSWD\Project 1\Profanity\quote.txt"
content = read_text(file_name)
check_profanity(content)