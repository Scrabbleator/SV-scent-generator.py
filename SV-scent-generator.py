import streamlit as st

# Character classes and their traits
character_classes = {
    "Alliance Swordsman": "Brave, Loyal, Honorable",
    "Cleric": "Wise, Compassionate, Calm",
    "Archer": "Precise, Agile, Focused",
    "Tracker": "Stealthy, Intuitive, Resilient",
    "Prelate's Chapter Swordsman": "Disciplined, Virtuous, Protector",
    "Hordesman": "Fierce, Wild, Unpredictable",
    "Fang Warrior (Solandrys)": "Loyal, Fierce, Tenacious",
    "Iron Legion Veteran": "Resilient, Stoic, Battle-Hardened",
    "Vontharian Legionnaire": "Strategic, Skilled, Traditional",
    "Bandit": "Cunning, Resourceful, Bold",
    "Champion Swordsman": "Masterful, Courageous, Determined"
}

# Scent families and notes
scent_families = {
    "Citrus": ["Lemon", "Bergamot", "Grapefruit", "Orange"],
    "Floral": ["Jasmine", "Rose", "Lavender", "White Lily"],
    "Woody": ["Cedar", "Sandalwood", "Pine", "Oak"],
    "Spicy": ["Cinnamon", "Pepper", "Clove", "Nutmeg"],
    "Herbal": ["Mint", "Thyme", "Basil", "Sage"],
    "Earthy": ["Moss", "Patchouli", "Vetiver", "Earth"],
    "Smoky": ["Tobacco", "Leather", "Burnt Wood", "Ash"]
}

# Function to generate a scent profile
def generate_scent_profile(character_class, selected_notes):
    class_traits = character_classes.get(character_class, "Unknown")
    profile = f"**Character Class:** {character_class}\n\n**Traits:** {class_traits}\n\n**Scent Notes:** {', '.join(selected_notes)}"
    return profile

# Streamlit App
st.title("Discover Your Signature Scent and Character Profile")
st.write("Follow the steps to reveal a unique scent profile that reflects your character and personality.")

# Step 1: Character Class Selection
st.header("Step 1: Choose Your Character Class")
character_class = st.selectbox("Select your character class:", list(character_classes.keys()))

# Step 2: Select Scent Families and Notes
st.header("Step 2: Choose Your Scent Notes")
selected_notes = []

# Allow the user to select up to 4 notes from different scent families
for family, notes in scent_families.items():
    if len(selected_notes) < 4:
        selected_note = st.selectbox(f"Choose a note from the {family} family", notes)
        if selected_note and selected_note not in selected_notes:
            selected_notes.append(selected_note)

# Display the final profile if the user has chosen between 1 and 4 notes
if st.button("Reveal Your Signature Scent Profile") and selected_notes:
    profile = generate_scent_profile(character_class, selected_notes)
    st.markdown(profile)
else:
    st.write("Please select up to 4 unique scent notes to create your profile.")
