*** Settings ***
Documentation       A resource file with reusable keywords and variables.
Library             ExcelLibrary
*** Keywords ***
Check created excel doc
    Create Excel Document doc_id=xlsx
    Close All Excel Documents