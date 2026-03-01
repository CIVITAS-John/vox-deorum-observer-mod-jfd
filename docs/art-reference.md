# Art Reference

All mod art lives under `Art/`. Civ5 loads DDS textures by filename (the engine searches registered art paths), so textures used in XML layouts are referenced by bare filename. Font icon sheets require a paired `.ggxml` descriptor that tells the engine the glyph layout.

---

## Font Icons (`Art/Font Icons/`)

Font icons are sprite sheets that Civ5 renders inline inside text strings. Each sheet has a `.dds` texture and a `.ggxml` descriptor. They are registered in the game database via `Core/JFDIconFonts_AIObserver.sql` and `Core/Overlay Maps/JFDIconFonts_OverlayMaps.sql`.

### `JFDFontIcons_AIObserver_22.dds` + `.ggxml`

- **Size:** 220×110 px, 10 glyphs per row, 5 rows (51 total glyphs)
- **DB key:** `ICON_FONT_TEXTURE_JFD_AIOBSERVER`
- **Used by:** Civ info panels, diplo corner, ranking displays throughout the observer UI

| Glyph indices | Icon names | Purpose |
|---|---|---|
| 1–4 | `ICON_GOLD_POS/NEG/EMP/NEU` | Gold yield indicators (positive, negative, empire, neutral) |
| 5–6 | `ICON_SCIENCE_POS/EMP` | Science yield indicators |
| 7–10 | `ICON_GOVERNMENT`, `ICON_GOVERNMENT_A`, `ICON_LEGISLATURE`, `ICON_LEGISLATURE_A` | Government and legislature status (active / inactive) |
| 11–12 | `ICON_CULTURE_A`, `ICON_RELIGION_A` | Active culture / active religion markers |
| 13–14 | `ICON_IDEOLOGY_A`, `ICON_IDEOLOGY` | Active / inactive ideology |
| 15–18 | `ICON_IDEOLOGY_OPINION_1–4` | Ideology pressure opinion tiers (1 = very negative … 4 = positive) |
| 19–20 | `ICON_RELATION_WAR` / `ICON_CAPITAL_A`, `ICON_CAPITAL_CAPTURED` | War relation; capital alive / capital captured |
| 21–22 | `ICON_TROPHY_IRON`, `ICON_TROPHY_GRAPHITE` | Ranking tier trophies (Iron and Graphite/Coal) |
| 23 | `ICON_CITY` | City marker |
| 24 | `ICON_PANTHEON_A` | Active pantheon marker |
| 25–28 | `ICON_FOOD_POS/NEG/NEU/VPOS` | Food growth indicators |
| 29–30 | `ICON_PEACE_FORCED`, `ICON_DOF` | Forced peace; Declaration of Friendship |
| 31–37 | `ICON_RELATION_HOSTILE/FRIENDLY/AFRAID/GUARDED/NEUTRAL/UNMET/DECEPTIVE` | Diplomatic relation icons |
| 38–42 | `ICON_STRENGTH_NOT`, `ICON_RESEARCH_NOT`, `ICON_OPEN_BORDERS_NOT`, `ICON_LEGEND_ERA_2`, `ICON_DOF_NOT` | Negative/missing-status icons: military strength, research agreement, open borders, era marker, DOF not established |
| 43 | `ICON_NORMAL_AGE` | Normal (non-golden) age indicator |
| 44–51 | (unmapped) | Reserved / available glyphs |

### `JFDFontIcons_Players_OverlayMaps_22.dds` + `.ggxml`

- **Size:** 220×132 px, 10 glyphs per row, 6 rows (60 total glyphs)
- **DB key:** `ICON_FONT_TEXTURE_JFD_OVERLAYMAPS_PLAYERS`
- **Used by:** Overlay maps legend panels (Players, Diplomacy overlays)

