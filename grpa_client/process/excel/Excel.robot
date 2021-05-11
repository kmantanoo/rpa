*** Settings ***
Documentation     A test suite with a single test for ExcelTesting.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot
Library           ExcelLibrary
*** Variables ***
${document}

*** Test Cases ***
Excel Testing Robot
    Create Excel Document    doc_id=sss
    Write Excel Cell            1   1   Row1  sheet_name=Sheet
    Write Excel Cell            2   1   Row2  sheet_name=Sheet
    Save Excel Document        filename=log/test.xlsx