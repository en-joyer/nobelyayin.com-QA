import playwright.sync_api
import xlsxwriter

workbook = xlsxwriter.Workbook('nobelakademi.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'İsim')
worksheet.write('B1', 'Rol')
worksheet.write('C1', 'Mail')
worksheet.write('D1', 'Çift Emailler')


isimler = []
roller = []
mailler = []
ciftemailler = []

with playwright.sync_api.sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.nobelyayin.com/kurumsal/")

    bilgilerDiv = page.query_selector(".kurumsalAdresler")
    bilgiler = bilgilerDiv.query_selector_all("li")

    for li in bilgiler:
        rol = li.query_selector_all("font")
        isim = li.query_selector_all("strong")
        mail = li.query_selector_all("span")

        if len(mail) > 1:
            print("Uyarı: Birden fazla mail adresi bulundu.")
            for email in mail:
                print(email.inner_text())
                print("*" * 50)
                ciftemailler.append(email.inner_text())
                worksheet.write_column(1, 3, ciftemailler)

        for i, isim in enumerate(isim):
            print("İsim"": " + isim.inner_text())
            isimler.append(isim.inner_text())
            worksheet.write_column(1, 0, isimler)
        
        for i, rol in enumerate(rol):
            print("Rol"": " + rol.inner_text())
            roller.append(rol.inner_text())
            worksheet.write_column(1, 1, roller) 
            
        for i, mail in enumerate(mail):
            print("Mail " + str(i+1) + ": " + mail.inner_text())
            mailler.append(mail.inner_text()) 
            worksheet.write_column(1, 2, mailler)
            
        print("=" * 50)



    browser.close()
    workbook.close()

print("İşlem tamamlandı.")
