import streamlit as st

# Set page configuration with a custom title and icon
st.set_page_config(page_title="Stelo Vienas Scent Generator", page_icon="✨")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background color for the entire app */
    .main {
        background-color: #f7f1e3;
        color: #333;
    }
    
    /* Decorative border for the reveal section */
    .reveal-box {
        border: 2px solid #b47e5f;
        padding: 20px;
        margin-top: 20px;
        background-color: #fbf3e3;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Custom font styling */
    h1, h2, h3 {
        color: #5b2c6f;
        font-family: 'Georgia', serif;
    }

    /* Styling for scent options */
    .option-box {
        padding: 8px;
        border-radius: 5px;
        margin-bottom: 10px;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
    }
    .option-box:hover {
        background-color: #e0e4cc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title and Introduction
st.title("✨ Discover Your Signature Scent in *Stelo Vienas* ✨")
st.write("Follow the steps to reveal a unique scent profile that reflects your character and personality.")

# Step 1: Character Class Selection
st.header("Step 1: Choose Your Character Class")
character_class = st.selectbox("Select your character class:", [
    "Alliance Swordsman", "Cleric", "Archer", "Tracker", "Prelate's Chapter Swordsman",
    "Hordesman", "Fang Warrior (Solandrys)", "Iron Legion Veteran", 
    "Vontharian Legionnaire", "Bandit", "Champion Swordsman"
])

# Step 2: Scent Selection with Decorative Boxes
st.header("Step 2: Choose Your Scent Notes (Up to 4)")
scent_families = {
    "Citrus": ["Lemon", "Bergamot", "Grapefruit", "Orange"],
    "Floral": ["Jasmine", "Rose", "Lavender", "White Lily"],
    "Woody": ["Cedar", "Sandalwood", "Pine", "Oak"],
    "Spicy": ["Cinnamon", "Pepper", "Clove", "Nutmeg"],
    "Herbal": ["Mint", "Thyme", "Basil", "Sage"],
    "Earthy": ["Moss", "Patchouli", "Vetiver", "Earth"],
    "Smoky": ["Tobacco", "Leather", "Burnt Wood", "Ash"]
}

selected_notes = []

# Display scent families with styled options
for family, notes in scent_families.items():
    if len(selected_notes) < 4:
        selected_note = st.selectbox(f"Choose a note from the {family} family:", notes, key=family)
        if selected_note and selected_note not in selected_notes:
            selected_notes.append(selected_note)

# Step 3: Reveal Profile in a Styled Box
if st.button("Reveal Your Signature Scent Profile") and selected_notes:
    st.markdown(f"""
    <div class="reveal-box">
        <h2>Your Character Class: {character_class}</h2>
        <p><strong>Character Traits:</strong> {character_classes.get(character_class, "Unique")}</p>
        <p><strong>Scent Notes:</strong> {', '.join(selected_notes)}</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.write("Please select up to 4 unique scent notes to create your profile.")
