import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Zaragoza Event Recommender", layout="centered")

# App Title
st.markdown("""
    <style>
        .title {
            color: #FF6347;  /* Tomato */
            font-size: 40px;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            color: #4682B4; /* Steel Blue */
            font-size: 18px;
            text-align: center;
        }
        .event-card {
            background-color: #f0f8ff; /* Alice Blue */
            border-radius: 10px;
            padding: 15px;
            margin-top: 15px;
            text-align: center;
        }
    </style>
    <div class="title">Bienvenido a Tirapaallá </div>
    <div class="subtitle">Busca eventos según tu hobby ;) </div>
""", unsafe_allow_html=True)

# Input fields
st.text("\n")  # Spacer
name = st.text_input("Tu Nombre:")
surname = st.text_input("Tu Apellido:")

# Dropdown menu for hobbies
hobbies = ["Cine", "Volleyball", "Concierto", "Museo", "Restaurante"]
hobby = st.selectbox("Cual es tu hobby favorito?:", hobbies)

# Button to get recommendations
if st.button("Recomiendame!"):
    if name and surname and hobby:
        st.markdown(f"### Hola {name} {surname}! Que tal?")
        st.markdown(f"Según tu hobby, **{hobby}**, te recomendamos los siguientes eventos en la comunidad de Aragón:")

        recommendations = {
            "Cine": ["Movie Marathon at Palafox Cinema", "Film Festival in Zaragoza", "Indie Movie Night", "Outdoor Cinema at Parque Grande", "Classic Movie Screening"],
            "Volleyball": ["Beach Volleyball Tournament", "Local Volleyball League", "Beginner Volleyball Workshop", "Zaragoza Sports Meetup", "Mixed Volleyball Challenge"],
            "Concierto": ["Rock Night at Sala López", "Jazz Evening at Café Dublín", "Orchestra Performance at Auditorio", "Open Mic Night", "Pop Concert at Principe Felipe"],
            "Museo": ["Goya Museum Tour", "Interactive Exhibit at CaixaForum", "Historical Artifacts at Alma Mater Museum", "Modern Art Show", "Guided Tour at Pablo Gargallo Museum"],
            "Restaurante": ["Wine Tasting at La Cata", "Tapas Night at El Tubo", "Paella Workshop", "Michelin Star Dinner", "Street Food Festival"]
        }

        events = recommendations[hobby]

        for i, event in enumerate(events):
            st.markdown(f"""
                <div class="event-card">
                    <h4>Event {i+1}: {event}</h4>
                    <p>[Placeholder for Image]</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Please complete all fields to get a recommendation.")

# Add footer with yellow background
st.markdown("""
    <style>
        /* Increase specificity to ensure the footer style is applied */
        .footer, .css-1d391kg {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: #808080; /* Grey */
            background-color: #FFEB3B; /* Yellow */
            padding: 10px 0;
        }
    </style>
    <div class="footer">Made with ❤️ in Zaragoza</div>
""", unsafe_allow_html=True)
