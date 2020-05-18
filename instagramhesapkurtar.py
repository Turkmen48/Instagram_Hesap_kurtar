from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instaspam:
    def __init__(self,hesap_adi,hesap_sahibi_adi,email,tel,aciklama):
        self.hesap_adi = hesap_adi
        self.hesap_sahibi_adi = hesap_sahibi_adi
        self.email = email
        self.tel = tel
        self.aciklama=aciklama
        self.browserprofile=webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option('prefs',{'intl.accpet_languages':'en,en_US'})
        self.browser=webdriver.Chrome('chromedriver.exe',chrome_options=self.browserprofile)
    def giris(self):
        self.browser.get("https://help.instagram.com/contact/606967319425038")
        time.sleep(2)
        fullname=self.browser.find_element_by_xpath("//*[@id='649649255120112']")
        fullname.send_keys(self.hesap_sahibi_adi)
        username=self.browser.find_element_by_xpath("//*[@id='1464214030500550']")
        username.send_keys(self.hesap_adi)
        e_mail=self.browser.find_element_by_xpath("//*[@id='328991337275965']")
        e_mail.send_keys(self.email)
        tel=self.browser.find_element_by_xpath("//*[@id='602863763172693']")
        tel.send_keys(self.tel)
        aciklama=self.browser.find_element_by_xpath("//*[@id='709786765737601']")
        aciklama.send_keys(self.aciklama)
        button=self.browser.find_element_by_xpath("//*[@id='u_0_7']")
        button.click()
        time.sleep(3)
        self.browser.close()




print("""
Bu program Turkmen tarafından kodlandı. 
Made by Turkmen
""")
hesap_adi=input("Hesabınızın kullanıcı adı")
hesap_sahibi=input("Hesap sahibinin adı")
email=input("Hesap sahibi emaili")
tel=input("hesap sahibi tel")


sec=input("Sistemde kayıtlı olan hazır bir açıklama metni mi gereyim? Yoksa kendi metnini mi girmek istersin?\nHazır metin girmek için 'h' tuşuna bas\nkendi metnini girmek için 'e' tuşuna bas")
if(sec=="e"):
    aciklama=input("aciklamanı gir")

else:
    aciklama="""
 I object to my account being closed.
 I certainly didn't break the rules.
 I want you to help me and reactivate my account. 
    """
sayac=0
while True:
    insta = Instaspam(hesap_adi, hesap_sahibi, email, tel,aciklama)
    insta.giris()
    sayac+=1
    print(f"şuana kadar {sayac} kere denendi")




