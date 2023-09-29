from tkinter import *

class Mask_type_numbers:
    def __init__(self):
        self.window_one = None
    def validaEntradas(self):
        ### Naming input validators
        self.vcmd8 = (self.window_one.register(self.valid_int8), "%P")
        self.vcmd6 = (self.window_one.register(self.valid_int6), "%P")
        self.vcmd4 = (self.window_one.register(self.valid_int4), "%P")
        self.vcmd2 = (self.window_one.register(self.valid_int2), "%P")
        self.vcmd12 = (self.window_one.register(self.valid_int12), "%P")
        self.vcmd8float = (self.window_one.register(self.valid_float8), "%P")
        self.vcmd9float = (self.window_one.register(self.valid_float9), "%P")
        self.vcmd4float = (self.window_one.register(self.valid_float4), "%P")
    def valid_int1(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int
            return False
        return 0 <= value <= 9
    def valid_int2(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99
    def valid_int4(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 9999
    def valid_int8(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99999999
    def valid_int12(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 999999999999
    def valid_float8(self, text):
        if text == "":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return len(text) < 9
    def valid_int6(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 999999
    def valid_float4(self, text):
        if text == "":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return len(text) < 5
    def valid_float9(self, text):
        if text == "":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return len(text) < 10