import requests, json,os.path
print("""
 _______  _  _  _______      _     ___    ___  
|__   __|(_)| ||__   __|    | |   |__ \  / _ \ 
   | |    _ | | __| |  ___  | | __   ) || (_) |
   | |   | || |/ /| | / _ \ | |/ /  / /  > _ < 
   | |   | ||   < | || (_) ||   <  / /_ | (_) |
   |_|   |_||_|\_\|_| \___/ |_|\_\|____| \___/ 

              INSTA :: @qq_iq                                 
""")
UFP = input('Username List : ')
if os.path.isfile(UFP) == False:
    input(" -"*10+"\n Err :: File Path Not Exist !\n"+" -"*10)
    exit()
sessionId = input("SessionID : ")
UFP = open(UFP).read().splitlines()
for UFP in UFP:
    url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+UFP+"&app_language=en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    cookies = {'sessionid': sessionId}
    post = requests.get(url=url,headers=headers,cookies=cookies).json()["status_msg"]
    def chk(ava):
        print ("\n", " -" * 18,"\n")
        data = '   @'+UFP+ava
        print (data)
    if post == "":
        chk("  :: Available +")
        open("Available.txt", "a").write(UFP+"\n")
    elif post == "Login expired":
        input(" -"*10+"\n Err :: Session ID Expired !\n"+" -"*10)
        exit()
    else:
        chk("  :: Not Available -")
