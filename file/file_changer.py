from spire.doc import *

from file.models import UploadedFile


class FileChanger:
    def __init__(self, form, ip):
        file = UploadedFile.objects.get(ip=ip)
        match form:
            case 'WORD to PDF':
                document = Document()
                document.LoadFromFile(file.path + '/' + file.file.__str__())
                document.SaveToFile(file.path + '/' + file.file.__str__().split('.')[0] + '.pdf')
                file.new_file = file.path + '/' + file.file.__str__().split('.')[0] + '.pdf'
                file.save()

