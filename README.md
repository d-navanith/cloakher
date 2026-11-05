# CloakHer (AegisPix) 🛡️

> **Adversarial Immunization & Invisible Steganographic Shield for Women's Social Imagery**  
> Developed for **Artemia 2.0** — IEEE WIE Student Branch Affinity Group, University of Sri Jayewardenepura.

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Frontend-TailwindCSS-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
[![IEEE WIE](https://img.shields.io/badge/Competition-Artemia_2.0-indigo)](https://wie.ieee.org/)

---

## 🌟 Overview

Every day, women share photographs on Instagram, Facebook, and WhatsApp. With the rise of Generative AI and illicit diffusion inpainting tools, bad actors can easily scrape these images and synthesize non-consensual deepfakes, face-swaps, and explicit blackmail material in seconds.

Existing safety systems are **100% reactive**—they only step in after a victim's dignity and mental health have already been violated.

**CloakHer** solves this by **immunizing photos before they are ever posted online**. Built on the mathematical foundation of **MIT PhotoGuard**, CloakHer injects microscopic, human-imperceptible adversarial perturbations and frequency-domain steganography into facial and anatomical pixels:
* **To human eyes:** The photo looks 100% natural, crisp, and ready for social media.
* **To generative AI models:** The latent representation collapses, causing AI face-swaps or inpainting engines to crash or return glitched, distorted artifacts.

---

## 🚀 Key Features (MoSCoW Prioritization)

### 1. One-Click Adversarial Photo Immunizer (`MUST`)
* **Adversarial Latent Perturbation:** Implements targeted gradient perturbation ($\pm 1.5$ RGB) across facial contours.
* **C2PA + DWT Steganography:** Injects an imperceptible cryptographic signature surviving screenshots and compression that signals compliant models to abort unauthorized synthesis.
* **Interactive Heatmap:** View an amplified ($\times 15$) visual map of the protective tensor.

### 2. Live AI Attack Simulator (`MUST`)
* Empirically proves the shield's efficacy to judges and users.
* Side-by-side simulation running an automated inpainting/face-swap attack against an **Unprotected Photo** (which gets altered) vs. a **CloakHer Protected Photo** (which catastrophically collapses the AI latent space).

### 3. Forensic Verifier & Sri Lanka CERT Takedown Generator (`MUST`)
* Computes zero-knowledge perceptual hashes (pHash) without storing user photos.
* Generates an official, legally formatted evidence affidavit compliant with Sri Lanka's **Computer Crimes Act No. 24 of 2007** and the **Electronic Transactions Act** for rapid police and platform takedowns.

---

## 🛠️ Tech Stack & Architecture

* **Frontend:** Responsive HTML5, Tailwind CSS, Lucide Icons, Vanilla ES6+ (Zero bloated bundler dependencies, works on any mobile or desktop browser).
* **Backend:** FastAPI (Python), Uvicorn ASGI server.
* **Adversarial Core:** NumPy, Pillow, PyTorch-ready tensor processing engine.
* **Privacy by Design:** **Zero-Storage Architecture**—all processing occurs strictly within transient volatile memory (RAM) and raw uncloaked photos are purged immediately.

---

## 💻 Local Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd idea_mart
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pillow numpy python-multipart reportlab
   ```

3. **Start the application:**
   ```bash
   python -m uvicorn main:app --app-dir app --host 127.0.0.1 --port 8000 --reload
   ```

4. **Access the web app:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

## 📑 Project Deliverables Included

* `app/`: Complete working web application (Frontend + Backend + Cloaking Engine).
* `CloakHer_Project_Proposal.pdf`: Formal IEEE WIE Ideathon project proposal document.
* `Template (1).pptx`: Artemia 2.0 Ideathon 4-part pitch presentation template.

---

## 👥 Team Details & Declaration

* **Competition:** Artemia 2.0 (Organized by IEEE WIE Student Branch Affinity Group, University of Sri Jayewardenepura)
* **Theme:** Women's Safety & Empowerment (UN SDGs 5, 9, 11)
