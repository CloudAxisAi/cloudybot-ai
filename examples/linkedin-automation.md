# Example: LinkedIn Lead Research with CloudyBot

Full walkthrough — finding 20 targeted leads without manually browsing LinkedIn.

**Manual time:** ~3 hours | **With CloudyBot:** ~12 minutes

---

## The Task

Paste this into CloudyBot:

```
Go to LinkedIn and find 20 CTOs at B2B SaaS companies based in the United Kingdom.
For each person return:
- Full name
- Company name
- Company size (employees)
- LinkedIn profile URL
- One sentence about what their company does

Format the results as a table.
```

---

## What CloudyBot Does

1. Opens a cloud browser
2. Navigates to LinkedIn search with filters: title = CTO, location = UK, industry = SaaS
3. Visits each profile to collect the required fields
4. Compiles into a structured table

---

## Sample Output

| Name | Company | Size | LinkedIn | What They Do |
|---|---|---|---|---|
| James T. | Acme SaaS | 50–200 | linkedin.com/in/... | Expense management for SMEs |
| Sarah M. | DataFlow | 10–50 | linkedin.com/in/... | Data pipeline automation |

---

## Export

Type: `Export this as a CSV` — CloudyBot returns a downloadable file.

---

## Chain It

```
For each person in this table, draft a personalised LinkedIn connection request
based on their company's product and size. Keep each message under 300 characters.
```

20 unique messages. No template spam.

---

[cloudybot.ai](https://cloudybot.ai) — free tier, no credit card needed.
