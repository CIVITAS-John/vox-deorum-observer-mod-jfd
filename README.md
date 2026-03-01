# JFD's AI Observer Interface

> **Adapted for [vox-deorum](https://github.com/CIVITAS-John/vox-deorum)**
> This fork adapts JFD's Observer Interface to display LLM player actions in real time as part of the vox-deorum project.

---

## Original Mod

**Name:** JFD's Utilities — AI Observer Interface
**Author:** JFD
**Version:** 11
**Mod ID:** `970aae10-1004-4c8a-af2d-8d601de5ec02`

A Civilization V mod that provides an enhanced spectator/observer UI for watching AI-only or CBR (Community Battle Royale) games. It replaces the standard minimap and top panel with richer visualization tools, and suppresses intrusive popups so you can watch AI play without interruption.

---

## Features (Original)

- **Big Minimap Overview** — full-screen minimap with color-coded territory, religion spread, unit positions, and terrain; collapsible legends for civs, city-states, and religions; per-player perspective filtering
- **Overlay Maps** — extensible overlay framework for diplomatic relations, ideology, stability, cultural influence, and more
- **Popup & Notification Suppression** — optionally silences ancient ruins, archaeology, golden age, great person, and new era popups
- **UI Integration** — custom top panel, diplo corner, city banners, and minimap panel tailored for passive observation
- **Utility Framework** — shared helpers for player ranking (gold/silver/bronze/coal/iron), city descriptors, religion majority detection, and mod compatibility checks

---

## Adaptation for vox-deorum

[vox-deorum](https://github.com/CIVITAS-John/vox-deorum) is a research project that integrates large language models (GPT, Claude, and local models) as Civilization V AI opponents. LLMs handle macro-strategic reasoning while the existing VPAI handles tactical execution.

This fork adapts the Observer Interface to **surface LLM player decisions in the game UI** — showing what each LLM player chose to do each turn, why, and how that maps to in-game actions. The goal is to make LLM-vs-LLM or LLM-vs-VPAI games observable and interpretable for researchers and spectators.

> **Status:** Under active development. Code substance is unchanged from JFD v11; documentation and vox-deorum integration hooks are being added.

---

## Credits

### Original Mod
| Role | Name |
|------|------|
| Code, Design, Research, Writing | **JFD** |
| Debugging config reference | Modiki ([source](https://modiki.civfanatics.com/index.php?title=Debugging_(Civ5)#Configuration)) |
| UI — Religion Spread | Whoward ([source](http://www.picknmixmods.com/mods/CivV/UI/Religion%20Spread.html)) |

### vox-deorum Adaptation
| Role | Name |
|------|------|
| Adaptation & Integration | CIVITAS-John |

---

## Documentation

- [docs/architecture.md](docs/architecture.md) — system architecture and data flow
- [docs/lua-reference.md](docs/lua-reference.md) — Lua function reference
- [docs/overlay-maps.md](docs/overlay-maps.md) — overlay map system deep-dive

---

## Related Projects

- [vox-deorum](https://github.com/CIVITAS-John/vox-deorum) — LLM AI for Civilization V
- [vox-deorum-replay](https://github.com/CIVITAS-John/vox-deorum-replay) — session replay viewer
- Original mod thread: CivFanatics (JFD's Utilities series)
