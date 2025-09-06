 #    streamlit run app.py

import streamlit as st
from textwrap import shorten
from urllib.parse import quote


# ✅ Must be the first Streamlit call
st.set_page_config(
    page_title="Home",   # Browser tab title
    page_icon="🏠",      # Optional favicon (emoji or path to .png/.ico)
    layout="wide"        # "centered" or "wide"
)


# ---------------Sidebar
from utils import apply_style_and_logo
apply_style_and_logo()

st.set_page_config(page_title="WT APPLICATIONS PLAT", page_icon="🚀", layout="wide")
# Spacer to push the link to the bottom (optional tweak for better placement)
#st.sidebar.markdown("<br>", unsafe_allow_html=True)
# Company website link
st.sidebar.markdown(
    '''
    <p style="text-align:left; font-size: 1.05rem; color: #009fb7;">
        <a href="https://www.wavetransition.com" target="_blank" style="color: #009fb7; text-decoration: none;">
            🌐 Visit WaveTransition
        </a>
    </p>
    ''',
    unsafe_allow_html=True
)


#st.image("schema.svg", use_container_width=True)
# ----------------------------
# 1) CONFIG: categories + sample data
# ----------------------------
CATEGORY_META = {
    "KDM": {"label": "KDM - Knowledge & Data Mapping", "color": "#93c5fd"},  # pastel blue
    "DDI": {"label": "DDI - Data Driven Insights", "color": "#6ee7b7"},  # pastel green
    "CBA": {"label": "CBA - Collaborative Business Applications", "color": "#fcd34d"},  # pastel amber
}

# Minimal SVGs for demo (replace with your own)

KDM_CHART = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="Definition-Search-Book--Streamline-Sharp" height="24" width="24">
  <desc>
    Definition Search Book Streamline Icon: https://streamlinehq.com
  </desc>
  <g id="definition-search-book">
    <g id="Group 176740">
      <path id="Ellipse 577" fill="#009fb7" d="M11.932 16.245a4.315 4.315 0 1 0 8.63 0 4.315 4.315 0 1 0 -8.63 0" stroke-width="1"></path>
      <path id="Union" fill="#2859c5" fill-rule="evenodd" d="M12.932 16.245a3.315 3.315 0 1 1 6.63 0 3.315 3.315 0 0 1 -6.63 0Zm3.315 -5.315a5.315 5.315 0 1 0 2.985 9.714l2.421 2.422 1.415 -1.414 -2.422 -2.422a5.315 5.315 0 0 0 -4.399 -8.3Z" clip-rule="evenodd" stroke-width="1"></path>
      <path id="Subtract" fill="#009fb7" fill-rule="evenodd" d="M22.932 14.91A6.815 6.815 0 1 0 9.77 18.37a1.593 1.593 0 0 0 -0.162 -0.007H0.932V0.934h8.675c0.868 0 1.571 0.704 1.571 1.572h1.51c0 -0.868 0.703 -1.572 1.571 -1.572h8.673v13.977Z" clip-rule="evenodd" stroke-width="1"></path>
      <path id="Subtract_2" fill="#2859c5" fill-rule="evenodd" d="M12.682 10.436V2.422h-1.5v9.264a6.855 6.855 0 0 1 1.5 -1.25Z" clip-rule="evenodd" stroke-width="1"></path>
    </g>
  </g>
</svg>"""

DDI_CHART = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="Signal-Full--Streamline-Sharp" height="24" width="24">
  <desc>
    Signal Full Streamline Icon: https://streamlinehq.com
  </desc>
  <g id="signal-full--phone-mobile-device-signal-wireless-smartphone-iphone-bar-bars-full-android">
    <path id="Subtract" fill="#009fb7" d="M2.25 19.5h5.5v-4.25h-5.5v4.25Z" stroke-width="1"></path>
    <path id="Subtract_2" fill="#009fb7" d="M9.25 19.5h5.5V8.75h-5.5V19.5Z" stroke-width="1"></path>
    <path id="Subtract_3" fill="#009fb7" d="M21.75 1.75h-5.5V19.5h5.5V1.75Z" stroke-width="1"></path>
    <path id="Subtract_4" fill="#2859c5" d="M1 21v2h22v-2H1Z" stroke-width="1"></path>
  </g>
</svg>
"""

