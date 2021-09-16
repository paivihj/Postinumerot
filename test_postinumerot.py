import postinumerot

alku = "Postinumerot: "

def test_kiuruvesi():

    tulos = postinumerot.find("Kiuruvesi")
    assert tulos==alku+("74701 74700")

def test_kivijarvi():

    tulos = postinumerot.find("kivijärvi")
    assert tulos==alku+("43800")

def test_yliolhava():

    tulos = postinumerot.find("Yli-Olhava")
    assert tulos==alku+("91150")

def test_beverly():

    tulos = postinumerot.find("Beverly Hills")
    assert tulos==("Postitoimipaikkaa ei löydy")

def test_smartpost():
    space = postinumerot.find("SMART POST")
    post = postinumerot.find("SMARTPOST")
    tulos=True
    if len(space)!=len(post):
        tulos = False
    assert tulos==True

def test_smartpsot():
    psot = postinumerot.find("SMARTPSOT")
    assert psot!=("Postitoimipaikkaa ei löydy")
