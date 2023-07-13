import playwright.sync_api

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

        for i, isim in enumerate(isim):
            print("İsim"": " + isim.inner_text())
        
        for i, rol in enumerate(rol):
            print("Rol"": " + rol.inner_text())
            
        for i, mail in enumerate(mail):
            print("Mail " + str(i+1) + ": " + mail.inner_text())
            
        print("=" * 50)

    browser.close()
