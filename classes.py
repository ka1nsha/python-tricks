from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Test(Base):
    def foo(self):
        pass


assert issubclass(Test, Base)
# https://docs.python.org/3/library/abc.html


class linkparser:
    def __init__(self,**kwargs) -> list:
        self.url = kwargs.get(url)
        self.source = requests.get(self.url).text
    
    def find_html(self):
        regex = "blabla" # Pseudo regex
        regex = re.compile(regex) # Pseudo-code
        veriler = re.findall(source, regex)  # Pseudo-code
        return veriler
    
    @property
    def return_source(self):
        return self.source
    def __str__(self):

urls = ["bla","blabla"]
for i in urls:
    vericek = linkparser(url=i)
    vericek.find_html) # Bulunan linkleri döndürecektir.
    print(linkparser.return_source) # __init__ aşamasında döndürülen verileri propery üzerinden sonradan çekebiliriz.
    # Benzer bir şeyi aşağıda ki gibi de yapabiliriz.
    vericek.source ## Fakat kabaca büyük bir classda yukarıdaki şekilde kullanımı daha uygundur?
