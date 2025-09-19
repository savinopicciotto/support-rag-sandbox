# Support RAG Sandbox

Goal: answer 10 gold support questions with citations from the help center and macros.

- Data: 150 articles, 30 macros
- Stack: Python, Vector DB, Render or Cloud Run, Postman
- Gold questions: 10/10 (target)

## Demo hub
- Live demo: https://example-demo-link
- 90-sec Loom: https://example-loom-link

If the app is cold on free hosting, first load may take 20 to 40 seconds.

## How to run locally
1. Python 3.11 recommended
2. `python -m venv .venv && source .venv/bin/activate` (Windows: `.\.venv\Scripts\activate`)
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and set values
5. `uvicorn app:app --reload`
6. Visit http://localhost:8000

## API
- `POST /ask` – body: `{ "query": "How do I reset my password?" }`
- returns: `{ "answer": "...", "citations": ["docs/123"] }`

## Proof moments to show
- Synonym match returns a cited answer
- Hover or click shows the citation source
- After adding one new doc, re-run shows improvement on a target question

## Next steps
Share a CSV or HTML export of help docs and macros. I will return a mini POC with a MAP (Mutual Action Plan).