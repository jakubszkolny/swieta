import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time

st.title("🎅 Świąteczny Mikołaj z animacją śniegu i migoczącymi bombkami")

# --- Sterowanie migotaniem bombek ---
if 'lights_on' not in st.session_state:
    st.session_state['lights_on'] = True

col1, col2 = st.columns(2)
with col1:
    if st.button("Stop migotanie"):
        st.session_state['lights_on'] = False
with col2:
    if st.button("Start migotanie"):
        st.session_state['lights_on'] = True

# --- Parametry śniegu ---
if 'snowflakes' not in st.session_state:
    st.session_state['snowflakes'] = [{'x': random.uniform(0,12), 
                                      'y': random.uniform(2,12), 
                                      'size': random.uniform(0.05,0.15)} for _ in range(50)]

# --- Funkcja rysująca scenę ---
def draw_scene():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_aspect("equal")
    ax.axis("off")
    
    # --- Tło: śnieg na ziemi ---
    ax.add_patch(patches.Rectangle((0, 0), 12, 2.5, color="#e6f7ff"))
    
    # --- Choinka ---
    tree_layers = [
        [[2,2.5], [3,6], [1,6]],
        [[2,5], [3,8], [1,8]],
        [[2,7.5], [3,10], [1,10]]
    ]
    for layer in tree_layers:
        ax.add_patch(patches.Polygon(layer, color="green"))
    
    # Korzeń choinki (brązowy)
    ax.add_patch(patches.Rectangle((1.8, 2.0), 0.4, 0.5, color="saddlebrown"))
    
    # Gwiazdka na czubku
    ax.add_patch(patches.RegularPolygon((2,10), numVertices=5, radius=0.2, color="yellow"))
    
    # Bombki na choince
    bombki_positions = [(2,5.5), (2.5,7), (1.5,8), (1.8,6), (2.2,8.5)]
    bombki_colors = ["red", "yellow", "blue", "purple", "orange"]
    
    if st.session_state['lights_on']:
        bombki_colors = [random.choice(["red", "yellow", "blue", "purple", "orange", "pink", "cyan"]) 
                         for _ in bombki_positions]
    
    for pos, color in zip(bombki_positions, bombki_colors):
        ax.add_patch(patches.Circle(pos, 0.15, color=color))
    
    # --- ŚWIĘTY MIKOŁAJ ---
    ax.add_patch(patches.Circle((8, 6), 1.3, color="red"))           # Korpus
    ax.add_patch(patches.Circle((8, 7.7), 0.8, color="#ffe0bd"))     # Głowa
    ax.add_patch(patches.Circle((8, 7.0), 0.6, color="white"))       # Broda
    ax.add_patch(patches.Polygon([[7.2, 8], [8, 9.3], [8.8, 8]], color="red")) # Czapka
    ax.add_patch(patches.Circle((8, 9.3), 0.25, color="white"))      # Pompon
    
    # Ręce uniesione do góry
    ax.add_patch(patches.Rectangle((6.2, 7.2), 0.8, 1.8, color="red"))
    ax.add_patch(patches.Rectangle((8.8, 7.2), 0.8, 1.8, color="red"))
    ax.add_patch(patches.Circle((6.6, 8.8), 0.35, color="brown"))
    ax.add_patch(patches.Circle((9.2, 8.8), 0.35, color="brown"))
    
    # Pasek i nogi
    ax.add_patch(patches.Rectangle((7.2, 5.3), 1.6, 0.3, color="black"))
    ax.add_patch(patches.Rectangle((7.3, 4.0), 0.6, 1.3, color="red"))
    ax.add_patch(patches.Rectangle((8.1, 4.0), 0.6, 1.3, color="red"))
    ax.add_patch(patches.Rectangle((7.2, 3.7), 0.8, 0.3, color="black"))
    ax.add_patch(patches.Rectangle((8.0, 3.7), 0.8, 0.3, color="black"))
    
    # Twarz
    ax.add_patch(patches.Circle((7.7, 8.0), 0.10, color="black"))
    ax.add_patch(patches.Circle((8.3, 8.0), 0.10, color="black"))
    ax.add_patch(patches.Circle((7.75, 8.05), 0.03, color="white"))
    ax.add_patch(patches.Circle((8.35, 8.05), 0.03, color="white"))
    ax.plot([7.7, 8.3], [7.45, 7.45], color="black", linewidth=2)
    
    # Prezenty
    def rysuj_prezent(x, y, size, kolor_pudelka, kolor_wstazki):
        ax.add_patch(patches.Rectangle((x, y), size, size, color=kolor_pudelka))
        ax.add_patch(patches.Rectangle((x + size*0.45, y), size*0.1, size, color=kolor_wstazki))
        ax.add_patch(patches.Rectangle((x, y + size*0.45), size, size*0.1, color=kolor_wstazki))
        ax.add_patch(patches.Ellipse((x + size/2 - size*0.12, y + size/2 + size*0.15), size*0.25, size*0.15, color=kolor_wstazki))
        ax.add_patch(patches.Ellipse((x + size/2 + size*0.12, y + size/2 + size*0.15), size*0.25, size*0.15, color=kolor_wstazki))
    
    rysuj_prezent(7.0, 3.0, 1.2, "#ff4444", "#ffee33")
    rysuj_prezent(8.4, 3.0, 1.0, "#44aaff", "#ffffff")
    rysuj_prezent(9.5, 3.2, 0.8, "#55cc55", "#ffdd00")
    
    # Śnieżynki
    for snowflake in st.session_state['snowflakes']:
        ax.add_patch(patches.Circle((snowflake['x'], snowflake['y']), snowflake['size'], color="white"))
    
    return fig

# --- Kontener Streamlit do animacji ---
placeholder = st.empty()

# --- Animacja ---
while True:
    # Aktualizujemy pozycje śnieżynek
    for snowflake in st.session_state['snowflakes']:
        snowflake['y'] -= 0.05
        if snowflake['y'] < 0:
            snowflake['y'] = 12
            snowflake['x'] = random.uniform(0,12)
    
    # Rysujemy scenę
    fig = draw_scene()
    placeholder.pyplot(fig)
    
    # Opóźnienie dla animacji
    time.sleep(0.1)
