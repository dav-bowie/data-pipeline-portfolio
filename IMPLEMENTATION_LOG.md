# Implementation Log — Data Pipeline Portfolio

**Purpose:** Historical record of what was built, when, and how. Use this when pulling up records to understand the project's current state and history.

---

## 1. Project Overview

| Field | Value |
|-------|-------|
| **Repository** | `data-pipeline-portfolio` |
| **GitHub URL** | https://github.com/dav-bowie/data-pipeline-portfolio |
| **GitHub Username** | dav-bowie |
| **Local Path (primary)** | `/Users/db/Desktop/DataAnalyst/data-pipeline-portfolio-repo` |
| **Local Path (backup)** | `/Users/db/Desktop/DataAnalyst/data-pipeline-portfolio` |

---

## 2. Folder Structure Implemented

```
data-pipeline-portfolio/
├── README.md                 # Main showcase — project overview, tech stack, how to run
├── index.html                # Portfolio landing page (GitHub Pages)
├── roadmap.html              # Full data pipeline mastery roadmap
├── requirements.txt          # Python dependencies for Streamlit
├── .gitignore               # Excludes .env, __pycache__, venv
├── IMPLEMENTATION_LOG.md     # This file
│
├── projects/
│   ├── saas-revenue/         # Project 01 — SaaS Revenue & Churn Pipeline
│   │   └── README.md
│   ├── ecommerce/            # Project 02 — E-Commerce Sales Intelligence
│   │   └── README.md
│   ├── data-quality/         # Project 03 — Data Quality Watchdog
│   │   └── README.md
│   ├── soccer-analytics/     # Project 04 — Soccer Analytics
│   │   └── README.md
│   └── live-dashboard/       # Project 05 — Live Financial Dashboard
│       └── README.md
│
├── dashboards/
│   └── app.py                # Streamlit app — MoM Revenue line chart
│
├── data/
│   └── revenue.csv           # Sample 12-month revenue data
│
├── pipelines/                # For N8N workflow JSON exports
│   └── .gitkeep
├── notebooks/                # For Jupyter EDA notebooks
│   └── .gitkeep
└── sql/                      # SQL scripts and schemas
    └── .gitkeep
```

---

## 3. Files Created & Their Purpose

