#Import the HTML file to parse
def read():

    #fileName = "test.htm"
    fileName = input("Enter HTML file: ")
    import parser

    
    if (fileName == "test.htm"):
        fileName = "core/test.htm"    
    if (":"  not in fileName):
        #Parse HTML for local file
        try:
            with open(fileName, "r") as file:
                HTML=file.read().split("\n")
                parser.parse(HTML, False, fileName)
                

        except AssertionError as msg:
            print(msg)
    else:
        #Parse HTML for websites on the internet
        import requests
        HTML = requests.get(fileName, verify=True)
        parser.parse(HTML.text.split(">"), False, fileName)
        
read()