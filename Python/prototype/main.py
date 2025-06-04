from .Flyer import Flyer
from .Poster import Poster
from .Brochur import Brochur

flyer = Flyer("A4", "Hello, World!", "Red")
flyerA3 = flyer.clone()
flyerA3.set_layout("A3")

poster = Poster("A3", "Hello, World!", "Blue")
posterA4 = poster.clone()
posterA4.set_layout("A4")

brochur = Brochur("A5", "Hello, World!", "Green")
brochurA4 = brochur.clone()
brochurA4.set_layout("A4")

flyer.print_info()
poster.print_info()
brochur.print_info() 


