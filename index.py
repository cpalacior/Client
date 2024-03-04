import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def downloadResource(params):
    response = requests.post('http://' + os.getenv('URL_PEERAS') + '/connect', json={"body":[params]})
    return response.text

def main():
    while(1):
        try:
            action = int(input('\nWhat would you like to do\n1 For download resource\n2 For upload resource\n0 To end service\n'))
        except:
            print("Enter a numeric value between 0-2")
            continue
        
        if(action == 1):
            resource = input("Enter the file you want to download:\n")
            path = downloadResource(resource)
            print(path.strip('"'))
            if path.strip('"') == '404':
                print('That file does not exist')
            else:
                response = requests.get(path.strip('"') + '/download/' + resource)
                print(response.text, "downloaded.")
        
        elif(action == 2):
            print("estamos en proceso")
            pass

        elif(action == 0):
            break
        
        else:
            print('Enter a correct value')
            
if __name__ == "__main__":
    main()