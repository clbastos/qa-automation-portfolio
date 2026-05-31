import pytest
import io
import sys
from playwright.sync_api import sync_playwright


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").click()
    page.wait_for_timeout(2000)
    
    #Clicar no botão de login
    page.locator("[data-test=\"login-button\"]").click()
    page.wait_for_timeout(2000) 

    #clicar no botão de adicionar ao carrinho o item
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    #clicar no carrinho
    page.wait_for_timeout(2000)
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.wait_for_timeout(2000)


    
    # Verificar se o item foi adicionado ao carrinho
    if page.locator("text=Sauce Labs Backpack").is_visible():
        print("✅ ITEM ADICIONADO AO CARRINHO COM SUCESSO!")
    else:
        print("❌ ERRO: Item não encontrado no carrinho!")





    input("Pressione Enter para fechar o navegador...")
    browser.close()