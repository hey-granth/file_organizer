import os
import shutil


def get_source_path():
    return os.path.join(os.path.expanduser('~'), 'Downloads')


def file_type(file):
    _, extension = os.path.splitext(file)
    extension = extension.lower()
    print(f"Extension: {extension}")

    filetypes = {
        '.pdf': 'PDFs',
        '.doc': 'Word',
        '.docx': 'Word',
        '.ppt': 'PowerPoints',
        '.pptx': 'PowerPoints',
        '.xls': 'Excel',
        '.xlsx': 'Excel',
        '.png': 'Images',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.hiec': 'Images',
        '.gif': 'Images',
        '.mp4': 'Videos',
        '.mov': 'Videos',
        '.avi': 'Videos',
        '.mkv': 'Videos',
        '.txt': 'Text',
        '.csv': 'Text',
        '.json': 'Text',
        '.xml': 'Text',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.zip': 'Zip',
        '.rar': 'Zip',
        '.tar': 'Zip',
        '.exe': 'Executables',
        '.apk': 'Executables',
        '.deb': 'Executables',
        '.py': 'Python Scripts',

    }

    folder = filetypes.get(extension, 'Misc')
    print(f"Folder: {folder}")
    return folder


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f'Moved {source} to {destination} Successfully')
    except Exception as e:
        print(e)


def main():
    source_path = get_source_path()

    for filename in os.listdir(source_path):
        source = os.path.join(source_path, filename)
        if os.path.isfile(source):
            destination_folder = file_type(filename)
            destination = os.path.join(source_path, destination_folder)
            if not os.path.exists(destination):
                os.mkdir(destination)
            move_file(source, os.path.join(destination, filename))

    print('Files Organized Successfully!')


if __name__ == '__main__':
    main()
