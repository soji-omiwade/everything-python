class Widget:
    def __init__(self, widget_name):
        self.width = self.height = 50
        self.widget_name = widget_name
        
    def resize(self, width, height):
        self.width, self.height = width, height
        
    def size(self):
        return self.width, self.height
        
    def dispose(self):
        del self