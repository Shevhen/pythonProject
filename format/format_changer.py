from spire.doc import *
# from spire.doc.common import *
# with open(file.file.__str__(), 'r') as fileg: text = fileg.read()
# with open(new_name, 'w') as fileg: fileg.write(text)

class FormatChanger:
    def __init__(self, file, new_name, f, *args, **kwargs):
        document = Document()
        match f:
            case 'DOC-EXCEL':
                document.LoadFromFile(file.file.__str__())
                document.SaveToFile(new_name)



