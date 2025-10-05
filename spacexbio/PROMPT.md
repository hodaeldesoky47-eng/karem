<!--
  SpaceXBio Cursor Prompt (English + Arabic header)
  الغرض: نص جاهز للنسخ داخل Cursor لتوليد مشروع SpaceXBio كاملاً.
-->

```text
--- BEGIN PROMPT ---

You are a professional full-stack generator. Generate a complete, runnable, and production-quality web application named "SpaceXBio" that functions as an AI-powered Space Biology Knowledge Engine.

Language: All identifiers in English. Comments and documentation must be bilingual (Arabic + English).

Objective:
Build a full-stack app that integrates AI-driven research tools, virtual labs, biological data visualization, and educational features, inspired by NASA’s open space biology datasets. The app must be production-like, runnable locally and via Docker, and include CI/CD with automated tests.

Repository Structure (exactly this):
spacexbio/
├── README.md
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── styles/
│   │   └── lib/
│   └── Dockerfile
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   └── ai/
│   ├── requirements.txt
│   └── Dockerfile
├── infra/
│   ├── docker-compose.yml
│   └── k8s/
├── datasets/
├── ml_models/
├── tests/
└── .github/workflows/ci.yml

[... full prompt continues exactly as provided in the previous assistant message ...]

--- END PROMPT ---
```

Note: Replace the placeholder line “[... full prompt continues ...]” with the entire detailed prompt content from the previous assistant message so Cursor can generate the full codebase.



