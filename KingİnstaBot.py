from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pyautogui
import subprocess as cmd
import platform
import os
if platform.system()=="Windows":
    cmd.call("color a",shell=True)

print("""
############################################
##                  ESATBEY35(KingKong)    #
##                  KingİnstaBot.py        #
############################################
""")



print("""Seçenekler:

1-)Biyografi Değiştir
2-)Foto Değiştir
3-)Unfollow Yapanları Tespit Et Ve Takipten Çık
4-)Biyografi Ve Foto Değiştir.
5-)Program Hakkında
9-)Programdan Çık
""")

secenekler=int(input("Seçiniz >>> "))
if platform.system()=="Windows":
    cmd.call("cls", shell=True)


liste=[]

takip=[]

unfollow=[]



sayi=1




def girisyapmak():
    ayarlar = Options()

    ayarlar.add_argument("--headless")

    ayarlar.add_argument("--windows-size=1920x1080")

    global driver

    driver = webdriver.Chrome(os.getcwd()+"\src\chromedriver.exe", chrome_options=ayarlar)

    if platform.system() == "Windows":
        cmd.call("cls", shell=True)
    sleep(2)
    if platform.system() == "Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    driver.get("https://www.instagram.com/")
    if platform.system() == "Windows":
        cmd.call("cls", shell=True)
    sleep(3)
    print("KingİnstaBot >>> ")
    global k_adi
    print("Bot Başlamıştır!\n")
    k_adi = input("KingİnstaBot >>> Kullanıcı Adını Giriniz: ")

    global sifre
    sifre = input("KingİnstaBot >>> Sifreyi Giriniz: ")
    print("\nGiriş Yapılıyor...\n")
    girisbutonu = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
    girisbutonu.click()
    sleep(2)
    kullaniciadi = driver.find_element_by_name("username")
    parola = driver.find_element_by_name("password")
    kullaniciadi.send_keys(k_adi)
    parola.send_keys(sifre)
    sleep(2)
    girisyap = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
    sleep(3)
    girisyap.click()
    sleep(3)



def fotodegistir():
    driver.get("https://www.instagram.com/accounts/edit/")
    koymakistediginizresminadresi=input("Resmin Dosya Yolunu Giriniz: ")
    sleep(3)
    fotodegistircss=driver.find_element_by_class_name("LUEBY")
    fotodegistircss.click()
    sleep(3)
    fotoseccss=driver.find_element_by_css_selector(".aOOlW.bIiDR")
    fotoseccss.click()
    pyautogui.typewrite(koymakistediginizresminadresi)
    sleep(1)
    pyautogui.press("enter")
    sleep(15)
    print("Foto Değiştirilmiştir!")
def biyodegistir():
    print("Lütfen Biyografinizi Önce Boş Bırakınız.!\n")
    biyodegiscek=input("Biyografiniz Ne İle Değişsin: ")
    driver.get("https://www.instagram.com/accounts/edit/")
    biyografi=driver.find_element_by_id("pepBio")
    biyografi.send_keys(biyodegiscek)
    sleep(2)
    gönderbuton=driver.find_element_by_css_selector("._5f5mN.jIbKX._6VtSN.yZn4P")
    gönderbuton.click()
    sleep(3)
    print("\nBiyografi Değiştirilmiştir!")



def takipciler():
    print("Takipçiler Tespit Ediliyor!\n")
    global cek
    global sayi1,sayi2
    sayi1=1
    sayi2=0
    driver.get("https://www.instagram.com/"+k_adi)
    sleep(3)
    takipci=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
    takipci.click()
    sleep(3)
    al = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span")
    while True:

        sayi2 += 1
        scr1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        takipciler=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/ul/div/li["+str(sayi2)+"]/div/div[1]/div/div[1]/a")
        liste.append(takipciler.text)
        if sayi2==int(al.text):
            break
        else:
            continue
    print("Takipçiler Tespit Edilmiştir!")

