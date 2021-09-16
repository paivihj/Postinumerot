import json
import urllib.request

def find(postitoimipaikka):
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        html = response.read()
    postinumerot=json.loads(html)
    check = postitoimipaikka.upper() in postinumerot.values()

    if check == True:
        lista = ""
        for ptp in postinumerot:
            if (postinumerot[ptp]==postitoimipaikka.upper().replace(" ", "")):
                lista = lista + " " + ptp
        return 'Postinumerot:' + lista
    else:
        return 'Postitoimipaikkaa ei löydy'

def manual():
    postitoimipaikka=input("Kirjoita postitoimipaikka: ")

    print(find(postitoimipaikka))

if __name__ == '__main__':
    manual()


