import random
import os
import requests
import tempfile
from flask import Flask, render_template, request
from MemeGenerator.MemeGenerator import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel

app = Flask(__name__)

# Initialize MemeEngine with the static directory for output
meme = MemeEngine('./static')

def setup():
    """Load all resources required by the app."""
    # Paths to the quote files using relative paths
    quote_files = [
            os.path.abspath('_data/DogQuotes/DogQuotesTXT.txt'),
            os.path.abspath('_data/DogQuotes/DogQuotesDOCX.docx'),
            os.path.abspath('_data/DogQuotes/DogQuotesPDF.pdf'),
            os.path.abspath('_data/DogQuotes/DogQuotesCSV.csv') ]

    # Use the Ingestor to parse all quotes
    quotes = []
    for file in quote_files:
        if os.path.isfile(file):  # Check if the file exists
            try:
                quotes.extend(Ingestor.parse(file))
            except Exception as e:
                print(f'Error parsing {file}: {e}')
        else:
            print(f'File not found: {file}')

    # Directory containing images with absolute path
    images_path = os.path.join(os.path.dirname(__file__), '_data/photos/dog/')

    # Use os.walk to find all images in the directory
    imgs = []
    for root, _, files in os.walk(images_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                imgs.append(os.path.join(root, file))

    if not imgs:
        print(f'No images found in directory: {images_path}')
    if not quotes:
        print(f'No quotes found in files: {quote_files}')

    return quotes, imgs

# Load the quotes and images on startup
quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """Generate a random meme."""
    if not quotes or not imgs:
        return render_template('meme_error.html', message='No quotes or images available.')

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """Display a form for the user to input meme information."""
    return render_template('meme_form.html')

@app.route('/create', methods=['POST'])
def meme_post():
    """Create a meme based on user input."""
    image_url = request.form.get('image_url', None)
    body = request.form.get('body', '')
    author = request.form.get('author', '')

    if not image_url:
        return render_template('meme_error.html', message='No image URL provided.')

    try:
        response = requests.get(image_url)
        response.raise_for_status()
        temp = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        temp.write(response.content)
        temp.close()
        path = meme.make_meme(temp.name, body, author)
        os.remove(temp.name)
        return render_template('meme.html', path=path)
    except requests.exceptions.RequestException as e:
        print(f'Error downloading image: {e}')
        return render_template('meme_error.html', message='Error downloading image.')
    except Exception as e:
        print(f'Error creating meme: {e}')
        return render_template('meme_error.html', message='Error creating meme.')

if __name__ == "__main__":
    app.run(debug=True)

