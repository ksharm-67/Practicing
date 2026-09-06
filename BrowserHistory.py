class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.browser = self.browser[:self.curr + 1]
        self.browser.append(url)
        self.curr = len(self.browser) - 1

    def back(self, steps: int) -> str:
        can_move = min(self.curr, steps)
        self.curr -= can_move
        return self.browser[self.curr]

    def forward(self, steps: int) -> str:
        can_move = min(len(self.browser) - 1 - self.curr, steps)
        self.curr += can_move
        return self.browser[self.curr]
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
