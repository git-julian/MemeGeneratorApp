# Meme Generator Project

## Overview

The Meme Generator project is designed to create humorous memes by overlaying quotes on images. It consists of two main modules: the Quote Engine and the Meme Generator. The project is built with Python and uses Flask for a web interface. The main functionalities include loading quotes from various file types, generating memes with custom captions, and providing both a command-line and web-based interface.

## Functionality Description of the Project Code

### 1. Quote Engine

- **Role:** Ingests quotes from various file formats and provides them for use in meme generation.
- **Submodules:**
  - **QuoteModel:** Defines a data model for quotes, consisting of the quote text and author.
  - **IngestorInterface:** An abstract base class defining the interface for all ingestors. Ensures consistent implementation across different file types.
  - **CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor:** Concrete classes that inherit from `IngestorInterface`. Each class handles the ingestion of quotes from specific file types such as CSV, DOCX, PDF, and TXT.
  - **Ingestor:** A unified interface that encapsulates all ingestors. It selects the appropriate ingestor based on the file type and extracts quotes accordingly.
- **Key Functionalities:**
  - Parsing various file types to extract quotes.
  - Returning a list of `QuoteModel` objects containing the text and author of each quote.

### 2. Meme Generator

- **Role:** Generates memes by overlaying quotes on images.
- **Submodules:**
  - **MemeEngine:** A class that handles image manipulation. It can:
    - Resize images to fit within a specified width while maintaining the aspect ratio.
    - Add text (quote and author) to an image at a random position.
    - Save the generated meme to an output directory.
- **Key Functionalities:**
  - Loading an image from disk.
  - Transforming the image by resizing and adding text.
  - Saving the modified image to the specified output directory.

### 3. Flask Web App

- **Role:** Provides a web interface for users to generate memes interactively.
- **Main Script:** `app.py`
- **Key Functionalities:**
  - **`/` Route:** Generates a random meme using a random quote and image. Displays the generated meme.
  - **`/create` Route (GET):** Displays a form for user input to create a custom meme.
  - **`/create` Route (POST):** Accepts user input, downloads an image from a URL, and generates a meme using the provided quote and author. Displays the generated meme.

### 4. Command-Line Interface

- **Role:** Allows users to generate memes via command-line input.
- **Main Script:** `meme.py`
- **Key Functionalities:**
  - Accepts three optional arguments: image path, quote body, and quote author.
  - If no arguments are provided, selects random values for the image and quote.
  - Generates a meme based on the provided or random inputs and saves it to a specified directory.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/git-julian/MemeGeneratorApp.git
    cd meme-generator
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install xpdf on your device:**
    - **Mac:** 
      ```bash
      brew install xpdf
      ```
    - **Windows:** 
      Download and add `xpdf` to your PATH.
    - **Linux:** 
      ```bash
      sudo apt-get install -y xpdf
      ```

## Usage

### 1. Command Line Interface (CLI)

You can run the `src/meme.py` to start the CLI. 

- **Arguments:**
  - `--path`: The path to the image file.
  - `--body`: The quote body to add to the image.
  - `--author`: The quote author.

**Example:**
```bash
python3 src/meme.py --path "_data/photos/dog/xander_1.jpg" --body "Stay positive" --author "Unknown"
 ```

### Web App



You can use the `app.py` script to start the Flask app. In oder to call the Skript navigate into to src Folder first.
```bash
cd src
python3 python3 app.py
 ```

Open your browser and go to http://127.0.0.1:5000/ to access the web interface. 



### Troubleshooting

	1.	Ensure correct file paths:
	•	Check that the paths to the quote files and images are correct.
	•	Make sure all required files are present in the expected directories.
	2.	Common Errors:
	•	If you encounter FileNotFoundError, ensure that the file paths are correct and the files exist.
	•	For ImportError, check that the module paths are correctly specified.
	3.	Dependency Issues:
	•	If you run into issues with dependencies, try reinstalling them using pip install -r requirements.txt.
