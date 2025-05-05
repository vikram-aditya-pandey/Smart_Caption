# 📸 Smart Image Caption Generator

A **Streamlit web app** that generates Instagram-style captions for your uploaded images using a locally hosted **Ollama LLaVA model** (vision-language model). Add optional context to tailor your captions for vacations, events, or product posts!

---

## 🚀 Features

* Upload any `.jpg`, `.jpeg`, or `.png` image
* Get natural-language captions for Instagram or other social media
* Optional: Add custom context for more relevant captioning
* Uses the **LLaVA** model via **Ollama** running locally

---

## 🖼️ How It Works

1. Upload an image via the Streamlit interface
2. (Optionally) enter context like *“sunset at the beach”*
3. The app sends the image and prompt to the **Ollama LLaVA model** running at `localhost:11434`
4. Displays a smart caption based on the image and context

---

## 🛠️ Requirements

* Python 3.8+
* Streamlit
* Requests
* Ollama installed with the `llava` model running locally

Install dependencies:

```bash
pip install streamlit requests
```

Start Ollama with LLaVA:

```bash
ollama run llava
```

---

Make sure Ollama is running locally at the same time on port `11434`.

---

## 💡 Example Use Cases

* Generating captions for Instagram or marketing posts
* Content creation for photography pages
* Automated alt-text generation for accessibility

---

## ⚠️ Notes

* This app requires **Ollama** to be installed and running locally. Learn more at [ollama.com](https://ollama.com).
* Ensure the `llava` model is pulled with `ollama pull llava` if you haven’t done so already.

