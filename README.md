# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System developed using Python, Natural Language Processing (NLP), and Machine Learning. It recommends similar movies based on the movie selected by the user using **TF-IDF Vectorization and Cosine Similarity**.

## 🚀 Live Demo

[Try the Movie Recommendation System](https://movie-recommendation-system-2-olws.onrender.com/)

## 📌 Project Overview

The Movie Recommendation System helps users discover movies based on their interests.

When a user selects a movie, the application analyzes its textual features, calculates similarity scores against other movies, and recommends the top 5 similar movies.

## ✨ Key Features

- Interactive movie selection.
- Content-Based Movie Recommendations.
- Top 5 similar movie suggestions.
- TF-IDF text vectorization.
- Cosine Similarity calculation.
- Interactive Streamlit interface.
- Deployed application using Render.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | TF-IDF and similarity calculation |
| NLP | Text feature processing |
| Streamlit | Web application |
| Pickle | Movie data serialization |
| Joblib | Similarity matrix storage |
| Render | Deployment |

## 🧠 How It Works

**1. Text Processing**

Movie-related textual information is prepared for feature extraction.

**2. TF-IDF Vectorization**

TF-IDF (Term Frequency–Inverse Document Frequency) converts textual movie information into numerical vectors.

**3. Cosine Similarity**

Cosine Similarity measures the similarity between movie feature vectors.

**4. Movie Recommendation**

The system identifies movies with the highest similarity scores and displays the top 5 recommendations.

## 📂 Project Structure

```text
Movie-Recommendation_system/
│
├── README.md
├── app.py
├── movies.pickle
├── similarities.joblib
└── requirements.txt
```

## ⚙️ Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/ranjith-boggula/Movie-Recommendation_system.git
```

**Step 2: Navigate to the project folder**

```bash
cd Movie-Recommendation_system
```

**Step 3: Create a virtual environment**

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

**Step 4: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 5: Run the application**

```bash
streamlit run app.py
```

The application will open in your browser using the local Streamlit URL.

## 📸 Application Screenshots

Add screenshots of your application here to demonstrate the user interface and movie recommendations.

## 🎯 Key Learning Outcomes

- Understanding NLP concepts and text feature extraction.
- Implementing TF-IDF Vectorization.
- Applying Cosine Similarity.
- Developing content-based recommendation systems.
- Building interactive applications using Streamlit.
- Deploying machine learning applications using Render.
- Managing projects using GitHub.

## 👨‍💻 Developer

**Boggula Ranjith**

GitHub: [ranjith-boggula](https://github.com/ranjith-boggula)

## 🔗 Project Links

- **Live Demo:** https://movie-recommendation-system-2-olws.onrender.com/
- **GitHub Repository:** https://github.com/ranjith-boggula/Movie-Recommendation_system

---

⭐ If you find this project useful, feel free to explore the repository!
