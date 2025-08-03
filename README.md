# 🌍 CountryGuessr

A web-based **country guessing game** built with Python and Flask that challenges players to identify a random country based on **directional arrows**, **distance feedback**, and **flags**.

---

## 🚀 Features

- 🌎 Randomly chosen target country from around the world.
- 📏 Distance-based color hints.
- 🧭 Directional arrow indicators (↑ ↓ ← →).
- 🚩 Display of guessed country flags.
- 👁 "Reveal Answer" button for surrendering.
- 🔄 Game reset functionality.

---

## 🛠 Tools & Technologies Used

| Tools / Technologies | Purpose                                    |
|-------------------|--------------------------------------------|
| Python 3.13.3        | Backend logic and game engine              |
| Flask             | Web framework for routing and templating   |
| HTML/CSS          | Frontend structure and styling             |
| REST Countries API| Country data including coordinates & flags |
| JavaScript        | Frontend interactivity (Reveal button)     |

---

## 📦 Installation

### 🗂️ Clone the Repository

```bash
git clone https://github.com/your-username/country-guessr.git
cd country-guessr
```

### 📦 Create and Activate a Virtual Environment (Recommended)

#### On **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On **macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 📄 Install Dependencies

Make sure you have Python 3.13.3 installed, then run:

```bash
pip install -r requirements.txt
```

> **Note:** Your `requirements.txt` should include:
> ```
> flask
> requests
> ```

---

## ▶️ Running the App

```bash
python app.py
```

Open your browser and go to:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
country-guessr/
│
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── style.css          # CSS styling
└── README.md              # Project documentation
```

---

## 🧠 How to Play

1. Enter a country name and hit "Guess".
2. See:
   - The **flag** of the guessed country.
   - **Distance** to the target (color-coded).
   - **Directional arrow** pointing toward the target.
3. Use "Reveal Answer" or "Reset" anytime.

---

<!-- ## 🔍 Future Enhancements

- 🌐 Use Haversine formula for geographic accuracy
- ⌨️ Country name autocomplete
- 💡 Hints for continent or capital
- 🗺 Map integration for visual feedback
- 📊 Score tracking or limited attempts

--- -->

<!-- ## 📜 License

This project is **proprietary software** and is **not licensed for public use or redistribution**.

All rights are reserved by the original author.  
You may not copy, modify, distribute, or use this project or any part of it without **explicit written permission**.

For inquiries, contact: [your-email@example.com]

--- -->

## 🙌 Acknowledgements

- [REST Countries API](https://restcountries.com/) for country data & flags
- Inspired by Globle, and geography quizzes
