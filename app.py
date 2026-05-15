import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Jumeirah Park · Villa Lookup",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 1.5rem; padding-bottom: 3rem; max-width: 920px;}

body, [data-testid="stAppViewContainer"] {background: #f4f6f9;}

.app-header {
    background: #1a2f4a;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 16px;
}
.app-title {font-size: 22px; font-weight: 800; color: #ffffff; margin: 0;}
.app-sub {font-size: 11px; color: #7ab0d8; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 6px;}
.stat-block {margin-left: auto; text-align: right;}
.stat-n {font-size: 28px; font-weight: 800; color: #ffffff; line-height: 1;}
.stat-l {font-size: 10px; color: #7ab0d8; text-transform: uppercase; letter-spacing: 1px;}

.sec-card {border-radius: 12px; margin-bottom: 12px; overflow: hidden; border: 1.5px solid;}
.s22  {border-color: #b8d0f0; background: #ffffff;}
.s23  {border-color: #b8e0c8; background: #ffffff;}
.s24  {border-color: #f0c898; background: #ffffff;}
.s25a {border-color: #d0b0f0; background: #ffffff;}
.s25b {border-color: #f0b0c8; background: #ffffff;}

.sec-hd {display: flex; align-items: center; gap: 12px; padding: 13px 20px; border-bottom: 1.5px solid;}
.hd22  {border-color: #b8d0f0; background: #eaf2ff;}
.hd23  {border-color: #b8e0c8; background: #eafaf0;}
.hd24  {border-color: #f0c898; background: #fff6ea;}
.hd25a {border-color: #d0b0f0; background: #f4eaff;}
.hd25b {border-color: #f0b0c8; background: #fff0f5;}

.ytag {font-size: 11px; font-weight: 800; letter-spacing: 2px; padding: 3px 10px; border-radius: 5px;}
.y22  {background: #1a4a8a; color: #ffffff;}
.y23  {background: #1a6a3a; color: #ffffff;}
.y24  {background: #8a4a10; color: #ffffff;}
.y25a {background: #5a1a8a; color: #ffffff;}
.y25b {background: #8a1a40; color: #ffffff;}
.slbl {font-size: 13px; color: #2a3a4a; font-weight: 700;}

.info-tbl {width: 100%; border-collapse: collapse;}
.info-tbl tr {border-bottom: 1px solid #e8eef4;}
.info-tbl tr:last-child {border: none;}
.info-tbl td {padding: 10px 20px; font-size: 13px; vertical-align: top;}
.info-tbl td.lbl {color: #4a6080; width: 38%; font-weight: 600;}
.info-tbl td.val {color: #0a1a2a; font-weight: 600; word-break: break-word;}
.nodata {padding: 14px 20px; font-size: 13px; color: #a0b0c0; font-style: italic;}

.pills {display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px;}
.pill  {font-size: 11px; font-weight: 700; padding: 5px 16px; border-radius: 20px;}
.p22  {background: #1a4a8a; color: #ffffff;}
.p23  {background: #1a6a3a; color: #ffffff;}
.p24  {background: #8a4a10; color: #ffffff;}
.p25a {background: #5a1a8a; color: #ffffff;}
.p25b {background: #8a1a40; color: #ffffff;}
.pno  {background: #e0e8f0; color: #90a8c0; border: 1px solid #c8d8e8;}

.villa-id {font-size: 30px; font-weight: 800; color: #0a1a2a; margin-bottom: 8px; letter-spacing: .3px;}
.not-found {background: #fff0f0; border: 1.5px solid #f0b0b0; border-radius: 10px; padding: 16px 20px; color: #a02020; font-size: 14px; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data(show_spinner="Loading property database…")
def load():
    url = "https://raw.githubusercontent.com/nomanalhuraiz-web/jumeirah-park-lookup/main/master_villa_db.csv"
    df = pd.read_csv(url, low_memory=False)
    df['villa_number'] = df['villa_number'].astype(str).str.strip()
    return df

df = load()
all_villas = sorted(df['villa_number'].dropna().unique().tolist())

# ── Field map ─────────────────────────────────────────────────────────────────
SECTIONS = [
    ("2022","CRM Owner Record","s22","hd22","y22","p22",[
        ("2022_owner_name","Owner Name"),("2022_joint_owner","Joint Owner"),
        ("2022_customer_type","Customer Type"),("2022_nationality","Nationality"),
        ("2022_property_type","Property Type"),("2022_bedrooms","Bedrooms"),
        ("2022_BUA_sqft","BUA (sqft)"),("2022_plot_area_sqft","Plot Area (sqft)"),
        ("2022_plan_type","Plan Type"),("2022_theme","Theme"),
        ("2022_telephone","Telephone"),("2022_mobile","Mobile"),
        ("2022_email","Email"),("2022_package","Package"),
        ("2022_comments","Comments"),("2022_updated_on","Last Updated"),
    ]),
    ("2023","Municipality Registry","s23","hd23","y23","p23",[
        ("2023_permit_number","Permit Number"),("2023_owner_name","Owner Name"),
        ("2023_phone","Phone"),("2023_mobile","Mobile"),("2023_email","Email"),
        ("2023_property_type","Property Type"),("2023_usage","Usage"),
        ("2023_rooms","Rooms"),("2023_BUA","BUA"),("2023_plot_area","Plot Area"),
        ("2023_actual_area_sqm","Actual Area (sqm)"),("2023_plot_number_dm","DM Plot Number"),
        ("2023_area_district","Area / District"),("2023_project","Project"),
        ("2023_comments","Comments"),("2023_updated_date","Last Updated"),
    ]),
    ("2024","Transaction Log","s24","hd24","y24","p24",[
        ("2024_buyer_name","Buyer Name"),("2024_seller_name","Seller Name"),
        ("2024_buyer_nationality","Buyer Nationality"),("2024_buyer_mobile","Buyer Mobile"),
        ("2024_max_price_AED","Max Price (AED)"),("2024_min_price_AED","Min Price (AED)"),
        ("2024_num_transactions","No. of Transactions"),("2024_size_sqm","Size (sqm)"),
        ("2024_property_type","Property Type"),("2024_land_number","Land Number"),
        ("2024_latest_txn_date","Latest Transaction Date"),
    ]),
    ("2025","Registry — Before April","s25a","hd25a","y25a","p25a",[
        ("2025_buyer_name","Buyer Name"),("2025_buyer_nationality","Buyer Nationality"),
        ("2025_buyer_mobile","Buyer Mobile"),("2025_buyer_passport","Passport Number"),
        ("2025_buyer_uae_id","UAE ID Number"),("2025_buyer_dob","Date of Birth"),
        ("2025_procedure_types","Procedure Types"),
    ]),
    ("2025","Transactions — April to December","s25b","hd25b","y25b","p25b",[
        ("2025_aprdec_owner_name","Owner Name"),("2025_aprdec_phone1","Phone"),
        ("2025_aprdec_mobile1","Mobile"),("2025_aprdec_txn_amount_AED","Transaction Amount (AED)"),
        ("2025_aprdec_actual_size_sqft","Actual Size (sqft)"),
        ("2025_aprdec_plot_size_sqft","Plot Size (sqft)"),
        ("2025_aprdec_built_up_sqft","Built Up (sqft)"),
        ("2025_aprdec_beds","Bedrooms"),("2025_aprdec_district","District"),
        ("2025_aprdec_date","Date"),
    ]),
]

# Fields that should NEVER get comma formatting
NO_COMMA_FIELDS = {
    '2022_telephone','2022_mobile','2022_email',
    '2023_permit_number','2023_phone','2023_mobile','2023_email','2023_plot_number_dm',
    '2024_buyer_mobile','2024_land_number',
    '2025_buyer_mobile','2025_buyer_passport','2025_buyer_uae_id',
    '2025_aprdec_phone1','2025_aprdec_mobile1',
}

def fmt(val, col=None):
    if val is None or (isinstance(val, float) and np.isnan(val)): return None
    s = str(val).strip()
    if s.lower() in ('nan','none','nat',''): return None
    # Never format these fields as numbers with commas
    if col in NO_COMMA_FIELDS:
        return s
    try:
        f = float(s)
        return f"{int(f):,}" if f == int(f) else f"{f:,.2f}"
    except: pass
    return s

def render(row):
    vid = row['villa_number']
    pill_labels = {"p22":"2022","p23":"2023","p24":"2024","p25a":"2025 (Before Apr)","p25b":"2025 (Apr–Dec)"}
    pills = ""
    for yr, lbl, sc, hdc, yc, pc, fields in SECTIONS:
        has = any(fmt(row.get(c), c) is not None for c,_ in fields)
        cls = pc if has else "pno"
        pills += f'<span class="pill {cls}">{pill_labels[pc]}</span>'

    cards = ""
    for yr, lbl, sc, hdc, yc, pc, fields in SECTIONS:
        rows = "".join(
            f'<tr><td class="lbl">{fl}</td><td class="val">{fmt(row.get(col), col)}</td></tr>'
            for col, fl in fields if fmt(row.get(col), col) is not None
        )
        body = f'<table class="info-tbl">{rows}</table>' if rows else '<p class="nodata">No data for this period</p>'
        cards += f"""<div class="sec-card {sc}">
          <div class="sec-hd {hdc}">
            <span class="ytag {yc}">{yr}</span>
            <span class="slbl">{lbl}</span>
          </div>{body}</div>"""

    st.markdown(
        f'<div class="villa-id">🏠 {vid}</div>'
        f'<div class="pills">{pills}</div>{cards}',
        unsafe_allow_html=True
    )

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="app-header">
  <div>
    <p class="app-sub">Jumeirah Park · Dubai</p>
    <p class="app-title">Villa Property Lookup</p>
  </div>
  <div class="stat-block">
    <div class="stat-n">{len(df):,}</div>
    <div class="stat-l">Properties</div>
  </div>
</div>""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])
with col1:
    query = st.text_input("Search", placeholder="Type Villa / Property ID  e.g.  JPB3VL001", label_visibility="collapsed")
with col2:
    pick = st.selectbox("Browse", ["— or browse all —"] + all_villas, label_visibility="collapsed")

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

search = query.strip().upper() if query.strip() else (pick if pick != "— or browse all —" else None)

if search:
    exact = df[df['villa_number'].str.upper() == search]
    if not exact.empty:
        render(exact.iloc[0])
    else:
        partial = df[df['villa_number'].str.upper().str.contains(search, na=False)]
        if not partial.empty:
            st.info(f"{len(partial)} partial matches found — select from the Browse dropdown on the right.")
        else:
            st.markdown(f'<div class="not-found">No property found for <strong>{search}</strong> — check the villa number format.</div>', unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align:center;padding:70px 0;color:#a0b8d0;'>
      <div style='font-size:40px;margin-bottom:16px;'>🏘</div>
      <div style='font-size:15px;font-weight:600;color:#2a4060;'>Enter a Villa Number or Property ID to view full details</div>
      <div style='font-size:12px;margin-top:10px;color:#7090a8;'>
        JPB3VL001 &nbsp;·&nbsp; JPMVIL047 &nbsp;·&nbsp; JPN3VL027 &nbsp;·&nbsp; JPA3VL001
      </div>
    </div>""", unsafe_allow_html=True)
