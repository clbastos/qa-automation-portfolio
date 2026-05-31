import pytest
import io
import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        accept_downloads=True,
        locale="pt-BR"
    )
    page = browser.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(20000)

    page.goto("https://www.saucedemo.com/", wait_until="domcontentloaded")
    page.wait_for_timeout(2000) 

        #Digitar o nome de usuário
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").click()
    page.wait_for_timeout(2000) 

    #Digitar a senha
    page.locator("[data-test=\"password\"]").fill("1234")
    page.locator("[data-test=\"password\"]").click()
    page.wait_for_timeout(2000)
    
    #Clicar no botão de login
    page.locator("[data-test=\"login-button\"]").click()
    page.wait_for_timeout(2000) 

    if page.url == "https://www.saucedemo.com/inventory.html":
        print("✅ LOGIN REALIZADO COM SUCESSO!")
    elif "error" in page.content().lower():
        print("❌ ERRO: Credenciais inválidas!")


    input("Pressione Enter para fechar o navegador...")
    browser.close()