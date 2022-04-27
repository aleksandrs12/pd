from msilib.schema import File
import re



a = open("filehandler.txt", "r")
a = a.read()


class FileHandler:

    def __init__(self, txt:str):
        self.txt = txt

    def how_many(self, letter: str):
        return len(re.findall(letter, self.txt))

    def get_number_sum(self):
        current_num = ''
        sum = 0
        for n in self.txt:
            if n.isdigit():
                current_num += n
            elif current_num != '':
                sum += int(current_num)
                current_num = ''
        return sum + int(current_num)
                

    def get_number_occ(self):
        current_num = ''
        sum = 0
        for n in self.txt:
            if n.isdigit():
                current_num += n
            elif current_num != '':
                sum += 1
                current_num = ''
        if current_num != '':
            sum += 1
        return sum 

a = FileHandler(a)

print(a.get_number_occ())