| Glyph indices | Icon names | Purpose |
|---|---|---|
| 2 | `ICON_LEGEND_ANARCHY` | Anarchy state indicator |
| 3–4 | `ICON_LEGEND_IDEOLOGY`, `ICON_LEGEND_NO_IDEOLOGY` | Ideology present / absent |
| 11 | `ICON_LEGEND_NO_FACTION`, `ICON_LEGEND_NO_RELIGION` | No faction / no religion (shared glyph) |
| 14–15 | `ICON_LEGEND_TECHNOLOGY`, `ICON_LEGEND_TECHNOLOGY_2/3` | Technology tier 1 / tier 2–3 |
| 17–20 | `ICON_LEGEND_TREASURY_1–4` | Treasury tier indicators |
| 21–24 | `ICON_LEGEND_GROWTH_1–4` | Growth tier indicators |
| 25–26 | `ICON_LEGEND_NO_POLICY_BRANCH`, `ICON_LEGEND_NO_DEFENSE_PACT` | No active policy branch / no defense pact |
| 31–40 | `ICON_LEGEND_ERA_1`, `ICON_LEGEND_ERA_3–10` | Era markers (Ancient through Future; era 2 is in the main AIObserver sheet) |
| 41–53 | `ICON_JFD_LEGEND_GOV_TRIBE`, `ICON_JFD_LEGEND_GOV_MONARCHY*`, `ICON_JFD_LEGEND_GOV_REPUBLIC*`, `ICON_JFD_LEGEND_GOV_THEOCRACY*` | JFD policy government icons with variant suffixes: base, `_A` (adopted), `_F` (flag?), `_O` (other), `_S` (state) |
| 54–56 | `ICON_JFD_LEGEND_GOV_MONARCHY_S`, `ICON_JFD_LEGEND_GOV_REPUBLIC_S`, `ICON_JFD_LEGEND_GOV_THEOCRACY_S` | State variants |

---

## Sovereign Government Icons (`Art/`)

### `JFDFontIcons_AIObserver_SovGovs_22.dds` + `JFDFontIcons_AIObserver_SovGovs_22.ggxml`

- **Size:** 506×22 px, 25 glyphs in a single row
- **DB key:** `ICON_FONT_TEXTURE_JFD_AIOBSERVER_SOV`
- **Used by:** Civ info panels when JFD's Sovereignty mod is active; government column of the observer sidebar
- **Dependency:** Only meaningful when Sovereignty mod is loaded; the mapping SQL still loads regardless

Each glyph is one government type icon. Mapping (glyph → `ICON_GOVERNMENT_JFD_*`):

| Glyph | Government |
|---|---|
| 1 | Monarchy |
| 3 | Principality |
| 4 | Tribe |
| 7 | Totalitarian / Papacy (shared) |
| 8 | Holy Roman |
| 9 | Mandate |
| 11 | Tribal |
| 12 | Republic |
| 14 | Caliphate |
| 15 | Theocratic |
| 16 | Shogunate |
| 17 | Merchant |
| 18 | Monastic |
| 19 | Military / Revolutionary (shared) |
| 21 | Nomadic |
| 22 | Imperial |
| 23 | Mamluke |

---

## UI Image Textures (`Art/Images/`)

### Toolbar Buttons

| File(s) | Size | Used in | Purpose |
|---|---|---|---|
| `IGEButton.dds` / `IGEButtonHL.dds` | 45×45 | `JFD_AIObserver_Functions.xml` | In-Game Editor (IGE) toolbar button. `IGEButtonHL` is the animated hover overlay. |
| `IGEButtonOld.dds` / `IGEButtonOldHL.dds` | 45×45 | (legacy) | Older IGE button artwork; kept as fallback / reference. |
| `overlaymapbutton.dds` / `overlaymapbuttonhl.dds` | 45×45 | `JFD_AIObserver_Functions.xml` | Overlay Maps popup button. `overlaymapbuttonhl` is the animated hover overlay. |
| `JFDOverlayMap64.dds` | 64×64 | overlay map SQL / notifications | Larger overlay map icon used in notification or atlas contexts. |
| `InfoAddictButton.dds` / `InfoAddictButtonHL.dds` | 45×45 | `TopPanel` override | Info Addict mod integration button. Shown when Info Addict is detected. |
| `PediaButton.dds` / `PediaButtonHL.dds` | 45×45 | `TopPanel` override | Civilopedia quick-access button added to the top panel. |
| `mainopen32.dds` / `mainopenhl32.dds` | 32×32 | `TopPanel` override | "Show interface" open-state toggle button (replaces base-game `mainopen.dds`). |
| `mainclose32.dds` / `mainclosehl32.dds` | 32×32 | `TopPanel` override | "Show interface" close-state toggle button (replaces base-game `mainclose.dds`). |

### Civ Info Box Backgrounds

Background panels used for the per-civ summary cards in the observer sidebar. Multiple height variants exist to accommodate different amounts of visible information (e.g. more rows when mods like Sovereignty or VMC are active).

| File | Approx. height | Notes |
|---|---|---|
| `civinfoboxsmall.dds` | small | Compact card (fewest stat rows) |
| `civinfoboxlarge.dds` | large | Expanded card |
| `civinfobox88.dds` | 88 px | Fixed-height variant |
| `civinfobox96.dds` | 96 px | Fixed-height variant |
| `civinfobox104.dds` | 104 px | Fixed-height variant |
| `civinfobox128.dds` | 128 px | Tallest fixed-height variant |

