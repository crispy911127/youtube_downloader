import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import subprocess
from subprocess import run, check_output
from downloader import download_audio, download_video, download_videohd, get_name

class Downloader(QDialog):
    
    def __init__(self):
        
        super(Downloader,self).__init__()
        loadUi('Downloader.ui',self)
        
        self.setWindowTitle('Downloader')
        self.PBClr.clicked.connect(self.on_PBClr_clicked)
        self.PB01.clicked.connect(self.on_PB01_clicked)
    
    @pyqtSlot()
    
    
    def on_PBClr_clicked(self):
        self.EdtURL.clear()

    def on_PB01_clicked(self):

        try:
            url = self.EdtURL.text()
            Downloader.on_PB01_clicked(download_video(str(url))) 
            self.EdtMem.setText(str(get_name(url, "mp4")) + " downloaded!")
        except AttributeError:
            pass
        
    def on_PB02_clicked(self):
        
        try:
            url = self.EdtURL.text()
            Downloader.on_PB02_clicked(download_audio(str(url)))
            self.EdtMem.setText(str(get_name(url, "mp3")) + " downloaded!")
        except AttributeError:
            pass
   
app=QApplication(sys.argv)
widget=Downloader()
widget.show()
sys.exit(app.exec_())

