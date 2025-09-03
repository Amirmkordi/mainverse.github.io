import ui_main
import uii_new
import uii_edittask
import uii_list
import uii_sort
import uii_task_by_tag
import uii_group
import uii_taglist
from importqt import *
class secondpage(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self,id):
        super().__init__()
        self.setupUi(self)
        self.new_task.clicked.connect(lambda: self.nt(id))
        self.edit_task.clicked.connect(lambda: self.et(id))
        self.tasks_list.clicked.connect(lambda: self.tal(id))
        self.sort.clicked.connect(lambda: self.s(id))
        self.group.clicked.connect(lambda: self.g(id))
        self.tasks_sort_by_tags.clicked.connect(lambda: self.tsbt(id))
        self.tags_list.clicked.connect(lambda: self.tl(id))
        self.exit.clicked.connect(lambda: self.exitt())
        self.show()
    def exitt(self):
        quit()
    def nt(self,id):
        self.close()
        self.thirdd = uii_new.new(id)
    def et(self,id):
        self.close()
        self.thirdd = uii_edittask.edit(id)
    def tal(self,id):
        self.close()
        self.thirdd = uii_list.list(id)
    def s(self,id):
        self.close()
        self.thirdd = uii_sort.sort(id)
    def g(self,id):
        self.close()
        self.thirdd = uii_group.group(id)
    def tsbt(self,id):
        self.close()
        self.thirdd = uii_task_by_tag.tsbt(id)
    def tl(self,id):
        self.close()
        self.thirdd = uii_taglist.taglist(id)
    