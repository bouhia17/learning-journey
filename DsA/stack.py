class Stack:
    def __init__(self):
        self.items=[]
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if len(self.items)>0:
            self.items.pop()
            return True
        return False
    def search(self,data):
        if data in self.items:
            return True
        return False
    def show(self):
        i=1
        while i<=len(self.items):
            print(self.items[-i])
            i+=1
        return True
    
