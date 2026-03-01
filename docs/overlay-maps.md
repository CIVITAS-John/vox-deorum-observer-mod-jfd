# Overlay Maps System

The overlay maps system is an extensible framework for displaying complex game-state information as color-coded map overlays. It is the primary extension point for vox-deorum LLM action visualization.

---

## Concepts

| Term | Meaning |
|------|---------|
| **Class** | A top-level category of overlay, e.g. "Players", "Religions", "Diplomacy" |
| **Filter** | A sub-view within a class, e.g. within "Diplomacy": "Relations", "Trade Routes" |
| **Option** | A per-overlay toggle or configuration value |
| **Legend entry** | A UI row in the sidebar showing what a color means |

---

## SQL Schema

All tables live in `Core/Overlay Maps/`. They are loaded `OnModActivated` before any Lua runs.

### `JFD_OverlayMapClasses` (defined in `JFDMaster_OverlayMaps.sql`)

Top-level overlay categories shown in the class dropdown.

| Column | Type | Description |
|--------|------|-------------|
| `Type` | TEXT (PK) | Unique key, e.g. `"OVERLAYMAP_CLASS_PLAYERS"` |
| `Description` | TEXT | Localization key for display name |
| `IconAtlas` | TEXT | Icon font atlas name |
| `IconIndex` | INTEGER | Icon index within atlas |
| `SortIndex` | INTEGER | Display order |

Rows defined in: `JFDOverlayMapClasses_OverlayMaps.sql`

### `JFD_OverlayMapFilters` (defined in `JFDMaster_OverlayMaps.sql`)

Sub-views within a class.

| Column | Type | Description |
|--------|------|-------------|
| `Type` | TEXT (PK) | Unique key, e.g. `"OVERLAYMAP_FILTER_PLAYERS_TERRITORY"` |
| `ClassType` | TEXT (FK → `JFD_OverlayMapClasses.Type`) | Parent class |
| `Description` | TEXT | Localization key for display name |
| `SortIndex` | INTEGER | Display order within class |

Rows defined in: `JFDOverlayMapFilters_OverlayMaps.sql`

### `JFD_OverlayMapOptions` (defined in `JFDMaster_OverlayMaps.sql`)

Per-overlay toggles and settings exposed in the UI.

| Column | Type | Description |
|--------|------|-------------|
| `Type` | TEXT (PK) | Unique key |
| `FilterType` | TEXT (FK → `JFD_OverlayMapFilters.Type`) | Parent filter |
| `Description` | TEXT | Localization key |
| `DefaultValue` | INTEGER | 0 = off, 1 = on |

Rows defined in: `JFDOverlayMapOptions_OverlayMaps.sql`

### `JFD_OverlayMaps` (the data rows)

The actual overlay entries — one row per civ/religion/etc. per overlay.

| Column | Type | Description |
|--------|------|-------------|
| `Type` | TEXT (PK) | Unique key |
| `FilterType` | TEXT (FK) | Which filter this entry appears under |
| `Description` | TEXT | Localization key for legend label |
| `Colour` | TEXT | Color reference (from `JFDColors_AIObserver.sql`) |

Data rows defined in:
- `JFDOverlayMaps_Players_OverlayMaps.sql` — player-based overlays
- `JFDOverlayMaps_Diplomacy_OverlayMaps.sql` — diplomacy overlays

---

## Built-in Overlay Classes

| Class Key | Description |
|-----------|-------------|
| `OVERLAYMAP_CLASS_PLAYERS` | Player territory and city positions |
| `OVERLAYMAP_CLASS_RELIGIONS` | Religious majority by tile |
| `OVERLAYMAP_CLASS_DIPLOMACY` | Diplomatic relations between civs |
| `OVERLAYMAP_CLASS_STABILITY` | Stability values (requires compatible mod) |
| `OVERLAYMAP_CLASS_IDEOLOGIES` | Ideology distribution |
| `OVERLAYMAP_CLASS_CULTURE` | Cultural influence spread |

---

## Lua Integration

The overlay UI is driven by `JFD_UI_OverlayMapsOverview.lua`. At runtime:

1. `JFD_GetOverlayMapClasses()` fetches all class rows → populates class dropdown.
2. `JFD_GetOverlayMapFilters(classType)` fetches filters for the selected class → populates filter dropdown.
3. `RefreshOverlayMaps()` colors map tiles by calling `JFD_AssignOverlayColour(playerID, filterType)` for each tile owner.
4. `RefreshLegends()` builds legend rows from the same data.

---

## Adding a New Overlay (vox-deorum Extension Point)

To add an overlay showing LLM player actions or decisions:

### 1. Define a new class (if needed)

In a new SQL file (e.g. `Core/Overlay Maps/JFDOverlayMapClasses_VoxDeorum.sql`):

```sql
INSERT OR REPLACE INTO JFD_OverlayMapClasses
    (Type, Description, SortIndex)
VALUES
    ('OVERLAYMAP_CLASS_VOXDEORUM', 'TXT_KEY_OVERLAYMAP_CLASS_VOXDEORUM', 100);
```

### 2. Define filters

```sql
INSERT OR REPLACE INTO JFD_OverlayMapFilters
    (Type, ClassType, Description, SortIndex)
VALUES
    ('OVERLAYMAP_FILTER_VD_ACTIONS', 'OVERLAYMAP_CLASS_VOXDEORUM', 'TXT_KEY_OVERLAYMAP_FILTER_VD_ACTIONS', 1);
```

### 3. Add localization strings

In a new XML file (e.g. `Core/Overlay Maps/JFDGameText_VoxDeorum_OverlayMaps.xml`):

```xml
<GameData>
  <Language_en_US>
    <Row Tag="TXT_KEY_OVERLAYMAP_CLASS_VOXDEORUM">
      <Text>LLM Actions</Text>
    </Row>
    <Row Tag="TXT_KEY_OVERLAYMAP_FILTER_VD_ACTIONS">
      <Text>Last Action</Text>
    </Row>
  </Language_en_US>
</GameData>
```

### 4. Register new files in the modinfo

Add `<UpdateDatabase>` entries for each new SQL/XML file in the `<OnModActivated>` block of the `.modinfo`.

### 5. Wire the color logic in Lua

In `JFD_OverlayMaps_Utils.lua`, extend `JFD_AssignOverlayColour()` to handle your new filter type, or add a new overlay-specific function and call it from `RefreshOverlayMaps()` in `JFD_UI_OverlayMapsOverview.lua`.

---

## Color Definitions

Colors used by overlays are defined in `Core/JFDColors_AIObserver.sql` and registered with Civ5's color system. Reference them by name string in overlay data rows and Lua color lookups.

Color format in SQL: `R G B A` as space-separated floats in `[0, 1]`.

Example:
```sql
INSERT OR REPLACE INTO Colors (Type, Red, Green, Blue, Alpha)
VALUES ('COLOR_JFD_PLAYER_1', 0.8, 0.2, 0.2, 1.0);
```
