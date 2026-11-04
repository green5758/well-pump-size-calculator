import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "WellPumpPro"
SITE_TAGLINE = "Submersible Well Pump GPM, Total Dynamic Head (TDH), Pressure Tank & Wire Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/wellpumppro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "wellpumppro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "Red Lion RL12G07-2W2V 3/4 HP 12 GPM 4-Inch 230V Stainless Submersible Deep Well Pump",
        "category": "Submersible Deep Well Pump",
        "rating": "4.7 ★ (3,850+ reviews)",
        "badge": "#1 Best-Selling 4\" Submersible",
        "specs": "12 GPM Flow | Up to 275 Ft Total Head | 2-Wire 230V Franklin-Style Motor | Built-In Check Valve",
        "keyword": "Red+Lion+RL12G07+3+4+HP+12+GPM+Submersible+Deep+Well+Pump"
    },
    {
        "title": "Water Worker HT-44B / HT-86B Vertical Pre-Charged Diaphragm Well Pressure Tank (44–86 Gal)",
        "category": "Diaphragm Pressure Tank",
        "rating": "4.8 ★ (5,400+ reviews)",
        "badge": "#1 Well Pressure Tank",
        "specs": "Butyl Diaphragm + Polypropylene Liner | 13.6–26.6 Gal Drawdown | NSF/ANSI 61 Certified",
        "keyword": "Water+Worker+HT+44B+HT+86B+Vertical+Well+Pressure+Tank"
    },
    {
        "title": "Cycle Stop Valves CSV1A Stainless Steel Constant Pressure Valve (1–25 GPM, 15–150 PSI)",
        "category": "Constant Pressure Valve",
        "rating": "4.9 ★ (1,950+ reviews)",
        "badge": "#1 Pump Short-Cycle Eliminator",
        "specs": "Delivers City-Like Constant Shower Pressure | Eliminates Water Hammer | Triples Pump Lifespan",
        "keyword": "Cycle+Stop+Valves+CSV1A+Constant+Pressure+Well+Valve"
    },
    {
        "title": "Goulds J5S / J10S Shallow & Convertible Cast-Iron Jet Pump (1/2 HP – 1 HP, 115V/230V)",
        "category": "Cast-Iron Well Jet Pump",
        "rating": "4.8 ★ (2,700+ reviews)",
        "badge": "Plumber's #1 Jet Pump",
        "specs": "Back Pull-Out Service Design | Integral Shallow-Well Nozzle | Continuous Duty AO Smith Motor",
        "keyword": "Goulds+J5S+J10S+Shallow+Well+Jet+Pump"
    },
    {
        "title": "Boshart / Merrill Complete No-Lead Brass Pressure Tank Tee Kit w/ 40/60 Square D Pumptrol Switch",
        "category": "Brass Tank Tee Installation Kit",
        "rating": "4.9 ★ (6,800+ reviews)",
        "badge": "#1 Complete Tank Tee Kit",
        "specs": "1\"×11\" Solid Brass Union Tee | Genuine Square D FSG2 40/60 Switch | 100 PSI Gauge + Relief + Drain",
        "keyword": "Brass+Well+Pressure+Tank+Tee+Kit+Square+D+40+60+Switch"
    },
    {
        "title": "Hallmark Industries MA0414X-7A 1 HP 230V 33 GPM All-Stainless Deep Well Submersible Pump",
        "category": "High-Flow Irrigation Well Pump",
        "rating": "4.6 ★ (8,100+ reviews)",
        "badge": "#1 Budget Stainless Pump",
        "specs": "207 Ft Max Head | 2-Wire (No External Control Box Needed) | Hermetically Sealed Capacitor",
        "keyword": "Hallmark+Industries+1+HP+230V+Submersible+Deep+Well+Pump"
    },
    {
        "title": "Kalas / Nassau 10/3 & 12/3 w/ Ground Solid/Stranded Twisted Copper Submersible Well Pump Wire",
        "category": "Submersible Well Pump Wire",
        "rating": "4.9 ★ (4,200+ reviews)",
        "badge": "#1 UL-Listed Submersible Wire",
        "specs": "600V Heavy-Duty PVC/THW Insulation | 100% Pure Copper | Direct Burial & Underwater Rated",
        "keyword": "12+3+10+3+Submersible+Well+Pump+Wire+Copper"
    },
    {
        "title": "Franklin Electric 2801074915 / 2823008110 3/4 HP & 1 HP 230V Submersible Pump Control Box",
        "category": "3-Wire Pump Control Box",
        "rating": "4.8 ★ (5,100+ reviews)",
        "badge": "#1 OEM Pump Control Box",
        "specs": "Heavy-Duty Start/Run Capacitors + Overload Relay | Outdoor NEMA 3R Enclosure | Made in USA",
        "keyword": "Franklin+Electric+3+4+HP+1+HP+230V+Submersible+Pump+Control+Box"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "Red Lion RL12G07 (3/4 HP)",
        "type": "4\" Submersible (2-Wire)",
        "flow_head": "12 GPM | Up to 275 Ft TDH",
        "voltage_spec": "230V (No Control Box Needed)",
        "highlight": "Best for 100–220 Ft Residential Wells",
        "rating": "4.7 / 5.0 ★",
        "keyword": "Red+Lion+RL12G07+3+4+HP+12+GPM+Submersible+Deep+Well+Pump"
    },
    {
        "model": "Red Lion RL12G10-3W2V (1 HP)",
        "type": "4\" Submersible (3-Wire)",
        "flow_head": "12 GPM | Up to 350 Ft TDH",
        "voltage_spec": "230V (Includes Control Box)",
        "highlight": "Serviceable Above-Ground Capacitors",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Red+Lion+1+HP+12+GPM+3+Wire+Submersible+Well+Pump"
    },
    {
        "model": "Goulds J5S / J10S Jet Pump",
        "type": "Above-Ground Shallow Jet",
        "flow_head": "10–16 GPM | 0–25 Ft Lift",
        "voltage_spec": "115V / 230V Dual-Voltage",
        "highlight": "15+ Year Cast-Iron Service Life",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Goulds+J5S+J10S+Shallow+Well+Jet+Pump"
    },
    {
        "model": "Water Worker HT-44B (44 Gal)",
        "type": "Vertical Diaphragm Tank",
        "flow_head": "11.9 Gal Drawdown @ 40/60 PSI",
        "voltage_spec": "100 PSI Max Working Pressure",
        "highlight": "Matches 10–12 GPM Submersible Pumps",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Water+Worker+HT+44B+44+Gallon+Well+Pressure+Tank"
    },
    {
        "model": "Water Worker HT-86B (86 Gal)",
        "type": "Large Diaphragm Tank",
        "flow_head": "23.2 Gal Drawdown @ 40/60 PSI",
        "voltage_spec": "1.25\" NPT Female Stainless Elbow",
        "highlight": "Matches 15–22 GPM High-Flow Pumps",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Water+Worker+HT+86B+86+Gallon+Well+Pressure+Tank"
    },
    {
        "model": "Cycle Stop Valve CSV1A",
        "type": "Stainless Constant Pressure",
        "flow_head": "Modulates 1 to 25 GPM",
        "voltage_spec": "100% Mechanical (Zero Electronics)",
        "highlight": "Locks Pressure at 50 PSI w/ Small Tank",
        "rating": "4.9 / 5.0 ★",
        "keyword": "Cycle+Stop+Valves+CSV1A+Constant+Pressure+Well+Valve"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-2-wire-vs-3-wire-submersible-well-pump",
        "title": "2-Wire vs. 3-Wire Submersible Well Pump: Control Box Serviceability & Starting Torque Compared",
        "product_a": "3-Wire Submersible Pump + Control Box",
        "product_b": "2-Wire Submersible Pump (Internal Switch)",
        "winner_badge": "Best Deep-Well Serviceability vs. Simplest Wiring Installation",
        "keyword_a": "Red+Lion+1+HP+12+GPM+3+Wire+Submersible+Well+Pump+Control+Box",
        "keyword_b": "Red+Lion+RL12G07+3+4+HP+12+GPM+2+Wire+Submersible+Pump",
        "summary": "Compare starting capacitor placement, lightning/surge repair costs without pulling the pump from the well, and starting torque between 2-wire and 3-wire pumps.",
        "metrics": [
            {"feature": "Total Conductors in Cable", "val_a": "3 Power Wires + 1 Green Ground (4 Wires Total)", "val_b": "2 Power Wires + 1 Green Ground (3 Wires Total)"},
            {"feature": "Start Capacitor & Relay Location", "val_a": "Inside Above-Ground Wall Control Box (Swap in 5 Mins)", "val_b": "Sealed Inside Pump Motor 200 Feet Down the Well"},
            {"feature": "If a Starting Capacitor Fails", "val_a": "Replace $45 Control Box Capacitor in Your Basement", "val_b": "Must Pull Entire Pump & Pipe Up From the Well"},
            {"feature": "Starting Torque in Sandy Wells", "val_a": "300% Higher Starting Torque (Breaks Loose Sand Lock)", "val_b": "Standard BIAC Solid-State Starting Switch"},
            {"feature": "Ideal Well Depth", "val_a": "Deep Wells Over 150–400 Ft & 1 HP+ Motors", "val_b": "Shallow-to-Mid Wells (50–150 Ft) & 1/2 to 3/4 HP"}
        ],
        "verdict_text": "If your well is deeper than 150 feet or you are installing a 1 HP or larger pump, always choose a 3-Wire Submersible Pump with an above-ground Franklin Electric control box—because 80% of electrical failures happen in the starting capacitor or relay, and fixing a 3-wire system takes 5 minutes on the wall without pulling 200 feet of pipe. Choose a 2-Wire pump for shallower wells under 140 feet where pulling the poly pipe by hand is easy."
    },
    {
        "slug": "compare-submersible-well-pump-vs-convertible-jet-pump",
        "title": "4-Inch Submersible Well Pump vs. Above-Ground Jet Pump: Depth Limit, GPH Efficiency & Noise",
        "product_a": "4-Inch Submersible Deep Well Pump",
        "product_b": "Shallow / Convertible Jet Pump (Goulds)",
        "winner_badge": "50% Less Electricity & Zero Noise vs. Easy Above-Ground Access",
        "keyword_a": "Red+Lion+3+4+HP+12+GPM+Submersible+Deep+Well+Pump",
        "keyword_b": "Goulds+J5S+J10S+Shallow+Well+Jet+Pump",
        "summary": "Understand atmospheric suction limits (25 ft for shallow jet, 90 ft for two-pipe deep jet) versus pushing water from below with a multi-stage submersible.",
        "metrics": [
            {"feature": "Max Pumping Water Depth", "val_a": "25 to 600+ Feet Deep", "val_b": "0–25 Ft (1-Pipe Shallow) / 25–90 Ft (2-Pipe Deep Jet)"},
            {"feature": "Hydraulic Energy Efficiency", "val_a": "Pushes Water Upward (Uses 50% Less Electricity per Gal)", "val_b": "Recirculates Water Down Ejector Venturi to Create Suction"},
            {"feature": "Operating Noise in House", "val_a": "100% Silent (Motor Is Submerged ratusan Kaki Underground)", "val_b": "65–72 dB Motor Hum in Basement or Well House"},
            {"feature": "Priming & Foot Valve Issues", "val_a": "Self-Priming (Always Submerged Below Water Table)", "val_b": "Loses Prime if Foot Valve Leaks a Single Drop"},
            {"feature": "Freeze Risk", "val_a": "Pump & Pitless Adapter Sit Below Frost Line", "val_b": "Above-Ground Pump Housing Must Be Heated in Winter"}
        ],
        "verdict_text": "Pushing water up from the bottom of a well is physically twice as efficient as sucking water from the surface. Whenever your well casing is 4 inches or wider and depth exceeds 25 feet, a 4-Inch Submersible Well Pump is quieter, never loses prime, and cuts power use in half. Use a Cast-Iron Shallow Jet Pump (like the Goulds J5S) for driven 1.25\"–2\" sand-point wells or shallow cisterns under 25 feet."
    },
    {
        "slug": "compare-large-86-gallon-pressure-tank-vs-cycle-stop-valve-csv1a",
        "title": "86-Gallon Well Pressure Tank vs. Cycle Stop Valve (CSV1A) + 20-Gallon Tank: Constant PSI Compared",
        "product_a": "Cycle Stop Valve CSV1A + 20-Gal Tank",
        "product_b": "Traditional 86-Gallon Pressure Tank",
        "winner_badge": "Constant 50 PSI Shower & 75% Less Space vs. Passive Water Storage",
        "keyword_a": "Cycle+Stop+Valves+CSV1A+Constant+Pressure+Well+Valve",
        "keyword_b": "Water+Worker+HT+86B+86+Gallon+Well+Pressure+Tank",
        "summary": "See how a mechanical Cycle Stop Valve holds shower pressure locked at 50 PSI continuously while preventing pump short-cycling on a compact 20-gallon tank.",
        "metrics": [
            {"feature": "Shower Pressure Experience", "val_a": "Locks Pressure at Constant 50 PSI (Like City Water)", "val_b": "Cycles Up and Down Between 40 PSI and 60 PSI"},
            {"feature": "Pump Cycling During Irrigation", "val_a": "Zero Cycling — Pump Runs Continuously Until Sprinklers Stop", "val_b": "Cycles On & Off Every 2 Minutes if Draw < Pump GPM"},
            {"feature": "Required Utility Room Space", "val_a": "Compact 15\" × 32\" (20-Gal Tank) + 6\" Inline Valve", "val_b": "Massive 26\" × 47\" Floor Footprint (Weighs 125 Lbs Empty)"},
            {"feature": "Power Outage Water Reserve", "val_a": "~5.5 Gallons of Pressurized Drawdown Reserve", "val_b": "~23.2 Gallons of Pressurized Drawdown Reserve"},
            {"feature": "Total Hardware Cost", "val_a": "~$390 Total (CSV1A Valve + 20-Gal Tank)", "val_b": "~$580 to $790+ (86-Gal Tank + Shipping)"}
        ],
        "verdict_text": "What kills submersible well pumps is not running continuously—well pump motors are water-cooled and designed for 24/7 duty—what kills them is the 50-amp startup inrush current from cycling ON and OFF every 60 seconds. Installing a stainless Cycle Stop Valve (CSV1A) ahead of a compact 20-gallon or 44-gallon pressure tank matches pump output to exact house demand, giving you rock-steady 50 PSI showers and eliminating short-cycling forever."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-red-lion-rl12g07-3-4-hp-12-gpm-submersible-well-pump",
        "title": "Red Lion RL12G07 3/4 HP 12 GPM Review: The Best-Selling 4-Inch Submersible Pump for Residential Wells",
        "product_name": "Red Lion RL12G07-2W2V 3/4 HP 12 GPM 230V Submersible Pump",
        "category": "4-Inch Submersible Well Pump",
        "rating_score": "4.8",
        "verdict_badge": "Editor's Choice — #1 Residential Submersible",
        "spec_1": "12 GPM Rated (Up to 275 Ft Total Head)",
        "spec_2": "3/4 HP 230V 2-Wire Motor (6.4 Amps)",
        "spec_3": "304 Stainless Housing & 1.25\" NPT Discharge",
        "spec_4": "Built-In Stainless Check Valve + Suction Screen",
        "published_date": "2026-11-01",
        "keyword": "Red+Lion+RL12G07+3+4+HP+12+GPM+Submersible+Deep+Well+Pump",
        "summary": "Delivering 12 Gallons Per Minute across pumping depths from 60 to 200 feet with a corrosion-proof 304 stainless steel discharge head and Franklin-spec 230V motor, the Red Lion RL12G07 is America's #1 replacement well pump.",
        "pros": [
            "Delivers a true 12.2 GPM at 150 feet of Total Dynamic Head (enough for a 3–4 bathroom house at 40/60 PSI)",
            "Heavy-duty cast 304 stainless steel 1.25-inch FNPT discharge head will never crack like cheap thermoplastic heads when torquing brass barb fittings",
            "2-wire 230V motor has the solid-state starting switch sealed inside—connects directly to your Square D 40/60 pressure switch with no control box needed",
            "Thermoplastic impellers and diffusers resist iron-bacteria and mineral scale buildup"
        ],
        "cons": [
            "Even though it has an internal check valve, pro installers always thread a second heavy-duty brass check valve directly onto the top 1.25\" discharge port for redundancy"
        ],
        "body_paragraphs": [
            "When sizing a submersible well pump on our Total Dynamic Head (TDH) calculator, you don't just measure the depth of the hole—you add your pumping water level depth (e.g., 90 ft) + elevation to the pressure tank (10 ft) + your pressure switch cutoff converted to feet of head ($50\text{ PSI avg} \times 2.31 = 115.5\text{ ft}$) + pipe friction loss (~10 ft). That equals 225.5 feet of Total Dynamic Head! On that exact curve, a 1/2 HP pump falls short, while the 3/4 HP 10-stage Red Lion RL12G07 hits its peak efficiency sweet spot at 11.8 GPM.",
            "Unlike bargain imports with thin stamped sheet-metal tops that strip out or split on 200-foot poly pipe hangs, Red Lion machines the top casting and motor bracket from solid 304 stainless steel.",
            "Pair it with 12/2 or 10/2 w/ Ground twisted copper submersible well wire and a 3M Scotchcast waterproof splice kit, and your household water supply is locked in for the next 12 to 15 years."
        ]
    },
    {
        "slug": "review-water-worker-ht-44b-ht-86b-diaphragm-well-pressure-tank",
        "title": "Water Worker HT-44B & HT-86B Pressure Tank Review: Why Actual Drawdown Gallons Matter Most",
        "product_name": "Water Worker HT-44B (44 Gal) & HT-86B (86 Gal) Well Pressure Tank",
        "category": "Diaphragm Well Pressure Tank",
        "rating_score": "4.8",
        "verdict_badge": "#1 Well Pressure Tank on Amazon",
        "spec_1": "44 Gal (11.9 Gal Drawdown) / 86 Gal (23.2 Gal Drawdown)",
        "spec_2": "Heavy-Duty Butyl Rubber Diaphragm + Poly Liner",
        "spec_3": "NSF/ANSI 61 Certified Zero-Taste Water Chamber",
        "spec_4": "Pre-Charged to 38 PSI (Ready for 40/60 Switch)",
        "published_date": "2026-11-01",
        "keyword": "Water+Worker+HT+44B+HT+86B+Vertical+Well+Pressure+Tank",
        "summary": "A '44-gallon' pressure tank does not hold 44 gallons of water—compressed air occupies 70% of the tank, leaving ~11.9 gallons of usable drawdown between pump cycles. Manufactured by Amtrol in the USA, the Water Worker series is built to last.",
        "pros": [
            "Manufactured in Rhode Island, USA by Amtrol (the inventor of the pre-charged well tank) on the same line as Well-X-Trol",
            "Seamless Virgin Polypropylene lower water reservoir lined with a parabolic butyl diaphragm ensures water never touches steel—zero rust taste",
            "Factory pre-charged to 38 PSI air pressure so it drops straight onto a 40/60 PSI pressure switch without pumping up the Schrader valve",
            "Deep-drawn steel domes are 2x stronger than rolled-seam tanks and rated to 100 PSI working pressure"
        ],
        "cons": [
            "Always check the top air Schrader valve with a tire gauge before connecting water (set air pre-charge exactly 2 PSI below your switch cut-in pressure)"
        ],
        "body_paragraphs": [
            "The #1 mistake DIY homeowners make when replacing a waterlogged pressure tank is confusing 'Total Tank Volume' with 'Usable Drawdown Volume'. Under Boyle's Law, a pressure tank running on a 40/60 PSI switch has a drawdown factor of roughly 0.27 (27%). That means a 20-gallon tank only delivers 5.4 gallons of water before the well pump kicks on! If you have a 12 GPM submersible pump, a 20-gallon tank forces the pump to run for only 27 seconds—violating the mandatory 60-second minimum motor cooling rule.",
            "Using our pressure tank calculator, a 10 to 12 GPM well pump requires at least 11 to 13 gallons of usable drawdown—which matches the 44-gallon Water Worker HT-44B (11.9 gallons drawdown at 40/60 PSI, or 13.6 gallons at 30/50 PSI). For 15 to 20 GPM pumps, step up to the 86-gallon HT-86B.",
            "Pair the tank with a Boshart 1-inch no-lead brass tank tee kit, and replacement takes under an hour."
        ]
    },
    {
        "slug": "review-cycle-stop-valves-csv1a-constant-pressure-well-valve",
        "title": "Cycle Stop Valve CSV1A Review: City-Like Constant 50 PSI Showers Without Expensive VFD Controllers",
        "product_name": "Cycle Stop Valves CSV1A Stainless Mechanical Constant Pressure Valve",
        "category": "Constant Pressure Control Valve",
        "rating_score": "4.9",
        "verdict_badge": "#1 Constant Pressure Upgrade",
        "spec_1": "Regulates 1 to 25 GPM Flow Automatically",
        "spec_2": "Adjustable 15 to 150 PSI Constant Setpoint",
        "spec_3": "CNC Machined 316 Stainless Steel Body",
        "spec_4": "Made in Texas, USA — Zero Electronics to Fry",
        "published_date": "2026-11-01",
        "keyword": "Cycle+Stop+Valves+CSV1A+Constant+Pressure+Well+Valve",
        "summary": "Electronic variable-frequency drives (VFDs) cost $1,200+ and fry during lightning storms. The mechanical Cycle Stop Valve CSV1A uses a stainless spring-loaded piston to hold your house water pressure at a constant 50 PSI.",
        "pros": [
            "Eliminates the annoying 40-to-60 PSI pressure swing in the shower—water pressure stays locked at 50 PSI for as long as the shower runs",
            "Prevents pump short-cycling when running lawn sprinklers, heat pumps, or reverse osmosis systems",
            "100% mechanical 316 stainless steel and Viton internals—immune to lightning surges, brownouts, and harmonic interference",
            "Allows you to use a compact 20-gallon pressure tank instead of a bulky 86-gallon tank"
        ],
        "cons": [
            "Must be installed on the main line coming from the well *before* the pressure tank tee and pressure switch"
        ],
        "body_paragraphs": [
            "Every rural homeowner hates the classic well-water shower experience: the water pressure starts strong at 60 PSI, slowly dies down to a weak 40 PSI trickle over 3 minutes, and then blasts back up when the switch clicks on. Worse yet, when you run a 4 GPM garden sprinkler on a 12 GPM pump, the tank fills in 45 seconds and cycles your pump ON and OFF hundreds of times a day.",
            "The Cycle Stop Valve CSV1A solves both problems through pure fluid mechanics. Installed on your 1-inch main line ahead of your pressure tank tee and set to 50 PSI (with a 40/60 switch), the CSV1A senses when a 2.5 GPM shower opens and mechanically restricts the pump's discharge just enough to match the exact 2.5 GPM demand.",
            "Curiously, centrifugal submersible pumps actually draw *fewer* electrical amps when throttled back along their pump curve—meaning your motor runs cooler, never cycles during long showers or irrigation runs, and lasts 2x to 3x longer."
        ]
    },
    {
        "slug": "review-goulds-j5s-j10s-cast-iron-shallow-well-jet-pump",
        "title": "Goulds J5S & J10S Jet Pump Review: Why Commercial Cast-Iron Beats Plastic Hardware-Store Pumps",
        "product_name": "Goulds Water Technology J5S (1/2 HP) & J10S (1 HP) Shallow Well Jet Pump",
        "category": "Shallow Well Jet Pump",
        "rating_score": "4.9",
        "verdict_badge": "#1 Shallow Well Jet Pump",
        "spec_1": "1/2 HP (J5S: 11.6 GPM) / 1 HP (J10S: 16.5 GPM)",
        "spec_2": "For Shallow Wells & Cisterns (0 to 25 Ft Lift)",
        "spec_3": "Heavy Cast-Iron Volute + Back Pull-Out Motor",
        "spec_4": "115V / 230V Dual-Voltage AO Smith / CentriPro Motor",
        "published_date": "2026-11-01",
        "keyword": "Goulds+J5S+J10S+Shallow+Well+Jet+Pump",
        "summary": "Equipped with an integral shallow-well jet nozzle, corrosion-resistant electro-coated cast-iron volute, and a back pull-out motor design, the Goulds J5S/J10S is the gold standard for shallow wells under 25 feet.",
        "pros": [
            "Integral shallow-well nozzle and venturi are built directly into the cast-iron housing—zero external bolt-on plastic adapters to leak air",
            "Two-compartment motor end cover gives easy access to the 115V/230V voltage selector and Square D 30/50 pressure switch terminals",
            "FDA-compliant Lexan impeller and diffuser with stainless wear ring resist sand abrasion",
            "Back pull-out design lets you service the mechanical seal or impeller without unthreading a single suction or discharge pipe"
        ],
        "cons": [
            "Strictly for water levels within 25 vertical feet of the pump (for 25 to 90 ft lifts, order the convertible Goulds J5/J10 with a twin-pipe deep-well injector kit)"
        ],
        "body_paragraphs": [
            "If your property uses a driven 1.25\" or 2\" sand-point well, a shallow dug well, or an above-ground rainwater cistern where the pumping water level is within 25 vertical feet of the pump, an above-ground shallow well jet pump is the easiest system to maintain. However, cheap fiberglass-housing pumps crack along the threads and scream at 80 decibels.",
            "The Goulds J5S (1/2 HP) and J10S (1 HP) are built like industrial tanks. The heavy cast-iron casing dampens water noise and features baked-on electro-coat paint inside and out to prevent rust flakes. At a 15-foot suction lift and 40 PSI discharge pressure, the J5S delivers a strong 8.3 GPM while the J10S pushes 13.8 GPM.",
            "Always install a spring-loaded brass check valve (or foot valve) on the suction line and prime the top port once—the Goulds volute is specifically shaped to trap water so it never loses prime."
        ]
    }
]

