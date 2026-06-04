# AI Real-Time Gym Coach

AI Real-Time Gym Coach is a computer vision based fitness application that helps users perform workouts with real-time feedback using a webcam.

The system detects body posture, counts repetitions automatically, tracks workout progress, and stores exercise history for future reference.

## Live Demo

🌐 https://gymai.alokteh.in

## Features

* Real-time pose detection and exercise tracking
* Automatic repetition counting
* Multiple exercise support
* AI-powered workout coaching
* Voice feedback during workouts
* User login system
* Workout history and progress tracking
* Responsive web interface

## Supported Exercises

* Squats
* Push-ups
* Lunges
* Shoulder Press
* Biceps Curls

## Tech Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### Computer Vision & AI

* MediaPipe
* OpenCV
* Groq API

### Database

* Supabase

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

Run the application:

```bash
streamlit run main.py
```

## Author

Alok Kumar

Feel free to explore the project and share your feedback.
