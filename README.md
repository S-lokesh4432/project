# 🌟 Motivational Quote Generator using Gemini AI

This is a web-based application that generates motivational quotes based on user input using Google's Gemini AI. It transforms the generated quote into a beautiful, shareable image with a scenic background and a clean design.

## 🚀 Features

- 🔮 AI-generated motivational quotes using Gemini
- 🖼️ Converts quotes into images with scenic backgrounds
- 🧊 Semi-transparent overlay for readability
- 🎨 Streamlit-based interface with Lottie animations
- 📥 One-click image download
- 💡 User-friendly and aesthetic UI

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit  
- **AI Model**: Google Gemini 1.5 Flash  
- **Image Rendering**: Pillow (PIL)  
- **Animation**: LottieFiles  
- **Language**: Python 3

## 📦 Installation

1. **Clone the Repository**
```bash
git clone (https://github.com/S-lokesh4432/project.git)
cd motivation-generator
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
Your requirements.txt should contain:
 streamlit
 google-generativeai
 pillow
 streamlit-lottie
 requests
```

3. **Set Your Gemini API Key**
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

4. **Run the App**
```bash
streamlit run motivation_app.py
```

## 🧱 Project Structure

```
motivation-generator/
├── motivation_app.py           # Main Streamlit app
├── assets/                     # (Optional) Custom Lottie or images
├── requirements.txt
└── README.md
```

## 🔍 Example Prompts

- "confidence"
- "exam preparation"
- "career growth"
- "mental peace"

## 🚧 Future Enhancements

- Let users upload custom backgrounds  
- Add multilingual quote generation  
- Share directly to Instagram or Twitter  
- Save quote history locally  
- Daily quote notifications

## 👨‍💻 Author

S.Lokesh 
Student Developer | AI Enthusiast

## 🙏 Acknowledgments

- [Google Gemini API](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [LottieFiles](https://lottiefiles.com/)
- [Unsplash](https://unsplash.com/) for background images
