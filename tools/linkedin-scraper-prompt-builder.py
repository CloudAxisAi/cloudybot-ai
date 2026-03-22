"""
LinkedIn Scraper Prompt Builder
--------------------------------
Generates a structured, optimised LinkedIn search prompt from your
Ideal Customer Profile (ICP) inputs.

Use the output with CloudyBot (cloudybot.ai) or any AI agent
that supports browser automation.

Usage:
    python linkedin-scraper-prompt-builder.py
    python linkedin-scraper-prompt-builder.py --example

No dependencies. Pure Python stdlib.
"""


def build_linkedin_prompt(
    job_titles: list,
    locations: list,
    industries: list,
    company_sizes: list,
    count: int = 20,
    output_fields: list = None,
    extra_filters: str = "",
) -> str:
    if output_fields is None:
        output_fields = [
            "Full name",
            "Job title",
            "Company name",
            "Company size (employees)",
            "LinkedIn profile URL",
            "Location",
            "One sentence about what their company does",
        ]

    titles_str = " OR ".join(f'"{t}"' for t in job_titles)
    locations_str = ", ".join(locations)
    industries_str = ", ".join(industries)
    sizes_str = ", ".join(company_sizes)
    fields_str = "\n".join(f"- {f}" for f in output_fields)

    prompt = f"""Go to LinkedIn and find {count} people who match the following criteria:

**Job Title:** {titles_str}
**Location:** {locations_str}
**Industry:** {industries_str}
**Company Size:** {sizes_str} employees
{f"**Additional filters:** {extra_filters}" if extra_filters else ""}

For each person, return the following fields:
{fields_str}

Format the results as a markdown table, sorted by company size (largest first).
If a field is not available, write "N/A".
After the table, add a brief summary of patterns you noticed."""

    return prompt


def interactive_builder():
    print("\n=== LinkedIn Prompt Builder ===\n")

    titles_input = input("Job titles (comma-separated, e.g. CTO, VP Engineering): ")
    job_titles = [t.strip() for t in titles_input.split(",") if t.strip()]

    locations_input = input("Locations (comma-separated, e.g. United Kingdom, London): ")
    locations = [l.strip() for l in locations_input.split(",") if l.strip()]

    industries_input = input("Industries (comma-separated, e.g. SaaS, Fintech): ")
    industries = [i.strip() for i in industries_input.split(",") if i.strip()]

    sizes_input = input("Company sizes (comma-separated, e.g. 10-50, 50-200): ")
    company_sizes = [s.strip() for s in sizes_input.split(",") if s.strip()]

    count_input = input("How many leads? (default 20): ").strip()
    count = int(count_input) if count_input.isdigit() else 20

    extra = input("Extra filters? (leave blank to skip): ").strip()

    prompt = build_linkedin_prompt(job_titles, locations, industries, company_sizes, count, extra_filters=extra)

    print("\n" + "=" * 60)
    print("YOUR PROMPT — paste into CloudyBot (cloudybot.ai):")
    print("=" * 60)
    print(prompt)
    print("=" * 60)

    return prompt


EXAMPLE_PROMPT = build_linkedin_prompt(
    job_titles=["CTO", "Head of Engineering", "VP Engineering"],
    locations=["United Kingdom", "Ireland"],
    industries=["SaaS", "Fintech", "B2B Software"],
    company_sizes=["10-50", "50-200"],
    count=25,
    extra_filters="posted on LinkedIn in the last 30 days",
)

if __name__ == "__main__":
    import sys
    if "--example" in sys.argv:
        print(EXAMPLE_PROMPT)
    else:
        interactive_builder()