CBA_CHART="""
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="User-Collaborate-Group--Streamline-Sharp" height="24" width="24">
  <desc>
    User Collaborate Group Streamline Icon: https://streamlinehq.com
  </desc>
  <g id="user-collaborate-group">
    <path id="Union" fill="#2859c5" fill-rule="evenodd" d="M9 3.5a2.5 2.5 0 1 1 -5 0 2.5 2.5 0 0 1 5 0Zm8.5 15a2.5 2.5 0 1 0 0 -5 2.5 2.5 0 0 0 0 5ZM13 23v-2s1.5 -1.5 4.5 -1.5S22 21 22 21v2h-9ZM2 10.5v-2S3.5 7 6.5 7 11 8.5 11 8.5v2H2Z" clip-rule="evenodd" stroke-width="1"></path>
    <path id="Union_2" fill="#009fb7" fill-rule="evenodd" d="M13.5 5H18v4.5h2V3h-6.5v2ZM4 14.5V21h6.5v-2H6v-4.5H4Z" clip-rule="evenodd" stroke-width="1"></path>
  </g>
</svg>
"""


SVG_APERTURE = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="Customer-Support-Setting--Streamline-Sharp" height="24" width="24">
  <desc>
    Customer Support Setting Streamline Icon: https://streamlinehq.com
  </desc>
  <g id="customer-support-setting--customer-phone-help-microphone-phone-support">
    <path id="Union" fill="#2859c5" d="m9.58296 19.5024 -0.46319 -3.206C10.0486 16.1022 11.0119 16 12 16s1.9514 0.1022 2.8802 0.2964l-0.4632 3.206 5.252 3.2825 3.7585 -4.0298 -0.7606 -0.6808c-1.8092 -1.6193 -3.9904 -2.8337 -6.4009 -3.499C14.9068 14.2001 13.476 14 12 14s-2.90678 0.2001 -4.26606 0.5753c-2.41043 0.6653 -4.59162 1.8797 -6.40086 3.499l-0.76057 0.6808 3.75843 4.0298 5.25202 -3.2825Z" stroke-width="1"></path>
    <path id="Subtract" fill="#8fbffa" fill-rule="evenodd" d="M8.99996 1.5H15v2.51239c0.301 0.10642 0.5947 0.22837 0.88 0.36489l1.7768 -1.77678 4.2427 4.24264 -1.7768 1.77676c0.1365 0.28533 0.2585 0.57902 0.3649 0.8801H23V14h-2.7472c-1.0907 -0.5635 -2.247 -1.0193 -3.4549 -1.3526 -0.4279 -0.1181 -0.862 -0.2208 -1.3015 -0.3074C15.4128 10.4813 13.8794 9 12 9c-1.8793 0 -3.41272 1.4812 -3.4964 3.3399 -0.43971 0.0866 -0.87394 0.1893 -1.30201 0.3075 -1.2079 0.3333 -2.36422 0.7891 -3.4549 1.3526H1V9.5h2.51241c0.10641 -0.30106 0.22836 -0.59473 0.36486 -0.88004L2.10051 6.8432l4.24264 -4.24264L8.11989 4.3773c0.28532 -0.13651 0.579 -0.25846 0.88007 -0.36488V1.5Z" clip-rule="evenodd" stroke-width="1"></path>
  </g>
</svg>"""
SVG_CHART = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" id="Definition-Search-Book--Streamline-Sharp" height="24" width="24">
  <desc>
    Definition Search Book Streamline Icon: https://streamlinehq.com
  </desc>
  <g id="definition-search-book">
    <g id="Group 176740">
      <path id="Ellipse 577" fill="#009fb7" d="M11.932 16.245a4.315 4.315 0 1 0 8.63 0 4.315 4.315 0 1 0 -8.63 0" stroke-width="1"></path>
      <path id="Union" fill="#2859c5" fill-rule="evenodd" d="M12.932 16.245a3.315 3.315 0 1 1 6.63 0 3.315 3.315 0 0 1 -6.63 0Zm3.315 -5.315a5.315 5.315 0 1 0 2.985 9.714l2.421 2.422 1.415 -1.414 -2.422 -2.422a5.315 5.315 0 0 0 -4.399 -8.3Z" clip-rule="evenodd" stroke-width="1"></path>
      <path id="Subtract" fill="#009fb7" fill-rule="evenodd" d="M22.932 14.91A6.815 6.815 0 1 0 9.77 18.37a1.593 1.593 0 0 0 -0.162 -0.007H0.932V0.934h8.675c0.868 0 1.571 0.704 1.571 1.572h1.51c0 -0.868 0.703 -1.572 1.571 -1.572h8.673v13.977Z" clip-rule="evenodd" stroke-width="1"></path>
      <path id="Subtract_2" fill="#2859c5" fill-rule="evenodd" d="M12.682 10.436V2.422h-1.5v9.264a6.855 6.855 0 0 1 1.5 -1.25Z" clip-rule="evenodd" stroke-width="1"></path>
    </g>
  </g>
</svg>"""
SVG_GRID = """<svg viewBox="0 0 24 24" width="40" height="40" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="3" y="3" width="8" height="8" stroke="currentColor" stroke-width="2"/>
<rect x="13" y="3" width="8" height="8" stroke="currentColor" stroke-width="2"/>
<rect x="3" y="13" width="8" height="8" stroke="currentColor" stroke-width="2"/>
<rect x="13" y="13" width="8" height="8" stroke="currentColor" stroke-width="2"/></svg>"""

