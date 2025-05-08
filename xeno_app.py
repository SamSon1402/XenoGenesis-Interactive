import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import random
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="XenoGenesis Interactive",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for retro gaming aesthetic in black and white
def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Space+Mono&display=swap');
        
        /* Main container */
        .main {
            background-color: white;
            color: black;
        }
        
        /* Headers */
        h1, h2, h3 {
            font-family: 'VT323', monospace;
            color: black;
            text-shadow: 2px 2px 0px #cccccc;
            letter-spacing: 2px;
        }
        
        /* Paragraph text */
        p, li, div {
            font-family: 'Space Mono', monospace;
            color: black;
        }
        
        /* Button styling */
        .stButton > button {
            font-family: 'VT323', monospace;
            font-size: 20px;
            border: 3px solid black;
            border-radius: 0px;
            box-shadow: 3px 3px 0px #888888;
            background-color: white;
            color: black;
            transition: all 0.1s;
        }
        
        .stButton > button:hover {
            background-color: black;
            color: white;
            transform: translate(2px, 2px);
            box-shadow: 1px 1px 0px #888888;
        }
        
        /* Select box styling */
        .stSelectbox > div > div {
            background-color: white;
            border: 3px solid black;
            border-radius: 0px;
            color: black;
            font-family: 'Space Mono', monospace;
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: white;
            background-image: linear-gradient(0deg, #f0f0f0 0%, white 100%);
            border-right: 3px solid black;
        }
        
        /* Pixel-perfect containers */
        .pixel-box {
            border: 3px solid black;
            background-color: white;
            padding: 20px;
            margin: 10px 0px;
            box-shadow: 5px 5px 0px #888888;
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background-color: black;
        }
        
        /* Metric styling */
        .stMetric {
            background-color: white;
            border: 2px solid black;
            padding: 10px;
            box-shadow: 3px 3px 0px #888888;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: white;
            border: 2px solid black;
            border-radius: 0px;
            color: black;
            font-family: 'VT323', monospace;
            padding: 10px 20px;
            font-size: 18px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: black;
            color: white;
        }
        
        /* Divider */
        hr {
            border-color: black;
            border-width: 2px;
        }
        
        /* Code blocks */
        code {
            background-color: #f0f0f0;
            color: black;
            border: 2px solid black;
            padding: 2px 5px;
            font-family: 'Space Mono', monospace;
        }
        
        /* Slider styling */
        .stSlider > div > div > div {
            background-color: black;
        }
        
        .stSlider > div > div > div > div {
            background-color: #888888;
            color: white;
        }
        
        /* Molecule box */
        .molecule-box {
            border: 3px solid black;
            background-color: white;
            padding: 15px;
            margin: 10px 5px;
            box-shadow: 5px 5px 0px #888888;
            transition: all 0.2s;
        }
        
        .molecule-box:hover {
            transform: scale(1.02);
            box-shadow: 7px 7px 0px #888888;
        }
        
        /* Property indicator - using patterns instead of colors */
        .property-indicator {
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 10px;
            vertical-align: middle;
            border: 2px solid black;
        }
        
        .property-high {
            background-image: linear-gradient(45deg, black 25%, transparent 25%, transparent 75%, black 75%, black),
                               linear-gradient(45deg, black 25%, transparent 25%, transparent 75%, black 75%, black);
            background-size: 10px 10px;
            background-position: 0 0, 5px 5px;
        }
        
        .property-medium {
            background-image: linear-gradient(to right, black 50%, transparent 50%);
            background-size: 10px 10px;
        }
        
        .property-low {
            background-image: linear-gradient(to right, black 25%, transparent 25%);
            background-size: 10px 10px;
        }
        
        /* Table styling */
        table {
            border: 3px solid black;
            background-color: white;
        }
        
        th {
            background-color: #f0f0f0;
            color: black;
            font-family: 'VT323', monospace;
            font-size: 20px;
            padding: 10px;
            border: 2px solid black;
        }
        
        td {
            font-family: 'Space Mono', monospace;
            color: black;
            padding: 8px;
            border: 1px solid black;
        }
        
        /* Checkbox styling */
        .stCheckbox label p {
            font-family: 'Space Mono', monospace;
            color: black;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            font-family: 'VT323', monospace;
            color: black;
        }
        
        /* Radio button styling */
        .stRadio label {
            font-family: 'Space Mono', monospace;
            color: black;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Title and introduction
def load_header():
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown("<h1>XenoGenesis Interactive</h1>", unsafe_allow_html=True)
        st.markdown("<h3>AI-Powered Therapeutic Design Explorer</h3>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='font-size:60px;text-align:right'>⚗️🧪</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pixel-box">
        <p>Welcome to XenoGenesis Interactive! This platform demonstrates how Explainable Generative AI can revolutionize <em>de novo</em> therapeutic design.</p>
        <p>Design novel molecular structures with desired properties, explore the AI's reasoning, and iterate towards breakthrough therapeutics!</p>
    </div>
    """, unsafe_allow_html=True)

# Simulated molecule data with ASCII art representation
molecules_data = {
    "XG-001": {
        "smiles": "c1ccc2c(c1)C(=O)N(C2=O)c3ccc(cc3)N4CCOCC4",
        "ascii_art": """
         O   O
         ║   ║
    ┌───┐C───N─┌───┐
    │   │     /│   │
    └───┘     └───┘
         │     │
         │     │
    ┌────┼─────┼────┐
    │    │     │    │
    │    N     │    │
    │    │     │    │
    └────┼─────┼────┘
         O─────O
        """,
        "binding_affinity": 85,
        "toxicity": 12,
        "stability": 93,
        "target": "EGFR Kinase",
        "important_substructures": ["Piperazine ring", "Phthalimide group"],
        "properties": {
            "Molecular Weight": "382.42 g/mol",
            "LogP": "3.2",
            "H-Bond Donors": "0",
            "H-Bond Acceptors": "5",
            "Rotatable Bonds": "4"
        },
        "xai_insights": [
            "Piperazine ring contributes significantly to target binding",
            "Low toxicity correlates with absence of reactive groups",
            "Phthalimide group improves metabolic stability"
        ]
    },
    "XG-042": {
        "smiles": "CC(C)Cc1ccc(cc1)[C@@H](C)C(=O)O",
        "ascii_art": """
    CH₃─CH─CH₃
         │
         CH₂
         │
    ┌────┼────┐
    │    │    │
    │    │    │
    │ ───CH── │
    │    │    │
    └────┼────┘
         │
    CH₃─CH
         │
         C═O
         │
         OH
        """,
        "binding_affinity": 72,
        "toxicity": 8,
        "stability": 95,
        "target": "COX-2",
        "important_substructures": ["Isobutyl group", "Carboxylic acid"],
        "properties": {
            "Molecular Weight": "206.28 g/mol",
            "LogP": "3.5",
            "H-Bond Donors": "1",
            "H-Bond Acceptors": "2",
            "Rotatable Bonds": "4"
        },
        "xai_insights": [
            "Isobutyl group increases selectivity for COX-2 over COX-1",
            "Carboxylic acid forms critical hydrogen bonds with target",
            "Methyl group at chiral center provides optimal spatial orientation"
        ]
    },
    "XG-118": {
        "smiles": "c1cc(ccc1C(=O)N)NC(=O)c2cc(ccc2)[N+](=O)[O-]",
        "ascii_art": """
           O
           ║
           C─NH₂
           │
    ┌──────┼──────┐
    │      │      │
    │      │      │
    │    NH│      │
    │      │      │
    └──────┼──────┘
           │
           C═O
           │
    ┌──────┼──────┐
    │      │      │
    │      │      │
    │      │      │
    │     NO₂     │
    └─────────────┘
        """,
        "binding_affinity": 94,
        "toxicity": 28,
        "stability": 77,
        "target": "TNF-alpha",
        "important_substructures": ["Amide linkage", "Nitro group", "Benzamide"],
        "properties": {
            "Molecular Weight": "285.26 g/mol",
            "LogP": "1.8",
            "H-Bond Donors": "2",
            "H-Bond Acceptors": "6",
            "Rotatable Bonds": "5"
        },
        "xai_insights": [
            "Nitro group enhances binding to TNF-alpha but increases toxicity",
            "Amide linkage provides conformational flexibility important for target recognition",
            "Terminal amide group forms key hydrogen bonds with binding pocket residues"
        ]
    },
    "XG-205": {
        "smiles": "COc1cc(cc(c1OC)OC)NC(=O)C=Cc2cc(c(c(c2)OC)O)OC",
        "ascii_art": """
    CH₃O          OCH₃
         \\      /
          \\    /
    ┌──────┼────┼──────┐
    │      │    │      │
    │     NH    │      │
    │      │    │      │
    └──────┼────┼──────┘
           │
           C═O
           │
           C═C
           │
    ┌──────┼──────┐
    │      │      │
    │   OCH₃ OH   │
    │      │      │
    └──────┼──────┘
           │
          OCH₃
        """,
        "binding_affinity": 89,
        "toxicity": 15,
        "stability": 82,
        "target": "NF-κB Pathway",
        "important_substructures": ["Methoxy groups", "α,β-unsaturated carbonyl", "Phenolic hydroxyl"],
        "properties": {
            "Molecular Weight": "389.41 g/mol",
            "LogP": "3.1",
            "H-Bond Donors": "2",
            "H-Bond Acceptors": "7",
            "Rotatable Bonds": "8"
        },
        "xai_insights": [
            "Multiple methoxy groups enhance cell membrane penetration",
            "α,β-unsaturated carbonyl acts as Michael acceptor for covalent binding to target",
            "Phenolic hydroxyl group forms critical hydrogen bond with key residue"
        ]
    }
}

# Define target profiles
target_profiles = {
    "EGFR Kinase": {
        "description": "Epidermal Growth Factor Receptor - a transmembrane protein involved in cell growth and division. Important target for cancer therapeutics.",
        "ideal_properties": "High binding affinity, low toxicity, medium to high stability, lipophilic character for membrane penetration.",
        "disease_relevance": "Non-small cell lung cancer, colorectal cancer, head and neck cancer",
        "binding_pocket": "ATP-binding site with key interactions at Met769, Thr830, and Asp831"
    },
    "COX-2": {
        "description": "Cyclooxygenase-2 - an enzyme responsible for inflammation and pain. Selective inhibition reduces side effects.",
        "ideal_properties": "Medium to high binding affinity, very low toxicity, high stability, appropriate size to fit binding pocket.",
        "disease_relevance": "Inflammation, pain, arthritis, some potential in cancer prevention",
        "binding_pocket": "Hydrophobic channel with a side pocket accessible by selective inhibitors"
    },
    "TNF-alpha": {
        "description": "Tumor Necrosis Factor alpha - a cell signaling protein involved in systemic inflammation. Key target for autoimmune diseases.",
        "ideal_properties": "Very high binding affinity, low to medium toxicity, medium stability, ability to disrupt protein-protein interactions.",
        "disease_relevance": "Rheumatoid arthritis, psoriasis, inflammatory bowel disease, ankylosing spondylitis",
        "binding_pocket": "Multimeric structure with inhibitors typically binding at subunit interfaces"
    },
    "NF-κB Pathway": {
        "description": "Nuclear Factor kappa B pathway - a protein complex controlling transcription, cytokine production, and cell survival.",
        "ideal_properties": "High binding affinity, low toxicity, medium stability, ability to modulate protein-protein interactions or DNA binding.",
        "disease_relevance": "Inflammatory diseases, cancer, septic shock, viral infection, autoimmune diseases",
        "binding_pocket": "Multiple potential binding sites including IKK complex and nuclear transcription factors"
    }
}

# Simulate loading animation
def loading_animation(text="PROCESSING", duration=3):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        dots = "." * (i % 4)
        status_text.markdown(f"<p style='font-family:VT323, monospace; font-size:20px; color:black'>{text}{dots}</p>", unsafe_allow_html=True)
        progress_bar.progress(i)
        time.sleep(duration/100)
    
    status_text.empty()
    progress_bar.empty()

# Pixel animation for generating molecules
def pixel_generating_animation():
    st.markdown("""
    <div style="text-align:center">
        <div style="display:inline-block; width:20px; height:20px; background:black; margin:5px; animation: pulse 1s infinite alternate;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:black; margin:5px; animation: pulse 1s infinite alternate 0.1s;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:black; margin:5px; animation: pulse 1s infinite alternate 0.2s;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:black; margin:5px; animation: pulse 1s infinite alternate 0.3s;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:black; margin:5px; animation: pulse 1s infinite alternate 0.4s;"></div>
        <style>
            @keyframes pulse {
                0% { opacity: 0.3; }
                100% { opacity: 1; }
            }
        </style>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2)

# Function to create a property indicator based on value
def property_indicator(value, max_value=100, inverse=False):
    percentage = value / max_value
    if inverse:
        percentage = 1 - percentage
    
    if percentage >= 0.8:
        return "<span class='property-indicator property-high'></span>"
    elif percentage >= 0.5:
        return "<span class='property-indicator property-medium'></span>"
    else:
        return "<span class='property-indicator property-low'></span>"

# Function to display a molecule card
def molecule_card(molecule_id, molecule_data):
    binding = molecule_data["binding_affinity"]
    toxicity = molecule_data["toxicity"]
    stability = molecule_data["stability"]
    
    st.markdown(f"""
    <div class="molecule-box">
        <h3 style="text-align:center">{molecule_id}</h3>
        <div style="font-family:monospace;white-space:pre;font-size:12px;background:#f0f0f0;padding:10px;border:2px solid black;">
{molecule_data['ascii_art']}
        </div>
        
        <div style="margin-top:15px;margin-bottom:15px;padding:10px;border:2px solid black;background:#f0f0f0;">
            <p><strong>SMILES:</strong> <code>{molecule_data['smiles']}</code></p>
            <p><strong>Target:</strong> {molecule_data['target']}</p>
        </div>
        
        <h4>PROPERTIES:</h4>
        <div style="margin-bottom:10px;">
            {property_indicator(binding, 100, False)} <strong>Binding Affinity:</strong> {binding}%
        </div>
        <div style="margin-bottom:10px;">
            {property_indicator(toxicity, 100, True)} <strong>Toxicity:</strong> {toxicity}%
        </div>
        <div style="margin-bottom:10px;">
            {property_indicator(stability, 100, False)} <strong>Stability:</strong> {stability}%
        </div>
        
        <h4>KEY SUBSTRUCTURES:</h4>
        <ul>
    """, unsafe_allow_html=True)
    
    for substructure in molecule_data["important_substructures"]:
        st.markdown(f"<li>{substructure}</li>", unsafe_allow_html=True)
    
    st.markdown("</ul></div>", unsafe_allow_html=True)

# Main application
def main():
    load_header()
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Sidebar for controls
    with st.sidebar:
        st.markdown("<h2 style='text-align: center'>DESIGN CONTROLS</h2>", unsafe_allow_html=True)
        
        # Target selection
        selected_target = st.selectbox(
            "SELECT TARGET",
            list(target_profiles.keys()),
            key="target_selector"
        )
        
        # Display target information
        st.markdown(f"""
        <div class="pixel-box">
            <h3>{selected_target}</h3>
            <p>{target_profiles[selected_target]['description']}</p>
            <p><strong>Disease relevance:</strong> {target_profiles[selected_target]['disease_relevance']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Property sliders for desired molecule properties
        st.markdown("<h3>DESIRED PROPERTIES</h3>", unsafe_allow_html=True)
        
        binding_pref = st.slider("Binding Affinity", 0, 100, 80, key="binding_pref")
        toxicity_pref = st.slider("Max Acceptable Toxicity", 0, 100, 20, key="toxicity_pref")
        stability_pref = st.slider("Stability", 0, 100, 75, key="stability_pref")
        
        # Additional property constraints
        st.markdown("<h3>STRUCTURAL CONSTRAINTS</h3>", unsafe_allow_html=True)
        
        max_mw = st.number_input("Max Molecular Weight", min_value=100, max_value=1000, value=500, step=50)
        
        druglike_props = st.checkbox("Enforce Drug-like Properties", value=True)
        allow_reactive = st.checkbox("Allow Reactive Groups", value=False)
        
        # Generate button
        if st.button("GENERATE MOLECULES", key="generate_btn"):
            pixel_generating_animation()
            loading_animation("RUNNING AI GENERATION", 4)
            st.session_state.molecules_generated = True
            
            # Simulate "matching" molecules to the specified criteria
            st.session_state.matched_molecules = []
            
            for molecule_id, molecule_data in molecules_data.items():
                # Simple scoring based on how well molecule matches preferences
                score = 0
                
                # Check binding affinity match
                if abs(molecule_data["binding_affinity"] - binding_pref) <= 20:
                    score += 1
                
                # Check toxicity constraint
                if molecule_data["toxicity"] <= toxicity_pref:
                    score += 1
                
                # Check stability match
                if abs(molecule_data["stability"] - stability_pref) <= 20:
                    score += 1
                
                # Add molecules with at least 2 of 3 criteria met
                if score >= 2:
                    st.session_state.matched_molecules.append(molecule_id)
            
            # If no molecules match, add at least one for demo purposes
            if not st.session_state.matched_molecules:
                st.session_state.matched_molecules = [random.choice(list(molecules_data.keys()))]
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: center; padding: 10px;'>
            <div style='font-family: VT323, monospace; font-size: 20px; color: black;'>
                XenoGenesis v0.1
            </div>
            <div style='font-family: Space Mono, monospace; font-size: 12px; color: #888888;'>
                Powered by Explainable AI
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content with tabs
    tab1, tab2, tab3 = st.tabs(["MOLECULE DESIGNER", "XAI INSIGHTS", "COMPARISON TOOL"])
    
    # Tab 1: Molecule Designer
    with tab1:
        st.markdown("<h2>GENERATIVE AI MOLECULE DESIGNER</h2>", unsafe_allow_html=True)
        
        # Introduction
        st.markdown(f"""
        <div class="pixel-box">
            <p>The AI will generate novel molecular structures optimized for the <span style='font-weight:bold'>{selected_target}</span> target.</p>
            <p>Adjust the desired properties in the sidebar and click 'GENERATE MOLECULES' to create new candidate structures.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display generated molecules if available
        if st.session_state.get('molecules_generated', False):
            if len(st.session_state.matched_molecules) > 0:
                st.markdown("<h3>GENERATED MOLECULES:</h3>", unsafe_allow_html=True)
                
                # Create columns for displaying molecules
                cols = st.columns(min(len(st.session_state.matched_molecules), 2))
                
                for idx, molecule_id in enumerate(st.session_state.matched_molecules):
                    with cols[idx % 2]:
                        molecule_card(molecule_id, molecules_data[molecule_id])
                
                # Store selected molecule in session state if user clicks on one
                if 'selected_molecule' not in st.session_state:
                    st.session_state.selected_molecule = st.session_state.matched_molecules[0]
            else:
                st.warning("No molecules matched your criteria. Try adjusting your preferences.")
        else:
            st.markdown("""
            <div style="text-align:center;margin:40px 0;padding:20px;border:2px dashed black;">
                <h3>MOLECULES WILL APPEAR HERE</h3>
                <p>Adjust parameters and click GENERATE MOLECULES to begin</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 2: XAI Insights
    with tab2:
        st.markdown("<h2>EXPLAINABLE AI INSIGHTS</h2>", unsafe_allow_html=True)
        
        # Intro text
        st.markdown("""
        <div class="pixel-box">
            <p>Explore how the AI reasons about molecule design. This section shows you <span style='font-weight:bold'>WHY</span> specific molecular features were selected and how they contribute to the desired properties.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Only show if molecules have been generated
        if st.session_state.get('molecules_generated', False) and len(st.session_state.get('matched_molecules', [])) > 0:
            # Molecule selector
            molecule_selector = st.selectbox(
                "SELECT MOLECULE FOR ANALYSIS",
                st.session_state.matched_molecules,
                key="molecule_analysis_selector"
            )
            
            # Get selected molecule data
            molecule_data = molecules_data[molecule_selector]
            
            # Display molecule and its data
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown(f"""
                <div class="pixel-box">
                    <h3 style="text-align:center">{molecule_selector}</h3>
                    <div style="font-family:monospace;white-space:pre;font-size:12px;background:#f0f0f0;padding:10px;border:2px solid black;">
{molecule_data['ascii_art']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="pixel-box">
                    <h3>MOLECULAR PROPERTIES</h3>
                    <table style="width:100%">
                """, unsafe_allow_html=True)
                
                for prop, value in molecule_data["properties"].items():
                    st.markdown(f"""
                    <tr>
                        <td style="font-weight:bold;width:50%">{prop}</td>
                        <td>{value}</td>
                    </tr>
                    """, unsafe_allow_html=True)
                
                st.markdown("</table></div>", unsafe_allow_html=True)
            
            # XAI Analysis
            st.markdown("<h3>AI REASONING ANALYSIS</h3>", unsafe_allow_html=True)
            
            # Key insights
            st.markdown("<div class='pixel-box'>", unsafe_allow_html=True)
            st.markdown("<h4>STRUCTURE-ACTIVITY RELATIONSHIPS:</h4>", unsafe_allow_html=True)
            
            for insight in molecule_data["xai_insights"]:
                st.markdown(f"""
                <div style="margin:10px 0;padding:10px;border:2px solid black;background:#f0f0f0;">
                    <p>• {insight}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # "What-if" scenarios - simulating XAI outputs
            st.markdown("<h4>WHAT-IF ANALYSIS:</h4>", unsafe_allow_html=True)
            st.markdown("""
            <p>The AI predicts how property changes would affect performance:</p>
            """, unsafe_allow_html=True)
            
            whatif_scenarios = [
                f"Removing {molecule_data['important_substructures'][0]} would decrease binding affinity by approximately 40%",
                f"Adding an additional hydroxyl group could improve solubility but may reduce membrane penetration",
                f"Converting amide linkage to ester would reduce stability while potentially decreasing toxicity"
            ]
            
            for scenario in whatif_scenarios:
                st.markdown(f"""
                <div style="margin:10px 0;padding:10px;border:2px solid black;background:#f0f0f0;">
                    <p>• {scenario}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Interactive substructure highlighting (simulated for MVP)
            st.markdown("<h3>INTERACTIVE SUBSTRUCTURE ANALYSIS</h3>", unsafe_allow_html=True)
            
            selected_substructure = st.radio(
                "HIGHLIGHT SUBSTRUCTURE",
                molecule_data["important_substructures"],
                key="substructure_selector"
            )
            
            # Simulated visualization with "highlighted" substructure
            st.markdown(f"""
            <div class="pixel-box">
                <p>Visualizing importance of <strong>{selected_substructure}</strong> in {molecule_selector}</p>
                <div style="text-align:center;padding:20px;background:#f0f0f0;border:2px solid black;">
                    <p style="font-family:monospace;">[Interactive molecular visualization would appear here]</p>
                    <p>This substructure contributes approximately {random.randint(20, 45)}% to the overall binding affinity</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Generate molecules first to see AI explanations.")
    
    # Tab 3: Comparison Tool
    with tab3:
        st.markdown("<h2>CANDIDATE COMPARISON TOOL</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="pixel-box">
            <p>Compare different candidate molecules side by side to evaluate their properties and make informed decisions about which structures to prioritize.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Only show if molecules have been generated
        if st.session_state.get('molecules_generated', False) and len(st.session_state.get('matched_molecules', [])) > 0:
            # If we have at least two molecules to compare
            if len(st.session_state.matched_molecules) >= 2:
                # Allow selecting molecules to compare
                st.markdown("<h3>SELECT MOLECULES TO COMPARE:</h3>", unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    molecule1 = st.selectbox(
                        "MOLECULE 1",
                        st.session_state.matched_molecules,
                        index=0,
                        key="compare_mol1"
                    )
                
                with col2:
                    # Default to second molecule if available, otherwise first
                    default_idx = min(1, len(st.session_state.matched_molecules) - 1)
                    molecule2 = st.selectbox(
                        "MOLECULE 2",
                        st.session_state.matched_molecules,
                        index=default_idx,
                        key="compare_mol2"
                    )
                
                # Display comparison
                if st.button("COMPARE MOLECULES", key="compare_btn"):
                    loading_animation("ANALYZING MOLECULES", 2)
                    
                    # Get molecule data
                    mol1_data = molecules_data[molecule1]
                    mol2_data = molecules_data[molecule2]
                    
                    # Side by side comparison
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        molecule_card(molecule1, mol1_data)
                    
                    with col2:
                        molecule_card(molecule2, mol2_data)
                    
                    # Comparative analysis
                    st.markdown("<h3>COMPARATIVE ANALYSIS</h3>", unsafe_allow_html=True)
                    
                    # Property comparison table
                    st.markdown("""
                    <div class="pixel-box">
                        <h4>PROPERTY COMPARISON:</h4>
                        <table style="width:100%">
                            <tr>
                                <th>Property</th>
                                <th>""" + molecule1 + """</th>
                                <th>""" + molecule2 + """</th>
                                <th>Difference</th>
                            </tr>
                    """, unsafe_allow_html=True)
                    
                    # Compare binding affinity
                    binding_diff = mol1_data["binding_affinity"] - mol2_data["binding_affinity"]
                    binding_arrow = "▲" if binding_diff > 0 else "▼" if binding_diff < 0 else "◆"
                    
                    st.markdown(f"""
                    <tr>
                        <td>Binding Affinity</td>
                        <td>{mol1_data["binding_affinity"]}%</td>
                        <td>{mol2_data["binding_affinity"]}%</td>
                        <td>{binding_arrow} {abs(binding_diff)}%</td>
                    </tr>
                    """, unsafe_allow_html=True)
                    
                    # Compare toxicity
                    toxicity_diff = mol1_data["toxicity"] - mol2_data["toxicity"]
                    # For toxicity, lower is better, so reverse the arrow
                    toxicity_arrow = "▼" if toxicity_diff > 0 else "▲" if toxicity_diff < 0 else "◆"
                    
                    st.markdown(f"""
                    <tr>
                        <td>Toxicity</td>
                        <td>{mol1_data["toxicity"]}%</td>
                        <td>{mol2_data["toxicity"]}%</td>
                        <td>{toxicity_arrow} {abs(toxicity_diff)}%</td>
                    </tr>
                    """, unsafe_allow_html=True)
                    
                    # Compare stability
                    stability_diff = mol1_data["stability"] - mol2_data["stability"]
                    stability_arrow = "▲" if stability_diff > 0 else "▼" if stability_diff < 0 else "◆"
                    
                    st.markdown(f"""
                    <tr>
                        <td>Stability</td>
                        <td>{mol1_data["stability"]}%</td>
                        <td>{mol2_data["stability"]}%</td>
                        <td>{stability_arrow} {abs(stability_diff)}%</td>
                    </tr>
                    """, unsafe_allow_html=True)
                    
                    # Compare molecular weight
                    mw1 = float(mol1_data["properties"]["Molecular Weight"].split()[0])
                    mw2 = float(mol2_data["properties"]["Molecular Weight"].split()[0])
                    mw_diff = mw1 - mw2
                    mw_arrow = "▲" if mw_diff > 0 else "▼" if mw_diff < 0 else "◆"
                    
                    st.markdown(f"""
                    <tr>
                        <td>Molecular Weight</td>
                        <td>{mol1_data["properties"]["Molecular Weight"]}</td>
                        <td>{mol2_data["properties"]["Molecular Weight"]}</td>
                        <td>{mw_arrow} {abs(mw_diff):.2f} g/mol</td>
                    </tr>
                    </table>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Recommendation
                    st.markdown("<h4>AI RECOMMENDATION:</h4>", unsafe_allow_html=True)
                    
                    # Simple scoring for recommendation
                    score1 = mol1_data["binding_affinity"] - mol1_data["toxicity"] + mol1_data["stability"]
                    score2 = mol2_data["binding_affinity"] - mol2_data["toxicity"] + mol2_data["stability"]
                    
                    recommended = molecule1 if score1 > score2 else molecule2
                    
                    st.markdown(f"""
                    <div class="pixel-box" style="border: 3px solid black; background-color: #f0f0f0;">
                        <p>Based on the comparative analysis, the AI recommends prioritizing <strong>{recommended}</strong> for further development.</p>
                        <p>Key advantages of {recommended}:</p>
                        <ul>
                    """, unsafe_allow_html=True)
                    
                    if recommended == molecule1:
                        advantages = [
                            f"{'Higher binding affinity' if mol1_data['binding_affinity'] > mol2_data['binding_affinity'] else ''}",
                            f"{'Lower toxicity profile' if mol1_data['toxicity'] < mol2_data['toxicity'] else ''}",
                            f"{'Better stability metrics' if mol1_data['stability'] > mol2_data['stability'] else ''}"
                        ]
                    else:
                        advantages = [
                            f"{'Higher binding affinity' if mol2_data['binding_affinity'] > mol1_data['binding_affinity'] else ''}",
                            f"{'Lower toxicity profile' if mol2_data['toxicity'] < mol1_data['toxicity'] else ''}",
                            f"{'Better stability metrics' if mol2_data['stability'] > mol1_data['stability'] else ''}"
                        ]
                    
                    # Filter out empty strings
                    advantages = [adv for adv in advantages if adv]
                    
                    for advantage in advantages:
                        st.markdown(f"<li>{advantage}</li>", unsafe_allow_html=True)
                    
                    st.markdown("</ul></div>", unsafe_allow_html=True)
                    
                    # Iterative design suggestions
                    st.markdown("<h3>ITERATIVE DESIGN SUGGESTIONS</h3>", unsafe_allow_html=True)
                    
                    st.markdown("""
                    <div class="pixel-box">
                        <p>The AI suggests the following modifications to improve these molecules:</p>
                        <ul>
                    """, unsafe_allow_html=True)
                    
                    suggestions = [
                        f"Combine the {mol1_data['important_substructures'][0]} from {molecule1} with the core scaffold of {molecule2}",
                        f"Modify the {random.choice(mol2_data['important_substructures'])} to reduce toxicity while maintaining binding",
                        "Introduce a linker region to improve flexibility and target interaction",
                        f"Explore bioisosteric replacements for the {random.choice(mol1_data['important_substructures'])}"
                    ]
                    
                    for suggestion in suggestions:
                        st.markdown(f"<li>{suggestion}</li>", unsafe_allow_html=True)
                    
                    st.markdown("""
                        </ul>
                        <div style="text-align:center;margin-top:20px;">
                            <button style="font-family:'VT323', monospace;font-size:18px;background:white;color:black;border:3px solid black;padding:10px 20px;cursor:pointer;box-shadow:3px 3px 0px #888888;">
                                GENERATE HYBRID MOLECULE (COMING SOON)
                            </button>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("Generate at least two molecules for comparison.")
        else:
            st.info("Generate molecules first to use the comparison tool.")

if __name__ == "__main__":
    main()