! pip install spotipy
import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
load_dotenv()
#Obtener las credenciales (usuario y contraseña)
id_cliente = os.environ.get("CLIENT_ID")
codigo_cliente = os.environ.get("CLIENT_SECRET")
autenticacion = SpotifyClientCredentials(client_id = id_cliente, client_secret = codigo_cliente)
spotify = sp.Spotify(auth_manager = autenticacion)
#Conseguir el top 10 de canciones más escuchadas en Spotify de mi artista favorito.
nombre_artista = "Emilia"
#Se ve en spotify en los ultimos números del url (https://open.spotify.com/intl-es/artist/0AqlFI0tz2DsEoJlKSIiT9)
id_artista = "0AqlFI0tz2DsEoJlKSIiT9"
print(f"Top 10 canciones más escuchadas en Spotify de {nombre_artista}:")
top_tracks = spotify.artist_top_tracks(id_artista)
for i, track in enumerate(top_tracks["tracks"][:7]):
    nombre = track["name"]
    popularidad = track["popularity"]
    print(f"{i+1}.{nombre}{popularidad}")
#Convertir en dataframe el resultado obtenido
datos = [{"nombre": track["name"],"popularidad": track["popularity"]}
         for track in top_tracks["tracks"][:100]]
emilia_df = pd.DataFrame(datos)
print(emilia_df)
#Analizar relación estadística
plt.scatter(emilia_df["popularidad"], emilia_df["nombre"], color = "pink")
plt.title("Popularidad de las canciones")
plt.xlabel("Popularidad")
plt.ylabel("Nombre de la canción")
plt.tight_layout()
plt.show()