def takipedilenler():
    print("Takip Edilenler Tespit Ediliyor!\n")
    global sayi3,sayi4
    driver.get("https://www.instagram.com/" + k_adi)
    sleep(3)
    takipedenlerr = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
    takipedenlerr.click()
    sleep(3)
    al = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span")
    sayi4 = int(al.text)
    sayi3=0
    while True:
        sayi3 += 1
        scr1 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        sleep(0.003)
        all=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/ul/div/li["+str(sayi3)+"]/div/div[1]/div/div[1]/a")
        takip.append(all.text)
        if sayi3==int(al.text):
            break
        else:
            continue
    print("Takip Edilenler Tespit Edilmiştir!")



def takiptencik():
    unfollowyapansayi=0
    for i in takip:
        if i in liste:
            continue
        else:
            unfollow.append(i)
            print("Takip Etmeyenin İnstagram Adı: ",i)

    takipcikarsayi=int(input("Ne Kadar Unfollow Yapan Çıkarılsın: "))
    if takipcikarsayi>len(unfollow):
        print("Unfollow Yapanların Sayısından Fazla Sayı Girdiniz!")
        exit()
    elif takipcikarsayi<0:
        print("0 dan Küçük Sayı Girilemez!")
        exit()
    else:
        for i in unfollow:
            driver.get("https://www.instagram.com/" + i)
            sleep(3)
            takipetmeyibirak = driver.find_element_by_css_selector("._5f5mN.-fzfL._6VtSN.yZn4P")
            takipetmeyibirak.click()
            print("\nTakip Bırakıldı: ", i)
            takipcikarsayi -=1
            if takipcikarsayi == 0:
                print("\nİşlem Bitmiştir!")
                break
            else:
                continue

if secenekler==9:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("\nProgramdan Çıkılıyor Lütfen Bekleyin...")
    sleep(1)
    exit()
elif secenekler==5:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("""
    ############################################
    ##Programın Adı:KingİnstaBot.py                 #
    ##Programı Hazırlayan:King Kong(EsatBey35) #
    ##Program Sürümü:1.0                       #
    ##Hazırlayanın Email'i:esat3515@gmail.com  #
    ############################################
    """)
elif secenekler==1:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("KingİnstaBot >>>")
    girisyapmak()
    if not "has_profile_pic" in driver.page_source:
        print("Kullanıcı Adı Şifre Yanlış Çıkış Yapılıyor.")
        driver.quit()
        exit()
    else:
        print("Giriş Yapıldı.")
        biyodegistir()
elif secenekler==2:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("KingİnstaBot >>>")
    girisyapmak()
    if not "has_profile_pic" in driver.page_source:
        print("Kullanıcı Adı Şifre Yanlış Çıkış Yapılıyor.")
        driver.quit()
        exit()

    else:
        print("Giriş Yapıldı.")
        fotodegistir()
elif secenekler==3:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("KingİnstaBot >>>")
    girisyapmak()
    if not "has_profile_pic" in driver.page_source:
        print("Kullanıcı Adı Şifre Yanlış Çıkış Yapılıyor.")
        driver.quit()
        exit()
    else:
        print("Giriş Yapıldı.")
        takipciler()
        takipedilenler()
        takiptencik()
elif secenekler==4:
    if platform.system()=="Windows":
        cmd.call("cls", shell=True)
        cmd.call("color a", shell=True)
    print("KingİnstaBot >>>")
    girisyapmak()
    if not "has_profile_pic" in driver.page_source:
        print("Kullanıcı Adı Şifre Yanlış Programdan Çıkış Yapılıyor.")
        driver.quit()
        exit()
    else:
        print("Giriş Yapıldı.")
        fotodegistir()
        biyodegistir()

else:
    print("Yanlış Seçenek Girdiniz Programdan Çıkılıyor!")
    exit()
try:
    os.remove(os.getcwd() + "\debug.log")
except:
    sleep(5)
    driver.quit()