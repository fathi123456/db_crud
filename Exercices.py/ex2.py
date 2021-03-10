#créer classe ville
class ville(): #là je ne sais pas du tout quoi faire à vrai dire, je ne maitrise pas encore les class
  def __init__(self, habitants, coord, superficie_km_2,image_url):
    self.habitants = habitants
    self.coord = coord
    self.superficie_km_2 = superficie_km_2
    self.image_url = image_url

#créer les villes à partir du dictionnaire
data_ville = {
    'Marseille' : {
        'habitants': 868277,
        'coord': (43.296346, 5.369889),
        'superficie_km_2': 240.62,
        'image_url':'https://upload.wikimedia.org/wikipedia/commons/4/4b/Marseille_panorama.jpg'
    },
    'Lyon':{
        'habitants': 518635,
        'coord': (45.759723,4.842223),
        'superficie_km_2': 47.87,
        'image_url':'https://upload.wikimedia.org/wikipedia/commons/a/a5/Lyon_Panorama_2006.jpg'
    },
    'Paris' :{
        'habitants': 2175601,
        'coord': (48.856578,2.351828),
        'superficie_km_2': 105.4,
        'image_url':'https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg'
    },
    'Nantes':{
        'habitants': 314138,
        'coord': (47.21806,-1.55278),
        'superficie_km_2': 65.19,
        'image_url':'https://upload.wikimedia.org/wikipedia/commons/9/95/Panorama_depuis_tour_Dobree.jpg'
    },
    'Bordeaux' :{
        'habitants': 257068,
        'coord': (44.837912,-0.579541),
        'superficie_km_2': 49.36,
        'image_url':'https://upload.wikimedia.org/wikipedia/commons/9/9a/Miroir_d%27eau_Bordeaux_panorama.jpg'
    }
}
#créer une liste de ces villes
list_villes = []
for i in data_ville :
  list_villes.append(i)

#faire une fonction qui retourne la plus petite ville en terme de superficie
def villelapluspetite(dicoville):
  taille_min = 9999999999 #dès qu'on a une valeur "raisonnable" d'unne superficie de ville, cette valeur sera changée
  ville = 'aucune'
  for i in dicoville :
    if taille_min > dicoville[i]['superficie_km_2']:
      taille_min = dicoville[i]['superficie_km_2']
      ville = i
  return ville #return donc 'aucune' si le dicoville donné est vide

print(villelapluspetite(data_ville))

#afficher toutes les villes avec leurs populations
for i in data_ville :
  print('Dans la ville de '+ i + ' il y a '+ str(data_ville[i]['habitants']) +' habitants.')

#afficher les villes avec leurs coordonnées sur une carte
import folium

def afficherville(dicoville,ville):
  coords = dicoville[ville]['coord'] #stocke les coordonnées de la ville
  map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=15) #crée la map centrée sur les coordonnées de la ville
  print(type(map))
  map.save(outfile='map.html') #sauvegarde dans le fichier map.html

