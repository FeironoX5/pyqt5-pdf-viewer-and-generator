# PyQt5 PDF viewer and generator + PyInstaller Export

[![Telegram](https://img.shields.io/badge/Telegram-lostinwinelands-blue)](https://t.me/lostinwinelands)
[![Instagram](https://img.shields.io/badge/Instagram-gleb.kiva-orange)](https://www.instagram.com/gleb.kiva)
![GitHub Repo stars](https://img.shields.io/github/stars/FeironoX5/pyqt5-pdf-viewer-and-generator?style=social)

## Journey description

I designed the poster layout in Figma so that my literature teacher could announce weekly film club meetings at my
school (you can check out the [Behance case](https://www.behance.net/gallery/161723541/LETFILM-Letovo-School-Film-Club))
.
However, I have been putting information about a new film into the template every week for over ten weeks now. This
app was created so that my literature teacher could generate posters himself.

## Upcoming fights

* [ ] Add ```requirments.txt```
* [ ] Convert the poster pictures to B&W to match the poster
* [ ] After zooming in on the PDF viewer, window zoom does not work properly
* [ ] Create Windows Installer
* [ ] Add limits to text inputs
* [ ] Centering text on badge with season and episode diagonally

## How do I join the journey?

1. Install packages (```pip install -r requirements.txt```)
2. This project contains a description generator for movies using Chat GPT. If you want to use it, enter your API key
   in ```DescriptionGenerator``` in ```generator.py```
3. Run ```main.py```

## How can I collect the treasure?

To build a project into an executable file, use auto-py-to-exe

1. Install package ```pip install auto-py-to-exe```
2. Open builder ```auto-py-to-exe``` in new web tab
3. In Settings section click "Import Config From JSON File" and choose ```pyinstaller-config.json``` from this repo
4. In output folder put ```assets``` folder, so that the tool has something to work with
