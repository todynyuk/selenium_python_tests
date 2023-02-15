import openpyxl


def get_data():
    data_buffer = openpyxl.load_workbook("/Users/tarasodynyuk/PycharmProjects/web_tests/resource/item.xlsx")
    data = data_buffer.active
    brands_list = []
    for row in range(1, 4):
        for col in data.iter_cols(3, 3):
            brands_list.append(col[row].value)
    return brands_list
