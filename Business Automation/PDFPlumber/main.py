import pandas as pd
import pdfplumber

# Texas
tx_list = []
with pdfplumber.open("pdfs/Texas.pdf") as tpdf:
    total_pagestx = len(tpdf.pages)
    for i in range(0, total_pagestx):
        first_page = tpdf.pages[i]
        variable_to_add = first_page.extract_text()
        tx_list.append(variable_to_add)
# print(tx_list)

# Louisiana
la_list = []
with pdfplumber.open("pdfs/Louisiana.pdf") as lapdf:
    total_pagesla = len(lapdf.pages)
    for i in range(0, total_pagesla):
        first_page = lapdf.pages[i]
        variable_to_add = first_page.extract_text()
        la_list.append(variable_to_add)
# print(la_list)

ka_list = []
with pdfplumber.open("pdfs/Kansas.pdf") as kapdf:
    total_pageska = len(kapdf.pages)
    for i in range(1, total_pageska):
        first_page = kapdf.pages[i]
        variable_to_add = first_page.extract_text()
        ka_list.append(variable_to_add)

na_list = []
with pdfplumber.open("pdfs/Nebraska.pdf") as napdf:
    total_pagesna = len(napdf.pages)
    for i in range(0, total_pagesna):
        first_page = napdf.pages[i]
        variable_to_add = first_page.extract_text()
        na_list.append(variable_to_add)
# print(na_list)

ut_list = []
with pdfplumber.open("pdfs/Utah.pdf") as utpdf:
    total_pagesut = len(utpdf.pages)
    for i in range(0, total_pagesut):
        first_page = utpdf.pages[i]
        variable_to_add = first_page.extract_text()
        ut_list.append(variable_to_add)
# print(ut_list)

utoos_list = []
with pdfplumber.open("pdfs/Utah out of state.pdf") as utoospdf:
    total_pagesutoos = len(utoospdf.pages)
    for i in range(0, total_pagesutoos):
        first_page = utoospdf.pages[i]
        variable_to_add = first_page.extract_text()
        utoos_list.append(variable_to_add)
# print(utoos_list)


# Playing with master list and reading lines, but puts the state as one line and another as
# with open("master_list.txt", encoding="utf8") as ma_list:
#     ln = ma_list.readline()
#     lncnt = 1
#     while ln:
#         print("Line {}: {}".format(lncnt, ln.strip()))
#         ln = ma_list.readline()
#         lncnt += 1


