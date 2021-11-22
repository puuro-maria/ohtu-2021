*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  viivi  viivi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kapteeni
    Output Should Contain  Username must be at least 3 digits long and contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  kapteeni  kapteen
    Output Should Contain  Password must be at least 8 digits long and contain at least one number

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pirulainen  pirulainen
    Output Should Contain  Password must be at least 8 digits long and contain at least one number

*** Keywords ***

Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command