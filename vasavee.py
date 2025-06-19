import streamlit as st
import random
import requests

st.set_page_config(page_title="Where Should I Travel?", page_icon="🌍")
st.title("🌍 Where Should I Travel? – AI Travel Advisor")
st.markdown("Tell me your travel vibe and budget, and I’ll suggest destinations for your next getaway!")

# --- User Inputs ---
mood = st.selectbox("Choose your vibe:", ["Adventure", "Relax", "Spiritual", "Culture", "Nature"])
budget = st.slider("Select your budget (in ₹):", 1000, 100000, step=1000)
season = st.radio("Preferred Season?", ["Any", "Winter", "Summer", "Monsoon"])
num_places = st.slider("How many places do you want to see?", 1, 5, 3)

# --- Destination Data ---
destinations = {
    "Adventure": [
        ("Rishikesh", "White-water rafting, trekking"),
        ("Manali", "Paragliding, skiing"),
        ("Auli", "Skiing and snow adventures"),
        ("Spiti Valley", "Bike rides, rugged beauty")
    ],
    "Relax": [
        ("Pondicherry", "Beaches, French cafes"),
        ("Alleppey", "Backwaters, houseboats"),
        ("Gokarna", "Peaceful beaches"),
        ("Kumarakom", "Lakeside retreats")
    ],
    "Spiritual": [
        ("Tiruvannamalai", "Arunachaleswara temple"),
        ("Varanasi", "Ganga aarti, ancient temples"),
        ("Bodh Gaya", "Meditation and Buddhist roots"),
        ("Rameswaram", "Temple town and ocean view")
    ],
    "Culture": [
        ("Jaipur", "Forts, palaces, local arts"),
        ("Mysuru", "Royal palace, silk markets"),
        ("Udaipur", "Lakes and havelis"),
        ("Khajuraho", "Heritage temples")
    ],
    "Nature": [
        ("Coorg", "Coffee estates, greenery"),
        ("Meghalaya", "Caves, root bridges"),
        ("Wayanad", "Forests and waterfalls"),
        ("Valparai", "Tea gardens, wildlife")
    ]
}

# --- Image Fallback Function ---
def get_image_url(place):
    query = place.lower().replace(" ", "-")
    url = f"https://source.unsplash.com/600x400/?{query},travel"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return url
    except:
        pass
    return "https://source.unsplash.com/600x400/?nature"

# --- Show Results ---
if st.button("Suggest Destination 🌐"):
    st.subheader(f"Here are your top {num_places} {mood.lower()} destinations:")
    suggested = random.sample(destinations[mood], k=min(num_places, len(destinations[mood])))
    
    for place, highlight in suggested:
        st.markdown(f"### 🗺️ {place}")
        st.image(get_image_url(place), caption=f"{place} scenery")
        st.markdown(f"**What you'll enjoy:** {highlight}")
        st.info(f"🌤️ Best Season: {season} | 💰 Budget: Up to ₹{budget}")
        st.markdown("---")
