from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter import *



merger = PdfFileMerger()

for pdf in range(1,3):
    merger.append("{}.pdf".format(pdf))

merger.write("mid_semester_report_206468480_301658852.pdf")
merger.close()






