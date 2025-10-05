<!--
  SpaceXBio README
  English + Arabic overview and setup instructions for the SpaceXBio project scaffold.
  الغرض: توثيق شامل للمشروع SpaceXBio مع تعليمات الإعداد والتشغيل محلياً وعبر Docker.
-->

# SpaceXBio — AI-Powered Space Biology Knowledge Engine (Scaffold)

This repository contains the seed files to drive automatic code generation in Cursor or any AI code generator, producing a complete SpaceXBio web application that integrates AI research tools, virtual labs, biological data visualization, and educational features inspired by NASA’s open space biology datasets.

هذه المستودع يحتوي على ملفات تمهيدية لتوليد كود مشروع SpaceXBio كاملاً عبر Cursor أو أي مولد كود ذكي، مع دمج أدوات بحث بالذكاء الاصطناعي ومعامل افتراضية وعرض بيانات حيوية وميزات تعليمية مستوحاة من بيانات ناسا المفتوحة.

## Contents

- `PROMPT.md`: A single, copy-ready prompt for Cursor to generate the full, runnable project with 10k+ lines of code.
- `.env.example`: Environment variable placeholders required by the generated system.

## How to Use

1. Open this repository in Cursor.
2. Open `PROMPT.md`, copy the entire prompt between “BEGIN PROMPT” and “END PROMPT”.
3. Paste it into a new Cursor chat and run. Cursor will generate the complete `spacexbio` project structure and code.

كيفية الاستخدام (عربي):
1. افتح هذا المستودع في Cursor.
2. انسخ المحتوى الكامل داخل `PROMPT.md` بين “BEGIN PROMPT” و “END PROMPT”.
3. الصق النص في محادثة جديدة داخل Cursor وشغّل التوليد.

## Notes

- The final generated project will include: Next.js + TypeScript frontend, FastAPI backend, AI/ML stubs, datasets, tests, Docker setup, and CI/CD workflow.
- This seed repo itself is minimal by design; it orchestrates generation of the full codebase via the provided prompt.

ملاحظات (عربي):
- المشروع النهائي الناتج سيتضمن واجهة Next.js، وواجهة خلفية FastAPI، ونماذج AI/ML تمهيدية، وبيانات تجريبية، واختبارات، وDocker، وCI/CD.
- هذا المستودع بذاته صغير، الهدف منه تشغيل توليد المشروع الكامل عبر النص في `PROMPT.md`.



