import fitz  # pip install PyMuPDF


def text_selection(file: str, find_text: str) -> dict:
    """
    Принимает файл и отдаёт координаты найденного текста в виде словаря.
    Также сохраняет файл в качестве примера
    :param file:
    :param find_text:
    :return:
    """
    document = fitz.open(file)
    dict_coordinates = dict()
    for index, page in enumerate(document, 1):
        # Поиск координат подходящего текста
        text_instances = page.search_for(find_text)
        if len(text_instances) != 0:
            dict_coordinates[index] = text_instances

        # Выделение координат
        for coordinates in text_instances:
            highlight = page.add_highlight_annot(coordinates)
            highlight.update()
    temp_file_name = file.split(".")[0]
    document.save(f"{temp_file_name}_temp.pdf")

    return dict_coordinates


print(text_selection(file="sample copy.pdf", find_text="zzz"))
