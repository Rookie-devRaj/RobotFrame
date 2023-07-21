*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://www.saucedemo.com/

*** Test Cases ***
Login and Add Items to Cart
    Open Browser    ${BASE_URL}    chrome
    Maximize Browser Window
    Input Text    id:user-name    standard_user
    Input Text    id:password    secret_sauce
    Submit Button    id:login-button
    Click Button    id:add-to-cart-sauce-labs-bike-light
    Click Link    css:a.shopping_cart_link
    Click Button    id:remove-sauce-labs-bike-light
    Click Button    id:continue-shopping
    Click Button    id:add-to-cart-sauce-labs-bike-light
    Click Link    css:a.shopping_cart_link
    Click Button    id:continue-shopping
    Click Button    id:checkout
    Input Text    id:first-name    Raj
    Input Text    id:last-name    Singh
    Input Text    id:postal-code    829107
    Submit Button    id:continue
    Submit Button    id:finish
    Click Button    id:back-to-products
    Click Button    id:react-burger-menu-btn
    Click Link    id:logout_sidebar_link
    Close Browser