APPS = [
    {
        "name": "Advanced Knowledge Repository",
        "category": "KDM",
        "tech": "Python Dash",
        "icon_svg": KDM_CHART,
        "description": "Documents repository tags based to provide context to humans and AI",
        "url": "https://wtadvancedknowledgerepository-a678ffa87164.herokuapp.com/",
    },
    {
        "name": "Anchor Brief",
        "category": "KDM",
        "tech": "Python Dash",
        "icon_svg": KDM_CHART,
        "description": " Fast, structured briefing notes on topics that have been pre-selected by WT's experts and advisors",
        "url": "https://wtanchorbrief-e2cd54050bf9.herokuapp.com/",
    },
    {
        "name": "Fair Fuel Comparison",
        "category": "DDI",
        "tech": "Python Streamlit",
        "icon_svg": DDI_CHART,
        "description": "Experiment with elasticity curves; fit, compare, and share.",
        "url": "https://wtfuelfaircomparison.streamlit.app/",
    },
    {
        "name": "NewsRanker",
        "category": "KDM",
        "tech": "Python Streamlit",
        "icon_svg": KDM_CHART,
        "description": "Newsletter based on public websites and rss feeds provider boosted by a Machine Learning approach to rank the importance of the news",
        "url": "https://wtnewsranker.streamlit.app/",
    },
    {
        "name": "Agentic Business Analyst",
        "category": "DDI",
        "tech": "Python Dash",
        "icon_svg": DDI_CHART,
        "description": "Agentic Analyst for Deep Financial & Market Exploration Across Energy Transition Supply Chains",
        "url": "https://wtagenticbusinessanalyst-8e0469aca662.herokuapp.com/",
    },
    {
        "name": "Company Search",
        "category": "DDI",
        "tech": "Python Streamlit",
        "icon_svg": DDI_CHART,
        "description": "Fast, Targeted Search Across Our Proprietary Company Database",
        "url": "https://wtcompaniesearch.streamlit.app/",
    },
    
    {
        "name": "EU Decarbon Policy",
        "category": "KDM",
        "tech": "Python Dash",
        "icon_svg": KDM_CHART,
        "description": "AI-Powered Conversations on Europe’s Path to Net Zero",
        "url": "https://wteudecarbonpolicy-e584e739c8f7.herokuapp.com/s",
    },
        
    
    
    
     {
        "name": "GEO EU Data Hub",
        "category": "CBA",
        "tech": "Python Qgis",
        "icon_svg": CBA_CHART,
        "description": "Integrating EU Energy & Infrastructure Data into One Geospatial Hub",
        "url": "static/WT_EU_GEO_DATA_HUB.png",
    },
    
    {
        "name": "BiomethanIT",
        "category": "CBA",
        "tech": "Python Streamlit",
        "icon_svg": CBA_CHART,
        "description": "In-Depth Overview of the Italian Biomethane Sector, Backed by Data and Business Modeling",
        "url": "https://wtbiomethanit.streamlit.app/",
    },
  
      {
        "name": "Fleet DecarbonAI",
        "category": "CBA",
        "tech": "Python Streamlit",
        "icon_svg": CBA_CHART,
        "description": "Data and AI for Greener Road Logistics Across Europe",
        "url": "static/WT_EU_GEO_DATA_HUB.png",
    },  
    
    
    
    
    
]


