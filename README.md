# Support RAG Sandbox
**Book 15 min:** https://calendly.com/savinop/intro

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

**POST** `/ask`

#### Headers
`Content-Type: application/json`

#### Body
~~~json
{ "query": "how do I reset my password?" }
~~~

#### Response (200)
~~~json
{
  "answer": "You can reset your password at ...",
  "citations": ["https://help.example.com/account/password-reset"],
  "sources": 3
}
~~~

#### Errors (examples)
~~~json
{ "error": "missing field: query" }
~~~
~~~json
{ "error": "upstream vector store unavailable" }
~~~

#### curl
~~~bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query":"how do I reset my password?"}'
~~~

## Proof moments
1. **Cited answer** - returns the policy with inline citations.
2. **Synonym handling** - “auto-ship” maps to “subscription” and still answers.
3. **Miss + fix** - show Logs, add a synonym or doc tag, re-ask and it works.
4. **Macro handoff** - suggests an agent macro when policy requires an action.
5. **Source drill-down** - click a citation to open the exact doc + date.

## Gold questions (10)
1) Cancel subscription  
2) Change shipping address  
3) Refund window  
4) Start a return  
5) Exchange policy  
6) Warranty / defects  
7) Track my order  
8) Update payment method  
9) Account deletion / GDPR  
10) Shipping times and cost

## Acceptance tests
- **AT-1 Cancel subscription**  
  Input: “cancel auto-ship”  
  Expect: policy steps + at least 1 citation to the subscription doc.

- **AT-2 Change address after order**  
  Input: “change shipping address”  
  Expect: allowed or not allowed, time window, link to policy doc.

- **AT-3 Refund window**  
  Input: “how long for a refund?”  
  Expect: number of days + condition(s) + citation.

- **AT-4 Returns**  
  Input: “start a return”  
  Expect: step list + portal link if available + citation.

- **AT-5 Warranty**  
  Input: “item arrived defective”  
  Expect: warranty length + proof required + macro suggestion if relevant.


See [ACCEPTANCE_TESTS.md](./ACCEPTANCE_TESTS.md) for step-by-step checks.


License: [MIT](./LICENSE)
