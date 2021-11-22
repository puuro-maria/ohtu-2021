*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go to Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  hiuspinni
    Set Password  salasana111
    Set Password Confirmation  salasana111
    Register
    Register Should Succeed

*** Keywords ***

Register
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password  ${password_confirmation}