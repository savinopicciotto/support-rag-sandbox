# Support RAG Sandbox - 3 Proof Moments

**Watch 90 sec:** https://www.loom.com/share/2b97ef1f9b204054ae7cec6c1d21cf8c?sid=6da15a56-984c-46e1-929e-89f45f78d616  
**Try the demo:** https://savinopicciotto.github.io/support-rag-sandbox/  
**Book 15 min:** https://calendly.com/savinop/intro?utm_source=rag-sandbox&utm_medium=demo&utm_campaign=90s

## What this shows
1. Miss → fix: toggle a doc off, re-run, add it back, re-run.
2. Zendesk-ready reply with source citation.
3. Trace view: tokens, synonyms, and scoring.

## How to try it
- Click **Test 1/2/3** or type a query like **change address**.  
- Use the **Simulate a miss and fix** toggle to prove relevance.  
- Click **Copy** on the reply block.

## Run locally (optional API)
1. Python 3.11 recommended  
2. `python -m venv .venv && source .venv/bin/activate`  (Windows: `.\.venv\Scripts\activate`)  
3. `pip install -r requirements.txt`  
4. Copy `.env.example` to `.env` and set values  
5. `uvicorn app:app --reload`  
6. Visit http://localhost:8000

## Repo
Source: https://github.com/savinopicciotto/support-rag-sandbox
