# Downloads Folder Organizer

This Python script automatically organizes files in your Downloads folder by moving them into categorized subdirectories based on their file types.

## Features

- Automatically detects file types based on extensions
- Creates category folders if they don't exist
- Moves files to appropriate folders
- Handles a wide range of file types including documents, images, videos, audio files, and more
- Provides console output for successful moves and any errors encountered

## Supported File Categories

- PDFs
- Word Documents
- PowerPoint Presentations
- Excel Spreadsheets
- Images (PNG, JPG, JPEG, HEIC, GIF)
- Videos (MP4, MOV, AVI, MKV)
- Text Files (TXT, CSV, JSON, XML)
- Audio Files (MP3, WAV)
- Compressed Files (ZIP, RAR, TAR)
- Executables (EXE, APK, DEB)
- Python Scripts

Files with unrecognized extensions are moved to a 'Misc' folder.

## Requirements

- Python 3.x
- No external libraries required (uses only built-in `os` and `shutil` modules)

## Usage

1. Clone this repository or download the script.
2. Run the script using Python:\
   `python file_organizer.py`\
   The script will automatically organize the files in your Downloads folder.

## How It Works

1. The script identifies your Downloads folder.
2. It iterates through each file in the Downloads folder.
3. Based on the file extension, it determines the appropriate category.
4. If a category folder doesn't exist, it creates one.
5. It moves the file to the corresponding category folder.
6. The script provides console output for each successful move or any errors encountered.

## Customization

You can easily customize the file types and categories by modifying the `filetypes` dictionary in the `file_type` function.

## Note

- This script moves files, not copies them. Ensure you have backups of important files before running the script.
- The script organizes files only in the Downloads folder. Modify the `get_source_path` function if you want to organize a different directory.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