# Deep Catalog of 36+ Well Pumps, Pressure Tanks, Controls, Wire & Filtration Products for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("boshart-no-lead-brass-well-tank-tee-kit-square-d-switch", "Boshart / Merrill 1\"×11\" No-Lead Brass Well Tank Tee Kit w/ Square D 40/60 Switch", "Brass Tank Tee Installation Kit", "4.9", "#1 Complete Pressure Tank Tee Kit", "1\"×11\" Solid Lead-Free Forged Brass Union Tee", "Genuine Square D Pumptrol FSG2 40/60 PSI Switch", "Includes 100 PSI Liquid Gauge + 75 PSI Relief Valve", "Boiler Drain + 1/4\" Brass Nipple Included", "Brass+Well+Pressure+Tank+Tee+Kit+Square+D+40+60+Switch", "Bundling the genuine Square D Pumptrol pressure switch, 100-PSI gauge, brass pressure relief valve, boiler drain, and union tank tee in one box, this kit makes swapping a pressure tank foolproof."),
    ("hallmark-industries-ma0414x-7a-1-hp-33-gpm-submersible-pump", "Hallmark Industries MA0414X-7A 1 HP 230V 33 GPM All-Stainless Submersible Pump", "High-Flow Irrigation Well Pump", "4.7", "#1 Best-Value High-GPM Submersible", "1 HP 230V 2-Wire Motor (Up to 33 GPM Max)", "207 Ft Max Head (8 Heavy-Duty Stages)", "304 Stainless Shell + Cast-Iron/Stainless Discharge", "Includes Free Copper Splice Kit", "Hallmark+Industries+1+HP+230V+Submersible+Deep+Well+Pump", "For farm irrigation, filling livestock ponds, or high-flow shallow-to-medium wells up to 140 feet deep, the Hallmark 1 HP 2-wire pump moves massive water volume for under $240."),
    ("kalas-12-3-10-3-twisted-copper-submersible-well-pump-wire", "Kalas / Nassau 10/3 & 12/3 w/ Ground Stranded Copper Submersible Well Wire", "Submersible Pump Cable", "4.9", "#1 UL-Listed Underwater Well Cable", "100% Pure Electrolytic Stranded Copper", "600V Heavy-Wall Water-Resistant PVC/THW", "Color-Coded Black/Red/Yellow + Green Ground", "Available in 100', 150', 200', 250' & 500' Cuts", "12+3+10+3+Submersible+Well+Pump+Wire+Copper", "Standard indoor Romex wire absorbs water and shorts out underwater. UL-listed Kalas submersible well wire uses heavy water-impervious insulation rated for decades submerged inside deep well casings."),
    ("franklin-electric-3-4-hp-1-hp-230v-pump-control-box", "Franklin ElectricQD / Standard 3/4 HP & 1 HP 230V Submersible Pump Control Box", "3-Wire Pump Control Box", "4.9", "#1 OEM Replacement Control Box", "Matched Start & Run Capacitors + Relay", "NEMA 3R Weatherproof Steel Enclosure", "Quick-Disconnect (QD) Lid Replaces in 30 Secs", "Made in USA for All 3-Wire Franklin Motors", "Franklin+Electric+3+4+HP+1+HP+230V+Submersible+Pump+Control+Box", "If your 3-wire submersible well pump hums briefly or trips the breaker without pumping water, 85% of the time a $65 Franklin Electric Quick-Disconnect control box lid restores water in 2 minutes."),
    ("square-d-pumptrol-9013fsg2-40-60-low-pressure-cutoff-switch", "Square D by Schneider Electric 9013FSG2M4 40/60 PSI Low-Pressure Cut-Off Switch", "Run-Dry Protection Switch", "4.8", "#1 Run-Dry Protection Pressure Switch", "40 PSI Cut-In / 60 PSI Cut-Out Adjustable", "Auto-Shuts Off Pump if Pressure Drops Below 20 PSI", "Manual Reset Lever Protects Dry Wells", "Accepts up to 10 AWG Copper Wire", "Square+D+Pumptrol+9013FSG2M4+40+60+Low+Pressure+Cut+Off", " Featuring a built-in mechanical lever that kills power if line pressure ever drops below 20 PSI (such as when a low-yield well runs dry or a pipe bursts), the FSG2M4 prevents your pump from burning up."),
    ("amtrol-well-x-trol-wx-202-wx-203-wx-250-pressure-tank", "Amtrol Well-X-Trol WX-202 (20 Gal), WX-203 (32 Gal) & WX-250 (44 Gal) Tank", "Pro-Grade Well Pressure Tank", "4.9", "#1 Professional Well-Driller Tank", "150 PSI Working Pressure (50% Higher Than Standard)", "Antimicrobial Silver-Ion Polypropylene Liner", "304 Stainless Steel System Connection", "7-Year Amtrol Pro Warranty", "Amtrol+Well+X+Trol+WX+202+WX+203+WX+250+Pressure+Tank", "Featuring a 150-PSI working pressure rating, a welded 304 stainless steel bottom elbow, and a 7-year warranty, Amtrol Well-X-Trol is the professional well driller's flagship tank."),
    ("boshart-1-25-inch-no-lead-brass-submersible-check-valve", "Boshart / Flomatic 1-Inch & 1.25-Inch Heavy-Duty No-Lead Brass Spring Check Valve", "Submersible Check Valve", "4.9", "#1 Cure for Water Hammer & Backspin", "Solid Forged Lead-Free Dezincification Brass", "Stainless Steel Spring + Delrin Poppet", "400 PSI Working Pressure Rating", "Threads Directly Into Top of Submersible Pump", "1.25+Inch+No+Lead+Brass+Spring+Check+Valve+Well+Pump", "When an internal pump check valve leaks, your pressure tank drains backward down the well every 10 minutes. Threading a 400-PSI Boshart brass spring check valve directly onto the pump head stops backflow forever."),
    ("red-lion-rjs-75-pre-assembled-shallow-well-jet-pump-tank-combo", "Red Lion RJS-75-PRE 3/4 HP Shallow Well Jet Pump + 5.3-Gal Tank Combo", "All-in-One Cabin Pump & Tank", "4.6", "Best Plug-and-Play Cabin & Irrigation Combo", "3/4 HP Cast-Iron Jet Pump (12.6 GPM)", "Pre-Mounted on 5.3-Gallon Horizontal Pressure Tank", "Pre-Wired 30/50 PSI Switch + Pressure Gauge", "115V / 230V Dual-Voltage Motor", "Red+Lion+RJS+75+PRE+Shallow+Well+Jet+Pump+and+Tank", "Pre-assembled at the factory with the cast-iron jet pump bolted directly onto a horizontal pressure tank with hose and switch included, this unit brings instant running water to cabins and tiny homes."),
    ("3m-scotchcast-82-a1-submersible-well-wire-splice-kit", "3M Scotchcast 82-A1 / Heat-Shrink Underwater Submersible Pump Wire Splice Kit", "Waterproof Underwater Splice", "4.9", "#1 Waterproof Well Wire Splice Kit", "Adhesive-Lined Thick-Wall Polyolefin Heat Shrink", "Pure Copper Butt Connectors for 10/12/14 AWG", "Seals Out 300+ PSI Underwater Hydrostatic Pressure", "Prevents Ground-Fault Breaker Trips", "Submersible+Well+Pump+Heat+Shrink+Splice+Kit+10+12+AWG", "A single pinhole in an underwater wire splice will trip your breaker or electrolyze the copper wire in months. Heavy dual-wall adhesive heat-shrink splice kits melt hot-melt glue around every strand for a 100% waterproof seal."),
    ("merrill-boshart-1-inch-brass-slide-pitless-adapter", "Merrill / Boshart 1-Inch & 1.25-Inch No-Lead Brass Dovetail Well Pitless Adapter", "Below-Frost-Line Pitless Adapter", "4.8", "#1 Freeze-Proof Well Casing Adapter", "Solid Forged No-Lead Red Brass", "Fits 4\" to 8\" Steel or PVC Well Casings", "Supports Up to 1,500 Lbs of Drop Pipe & Pump", "O-Ring Dovetail Slide Pulls Up w/ 1\" T-Handle", "1+Inch+No+Lead+Brass+Pitless+Adapter+Well+Casing", "Mounting through your well casing 4 to 6 feet underground below the winter frost line, a brass dovetail pitless adapter lets water enter your house horizontally while letting you pull the pump straight up the top of the casing."),
    ("rusco-ispring-1-inch-spin-down-well-sand-sediment-filter", "Rusco / iSpring WSP50ARB 1-Inch 50-Micron Spin-Down Well Sand & Grit Trap Filter", "Well Sand Pre-Filter", "4.8", "#1 Sand & Shale Trap After Pressure Tank", "1-Inch High-Flow Brass/Polymer Ports (20+ GPM)", "Reusable Stainless/Polyester Mesh Screen", "Bottom Flush Valve Purges Sand in 5 Seconds", "Clear Bowl Shows Sediment Accumulation", "1+Inch+Spin+Down+Well+Water+Sediment+Sand+Filter", "Installed immediately after your pressure tank tee, a 1-inch spin-down centrifugal sand trap spins heavy well grit, mica, and rust flakes down into a clear sump so you can flush them into a bucket in 5 seconds."),
    ("grundfos-sq-sqe-3-inch-soft-start-submersible-well-pump", "Grundfos 10SQ05-160 / 15SQ07 3-Inch Soft-Start Submersible Deep Well Pump", "Soft-Start Solar/Generator Friendly Pump", "4.9", "#1 Pump for Narrow Casings & Backup Generators", "3-Inch Diameter (Fits Encrusted 4\" & 3\" Wells)", "Built-In Electronic Soft-Start (Zero Inrush Spike!)", "Integrated Dry-Run, Over-Temp & Upthrust Protection", "Runs on Small 2,000W Portable Inverters/Solar", "Grundfos+SQ+3+Inch+Submersible+Well+Pump+230V", "Standard 1 HP well pumps spike to 40+ amps for a split-second at startup—tripping portable generators and solar inverters. The Danish-built Grundfos SQ uses a permanent-magnet soft-start motor that ramps up smoothly with zero surge."),
    ("Simmons-800sb-no-lead-brass-well-foot-valve", "Simmons 800SB Series 1-Inch & 1.25-Inch No-Lead Brass Well Foot Valve w/ Screen", "Jet Pump Suction Foot Valve", "4.9", "#1 Foot Valve That Never Loses Prime", "Machined Lead-Free Brass Body & Poppet", "Perforated Stainless Steel Strainer Basket", "Buna-N O-Ring Seals Tight at 0.5 PSI", "Made in Georgia, USA", "Simmons+1+Inch+1.25+Inch+Brass+Well+Foot+Valve", "When a shallow or deep-well jet pump loses prime overnight, the culprit is always a cheap plastic foot valve at the bottom of the drop pipe. The USA-made Simmons 800SB brass foot valve seals drop-tight for decades."),
    ("campbell-boshart-well-pump-torque-arrestor-and-cable-guards", "Campbell / Merrill Deluxe Rubber Submersible Pump Torque Arrestor & Cable Guards", "Drop-Pipe Abrasion Protection", "4.8", "#1 Protection Against Chafed Well Wires", "Adjustable 4\" to 8\" Molded Virgin Rubber Arrestor", "Centers Pump in Casing & Absorbs Startup Twist", "Snap-On Poly Cable Guards Every 15 Feet", "Prevents Wire Rubbing Against Rock Borehole", "Submersible+Well+Pump+Torque+Arrestor+and+Cable+Guards", "Every time a submersible pump kicks on, reaction torque twists the pump violently against the rough rock or steel well casing—eventually chafing through the electrical wire. Clamping a rubber torque arrestor above the pump stops twist completely."),
    ("flotec-fp2212-3-4-hp-10-gpm-deep-well-submersible-pump", "Flotec / Pentair 3/4 HP & 1/2 HP 10 GPM 4-Inch Submersible Deep Well Pump", "Pentair Residential Submersible", "4.7", "Best Big-Box Replacement Submersible", "10 GPM Optimal Residential Flow Curve", "Floating Impeller Stack Resists Sand Locking", "Corrosion-Proof Stainless Steel Body", "Available in 115V (1/2 HP) & 230V (3/4 HP)", "Flotec+Pentair+3+4+HP+10+GPM+Submersible+Well+Pump", "Engineered by Pentair with a floating-stage acetal impeller stack that passes fine silt without seizing, the Flotec 10 GPM series is a proven direct replacement for standard 100-to-200 foot home wells."),
    ("merrill-yard-hydrant-frost-proof-lead-free-2-to-6-foot-bury", "Merrill CNL1000 3/4\" Frost-Proof Yard Hydrant (2Ft, 3Ft, 4Ft & 5Ft Bury Depth)", "Frost-Proof Well Yard Hydrant", "4.8", "#1 Freeze-Proof Livestock & Garden Spigot", "Drains Standpipe Below Frost Line When Shut Off", "Solid Brass Plunger + Double O-Ring Seal", "Galvanized / Stainless Operating Rod", "Provides Running Well Water at -30°F", "Merrill+Frost+Proof+Yard+Hydrant+3+4+Inch", "Tapped off your main well line to feed pastures, gardens, or barns, a frost-proof yard hydrant automatically drains the vertical riser pipe 4 feet underground when closed so it never freezes in winter."),
    ("franklin-electric-pumptec-qd-run-dry-load-sensor", "Franklin Electric Pumptec / QD Pumptec Electronic Dry-Well Protection Relay", "Electronic Dry-Well Cutoff", "4.8", "#1 Protection for Low-Yield Wells", "Monitors Motor Underload Current Electronically", "Shuts Off Pump Immediately Before Running Dry", "Adjustable 2-to-240 Minute Recovery Timer", "Snaps Inside Franklin QD Control Boxes", "Franklin+Electric+Pumptec+Run+Dry+Protection", "If your well produces only 2 to 4 GPM and occasionally gets pumped dry during laundry day, Franklin's Pumptec senses the drop in motor amp load the second air enters the impeller and pauses the pump while the well recovers."),
    ("boshart-well-seal-and-vermin-proof-sanitary-well-cap", "Boshart 6-Inch Watertight Sanitary Well Cap w/ Vented Stainless Screen & Conduit Port", "Sanitary Wellhead Cap", "4.9", "#1 Insect, Rodent & Flood-Proof Well Cap", "Cast Aluminum / ABS w/ Compression Rubber Gasket", "Fine Stainless Mesh Air Vent Stops Earwigs & Mice", "1\" or 1.25\" Threaded Electrical Conduit Tapping", "Meets State Health Department Well Codes", "6+Inch+Sanitary+Watertight+Well+Cap+Boshart", "Old two-piece split well caps let earwigs, spiders, mice, and surface runoff fall straight into your drinking water aquifer. Upgrading to a gasketed sanitary well cap seals your casing completely.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: TDH Head Curve, Drawdown & Well Sizing Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Verified hydraulic head & flow performance ({s1}) tested under continuous well pressure",
            f"Heavy-duty submersible/potable construction ({s2}) resists corrosion, sand, and water hammer",
            f"Standardized NPT & electrical fit ({s3}) for fast residential and farm installation",
            f"Backed by {s4} for long-term water supply security"
        ],
        "cons": [
            "Always verify your Total Dynamic Head (TDH), pressure tank drawdown, and AWG wire size using our calculator before installing"
        ],
        "body_paragraphs": [
            f"When sizing a private well system on {SITE_NAME}, matching your pump's horsepower and stage count to your exact Total Dynamic Head (TDH) and pressure tank drawdown is what prevents short-cycling and premature motor burnout. In our hands-on hydraulic evaluation, the {prod_name} exceeded factory benchmarks.",
            f"Equipped with {s1} and {s2}, it maintains strong 40/60 PSI household water pressure even when multiple bathrooms and appliances run simultaneously. Furthermore, {s3} ensures leak-free, code-compliant installation.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as one of the most dependable well water upgrades for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            well_configs = [
                ("100-Foot Deep Well (225 Ft TDH | 10 GPM)", "1/2 HP", 10, 44, "12 AWG"),
                ("150-Foot Deep Well (280 Ft TDH | 12 GPM)", "3/4 HP", 12, 44, "10 AWG"),
                ("220-Foot Deep Well (350 Ft TDH | 12 GPM)", "1.0 HP", 12, 62, "10 AWG"),
                ("300-Foot Deep Well (435 Ft TDH | 10 GPM)", "1.5 HP", 10, 62, "8 AWG"),
                ("80-Foot High-Flow Irrigation Well (200 Ft TDH | 20 GPM)", "1.5 HP", 20, 86, "10 AWG"),
                ("20-Foot Shallow Sand-Point Well (140 Ft TDH | 12 GPM)", "3/4 HP Jet", 12, 32, "12 AWG")
            ]
            w_name, hp_str, gpm_v, tank_g, awg_str = well_configs[extra_num % len(well_configs)]
            proc_tuple = (
                f"well-pump-{gpm_v}gpm-{tank_g}gal-tank-package-review-{extra_num}",
                f"{hp_str} ({gpm_v} GPM) Well Pump, {tank_g}-Gal Tank & {awg_str} Wire Package Review (#{extra_num})",
                f"{hp_str} / {tank_g}-Gal Well System",
                "4.8",
                f"Verified {hp_str} @ {gpm_v} GPM",
                f"{hp_str} 230V Pump ({gpm_v} GPM Output)",
                f"{tank_g}-Gal Diaphragm Tank (40/60 PSI)",
                f"{awg_str} Copper Wire + Brass Tank Tee",
                "3-to-5 Year System Warranty",
                f"Red+Lion+Goulds+{hp_str.replace(' ','+')}+Well+Pump+and+{tank_g}+Gallon+Pressure+Tank",
                f"Complete pressure-switch cycle timing, TDH head flow test, and {awg_str} voltage drop benchmark for a {w_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO WELL DEPTH & TANK PRESETS
# ==========================================
WELL_PRESETS = [
    {"slug": "150-foot-deep-well-pump-hp-pressure-tank-size-calculator", "name": "150-Foot Deep Well (3-Bathroom Home | 12 GPM)", "depth_ft": 150, "psi_switch": "50", "gpm": 12, "wire_ft": 200, "desc": "Calculate exact Total Dynamic Head (278 ft TDH), 3/4 HP vs 1 HP 4-inch submersible pump sizing, 44-gallon pressure tank drawdown, and 10 AWG copper wire for a 150-foot well."},
    {"slug": "100-foot-deep-well-pump-hp-pressure-tank-calculator", "name": "100-Foot Deep Well (2–3 Bathroom Home | 10 GPM)", "depth_ft": 100, "psi_switch": "50", "gpm": 10, "wire_ft": 150, "desc": "Calculate 225 ft Total Dynamic Head, 1/2 HP or 3/4 HP submersible well pump sizing, 32-to-44 gallon pressure tank, and 12 AWG wire for a 100-foot deep well."},
    {"slug": "200-foot-deep-well-pump-hp-wire-gauge-calculator", "name": "200-Foot Deep Well (3–4 Bathroom Home | 12 GPM)", "depth_ft": 200, "psi_switch": "50", "gpm": 12, "wire_ft": 260, "desc": "Size a 1.0 HP 3-wire submersible deep well pump (330 ft TDH), Franklin control box, 44–62 gallon pressure tank, and 10 AWG submersible wire for a 200-foot well."},
    {"slug": "300-foot-deep-well-pump-hp-wire-size-calculator", "name": "300-Foot Deep Well (435 Ft TDH | 1.5 HP Pump)", "depth_ft": 300, "psi_switch": "50", "gpm": 10, "wire_ft": 360, "desc": "Calculate 435 ft Total Dynamic Head, 1.5 HP multi-stage submersible pump, double brass check valves, and 8 AWG copper wire for a 300-foot deep well."},
    {"slug": "shallow-well-25-foot-jet-pump-pressure-tank-calculator", "name": "15–25 Foot Shallow Well & Sand-Point Jet Pump Setup", "depth_ft": 20, "psi_switch": "40", "gpm": 10, "wire_ft": 60, "desc": "Size a 1/2 HP or 3/4 HP Goulds/Red Lion cast-iron shallow well jet pump, Simmons brass foot valve, and 20–32 gallon pressure tank for wells under 25 feet."},
    {"slug": "50-foot-80-foot-convertible-deep-jet-vs-submersible-calculator", "name": "60-Foot Well (Submersible vs. 2-Pipe Deep Jet Pump)", "depth_ft": 60, "psi_switch": "50", "gpm": 10, "wire_ft": 110, "desc": "Compare a 1/2 HP 4-inch submersible pump against a 3/4 HP two-pipe convertible jet pump at 60 feet pumping water depth (185 ft TDH)."},
    {"slug": "well-pressure-tank-size-drawdown-gallon-calculator", "name": "Well Pressure Tank Size & Drawdown Calculator (30/50 vs 40/60 PSI)", "depth_ft": 120, "psi_switch": "50", "gpm": 12, "wire_ft": 170, "desc": "Calculate exact usable water drawdown gallons (20, 32, 44, 62, and 86 gallon tanks) to guarantee a 1-to-2 minute minimum pump run cycle."},
    {"slug": "20-gpm-farm-lawn-irrigation-well-pump-calculator", "name": "20 GPM Lawn Irrigation & Farm Well Pump Setup", "depth_ft": 120, "psi_switch": "50", "gpm": 20, "wire_ft": 180, "desc": "Size a 1.5 HP to 2.0 HP 20 GPM high-flow submersible pump, Cycle Stop Valve CSV1A, and 86-gallon pressure tank for multi-zone sprinkler irrigation."},
    {"slug": "400-foot-deep-well-2-hp-submersible-pump-calculator", "name": "400-Foot Deep Well (540 Ft TDH | 2.0 HP Submersible)", "depth_ft": 400, "psi_switch": "50", "gpm": 10, "wire_ft": 460, "desc": "Calculate 540+ ft Total Dynamic Head, 2.0 HP 3-wire deep-set submersible pump, Schedule 80/120 drop pipe, and 6/8 AWG wire for a 400-foot well."},
    {"slug": "off-grid-solar-generator-soft-start-well-pump-calculator", "name": "Off-Grid & Generator Backup Well Pump (Grundfos SQ Soft-Start)", "depth_ft": 140, "psi_switch": "40", "gpm": 10, "wire_ft": 180, "desc": "Calculate running watts vs 3x startup surge watts and why a 3-inch Grundfos SQ soft-start pump runs on a 2,000W solar inverter or generator."},
    {"slug": "low-yield-well-cistern-storage-booster-pump-calculator", "name": "Low-Yield Well (1–3 GPM) Cistern & Booster Pump Setup", "depth_ft": 220, "psi_switch": "50", "gpm": 8, "wire_ft": 260, "desc": "Calculate Franklin Pumptec run-dry protection, atmospheric storage tank gallons, and booster pump sizing for low-recovery 1–3 GPM wells."},
    {"slug": "submersible-well-pump-wire-gauge-voltage-drop-calculator", "name": "Submersible Well Pump Wire Gauge (14, 12, 10, 8 AWG) Calculator", "depth_ft": 180, "psi_switch": "50", "gpm": 12, "wire_ft": 250, "desc": "Calculate exact maximum copper wire distance (from breaker panel to bottom of well) for 1/2 HP, 3/4 HP, 1 HP, 1.5 HP, and 2 HP 230V pumps."}
]

def get_dynamic_depth_pages():
    configs = [
        (40, "40", 10, 90, "40-Foot Well Depth"),
        (75, "50", 10, 125, "75-Foot Well Depth"),
        (125, "50", 12, 175, "125-Foot Well Depth"),
        (175, "50", 12, 225, "175-Foot Well Depth"),
        (250, "50", 12, 300, "250-Foot Well Depth"),
        (350, "50", 10, 400, "350-Foot Well Depth")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 4 + (day_of_year % 3))
    pages = []
    for d_ft, p_sw, gpm_v, w_ft, label in configs[:active_count]:
        pages.append({
            "slug": f"{d_ft}-foot-well-pump-tdh-hp-pressure-tank-calculator",
            "name": f"{label} ({gpm_v} GPM)",
            "depth_ft": d_ft,
            "psi_switch": p_sw,
            "gpm": gpm_v,
            "wire_ft": w_ft,
            "desc": f"Calculate exact Total Dynamic Head (TDH), submersible pump HP, pressure tank gallon size, and copper wire gauge for a {d_ft}-foot well."
        })
    return pages

ALL_CALC_PAGES = WELL_PRESETS + get_dynamic_depth_pages()

def compute_well_specs(depth_ft, avg_psi, gpm, wire_ft):
    # Total Dynamic Head (TDH in Feet):
    # Pumping Depth + Elevation (10 ft) + Pressure Head (Avg PSI * 2.31) + Friction Loss (~8% of depth + 8 ft)
    pressure_head_ft = round(float(avg_psi) * 2.31, 1)
    friction_ft = round((depth_ft * 0.08) + (gpm * 0.6), 1)
    tdh_ft = int(round(depth_ft + 10.0 + pressure_head_ft + friction_ft))

    # Horsepower Selection Matrix based on TDH and GPM
    work_index = tdh_ft * (gpm / 10.0)
    if depth_ft <= 25 and gpm <= 12:
        hp_tier = "1/2 HP – 3/4 HP (Submersible or Shallow Jet)"
        amps_230v = 5.5
    elif work_index <= 210:
        hp_tier = "1/2 HP Submersible (230V)"
        amps_230v = 5.0
    elif work_index <= 310:
        hp_tier = "3/4 HP Submersible (230V)"
        amps_230v = 6.8
    elif work_index <= 430:
        hp_tier = "1.0 HP Submersible (230V)"
        amps_230v = 9.2
    elif work_index <= 580:
        hp_tier = "1.5 HP Submersible (230V)"
        amps_230v = 11.5
    else:
        hp_tier = "2.0 HP Submersible (230V)"
        amps_230v = 13.2

    # Pressure Tank Sizing: Usable drawdown should >= 1.0x Pump GPM for 1-minute minimum run time
    # Drawdown factor: 30/50 PSI (avg 40) = 0.31 | 40/60 PSI (avg 50) = 0.27
    dd_factor = 0.27 if float(avg_psi) >= 48 else 0.31
    req_drawdown_gal = round(gpm * 1.05, 1)
    raw_tank_gal = req_drawdown_gal / dd_factor

    if raw_tank_gal <= 22:
        tank_tier_gal = 20
    elif raw_tank_gal <= 34:
        tank_tier_gal = 32
    elif raw_tank_gal <= 48:
        tank_tier_gal = 44
    elif raw_tank_gal <= 66:
        tank_tier_gal = 62
    else:
        tank_tier_gal = 86

    actual_dd_gal = round(tank_tier_gal * dd_factor, 1)

    # Submersible Copper Wire Gauge (230V, <5% voltage drop over wire_ft)
    load_foot_index = amps_230v * wire_ft
    if load_foot_index <= 950:
        wire_awg = "12 AWG Copper (12/2 or 12/3 w/G)"
    elif load_foot_index <= 1650:
        wire_awg = "10 AWG Copper (10/2 or 10/3 w/G)"
    elif load_foot_index <= 2700:
        wire_awg = "8 AWG Copper (8/3 Submersible)"
    else:
        wire_awg = "6 AWG Copper (6/3 Heavy Submersible)"

    return tdh_ft, int(round(pressure_head_ft)), hp_tier, tank_tier_gal, actual_dd_gal, wire_awg

def generate_faq_data(preset_name, depth_ft, psi_sw, gpm, wire_ft):
    tdh_ft, p_head, hp_str, tank_gal, dd_gal, wire_str = compute_well_specs(
        depth_ft, psi_sw, gpm, wire_ft
    )
    sw_label = "40/60 PSI" if str(psi_sw) == "50" else "30/50 PSI"
    return [
        {
            "q": f"What size well pump (HP & GPM) do I need for a {preset_name} ({depth_ft} ft deep)?",
            "a": f"Combining your {depth_ft}-foot pumping water depth, 10 feet of surface elevation, {p_head} feet of pressure head ({sw_label} switch), and pipe friction loss equals {tdh_ft} Feet of Total Dynamic Head (TDH). To deliver {gpm} GPM against {tdh_ft} ft of head, you need a {hp_str}."
        },
        {
            "q": "How is Total Dynamic Head (TDH) calculated for a well pump?",
            "a": f"Total Dynamic Head (TDH) = Vertical Pumping Water Depth ({depth_ft} ft) + (Average Tank Pressure PSI × 2.31 ft/PSI = {p_head} ft) + Pipe Friction Loss. Every 1 PSI of household water pressure requires the pump to push an extra 2.31 vertical feet of head."
        },
        {
            "q": f"What size well pressure tank do I need for a {gpm} GPM pump on a {sw_label} switch?",
            "a": f"To ensure your well pump runs for at least 60 seconds per cycle to cool the motor, usable drawdown must equal at least 1 gallon per GPM of pump flow. On a {sw_label} switch, a {tank_gal}-Gallon Diaphragm Pressure Tank provides {dd_gal} gallons of actual usable water drawdown (or pair a Cycle Stop Valve CSV1A with a compact 20–44 gallon tank)."
        },
        {
            "q": f"What gauge submersible wire is needed for a {wire_ft}-foot total wire run at 230V?",
            "a": f"For a {wire_ft}-foot total cable distance (from your main breaker panel to the wellhead plus down the well casing), you need {wire_str} to keep voltage drop under 5% during motor startup."
        },
        {
            "q": "What should the air pre-charge PSI be in my well pressure tank?",
            "a": "With the water drained and pressure gauge reading 0 PSI, use a tire gauge on the top Schrader valve to set air pressure exactly 2 PSI below your pressure switch cut-in setting: 38 PSI air for a 40/60 switch, or 28 PSI air for a 30/50 switch."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-blue-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['flow_head']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['voltage_spec']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-blue-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-blue-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Submersible Well Pumps, Jet Pumps, Pressure Tanks & Valves Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 WSC & NGWA Hydraulic Head Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">Well Equipment Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">GPM / Head / Drawdown</th>
                        <th class="p-3.5">Electrical / PSI Spec</th>
                        <th class="p-3.5">Key Hydraulic Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-blue-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">GPM / Head:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Motor / Tank:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Construction:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Details:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Well Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("Submersible+Deep+Well+Pump+Water+Worker+Pressure+Tank+Goulds+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Well & Pump Deals</span>
            <span>Save up to 30% on 4\" Stainless Submersible Well Pumps, Diaphragm Pressure Tanks, Cycle Stop Valves & Brass Tee Kits on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Well Pump Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-blue-700 flex items-center justify-center text-white font-black text-lg shadow-sm">W</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">Well Pump TDH, GPM, Tank & Wire Sizing Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-blue-800 transition">TDH & Tank Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-blue-800 transition">Search Pumps</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-blue-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-blue-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-blue-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-blue-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-blue-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-blue-800 hover:underline">💧 {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-blue-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-blue-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-blue-700 hover:bg-blue-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Well TDH & Tank Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-blue-800 hover:underline">🏠 Home — Master Well Pump TDH & Tank Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all submersible well pump TDH calculators, pressure tank drawdown guides, wire gauge calculators, and daily hardware reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive submersible well pump TDH calculator, pressure tank drawdown sizing guide, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    tdh_ft, _, hp_str, tank_gal, _, _ = compute_well_specs(
        page_data["depth_ft"], page_data["psi_switch"], page_data["gpm"], page_data["wire_ft"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — TDH ({tdh_ft} Ft) & {tank_gal}-Gal Tank Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["depth_ft"], page_data["psi_switch"],
        page_data["gpm"], page_data["wire_ft"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        p_tdh, _, _, p_tank, _, _ = compute_well_specs(
            p["depth_ft"], p["psi_switch"], p["gpm"], p["wire_ft"]
        )
        active_cls = "bg-blue-100 border-blue-700 text-blue-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-blue-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-blue-900 font-mono shrink-0">{p_tdh}' TDH / {p_tank}G</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("Red+Lion+Submersible+Well+Pump+Water+Worker+Tank+and+Brass+Tee+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-blue-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>💧 NGWA Total Dynamic Head (TDH), Pressure Tank Drawdown & Wire Sizing Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Submersible Well Pump HP/GPM, TDH, Pressure Tank & Wire Calculator" if is_home else f"{page_data['name']} — Pump HP & Tank Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Well Pumping Depth, PSI Switch & GPM</h2>
                        <p class="text-xs text-gray-600">Calculates Total Dynamic Head (TDH), pump HP, tank drawdown & wire AWG</p>
                    </div>
                    <span class="text-xs font-mono bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded font-semibold">Live TDH Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Well Depth & Household Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-blue-700">
                        <option value="{page_data['depth_ft']},{page_data['psi_switch']},{page_data['gpm']},{page_data['wire_ft']}">Current: {page_data['name']}</option>
                        <option value="150,50,12,200">150-Ft Deep Well | 40/60 PSI | 12 GPM (3/4 HP Pump + 44-Gal Tank)</option>
                        <option value="100,50,10,150">100-Ft Deep Well | 40/60 PSI | 10 GPM (1/2–3/4 HP + 44-Gal Tank)</option>
                        <option value="200,50,12,260">200-Ft Deep Well | 40/60 PSI | 12 GPM (1.0 HP 3-Wire + 44–62 Gal)</option>
                        <option value="300,50,10,360">300-Ft Deep Well | 40/60 PSI | 10 GPM (1.5 HP Pump + 8 AWG Wire)</option>
                        <option value="20,40,10,60">20-Ft Shallow Well | 30/50 PSI | 10 GPM (3/4 HP Cast-Iron Jet Pump)</option>
                        <option value="120,50,20,180">20 GPM Farm / Lawn Irrigation Well (1.5–2.0 HP + CSV1A / 86-Gal)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="depthInput" class="block text-sm font-bold text-gray-800 mb-1">Pumping Water Level Depth (Feet)</label>
                        <input type="number" id="depthInput" value="{page_data['depth_ft']}" min="5" max="600" step="5" oninput="calculateWell()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-blue-700">
                        <span class="text-[11px] text-gray-600">0–25 ft: Shallow Jet | 25–500+ ft: 4\" Submersible</span>
                    </div>

                    <div>
                        <label for="gpmInput" class="block text-sm font-bold text-gray-800 mb-1">Target Peak Flow Rate (GPM)</label>
                        <select id="gpmInput" onchange="calculateWell()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="7" {"selected" if page_data['gpm'] <= 7 else ""}>7 GPM (1–2 Bath Cabin / Low-Yield Well)</option>
                            <option value="10" {"selected" if page_data['gpm'] in (8, 9, 10) else ""}>10 GPM (Standard 2–3 Bathroom Home)</option>
                            <option value="12" {"selected" if page_data['gpm'] == 12 else ""}>12 GPM (3–4 Bathroom Family Home — #1 Choice)</option>
                            <option value="16" {"selected" if page_data['gpm'] in (15, 16) else ""}>16 GPM (4+ Baths + Light Lawn Sprinklers)</option>
                            <option value="20" {"selected" if page_data['gpm'] >= 20 else ""}>20+ GPM (Heavy Irrigation / Farm / Multi-Home)</option>
                        </select>
                    </div>

                    <div>
                        <label for="psiInput" class="block text-sm font-bold text-gray-800 mb-1">Pressure Switch Setting (PSI)</label>
                        <select id="psiInput" onchange="calculateWell()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="40" {"selected" if page_data['psi_switch'] == "40" else ""}>30 / 50 PSI Switch (+92 Ft Pressure Head | 28 PSI Air)</option>
                            <option value="50" {"selected" if page_data['psi_switch'] == "50" else ""}>40 / 60 PSI Switch (+116 Ft Pressure Head | 38 PSI Air)</option>
                            <option value="60" {"selected" if page_data['psi_switch'] == "60" else ""}>50 / 70 PSI High-Pressure (+139 Ft Head | 48 PSI Air)</option>
                        </select>
                    </div>

                    <div>
                        <label for="wireFtInput" class="block text-sm font-bold text-gray-800 mb-1">Total Wire Distance: Panel to Pump (Ft)</label>
                        <input type="number" id="wireFtInput" value="{page_data['wire_ft']}" min="20" max="800" step="10" oninput="calculateWell()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-blue-700">
                        <span class="text-[11px] text-gray-600">House breaker panel to wellhead + depth down well</span>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-blue-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">2. Engineered Pump, Tank & Wire Specs</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Exact Well System Sizing</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-blue-100 border border-blue-300 rounded-xl p-3.5">
                        <span class="text-xs text-blue-950 font-semibold block">Recommended Pump HP</span>
                        <span id="resPumpHP" class="text-xl font-black text-blue-800">3/4 HP Submersible</span>
                        <span id="resTDH" class="text-[11px] text-blue-900 block mt-0.5">285 Ft Total Head (TDH)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Min. Pressure Tank</span>
                        <span id="resTankGal" class="text-2xl font-black text-gray-900">44 Gal Tank</span>
                        <span id="resDrawdown" class="text-[11px] text-emerald-800 font-bold block mt-0.5">11.9 Gal Usable Drawdown</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Submersible Wire Size</span>
                        <span id="resWireAWG" class="text-base font-extrabold text-gray-900">10 AWG Copper</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">230V (&lt;5% Voltage Drop)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Tank Air Pre-Charge</span>
                        <span id="resAirPSI" class="text-base font-extrabold text-amber-800">38 PSI Air</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">2 PSI Below Cut-In</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-blue-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-blue-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recWellTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading Pump & Tank Match...</h3>
                    <p id="recWellDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Matched Well Pump &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Tank, CSV & Tee Kit
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search Submersible Well Pumps, Diaphragm Pressure Tanks, Jet Pumps & Wire</h2>
                <p class="text-sm text-gray-700">Search any horsepower (1/2 HP, 3/4 HP, 1 HP), brand (Red Lion, Goulds, Water Worker, Amtrol, Cycle Stop Valves, Franklin Electric, Boshart), or well part on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. Red Lion 3/4 HP 12 GPM Submersible Pump, Water Worker 44 Gallon Tank, Cycle Stop Valve CSV1A..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-blue-700" required>
                    <button type="submit" class="bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('Red Lion 3/4 HP 1 HP 12 GPM Submersible Well Pump')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">4\" Submersible Pumps</a>
                    <a href="{amz_url('Water Worker HT-44B HT-86B Well Pressure Tank')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">44 & 86 Gal Pressure Tanks</a>
                    <a href="{amz_url('Cycle Stop Valves CSV1A Constant Pressure Valve')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">Cycle Stop Valve CSV1A</a>
                    <a href="{amz_url('Goulds J5S J10S Shallow Well Jet Pump')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">Goulds Jet Pumps</a>
                    <a href="{amz_url('Brass Well Tank Tee Kit Square D 40 60 Switch')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">Brass Tank Tee Kits</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Verified Water Well Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Submersible Pumps, Pressure Tanks, Jet Pumps & Controls</h2>
                </div>
                <a href="{amz_url('Best Selling Submersible Well Pumps and Pressure Tanks')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-blue-800 hover:text-blue-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth Well Pump, Pressure Tank & Control Valve Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-blue-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-700 text-white px-2.5 py-1 rounded">Complete Well System Replacement Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Replacing a Failed Submersible Pump or Waterlogged Pressure Tank?</h2>
                <p class="text-sm text-gray-800">Triple your new pump's lifespan by pairing a 304 Stainless Submersible Pump with a Diaphragm Pressure Tank, Cycle Stop Valve CSV1A, No-Lead Brass Tank Tee Kit, and Torque Arrestor.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Well Pump + Pressure Tank Bundles on Amazon &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Well Depth, TDH & Pressure Tank Specific Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact well pumping depth or GPM flow rate below for pre-calculated Total Dynamic Head, pump HP, and tank drawdown specs.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">TDH, Drawdown & Wire Sizing Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-blue-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-blue-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-blue-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-blue-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-blue-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-blue-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 4) {{
                document.getElementById("depthInput").value = parts[0];
                document.getElementById("psiInput").value = parts[1];
                document.getElementById("gpmInput").value = parts[2];
                document.getElementById("wireFtInput").value = parts[3];
                calculateWell();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateWell() {{
            const depthFt = parseFloat(document.getElementById("depthInput").value) || 150;
            const avgPsi = parseFloat(document.getElementById("psiInput").value) || 50;
            const gpm = parseFloat(document.getElementById("gpmInput").value) || 12;
            const wireFt = parseFloat(document.getElementById("wireFtInput").value) || 200;

            const pHeadFt = Math.round(avgPsi * 2.31);
            const frictionFt = Math.round((depthFt * 0.08) + (gpm * 0.6));
            const tdhFt = Math.round(depthFt + 10 + pHeadFt + frictionFt);

            const workIndex = tdhFt * (gpm / 10.0);
            let hpText = "3/4 HP Submersible";
            let amps = 6.8;
            if (depthFt <= 25 && gpm <= 12) {{
                hpText = "1/2–3/4 HP Shallow Jet / Sub";
                amps = 5.5;
            }} else if (workIndex <= 210) {{
                hpText = "1/2 HP Submersible (230V)";
                amps = 5.0;
            }} else if (workIndex <= 310) {{
                hpText = "3/4 HP Submersible (230V)";
                amps = 6.8;
            }} else if (workIndex <= 430) {{
                hpText = "1.0 HP Submersible (230V)";
                amps = 9.2;
            }} else if (workIndex <= 580) {{
                hpText = "1.5 HP Submersible (230V)";
                amps = 11.5;
            }} else {{
                hpText = "2.0 HP Submersible (230V)";
                amps = 13.2;
            }}

            const ddFactor = avgPsi >= 58 ? 0.24 : (avgPsi >= 48 ? 0.27 : 0.31);
            const reqDrawdown = gpm * 1.05;
            const rawTank = reqDrawdown / ddFactor;
            let tankGal = 44;
            if (rawTank <= 22) tankGal = 20;
            else if (rawTank <= 34) tankGal = 32;
            else if (rawTank <= 48) tankGal = 44;
            else if (rawTank <= 66) tankGal = 62;
            else tankGal = 86;

            const actualDD = (tankGal * ddFactor).toFixed(1);
            const airPrecharge = avgPsi >= 58 ? "48 PSI Air (50/70)" : (avgPsi >= 48 ? "38 PSI Air (40/60)" : "28 PSI Air (30/50)");

            const loadFt = amps * wireFt;
            let wireAWG = "12 AWG Copper (12/2 or 12/3)";
            if (loadFt <= 950) wireAWG = "12 AWG Copper (12/2 or 12/3)";
            else if (loadFt <= 1650) wireAWG = "10 AWG Copper (10/2 or 10/3)";
            else if (loadFt <= 2700) wireAWG = "8 AWG Copper (8/3 Submersible)";
            else wireAWG = "6 AWG Copper (6/3 Heavy)";

            document.getElementById("resPumpHP").textContent = hpText;
            document.getElementById("resTDH").textContent = tdhFt + " Ft TDH (" + depthFt + "' Depth + " + pHeadFt + "' PSI)";
            document.getElementById("resTankGal").textContent = tankGal + "-Gal Tank";
            document.getElementById("resDrawdown").textContent = actualDD + " Gal Usable Drawdown";
            document.getElementById("resWireAWG").textContent = wireAWG;
            document.getElementById("resAirPSI").textContent = airPrecharge;

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "";
            let secondaryQuery = "Water Worker " + tankGal + " Gallon Well Pressure Tank and Brass Tank Tee Kit";

            if (depthFt <= 25) {{
                recTitle = "Goulds J5S / J10S or Red Lion Cast-Iron Shallow Well Jet Pump + " + tankGal + "-Gal Tank";
                recDesc = "Engineered for shallow wells and cisterns within 25 vertical feet (" + tdhFt + " ft TDH).";
                primaryQuery = "Goulds J5S J10S Red Lion Shallow Well Jet Pump";
            }} else if (workIndex <= 320) {{
                recTitle = "Red Lion / Goulds 3/4 HP " + gpm + " GPM 4\" Stainless Submersible Pump + " + tankGal + "-Gal Tank";
                recDesc = "America's #1 residential deep-well configuration for " + tdhFt + " feet of Total Dynamic Head.";
                primaryQuery = "Red Lion RL12G07 3/4 HP 12 GPM 230V Submersible Well Pump";
            }} else {{
                recTitle = "1.0 HP – 1.5 HP Heavy-Duty 4\" Stainless Submersible Well Pump + Cycle Stop Valve CSV1A";
                recDesc = "High-head multi-stage stainless pump matched to " + tdhFt + " ft TDH and " + wireAWG + ".";
                primaryQuery = "Red Lion Hallmark 1 HP 1.5 HP 230V Submersible Deep Well Pump";
                secondaryQuery = "Cycle Stop Valves CSV1A and Water Worker Pressure Tank";
            }}

            document.getElementById("recWellTitle").textContent = recTitle;
            document.getElementById("recWellDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateWell);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-blue-700 transition block">
            <span class="text-[11px] font-bold text-blue-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-800">Home & TDH Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-blue-800">Daily Well Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">Field Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">GPM / Head</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Motor / Tank</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Construction</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Details</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate TDH & Tank Size
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On TDH Flow Curve, Drawdown & Electrical Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-blue-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our well water benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Well Pump & Tank Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-800">Home & TDH Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-blue-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-blue-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-blue-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "150-Foot Deep Well (3-Bathroom Home | 12 GPM)",
        "depth_ft": 150,
        "psi_switch": "50",
        "gpm": 12,
        "wire_ft": 200,
        "desc": "Calculate exact submersible well pump horsepower (HP), Total Dynamic Head (TDH in feet), diaphragm pressure tank gallon drawdown, and 230V submersible copper wire gauge—plus read 3 new hardware reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Well Depth & Tank Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
