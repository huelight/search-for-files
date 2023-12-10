# Search by Extension

**Search by Extension** is a simple command-line utility born out of the necessity to efficiently find files on your PC based on their extensions and the date of creation or modification. If you have a large number of files and struggle to locate specific documents, this tool can be handy in narrowing down your search.

## How to Use

1. **Run the Program:**
   - Execute the Python script `main.py` in your terminal or command prompt.

2. **Enter Search Criteria:**
   - Enter the file extension you are looking for (e.g., `.pdf`).
   - Input the year and month to filter files created or modified during that period.

3. **View Results:**
   - The program will display a list of files matching the specified extension and creation or modification date.

4. **Repeat as Needed:**
   - Feel free to run the program multiple times with different search criteria until you find the files you are looking for.

## How It Works

- The program utilizes your PC's file system to search for files with the specified extension.
- It takes into account the creation or modification date to provide a more focused result.
- The results are displayed in the terminal or command prompt, helping you quickly identify the relevant files.

## Example

```bash
python main.py
```

- Enter the extension (e.g., .pdf): .pdf

- Enter the year you want to search (e.g., 2022): 2022

- Enter the month you want to search (e.g., 01 for January): 01

The program will then list files with the .pdf extension that were created or modified in January 2022.

## Customize and Contribute
Feel free to customize the code to suit your specific needs or contribute to the project to enhance its functionality. If you encounter any issues or have ideas for improvement, please open an issue or submit a pull request.