### Civ Symbol Frames

Decorative ring / frame drawn around civilization symbol icons.

| File | Icon size | Purpose |
|---|---|---|
| `civsymbolsframe24.dds` | 24 px | Frame for 24px civ icons (compact lists) |
| `civsymbolsframe32.dds` | 32 px | Frame for 32px civ icons (main sidebar) |
| `aiobserversymbolframe32.dds` | 32 px | Observer-specific frame (no ranking tier) |
| `aiobserversymbolrankedframe32.dds` | 32 px | Frame with ranking-tier color band |
| `aiobserversymbolrankedframe45.dds` | 45 px | Larger ranked frame for prominent display |

### Top Panel Elements

The mod replaces `TopPanel.xml` and its background layer. These textures build up the custom top-bar layout from left to right.

| File | Purpose |
|---|---|
| `topleft_aiobserver.dds` | Primary top-left corner panel piece |
| `topleft_aiobserver1.dds` | Variant 1 of the top-left corner |
| `topleft_aiobserver2.dds` | Variant 2 (e.g. with/without golden age glow) |
| `topleftaiobserver.dds` | Alternative naming for top-left base |
| `topleftaiobserver2.dds` | Alternative naming variant 2 |
| `topleftaiobserver3.dds` | Alternative naming variant 3 |
| `topleftaiobserver3_GA.dds` | Variant 3 with golden age highlight |
| `topleftbtm_aiobserver.dds` | Bottom edge of the top-left panel block |
| `topleftfancy_aiobserver.dds` | Fancy decorated top-left corner (used in the ornate panel style) |
| `topleft001alt.dds` | Top-left corner piece, alternate design |
| `topleft2aiobserver.dds` | Second (right-adjacent) top-left area base |
| `topleft2_aiobserver2.dds` | Second area variant 2 |
| `topleft2_aiobserver3.dds` | Second area variant 3 |
| `topleft2frame.dds` | Horizontal frame bar for the second row |
| `topleft2frameend.dds` | End cap for the second-row frame bar |
| `topleftframe.dds` | Top panel horizontal frame strip |
| `topleftframe2.dds` | Alternate frame strip |
| `topleftframe22.dds` | 22px-height frame strip |
| `topleftframeL.dds` | Left end cap of the frame strip |
| `topleftframeR.dds` | Right end cap of the frame strip |
| `topleftframeRalt.dds` | Alternate right end cap |
| `topcentreaiobserver.dds` | Center piece of the top panel (between left and right blocks) |
| `topright020_esp_shorter.dds` | Top-right corner element (shortened to clear the minimap) |

### Decorative / Framing Elements

| File | Purpose |
|---|---|
| `fancytrim_cut.dds` | Horizontal decorative trim strip, saturated/colored |
| `fancytrimdesat_cut.dds` | Same trim, desaturated (used as inactive or secondary state) |
| `fancyfern.dds` | Left-side ornamental fern flourish |
| `fancyfernR.dds` | Right-side mirror of `fancyfern.dds` |
| `leftportraitdecor128real.dds` | 128 px decorative surround for the leader portrait on the left civ-info panel |
| `leadernamebar.dds` | Background bar behind the leader name label in the civ card |
| `diplobox.dds` | Background box for the diplomatic status row |
| `diplomacypanelleft.dds` | Left-side decorative border for the diplomacy section |
| `bottomright128x224_2.dds` | Bottom-right corner decoration on the main observer panel (128×224 px) |

### Turn Banner

| File | Purpose |
|---|---|
| `TurnBanner.dds` | Full-width banner displayed at the start of each turn (shows turn number / AI turn indicator) |

---

## Adding New Art

When adding a new DDS for the vox-deorum LLM display panels:

1. Place the file in `Art/Images/` (UI textures) or `Art/Font Icons/` (icon font sheets).
2. Reference it in your `.xml` layout as `Texture="yourfile.dds"` (bare filename, no path prefix needed for files in the mod's art directories).
3. If it is a font-icon sheet, add a `.ggxml` descriptor and register it in a new SQL file under `Core/` with `INSERT OR REPLACE INTO IconFontTextures` and `IconFontMapping` rows. Follow the pattern in `Core/JFDIconFonts_AIObserver.sql`.
4. Add the file to the `<Files>` list in `JFD's Utilities - AI Observer Interface (v 11).modinfo` so Civ5 knows to load it.
5. Prefix new icon names with `VD_` (e.g. `ICON_VD_LLM_ACTION`) to avoid collisions with JFD's namespace.
