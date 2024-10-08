import os
import subprocess

def get_file_type(filename):
    result = subprocess.run(['file', '-b', filename], capture_output=True, text=True)
    return result.stdout.strip()

def get_extension(file_type):
    if 'JPEG image' in file_type:
        return '.jpg'
    elif 'PNG image' in file_type:
        return '.png'
    elif 'PDF document' in file_type:
        return '.pdf'
    elif 'Microsoft Word' in file_type:
        if 'Microsoft Word 2007+' in file_type:
            return '.docx'
        else:
            return '.doc'
    elif 'Microsoft Excel' in file_type:
        return '.xls'
    elif 'executable' in file_type.lower():
        return '.exe'
    elif 'zip archive' in file_type.lower():
        return '.zip'
    elif '7-zip archive' in file_type.lower():
        return '.7z'
    elif 'ascii text' in file_type.lower():
        return '.txt'
    elif 'DLL' in file_type:
        return '.dll'
    elif 'data' in file_type.lower() or 'data file' in file_type.lower():
        return '.dat'
    # Extensions SolidWorks ajoutées
    elif 'SolidWorks Part' in file_type:
        return '.sldprt'
    elif 'SolidWorks Assembly' in file_type:
        return '.sldasm'
    elif 'SolidWorks Drawing' in file_type:
        return '.slddrw'
    elif 'SolidWorks Template' in file_type:
        return '.prtdot'  # ou .asmdot, .drwdot selon le type de template
    # Ajoutez d'autres types de fichiers selon vos besoins
    else:
        return '.unknown'

for filename in os.listdir('.'):
    if filename.endswith('.CHK') or filename.endswith('.unknown'):
        file_type = get_file_type(filename)
        new_extension = get_extension(file_type)
        new_filename = os.path.splitext(filename)[0] + new_extension
        if new_filename != filename:
            os.rename(filename, new_filename)
            print(f'Renamed {filename} to {new_filename}')
        else:
            print(f'Skipped {filename} (no change needed)')