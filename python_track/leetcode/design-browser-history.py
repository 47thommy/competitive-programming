class ListNode:
    def __init__(self, prev=None, val=0, next=None):
        self.prev = prev
        self.val = val
        self.next = next
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.root = ListNode(None, self.homepage, None)
        self.current_page = self.root
        
    def visit(self, url: str) -> None:
        self.current_page.next = ListNode(self.current_page, url, None)
        self.current_page = self.current_page.next
        
    def back(self, steps: int) -> str:
        counter = 0
        while counter<steps:
            if self.current_page.prev is None: return self.homepage
            self.current_page = self.current_page.prev
            counter+=1
        return self.current_page.val

    def forward(self, steps: int) -> str:
        counter = 0
        while counter<steps:
            if self.current_page.next is None: return self.current_page.val
            self.current_page = self.current_page.next
            counter+=1
        return self.current_page.val