class Lists (object):

    def __init__(self, list1, list2):
        self.list_uno = list1
        self.list_dos = list2

    def add_lists (self):
        res_list = []
        for i in range(0, len(self.list_uno)):
            res_list.append(self.list_uno[i] + self.list_dos[i])

        print (res_list)

    def append_lists (self):
        print (self.list_uno + self.list_dos)

list1 = [2, 4, 6, 8]        
list2 = [1, 3, 5, 7]

L = Lists (list1, list2)
L.add_lists()
L.append_lists()



   
