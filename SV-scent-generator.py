import streamlit as st

# Set up the app title and description
st.title("Discover Your Signature Scent in *Stelo Vienas*")
st.write("Follow the steps to reveal the unique scent that reflects your journey through *Stelo Vienas*.")

# Step 1: Character Class Selection
st.header("Step 1: Choose Your Character Class")
character_class = st.selectbox(
    "Which character class resonates with you the most?",
    ("Mystic", "Scholar", "Warrior", "Adventurer")
)

# Step 2: Aroma Selection Based on Character Class
st.header("Step 2: Select Your Aromas")
if character_class == "Mystic":
    aroma = st.multiselect(
        "Select up to two aromas that resonate with your spirit:",
        ["Night Bloom", "Incense", "Herbal Mist"]
    )
elif character_class == "Scholar":
    aroma = st.multiselect(
        "Select up to two aromas that speak of knowledge:",
        ["Leather", "Fresh Ink", "Sandalwood"]
    )
elif character_class == "Warrior":
    aroma = st.multiselect(
        "Choose up to two aromas that fuel your courage:",
        ["Blood Orange", "Cedar", "Iron"]
    )
else:  # Adventurer
    aroma = st.multiselect(
        "Select up to two aromas that evoke adventure:",
        ["Wild Mint", "Ocean Mist", "Pine Resin"]
    )

# Step 3: Display Outcome
if st.button("Reveal Your Signature Scent"):
    if character_class == "Mystic" and set(aroma) == {"Night Bloom", "Incense"}:
        st.subheader("Veil of Midnight")
        st.write("A lingering scent of moonlit flowers and incense smoke, filling the air with whispers of secrets.")
    elif character_class == "Mystic" and set(aroma) == {"Night Bloom", "Herbal Mist"}:
        st.subheader("Twilight Grove")
        st.write("The gentle fragrance of herbs under a starlit sky, with hints of mystical blooms.")
    elif character_class == "Mystic" and set(aroma) == {"Incense", "Herbal Mist"}:
        st.subheader("Sacred Hearth")
        st.write("A blend of smoke and earth, evoking ancient rituals and hidden knowledge.")
    elif character_class == "Scholar" and set(aroma) == {"Leather", "Fresh Ink"}:
        st.subheader("The Quiet Archive")
        st.write("The scent of wisdom bound in leather and fresh ink, conjuring a sense of discovery and thought.")
    elif character_class == "Scholar" and set(aroma) == {"Leather", "Sandalwood"}:
        st.subheader("Timeless Study")
        st.write("A blend of warm sandalwood and worn leather, like a sanctuary of hidden knowledge.")
    elif character_class == "Scholar" and set(aroma) == {"Fresh Ink", "Sandalwood"}:
        st.subheader("Script of the Ages")
        st.write("A fragrance as sharp and grounded as ink on parchment, softened by the warmth of sandalwood.")
    elif character_class == "Warrior" and set(aroma) == {"Blood Orange", "Cedar"}:
        st.subheader("Vanguard’s Charge")
        st.write("The bright energy of citrus balanced with the earthy strength of cedar—a scent for those who lead.")
    elif character_class == "Warrior" and set(aroma) == {"Blood Orange", "Iron"}:
        st.subheader("Forge’s Edge")
        st.write("A sharp, invigorating fragrance of metal and citrus, like the spark of a warrior’s blade.")
    elif character_class == "Warrior" and set(aroma) == {"Cedar", "Iron"}:
        st.subheader("Ironwood Resolve")
        st.write("The grounded strength of cedar entwined with the metallic tang of iron, symbolizing resilience.")
    elif character_class == "Adventurer" and set(aroma) == {"Wild Mint", "Ocean Mist"}:
        st.subheader("Breeze of the Open")
        st.write("A crisp blend of mint and sea air, evoking freedom and discovery.")
    elif character_class == "Adventurer" and set(aroma) == {"Wild Mint", "Pine Resin"}:
        st.subheader("Forest Wanderer")
        st.write("A fragrance of fresh mint and pine, like a path through sunlit woods.")
    elif character_class == "Adventurer" and set(aroma) == {"Ocean Mist", "Pine Resin"}:
        st.subheader("Edge of the World")
        st.write("The earthy tang of pine with the cool embrace of the ocean, a call to distant horizons.")
    else:
        st.write("Please select up to two aromas to reveal your signature scent.")