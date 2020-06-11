from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import ttk
import os
from selenium.webdriver.common.action_chains import ActionChains

window = tk.Tk()
window.title("Katagori XML Olusturucu")
window.geometry('510x150')

urlLabel = ttk.Label(window, text="Lütfen kategori URL'si giriniz: ")
urlLabel.grid(column=0, row=0, padx=(10, 10), pady=(2, 2))

urlEntry = ttk.Entry(window, width=50)
urlEntry.grid(column=1, row=0, padx=(10, 10), pady=(2, 2))
urlEntry.focus()

counterLabel = ttk.Label(window, text="Başlangıç Stok Kodu giriniz: ")
counterLabel.grid(column=0, row=1, padx=(10, 10), pady=(2, 2))

counterEntry = ttk.Entry(window, width=50)
counterEntry.grid(column=1, row=1, padx=(10, 10), pady=(2, 2))

infoLabel = ttk.Label(window, text="")
infoLabel.grid(column=1, row=4, padx=(10, 10), pady=(2, 2))
infoLabel2 = ttk.Label(window, text="")
infoLabel2.grid(column=1, row=5, padx=(10, 10), pady=(2, 2))

mainCatagoryLabel = ttk.Label(window, text="Ana Kategori Seçiniz: ")
mainCatagoryLabel.grid(column=0, row=2, padx=(10, 10), pady=(2, 2))
mainCatagoryValues = ["HOPARLÖR", "ANFİ&MİKSER", "MİKROFON", "TAŞINABİLİR SİSTEM", "STÜDYO EKİPMAN", "SAHNE IŞIK",
                      "OKUL", "CAMİ", "STAND", "KABLO&JAK", "HAZIR PAKET", "MÜZİK ALETLERİ"]
mainCatagoryComboBox = ttk.Combobox(window, state="readonly", values=mainCatagoryValues)
mainCatagoryComboBox.grid(column=1, row=2, padx=(10, 10), pady=(2, 2))

subCatagoryLabel = ttk.Label(window, text="Alt Kategori Seçiniz: ")
subCatagoryLabel.grid(column=0, row=3, padx=(10, 10), pady=(2, 2))
subCatagoryValues = [["-ANA KATEGORİ SEÇİNİZ-"],
                     ["KABİN HOPARLÖR", "DUVAR HOPARLÖR", "TAVAN HOPARLÖR", "HOPARLÖR BİLEŞENLERİ",
                      "TAŞINABİLİR HOPARLÖR",
                      "AKTİF HOPARLÖR", "HORN HOPARLÖR", "SIVA ÜSTÜ", "ÜNİT"],
                     ["MİKSERLER", "MONO / STEREO ANFİLER", "BÖLGELİ ANFİLER", "EV ANFİLERİ", "CAMİ ANFİLERİ",
                      "SES MİKSERLERİ",
                      "POWER ANFİLER", "MEVLÜT ANFİLERİ", "ÇANTA AMFİLER"],
                     ["KABLOSUZ MİKROFON", "KABLOLU MİKROFON", "MASA MİKROFON", "YAKA MİKROFON", "CONDENSER", "MEGAFON",
                      "HEADSET",
                      "DAVUL", "KORO", "KAMERA", "ENSTRÜMAN"],
                     ["LASTVOİCE", "HEPA MERZ", "WESTA", "OYİLİTY", "OSAWA", "ANEKA"],
                     ["REFERANS MONİTÖRÜ", "CONDENSER MİKROFON", "KULAKLIK", "HAZIR PAKETLER", "KAYIT MİKSER",
                      "SES KARTI",
                      "MİDİ KLAVYE", "STANDLAR", "POP FİLTRE", "SHOCK MOUNT", "PHANTOM"],
                     ["MARKALAR", "SİS & KAR MAKİNELERİ", "MOVİNG HEAD", "LAZER IŞIK", "LED & PAR", "SPOT IŞIK",
                      "STROBE ÇAKAR",
                      "DİSKO TOPU", "IŞIK MASASI", "AYNALI KÜRE", "KAMPANYA"],
                     ["TAVSİYE ETTİKLERİMİZ", "HAZIR PAKETLER", "İÇ MEKAN HOPARLÖRÜ", "DIŞ MEKAN HOPARLÖRÜ",
                      "ZİL SAATLERİ",
                      "OKUL ANFİLERİ", "TÖREN HOPARLÖRLERİ", "MİKROFONLAR"],
                     ["HAZIR PAKETLER", "CAMİ ANFİLERİ", "İÇ HOPARLÖR", "EZAN HOPARLÖR", "EZANMATİKLER",
                      "VAKİTMATİKLER",
                      "EL MİKROFONLAR", "YAKA MİKROFONLAR", "MEVLÜT ANFİLERİ"],
                     ["DİĞER", "MİKROFON SEHPASI", "NOTA SEHPASI", "ORG SEHPASI", "HOPARLÖR SEHPASI", "HOPARLÖR ASKISI",
                      "GİTAR / BAĞLAMA", "MONİTÖR STANDI", "MİKSER STANDI", "IŞIK STANDLARI"],
                     ["HAZIR KABLOLAR", "HOPARLÖR KABLOLARI", "MİKROFON KABLOSU", "SPEAKON KONNEKTÖR", "XLR JAK",
                      "GİTAR JAK",
                      "MULTİCORE", "STAGE BOX", "RCA/AUX KABLO"],
                     ["CANLI MÜZİK PAKETLERİ", "AKTİF + PASİF HOPARLÖR SET", "DUVAR HOPARLÖR SETLERİ",
                      "TAVAN HOPARLÖR SETLERİ",
                      "CAMİ PAKETLERİ", "OKUL PAKETLERİ", "STÜDYO KAYIT PAKETLERİ"],
                     ["TELLİ ÇALGILAR", "VURMALI ÇALGILAR", "ÜFLEMELİ ÇALGILAR", "TUŞLU ÇALGILAR", "YAYLI ÇALGILAR",
                      "YAMAHA MÜZİK ALETLERİ"]]