# ----------------------------
# 2) STYLE
# ----------------------------
st.markdown("""
    <style>
    :root {
      --card-bg: rgba(0, 47, 77, 0.8); /* derived from secondaryBackgroundColor */
      --text: #ededf1; /* from your theme */
    }
    @media (prefers-color-scheme: dark) {
      :root { --card-bg: rgba(0, 47, 77, 0.9); --text: #ededf1; }
    }
    .card {
      background: var(--card-bg);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      padding: 20px;
      height: 100%;
      color: var(--text);
    }
    .card h3 {
      margin: 0 0 8px 0;
      font-size: 1.2rem;
      line-height: 1.5;
    }
    .card .desc {
      color: var(--text);
      opacity: 0.9;
      font-size: 1rem;
      margin: 8px 0 16px 0;
    }
    .badge {
      display:inline-flex;
      align-items:center;
      gap:.4rem;
      padding:4px 12px;
      border-radius: 999px;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text);
      background: rgba(255,255,255,0.1);
    }
    .row { display:flex; gap: 16px; }
    .iconwrap {
      display:flex;
      align-items:center;
      justify-content:center;
      width:48px;
      height:48px;
      border-radius:12px;
      background: rgba(255,255,255,0.1);
    }
    .iconwrap svg { color: currentColor; }
    .meta {
      display:flex;
      align-items:center;
      gap:10px;
      margin-bottom:10px;
    }
    .kicker {
      font-size:.85rem;
      opacity:.85;
      color: var(--text);
    }
    .button {
      text-decoration:none;
      padding: 10px 14px;
      border-radius: 10px;
      font-weight:600;
      color: var(--text);
      border: 1px solid rgba(255,255,255,0.2);
    }
    .button:hover {
      filter: brightness(1.1);
    }
    .grid {
      display: grid;
      gap: 16px;
      grid-template-columns: repeat(1, minmax(0, 1fr));
    }
    @media (min-width: 800px) {
      .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    @media (min-width: 1200px) {
      .grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    }
    .cat-header {
      display:flex;
      align-items:center;
      justify-content:space-between;
      margin: 4px 0 12px 0;
    }
    .count {
      font-size: .9rem;
      opacity: .85;
      color: var(--text);
    }
    .tech-chip {
      font-size:.78rem;
      padding: 4px 8px;
      border-radius: 999px;
      background: rgba(255,255,255,0.1);
      margin-left: 6px;
      color: var(--text);
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 3) HEADER & CONTROLS
# ----------------------------
st.title("WT Applications Platform Hub")

st.markdown("""
    <style>
    .custom-caption {
        font-size: 3.0rem;  /* Adjust size */
        font-weight: 800;
        color: #20c997;  /* Match your theme text color */
        opacity: 0.9;
        margin-top: -100px;
    }
    </style>
    <p class="custom-caption">Your Gateway to Our Business Applications</p>
""", unsafe_allow_html=True)
#st.caption("Your Gateway to Our Business Applications")

left, right = st.columns([3, 2])
with left:
    q = st.text_input("Search apps", placeholder="Search by name or description...")
with right:
    tech_filter = st.multiselect("Filter by tech", options=sorted({a["tech"] for a in APPS}), default=None)

# ----------------------------
# 4) FILTERING
# ----------------------------
def matches(app):
    if q:
        hay = f'{app["name"]} {app["description"]}'.lower()
        if q.lower() not in hay:
            return False
    if tech_filter:
        if app["tech"] not in tech_filter:
            return False
    return True

apps_filtered = [a for a in APPS if matches(a)]

# ----------------------------
# 5) RENDER: categories emphasized
# ----------------------------
for cat_key in ["KDM", "DDI", "CBA"]:
    items = [a for a in apps_filtered if a["category"] == cat_key]
    label = CATEGORY_META[cat_key]["label"]
    color = CATEGORY_META[cat_key]["color"]

    # Category header
    st.markdown(
        f"""
        <div class="cat-header">
            <div class="badge" style="background:{color}1a; color:{color}; border: 1rem solid {color}40;">
                <span>●</span> {label}
            </div>
            <div class="count">{len(items)} app(s)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not items:
        st.info(f"No apps in {label} match the current filters.")
        continue

    # Grid of cards
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    for app in items:
        #title_link = f'<a href="{app["url"]}" target="_blank" class="button" style="border-color:{color}40;">Open app ↗</a>'
        # safe short description for consistent height
        
        
        if app["url"].endswith((".png", ".jpg", ".jpeg", ".webp")):
          title_link = f'<img src="{app["url"]}" alt="No Link - Local" style="max-height:160px; border-radius:10px; margin-left:10px;">'
        else:
          title_link = f'<a href="{app["url"]}" target="_blank" class="button" style="border-color:{color}40;">Open app ↗</a>'
        
               
        
        desc = shorten(app["description"], width=250, placeholder="…")
        icon = app["icon_svg"]

        st.markdown(
            f"""
            <div class="card">
              <div class="meta">
                <div class="iconwrap" style="color:{color}">{icon}</div>
                <div>
                  <div class="kicker" style="color:{color}; font-weight:700;">{CATEGORY_META[app["category"]]["label"]}</div>
                  <h3>{app["name"]}</h3>
                </div>
              </div>
              <div class="desc">{desc}</div>
              <div style="display:flex; align-items:center; justify-content:space-between;">
                <div>
                  <span class="tech-chip">{app["tech"]}</span>
                </div>
                {title_link}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# 6) FOOTER / NEXT PHASE HINT
# ----------------------------
with st.expander("About this platform"):
    st.markdown("""
- **Data-driven:** Edit the `APPS` list to add/remove apps, change categories (A/B/C), or swap SVG icons.
- **Icons:** Paste inline SVG strings in `icon_svg` for crisp, theme-friendly icons.
- **Per-app pages (Phase 2):** Turn this into a multi-page app by creating a `/pages` folder and adding `01_<AppName>.py` for details, docs, screenshots, etc.
- **Styling:** Category colors come from `CATEGORY_META`; tweak them to match your brand.
    """)