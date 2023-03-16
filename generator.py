import os
import textwrap

import openai
from PIL import Image, ImageDraw
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.lib import pagesizes


def image_round(image, r):
    mask = Image.new(image.mode, (image.width, image.height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(mask)
    draw.arc([(0, 0), (2 * r - 1, 2 * r - 1)], 180, 270, (0, 0, 0, 255))
    draw.arc([(image.width - 2 * r, 0), (image.width, 2 * r - 1)], 270, 0, (0, 0, 0, 255))
    draw.arc([(image.width - 2 * r, image.height - 2 * r), (image.width, image.height)],
             0, 90, (0, 0, 0, 255))
    draw.arc([(0, image.height - 2 * r), (2 * r - 1, image.height)], 90, 180, (0, 0, 0, 255))
    ImageDraw.floodfill(mask, (image.width / 2, image.height / 2), (0, 0, 0, 255))
    return Image.composite(image, mask, mask)


class WorkerSignals(QObject):
    error = pyqtSignal(str)
    file_saved_as = pyqtSignal(str)
    description_generated = pyqtSignal(str)


class DescriptionGenerator(QRunnable):
    def __init__(self, req):
        super().__init__()
        openai.api_key = "ENTER API KEY HERE :)"
        self.req = req
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            res = openai.Completion.create(
                model="text-davinci-003",
                prompt='Очень краткое описание фильма "' + self.req + '".',
                max_tokens=120,
                temperature=0.6).choices[0].text
        except Exception as e:
            self.signals.error.emit(str(e))
            return
        self.signals.description_generated.emit(res)


class Generator(QRunnable):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            template = PdfReader("assets/file.pdf", decompress=False).pages[0]
            template_obj = pagexobj(template)
            save_name = os.path.join(os.path.expanduser("~"), "Downloads/", self.data['name'].replace(' ', '') + '.pdf')
            canvas = Canvas(save_name)
            xobj_name = makerl(canvas, template_obj)
            canvas.doForm(xobj_name)

            PAGE_SIZE = pagesizes.A4
            PAGE_WIDTH = PAGE_SIZE[0]
            PAGE_HEIGHT = PAGE_SIZE[1]
            pdfmetrics.registerFont(TTFont('FiraBold', 'assets/FiraSans-SemiBold.ttf'))
            pdfmetrics.registerFont(TTFont('Fira', 'assets/FiraSans-Regular.ttf'))

            img = Image.open(self.data['poster_path'][0])
            img = img.resize((455 * img.width // img.height, 455), Image.LANCZOS)
            img_width, img_height = img.size
            left = (img_width - 313) // 2
            top = (img_height - 455) // 2
            right = (img_width + 313) // 2
            bottom = (img_height + 455) // 2

            cropped_img = img.crop((left, top, right, bottom))
            img_width, img_height = cropped_img.size
            cropped_img = cropped_img.convert('RGBA')
            cropped_img = image_round(cropped_img, 11)
            cropped_img.save("assets/poster.png")

            canvas.drawImage("assets/poster.png", (PAGE_WIDTH - img_width) // 2, PAGE_HEIGHT - 34 - img_height,
                             mask='auto')

            canvas.setFillColorRGB(255, 255, 255)
            canvas.setFont("FiraBold", 25)
            name_text = self.data['name']
            name_width = stringWidth(name_text, "FiraBold", 24)
            canvas.drawString((PAGE_WIDTH - name_width) // 2, 195, name_text)

            canvas.setFont("Fira", 18)
            canvas.rotate(13.4)
            canvas.setFillColorRGB(0, 0, 0)
            num_text = 'S' + self.data['season'] + 'E' + self.data['episode']
            canvas.drawString(473, 108, num_text)

            canvas.setFillColorRGB(255, 255, 255)
            canvas.setFont("Fira", 21)
            description_text = self.data['description'].replace('\n', ' ')
            canvas.rotate(-13.4)
            if description_text:
                lines = textwrap.wrap(description_text, width=37)
                first_line = lines[0]
                remainder = ' '.join(lines[1:])
                lines = textwrap.wrap(remainder, 37)
                lines = lines[:4]
                line_width = stringWidth(first_line, "Fira", 21)
                canvas.drawString((PAGE_WIDTH - line_width) // 2, 163, first_line)
                for n, l in enumerate(lines, 1):
                    line_width = stringWidth(l, "Fira", 21)
                    canvas.drawString((PAGE_WIDTH - line_width) // 2, 163 - (n * 26), l)
            canvas.save()
        except Exception as e:
            self.signals.error.emit(str(e))
            return
        self.signals.file_saved_as.emit(save_name)
