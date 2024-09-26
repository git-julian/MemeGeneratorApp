import os
import random
import argparse

# Import the Ingestor and MemeGenerator classes
from MemeGenerator.MemeGenerator import MemeEngine
from QuoteEngine.Ingestor import Ingestor 
from QuoteEngine.QuoteModel import QuoteModel

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an image path and a quote.

    If any argument is None, a random selection is made.

    :param path: Path to an image file.
    :param body: Quote body to add to the image.
    :param author: Quote author to add to the image.
    :return: The file path to the generated meme image.
    """
    img = None
    quote = None


    if path is None:
        images = "src/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs.extend([os.path.join(root, name) for name in files if name.lower().endswith(('.jpg', '.png', '.jpeg'))])

        img = random.choice(imgs)
    else:
        img = path


    print(os.path.dirname(os.path.abspath(__file__)))

    if body is None and author is None:

        quote_files = [
            os.path.abspath('src/_data/DogQuotes/DogQuotesTXT.txt'),
            os.path.abspath('src/_data/DogQuotes/DogQuotesDOCX.docx'),
            os.path.abspath('src/_data/DogQuotes/DogQuotesPDF.pdf'),
            os.path.abspath('src/_data/DogQuotes/DogQuotesCSV.csv') ]
        
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    elif body is not None and author is not None:
        quote = QuoteModel(body, author)
    else:
        raise Exception('Both body and author are required if one is provided.')

    meme = MemeEngine('created_memes')
    path = meme.make_meme(img, quote.body, quote.author)
    print(f'Meme generated at: {path}')
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments:
    #   --path: path to an image file
    #   --body: quote body to add to the image
    #   --author: quote author to add to the image
    parser = argparse.ArgumentParser(description='Generate a meme.')
    parser.add_argument('--path', type=str, help='Path to an image file.')
    parser.add_argument('--body', type=str, help='Quote body to add to the image.')
    parser.add_argument('--author', type=str, help='Quote author to add to the image.')

    args = parser.parse_args()
    generate_meme(args.path, args.body, args.author)
    