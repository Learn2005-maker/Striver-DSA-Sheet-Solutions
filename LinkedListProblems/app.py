# Designing A Browser History using DLL impletation
# This code is logic for browser history later you can improve the code with Gui appliaction
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None
        
class Browser:
    def __init__(self,homepage):
        self.currentpage=Node(homepage)
        
    def visit(self,url):
        newnode=Node(url)
        # clear forward history
        self.currentpage.next=None
        self.currentpage.next=newnode
        newnode.prev=self.currentpage
        self.currentpage=newnode
    def back(self,steps):
        while steps:
            if self.currentpage.prev:
                self.currentpage=self.currentpage.prev
            else:
                break
            steps-=1
        return self.currentpage.data     
    def forward(self,steps):
        while steps:
            if self.currentpage.next:
                self.currentpage=self.currentpage.next
            else:
                break
            steps-=1
        return self.currentpage.data    
browser=Browser("google.com")        
browser.visit("github.com")
browser.visit("takeUforward.com")
browser.visit("leetcode.com")

print(browser.back(1))
print(browser.back(1))
print(browser.forward(2))
browser.visit("Onlinecompiler.com")




