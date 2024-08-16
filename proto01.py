"""
Prototipo de visualizador de animes pirañas
"""
import tkinter as tk
from tkinter import ttk
import threading
import os
from animeflv import AnimeFLV

def main():
    with AnimeFLV() as api:
        try:
            serie = input("Serie: ")
            elementos = api.search(serie)
            
            for i, elemento in enumerate(elementos):
                print(f"{i}) {elemento.title}")

            seleccion = int(input("Selecciona una opcion: "))
            info = api.get_anime_info(elementos[seleccion].id)

            info.episodes.reverse()  # Corrige el error de la reversa de episodios
            for j, episode in enumerate(info.episodes):
                print(f"{j} | Episodio - {episode.id}")

            index_Episodio = int(input("Selecciona el Episodio: "))
            serie = elementos[seleccion].id
            capitulo = info.episodes[index_Episodio].id 
            resultados = api.get_links(serie, capitulo)
            
            for resultado in resultados:
                print(f"{resultado.server} - *+*+*+*+*+* {resultado.url}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

root = tk.Tk()
root.title("piraña")


