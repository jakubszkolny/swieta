import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title("🎄 Świąteczny Mikołaj z prezentami")

# Tworzymy figurę matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.set_aspect("equal")
ax.axis("off")

# --- TŁO ŚWIĄTECZNE ---

# Śnieg na ziemi
ax.add_patch(patches.Rectangle((0, 0), 12, 2.5, color="#e6f7ff"))

# Choinka po lewej
ax.add_patch(patches.Polygon([[2,2.5], [3,6], [1,6]], color="green"))   # dolna część
ax.add_patch(patches.Polygon([[2,5], [3,8], [1,8]], color="green"))     # środkowa część
ax.add_patch(patches.Polygon([[2,7.5], [3,10], [1,10]], color="green"))  # górna część

# Bombki na choince
ax.add_patch(patches.Circle((2,5.5), 0.15, color="red"))
ax.add_patch(patches.Circle((2.5,7), 0.15, color="yellow"))
ax.add_patch(patches.Circle((1.5,8), 0.15, color="blue"))

# Gwiazdka na czubku
ax.add_patch(patches.RegularPolygon((2,10), numVertices=5, radius=0.2, color="yellow"))

# --- ŚWIĘTY MIKOŁAJ ---
ax.add_patch(patches.Circle((8, 6), 1.3, color="red"))           # Korpus
ax.add_patch(patches.Circle((8, 7.7), 0.8, color="#ffe0bd"))     # Głowa
ax.add_patch(patches.Circle((8, 7.0), 0.6, color="white"))       # Broda
ax.add_patch(patches.Polygon([[7.2, 8], [8, 9.3], [8.8, 8]], color="red")) # Czapka
ax.add_patch(patches.Circle((8, 9.3), 0.25, color="white"))      # Pompon

# Ręce uniesione do góry
ax.add_patch(patches.Rectangle((6.2, 7.2), 0.8, 1.8, color="red"))  # lewa ręka
ax.add_patch(patches.Rectangle((8.8, 7.2), 0.8, 1.8, color="red"))  # prawa ręka
ax.add_patch(patches.Circle((6.6, 8.8), 0.35, color="brown"))       # lewa rękawiczka
ax.add_patch(patches.Circle((9.2, 8.8), 0.35, color="brown"))       # prawa rękawiczka

# Pasek i nogi
ax.add_patch(patches.Rectangle((7.2, 5.3), 1.6, 0.3, color="black"))
ax.add_patch(patches.Rectangle((7.3, 4.0), 0.6, 1.3, color="red"))
ax.add_patch(patches.Rectangle((8.1, 4.0), 0.6, 1.3, color="red"))
ax.add_patch(patches.Rectangle((7.2, 3.7), 0.8, 0.3, color="black"))
ax.add_patch(patches.Rectangle((8.0, 3.7), 0.8, 0.3, color="black"))

# Twarz: oczy i usta
ax.add_patch(patches.Circle((7.7, 8.0), 0.10, color="black"))
ax.add_patch(patches.Circle((8.3, 8.0), 0.10, color="black"))
ax.add_patch(patches.Circle((7.75, 8.05), 0.03, color="white"))
ax.add_patch(patches.Circle((8.35, 8.05), 0.03, color="white"))
ax.plot([7.7, 8.3], [7.45, 7.45], color="black", linewidth=2)

# --- Prezenty na ziemi ---
def rysuj_prezent(x, y, size, kolor_pudelka, kolor_wstazki):
    ax.add_patch(patches.Rectangle((x, y), size, size, color=kolor_pudelka))
    ax.add_patch(patches.Rectangle((x + size*0.45, y), size*0.1, size, color=kolor_wstazki))
    ax.add_patch(patches.Rectangle((x, y + size*0.45), size, size*0.1, color=kolor_wstazki))
    ax.add_patch(patches.Ellipse((x + size/2 - size*0.12, y + size/2 + size*0.15), size*0.25, size*0.15, color=kolor_wstazki))
    ax.add_patch(patches.Ellipse((x + size/2 + size*0.12, y + size/2 + size*0.15), size*0.25, size*0.15, color=kolor_wstazki))

rysuj_prezent(7.0, 3.0, 1.2, "#ff4444", "#ffee33")
rysuj_prezent(8.4, 3.0, 1.0, "#44aaff", "#ffffff")
rysuj_prezent(9.5, 3.2, 0.8, "#55cc55", "#ffdd00")

# Wyświetlamy wykres w Streamlit
st.pyplot(fig)
