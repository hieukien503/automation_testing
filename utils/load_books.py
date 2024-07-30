from lib import pd, gb

def load_books():
    gb.dfEbookData = pd.read_excel(
        open('./testData/bookData.xlsx', mode='rb'),
        sheet_name='EBook_Data'
    )

    gb.dfEbookName = pd.read_excel(
        open('./testData/bookData.xlsx', mode='rb'),
        sheet_name='EBook_Name'
    )

    for action, ebook_name in zip(gb.dfEbookData['Action'], gb.dfEbookData['Name']):
        gb.ebooks[action].append(ebook_name)
    