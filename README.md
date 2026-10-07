# StudySpot

A small product project by **Pranjal**.

StudySpot helps students choose a place to study based on what matters to them that day: quiet, Wi-Fi, seating, and whether they are working alone or with a group.

## Why I built it

I noticed that choosing a study location is a small but repeated decision. A library can be great for focused work but bad for a group meeting, while a cafe can have the opposite problem. I wanted to test whether a lightweight recommendation tool could make that decision faster.

## MVP

The first version intentionally stays simple. A user selects a few preferences and StudySpot ranks a small set of locations using a weighted score. I chose transparent scoring instead of a complicated ML model because an early product needs to prove the problem is useful before adding technical complexity.

## Product process

1. Define the student problem and assumptions.
2. Write a short PRD and choose the MVP.
3. Prioritize only the inputs needed for a useful recommendation.
4. Build the recommendation logic in Python/Streamlit.
5. Test with students and record real feedback.
6. Improve the weights/features based on what users actually care about.

See `docs/PRD.md`, `docs/ROADMAP.md`, and `docs/USER_RESEARCH.md`.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tech

- Python
- pandas
- Streamlit
- CSV sample data

## What I would measure

For an actual pilot, I would track recommendation acceptance (did the user choose one of the suggested places?), repeat use, and a simple 1–5 usefulness rating. I have not claimed these results because this repository currently uses sample data and has not been launched to real users.

## Business idea

The student version would stay free. If the concept proved useful, a university could potentially sponsor a campus version containing live library/campus-space information. This is only a hypothesis to test, not a validated business model.

## Next step

Test the MVP with 5–10 students and replace the assumptions in `USER_RESEARCH.md` with actual findings.