| File | Purpose |
|------|---------|
| `index.html` | Portfolio landing page. Links to roadmap, projects (GitHub), and live dashboards. |
| `roadmap.html` | Full data pipeline mastery roadmap. Tabs: Roadmap, Tech Stack, Projects, Repo + Website, N8N Pipelines, Skills Plan, Soccer. Contains `PORTFOLIO` config object for live links. |
| `dashboards/app.py` | Streamlit app. Uses `Path(__file__)` for data path so it works locally and on Streamlit Cloud. Plots `data/revenue.csv` as MoM line chart. |
| `data/revenue.csv` | Sample CSV: `month`, `revenue` columns. 12 months of synthetic data. |
| `requirements.txt` | `streamlit`, `pandas`, `plotly`, `sqlalchemy`, `psycopg2-binary` |
| `.gitignore` | `.env`, `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `.env.local`, `.DS_Store` |
| `projects/*/README.md` | Template per project: Objective, Architecture, Key Findings, Tech Stack, Live Demo, How to Run |

---

## 4. Live URLs (as of Implementation)

| Resource | URL | Status |
|----------|-----|--------|
| GitHub Repo | https://github.com/dav-bowie/data-pipeline-portfolio | Live |
| Portfolio (GitHub Pages) | https://dav-bowie.github.io/data-pipeline-portfolio/ | Live |
| Roadmap (GitHub Pages) | https://dav-bowie.github.io/data-pipeline-portfolio/roadmap.html | Live |
| Streamlit Dashboard | https://dav-bowie-datapipeline.streamlit.app | Configured (first deploy pending) |

---

## 5. What Was Implemented (Chronological)

### Phase 1 — Repo & Structure
- Created folder structure per roadmap instructions
- Set up `projects/`, `dashboards/`, `pipelines/`, `notebooks/`, `sql/`, `data/`
- Added project README templates with Objective, Architecture, Key Findings, Tech Stack, Live Demo, How to Run

### Phase 2 — Streamlit App
- Created `dashboards/app.py` with Plotly line chart
- Added `data/revenue.csv` (sample MoM revenue)
- Used `Path(__file__).parent.parent / "data" / "revenue.csv"` for cross-platform and Streamlit Cloud compatibility

### Phase 3 — GitHub Integration
- Cloned repo `https://github.com/dav-bowie/data-pipeline-portfolio.git` into `data-pipeline-portfolio-repo`
- Copied full structure into cloned repo
- Updated all placeholders (`yourname`, `yourusername`) to `dav-bowie`

### Phase 4 — Portfolio Website
- Created `index.html` with project links (GitHub repo tree URLs)
- Added "Learning Roadmap" button → `roadmap.html`
- Project cards link to GitHub project folders

### Phase 5 — Roadmap (Active Links)
- Added `roadmap.html` from `data-analytics-roadmap.html`
- Introduced `PORTFOLIO` config object at top of script for centralized URLs
- Project cards 01–05 link to GitHub project folders via config
- Hero: Live Portfolio, Live Dashboard buttons
- Footer: My Repo, Live Dashboard, Portfolio Site links
- Copied `roadmap.html` into portfolio repo

### Phase 6 — GitHub Pages
- GitHub Pages enabled: Source = main branch, Path = / (root)
- Portfolio and roadmap confirmed live

### Phase 7 — Streamlit Community Cloud (Connected to GitHub)
- Connected Streamlit Community Cloud to GitHub repo: `dav-bowie/data-pipeline-portfolio`
- Branch: `main`
- Main file path: `dashboards/app.py`
- Selected app subdomain: `dav-bowie-datapipeline` (domain shown as available at setup time)
- Note: credentials/tokens are **not** stored in this repo; keep secrets in Streamlit “Secrets” and/or local `.env` (already gitignored)

---

## 6. Configuration Reference

### Roadmap `PORTFOLIO` Object (in `roadmap.html`)

```javascript
const PORTFOLIO = {
  repo: 'https://github.com/dav-bowie/data-pipeline-portfolio',
  portfolio: 'https://dav-bowie.github.io/data-pipeline-portfolio',
  streamlit: 'https://dav-bowie.streamlit.app',
  projects: {
    saas: '.../projects/saas-revenue',
    ecommerce: '.../projects/ecommerce',
    dataQuality: '.../projects/data-quality',
    soccer: '.../projects/soccer-analytics',
    liveDashboard: '.../projects/live-dashboard',
    dashboards: '.../dashboards',
    pipelines: '.../pipelines',
    notebooks: '.../notebooks'
  }
};
```

Update this object when adding new projects or changing URLs.

---

## 7. Pending / Not Yet Done

| Item | Notes |
|------|-------|
| Streamlit Cloud deploy | Streamlit app configured (repo/branch/path set). Complete first deploy + verify app loads at `https://dav-bowie-datapipeline.streamlit.app`. |
| Supabase setup | Optional. Connection string in `.env`; add `.env` to `.gitignore` (already done) |
| Project content | Fill in each `projects/*/README.md` with real objectives, architecture, findings |
| N8N pipelines | Add workflow JSON exports to `pipelines/` |
| Notebooks | Add Jupyter EDA notebooks to `notebooks/` |
| SQL scripts | Add SQL scripts/schemas to `sql/` |

---

## 8. Local Commands Reference

```bash
# Navigate to repo
cd /Users/db/Desktop/DataAnalyst/data-pipeline-portfolio-repo

# Install dependencies
pip install -r requirements.txt

# Run Streamlit locally
streamlit run dashboards/app.py

# Git push (after changes)
git add .
git commit -m "Description of changes"
git push
```

---

## 9. Key Decisions Made

| Decision | Reason |
|----------|--------|
| Project links go to GitHub | GitHub Pages doesn’t render subfolder READMEs; GitHub tree URLs work reliably |
| `Path(__file__)` for data path | Ensures app works locally and on Streamlit Cloud |
| Centralized `PORTFOLIO` config in roadmap | One place to update all live links |
| Two local folders | `data-pipeline-portfolio` = original; `data-pipeline-portfolio-repo` = git-tracked clone |

---

*Last updated: March 9, 2026*
