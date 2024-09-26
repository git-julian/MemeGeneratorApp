from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeEngine:
    """A class to generate memes by adding text to images."""

    def __init__(self, output_dir: str):
        """Initialize MemeGenerator with output directory.

        :param output_dir: The directory where generated memes will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """Create a meme with an image and a quote.

        :param img_path: Path to the input image.
        :param text: Quote body to add to the image.
        :param author: Quote author to add to the image.
        :param width: The desired width of the meme image.
        :return: Path to the saved meme image.
        """
        try:
            # Load the image
            img = Image.open(img_path)
        except Exception as e:
            raise Exception(f"Unable to open image at {img_path}") from e

        # Resize image while maintaining aspect ratio
        aspect_ratio = img.height / img.width
        new_width = width
        new_height = int(aspect_ratio * new_width)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Prepare the text to add
        quote = f'"{text}" - {author}'
        draw = ImageDraw.Draw(img)

        # Choose a font and size
        try:
            font = ImageFont.truetype('./_fonts/LilitaOne-Regular.ttf', size=20)
        except IOError:
            font = ImageFont.load_default()

        # Wrap text to fit within the image width
        wrapped_text = textwrap.fill(quote, width=40)

        # Calculate text size using textbbox (replacing deprecated textsize)
        text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Calculate position for the text
        x = random.randint(10, max(10, img.width - text_width - 10))
        y = random.randint(10, max(10, img.height - text_height - 10))

        # Add text to the image
        draw.text(
            (x, y), wrapped_text, font=font, fill='white',
            stroke_width=1, stroke_fill='black'
        )

        # Save the meme
        meme_filename = f'meme_{random.randint(0, 1000000)}.jpg'
        meme_path = os.path.join(self.output_dir, meme_filename)
        img.save(meme_path)

        return meme_path