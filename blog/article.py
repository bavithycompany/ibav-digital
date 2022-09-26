import markdown
from bs4 import BeautifulSoup
from slugify import slugify

md = """"
    # Ceci est un ros ttre
    ## Iici c'est un sous titre

    Donc comme vous le savez il est tres complique de faire les choses normalement dans un context ou meme *l'argent* 
    de la **connection** est complique a trouver 


    Donc on va faire une petite liste de ce qu'on aime faire dans la vie  
    * Manger
    * Dormir
    * Jouer
    """

html = markdown.markdown(md)
print(html)
