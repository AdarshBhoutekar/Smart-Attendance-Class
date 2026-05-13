# SnapClass

### Attendance, reimagined with AI.

SnapClass is an AI-powered classroom attendance platform built to make attendance faster, smarter, and far less manual. Instead of relying on roll calls, spreadsheets, or repetitive admin work, SnapClass lets teachers manage attendance through face recognition, voice recognition, and simple self-enrollment flows.

Designed as a modern education product, SnapClass combines a clean Streamlit interface with Supabase-backed data storage to create a practical biometric attendance experience for both teachers and students.

---

## Links

- Repository: [SnapClass GitHub](https://github.com/AdarshBhoutekar/SnapClass)
- Live Product: [SnapClass Live Demo](https://snapclass-app.streamlit.app/)
- Product Overview: [Add Overview Link Here](#)

---

## Suggested Repository Name

`snapclass-ai`

---

## Why SnapClass

Attendance is one of the most repetitive tasks in education. It consumes class time, creates administrative overhead, and often depends on manual verification. SnapClass addresses that problem by turning attendance into a lightweight AI workflow.

Teachers can create subjects, share join codes, and mark attendance using classroom photos or voice recordings. Students can log in using face recognition, register once, and join classes through a quick-link experience. The result is a system that feels closer to a modern product than a traditional academic tool.

---

## What the Product Does

SnapClass provides two connected experiences in one application:

### Teacher Experience

- Create and manage subjects
- Share subject access using join codes and QR-supported links
- Run face-based attendance using classroom photos
- Run voice-based attendance using recorded classroom audio
- View attendance summaries and session records

### Student Experience

- Log in with Face ID
- Create a student profile if not already recognized
- Optionally enroll a voice sample for voice attendance
- Join subjects with shared codes or links
- View enrolled subjects and attendance participation

---

## Key Features

- AI-powered attendance using face recognition
- Optional voice-based attendance for enrolled students
- Separate teacher and student portals
- Subject creation and subject-wise attendance management
- Teacher authentication with password hashing
- Student biometric registration flow
- Quick enrollment through join links
- QR code generation for class sharing
- Attendance record storage with timestamps
- Supabase-backed data operations

---

## Product Highlights

### 1. Face Recognition Attendance

Teachers can upload classroom photos and let the system identify which enrolled students are present. The application extracts face embeddings, compares them against stored student profiles, and produces an attendance result set ready to log.

### 2. Voice Attendance

SnapClass also supports a voice-driven attendance workflow. Students can optionally register a voice sample, and teachers can record classroom audio to identify speakers from enrolled voice embeddings.

### 3. Self-Enrollment Flow

Instead of manually adding students to each class, teachers can share a join code or QR-friendly link. Students can use that code to enroll themselves into a subject, making onboarding simpler and faster.

### 4. Clean Dual-Portal Experience

The product is split into dedicated student and teacher flows, which keeps the experience intuitive. Teachers get subject and attendance management tools, while students get enrollment and participation visibility.

### 5. Lightweight Cloud-Backed Architecture

SnapClass uses Streamlit for the application interface and Supabase for cloud data access. This makes the project simple to run, easy to demo, and practical to extend.

---

## Tech Stack

| Category | Technologies | Purpose |
| --- | --- | --- |
| Language | Python | Core development language used across the entire application |
| Frontend / App Layer | Streamlit | Builds the web interface for teacher and student portals |
| Database | Supabase | Stores teachers, students, subjects, enrollments, and attendance logs |
| Face Recognition Stack | dlib, scikit-learn, `face_recognition_models` | Detects faces, generates embeddings, and matches students for attendance |
| Voice Recognition Stack | Librosa, Resemblyzer | Processes classroom audio and identifies enrolled speakers for voice attendance |
| Data Handling | NumPy, Pandas | Supports numerical processing, attendance result preparation, and tabular summaries |
| Image Processing | Pillow | Handles uploaded images used during face-based attendance workflows |
| Security | bcrypt | Hashes teacher passwords before storing them |
| QR / Sharing | Segno | Generates QR codes for quick subject joining and class sharing |

---

## Architecture Overview

The project is organized into small focused modules:

- `screens` handles full-page student, teacher, and home experiences
- `components` contains reusable dialogs and UI blocks
- `pipelines` contains face recognition and voice recognition logic
- `database` manages Supabase configuration and helper methods
- `ui` contains shared styling and layout utilities

This structure keeps product flows separated from AI pipelines and database access, which makes the codebase easier to maintain and scale.

---

## Folder Structure

```text
SnapClass/
|-- app.py
|-- requirements.txt
|-- README.md
`-- src/
    |-- components/
    |   |-- create_subject_dialog.py
    |   |-- dialog_add_photo.py
    |   |-- dialog_attendance_results.py
    |   |-- dialog_auto_enroll.py
    |   |-- dialog_enroll.py
    |   |-- dialog_shared_subject.py
    |   |-- dialog_voice_attendance.py
    |   |-- footer.py
    |   |-- header.py
    |   `-- subject_card.py
    |-- database/
    |   |-- config.py
    |   `-- db.py
    |-- pipelines/
    |   |-- face_pipeline.py
    |   `-- voice_pipeline.py
    |-- screens/
    |   |-- home_screen.py
    |   |-- student_screen.py
    |   `-- teacher_screen.py
    `-- ui/
        `-- base_layout.py
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AdarshBhoutekar/SnapClass.git
cd SnapClass
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Supabase secrets

Create `.streamlit/secrets.toml` and add:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

### 6. Start the app

```bash
streamlit run app.py
```

---

## Expected Database Tables

The current application expects these tables in Supabase:

- `teachers`
- `students`
- `subjects`
- `subject_students`
- `attendance_logs`

These tables support:

- teacher account records
- student biometric profile records
- subject creation and mapping
- enrollment relationships
- attendance history and session logs

---

## User Flow

### Teacher Flow

1. Teacher enters the teacher portal.
2. Teacher logs in or creates an account.
3. Teacher creates subjects.
4. Teacher shares a subject code or link with students.
5. Teacher uploads classroom photos or records audio.
6. SnapClass analyzes the input and generates attendance results.
7. Attendance is saved and available in the records section.

### Student Flow

1. Student enters the student portal.
2. Student logs in using face recognition.
3. If not recognized, the student creates a new profile.
4. Student can optionally enroll a voice sample.
5. Student joins a subject with a code or shared link.
6. Student can view enrolled subjects and attendance-related information.

---

## Where This Project Stands Out

SnapClass is more than a simple attendance tracker. It combines:

- product-style UX with clear teacher and student journeys
- practical AI use cases instead of novelty-only features
- biometric registration plus subject enrollment in one flow
- cloud-backed attendance records for real classroom use

This makes it a strong fit for demos, showcases, academic submissions, and early-stage edtech product concepts.

---

## Optional Improvements

- Add a proper Supabase schema export for one-step setup
- Add admin controls and multi-institution support
- Add analytics dashboards for attendance trends
- Export attendance data to CSV or Excel
- Add confidence scoring and manual review before final logging
- Improve audio preprocessing for noisy classrooms
- Add anti-spoofing or liveness verification for stronger biometric security
- Add automated tests for database helpers and AI pipelines
- Add Docker support for easier deployment
- Add screenshots, mockups, and walkthrough media for presentation use

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Final Note

SnapClass is a strong foundation for an AI-first education workflow. It shows how face recognition, voice recognition, and modern classroom software can come together in a product that saves time, reduces friction, and makes attendance feel effortless.
