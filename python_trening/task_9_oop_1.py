class Input:

    def __init__(self, loc):
        self.loc = loc
search = Input('input#search')
print(search.loc)


class Page:
    def __init__(self, url):
        self.url = url
    def get(self):
        print(self.url)

home = Page('https')
home.get()