subCatagoryComboBox = ttk.Combobox(window, state="readonly", values=subCatagoryValues[0])
subCatagoryComboBox.grid(column=1, row=3, padx=(10, 10), pady=(2, 2))


def subCatagoryUptade(self):
    subCatagoryComboBox.set("-SEÇİNİZ-")
    subCatagoryComboBox.configure(values=subCatagoryValues[mainCatagoryComboBox.current() + 1])


mainCatagoryComboBox.bind("<<ComboboxSelected>>", subCatagoryUptade)


def recFillList(productImageSource):
    if len(productImageSource) < 5:
        productImageSource.append(
            "<Resim" + str((len(productImageSource) + 1)) + "></Resim" + str((len(productImageSource) + 1)) + ">")
        return recFillList(productImageSource)
    else:
        return productImageSource


def clicked():
    mainCatagoryText = mainCatagoryComboBox.get()
    mainCatagoryText = re.sub('&', '', mainCatagoryText)
    mainCatagoryText = re.sub('/', '', mainCatagoryText)
    mainCatagoryText = re.sub('\+', '', mainCatagoryText)
    mainCatagoryText = re.sub(' ', '', mainCatagoryText)
    mainCatagoryText = re.sub('İ', 'I', mainCatagoryText)
    mainCatagoryText = re.sub('Ş', 'S', mainCatagoryText)
    mainCatagoryText = re.sub('Ç', 'C', mainCatagoryText)
    mainCatagoryText = re.sub('Ö', 'O', mainCatagoryText)
    mainCatagoryText = re.sub('Ü', 'U', mainCatagoryText)
    mainCatagoryText = re.sub('Ğ', 'G', mainCatagoryText)
    try:
        os.mkdir("XMLs")
    except FileExistsError:
        print("Directory already exists")
    try:
        os.mkdir("XMLs\\" + mainCatagoryText)
    except FileExistsError:
        print("Directory already exists")

    #fileName = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    fileName = subCatagoryComboBox.get()
    fileName = re.sub('&', '', fileName)
    fileName = re.sub('/', '', fileName)
    fileName = re.sub('\+', '', fileName)
    fileName = re.sub(' ', '', fileName)
    fileName = re.sub('İ', 'I', fileName)
    fileName = re.sub('Ş', 'S', fileName)
    fileName = re.sub('Ç', 'C', fileName)
    fileName = re.sub('Ö', 'O', fileName)
    fileName = re.sub('Ü', 'U', fileName)
    fileName = re.sub('Ğ', 'G', fileName)

    resultFile = open("XMLs\\" + mainCatagoryText + "\\" + fileName + ".xml", "w", encoding='utf-8')
    resultFile.write("<root>\n")

    StockCode = int(counterEntry.get())

    options = Options()
    options.headless = True
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get(urlEntry.get())

    for i in range(0, 100):
        ActionChains(browser).move_to_element(
            browser.find_element_by_xpath('//*[@id="divSayfalamaAlt"]')).perform()
        time.sleep(5)
    time.sleep(250)

    failedLinks = []
    links = browser.find_elements_by_xpath('//div[@class="productName"]/a')

    for link in links:
        try:
            newBrowser = webdriver.Chrome()
            newBrowser.get(link.get_attribute('href'))
            time.sleep(1)

            productName = newBrowser.find_element_by_xpath('//h1/span').text

            productCatagoryText = mainCatagoryComboBox.get() + "|" + subCatagoryComboBox.get()

            productPrices = newBrowser.find_elements_by_xpath('//span[@class="spanFiyat"]')

            productOldPrices = productPrices[0].text[1::]
            productOldPricesText = str(productOldPrices).replace('.', '')

            productNewPrices = productPrices[1].text[1::]
            productNewPricesText = str(productNewPrices).replace('.', '')

            productBrand = newBrowser.find_element_by_xpath('//span[@class="right_line Marka"]/a/span').text

            productDetailSource = newBrowser.find_element_by_xpath('//div[@class="urunTabAlt"]').text
            productDetailSource = re.sub('yonka', 'ekonomi', productDetailSource)
            productDetailSource = re.sub('Yonka', 'Ekonomi', productDetailSource)

            productStockCode = str(StockCode)

            productImageSource = []
            productImageSources = newBrowser.find_elements_by_xpath('//img[@id="imgurunresmi"]')

            i = 1

            for productImage in productImageSources:
                productImageSourceText = re.sub('thumb/', '', productImage.get_attribute('src'))
                productImageSourceText = re.sub('https', 'http', productImageSourceText)
                if i == 1:
                    productImageSourceText = "<Resim>" + productImageSourceText + "</Resim>"
                else:
                    productImageSourceText = "<Resim" + str(i) + ">" + productImageSourceText + "</Resim" + str(i) + ">"
                i += 1
                productImageSource.append(productImageSourceText)

            productImageSource = recFillList(productImageSource)

            urunXML = "<urun>\n" + "<StokKodu>" + productStockCode + "</StokKodu>\n" + "<Katagori>" + productCatagoryText + \
                      "</Katagori>\n" + "<StokAdi>" + productName + "</StokAdi>\n" + "<PiyasaFiyati>" + productOldPricesText + \
                      "</PiyasaFiyati>\n" + "<SatisFiyati1>" + productNewPricesText + "</SatisFiyati1>\n" + "<MarkaAdi>" + productBrand + \
                      "</MarkaAdi>\n" + "<Detay>" + productDetailSource + "</Detay>\n" + \
                      productImageSource[0] + "\n" + productImageSource[1] + "\n" + productImageSource[2] + "\n" + \
                      productImageSource[3] + "\n" + "</urun>\n"

            urunXML = re.sub('&', '-', urunXML)

            resultFile.write(urunXML)

            infoLabel.configure(text=productStockCode + " stok kodlu ürün eklendi!")

            print(productStockCode + " stok kodlu " + productName + " eklendi!")
            StockCode += 1

        except:
            print("Ürün eklenemedi! Sıradaki ürüne geçiliyor...")
            failedLinks.append(link.get_attribute('href'))
        newBrowser.close()

    time.sleep(10)
    resultFile.write("</root>")

    browser.close()
    result = str(len(links)) + " üründen, " + str((len(links) - len(failedLinks))) + " ürün eklendi."
    if (StockCode - 1) < int(counterEntry.get()):
        result2 = "Ürün eklenemedi!"
    else:
        result2 = "En son " + str(StockCode - 1) + " stok kodlu ürün eklendi! Tarama tamamlandı!"

    print(result)
    infoLabel.configure(text=result)
    infoLabel2.configure(text=result2)

    print("Eklenemeyen ürünler:")
    print(failedLinks)


functionButon = ttk.Button(window, text="XML Oluştur", command=clicked)
functionButon.grid(column=0, row=4, padx=(10, 10), pady=(2, 2))
window.call('wm', 'attributes', '.', '-topmost', '1')
window.mainloop()
