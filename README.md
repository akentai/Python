# Voice-Based Educational Game for Children

This project is an interactive **speech recognition game** designed to help **young children** learn vocabulary categories like **fruits**, **sports**, and **seasons** in Greek, using **images and voice input**.

Originally developed as an experimental prototype for **kindergarten classrooms**, the game uses **Python, Tkinter, and Google's Speech API** to encourage pronunciation and language practice in a playful way.

The game was developed as part of the **eMascot**, a prototype **educational teddy bear with technological enhancements**, and was integrated into **Hara Sparou’s Bachelor thesis** titled:

> **"The Use of eMascot in a Typical Greek Kindergarten"**  
> Department of Education, Crete, Greece

---

## What It Does

- Displays images (e.g. fruits) and prompts children to **say the name** aloud
- Uses **speech recognition** to verify correct pronunciation
- Provides immediate feedback on correctness
- Translates spoken Greek words to English and reads them aloud
- Includes a graphical interface with a friendly flow:
  - Start → Category Selection → Voice Game → Feedback → Restart

---

## Technical Highlights

- `speech_recognition` and `gTTS` for voice input/output
- `Tkinter` for GUI flow across game stages
- `google_trans_new` for on-the-fly translation

---

## Educational Purpose

Designed to:
- Reinforce vocabulary in a **multisensory** way (visual + auditory)
- Promote **pronunciation skills**
- Offer **accessible learning** for children unfamiliar with reading
- Bridge language learning via **real-time translation**

---
