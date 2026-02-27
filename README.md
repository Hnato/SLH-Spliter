# SLH Word Splitter 2026 ☕

**SLH Word Splitter** is a cutting-edge, futuristic desktop application designed for the 2026 digital era. It segments large text volumes into manageable parts based on a precise word count, featuring a hyper-polished "Cyber-Coffee" interface with glassmorphism effects and neon accents.

<img src="source_files/SLH.png" alt="SLH" width="340" height="340" />

## 🌟 Futuristic Features

- **Neural-Link Segmentation**: High-speed word-based processing that respects linguistic boundaries.
- **Glassmorphism UI**: A sleek, minimalist interface with translucent elements and rounded aesthetics.
- **Cyber-Coffee Aesthetic**: Clean White (#FFFFFF) theme with Forest Green (#228B22) typography, Brown (#8B4513) outlines, and an Amber (#D2691E) coffee icon.
- **Micro-Interactions**: Smooth hover effects, animated transitions, and dynamic feedback.
- **Adaptive Density Control**: Interactive slider from **100 to 16,000 words** with persistent memory.
- **Archive Export**: One-click system export to organized `.txt` files with Node-based numbering.

## 🚀 Installation & Usage

### 1. Standalone System (Portable)
Simply download and run `SLHSpliter.exe`. No installation required. Optimized for Windows 10/11.

### 2. Operational Guide
1. **Calibrate Density**: Use the slider to set your target word count per part.
2. **Input Data**: Paste your source text into the central terminal area.
3. **Engage Split**: Click the neon button to process the data.
4. **Export System**: Save the results to your persistent storage.

## 💻 Developer Information

### Prerequisites
- Python 3.11+
- `customtkinter`: Modern UI library
- `Pillow`: Image processing

### Building from Source
To compile the futuristic standalone executable:
```powershell
pip install customtkinter Pillow pyinstaller
python -m PyInstaller --noconsole --onefile --icon="source_files/SLH.ico" --add-data="source_files/SLH.ico;source_files" --name="SLHSpliter" --distpath="." --clean source_files/SLH_Word_Splitter.py
```

## 📦 Project Structure
- `source_files/`: Core Python logic and visual assets.
- `SLHSpliter.exe`: The final production build.
- `config.json`: Persistent user configuration.

## 📄 License
Licensed under the MIT Digital License.

---
*Brewed with love and ☕ for you !!!*
*By Hnato*
