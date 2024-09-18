from gtts import gTTS
import os
from pdfreader import SimplePDFViewer
from tkinter import *
from tkinter.filedialog import askopenfilename

"""A GUI module that converts a selected PDF file into an mp3 file"""

# Colors for GUI
DARK = "#222831"
MID = "#393E46"
BLUE = "#00ADB5"
WHITE = "#EEEEEE"


class PDFConverter:
    """Class that handles PDF conversion to audio file"""
    def __init__(self):
        self.text = ""

    def upload(self):
        """Asks user to select file for filepath. File must be pdf.
        Converts the image into text and displays on screen."""
        self.text = ""
        user_choice = askopenfilename()
        if user_choice != "" and user_choice.endswith('.pdf'):
            file = open(user_choice, "rb")
            viewer = SimplePDFViewer(file)
            viewer.render()
            for canvas in viewer:
                page = "".join(canvas.strings)
                self.text += page
            self.text = self.text.replace("  ", "\n")
            text_label.delete("1.0", END)
            text_label.insert(1.0, f"{self.text}\n\n")
            text_label.grid(column=0, row=3, pady=5, columnspan=2)
            convert_to_audio.grid(column=1, row=1, pady=5)

        else:
            text_label.delete("1.0", END)
            text_label.insert(1.0, "That is not a PDF. Please try again.")
            text_label.grid(column=0, row=3, pady=5, columnspan=2)

    def convert(self):
        """Takes text from PDF and converts it to an audio file which saves as pdf.mp3"""
        language = "en"
        converter = gTTS(text=self.text, lang=language, slow=False)
        converter.save("pdf.mp3")
        os.system("pdf.mp3")


# Window Config
window = Tk()
window.minsize(200, 200)
window.config(pady=20, padx=20, background=DARK)
new_conv = PDFConverter()
# Labels and Buttons
header = Label(text="PDF To Text", fg=WHITE, bg=DARK, font=("georgia", 20, "bold"), pady=20)
header.grid(column=0, row=0, columnspan=2)
upload_button = Button(text="Select PDF", fg=BLUE, bg=MID, font=("georgia", 10, "normal"), command=new_conv.upload)
upload_button.grid(column=0, row=1, pady=5)
convert_to_audio = Button(text="Convert to MP3", fg=BLUE, bg=MID, font=("georgia", 10, "normal"), command=new_conv.convert)
# Text Display Label
text_label = Text(wrap="word", fg=BLUE, bg=MID, font=("georgia", 12, "normal"), padx=10)
window.mainloop()
