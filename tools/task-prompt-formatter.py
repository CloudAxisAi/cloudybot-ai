"""
Task Prompt Formatter
----------------------
Turns a vague task description into a structured, AI-ready prompt.

AI agents perform significantly better with clear, specific, well-formatted tasks.
This tool adds that structure automatically.

Usage:
    python task-prompt-formatter.py
    python task-prompt-formatter.py --template competitor_research

No dependencies. Pure Python stdlib.
"""


def format_task_prompt(raw_input, output_format="markdown table", constraints=None, steps=None):
    """
    Format a raw task description into a structured AI prompt.

    Args:
        raw_input:      Your original task description
        output_format:  How you want the result (e.g. "markdown table", "bullet list", "JSON")
        constraints:    List of rules or limits
        steps:          List of explicit steps (optional)

    Returns:
        A well-structured prompt string.
    """
    constraints = constraints or []
    steps = steps or []

    lines = [f"**Task:** {raw_input}\n"]

    if steps:
        lines.append("**Steps:**")
        for i, step in enumerate(steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    lines.append(f"**Output format:** {output_format}\n")

    if constraints:
        lines.append("**Constraints:**")
        for c in constraints:
            lines.append(f"- {c}")
        lines.append("")

    lines.append(
        "If any step fails or information is unavailable, note it clearly "
        "rather than skipping or guessing."
    )

    return "\n".join(lines)


TEMPLATES = {
    "competitor_research": {
        "goal": "Research the top {count} competitors of {product} in the {market} market.",
        "steps": [
            "Search Google for '{product} competitors' and '{market} alternatives'",
            "Visit each competitor's website and pricing page",
            "Identify key features and target audience",
            "Check G2 or Capterra for average rating and top complaints",
        ],
        "output_format": "markdown table with a 'Gaps & Opportunities' section",
        "constraints": [
            "Only include actively maintained products",
            "If pricing is not public, write 'Contact for pricing'",
        ],
    },
    "linkedin_research": {
        "goal": "Find {count} {job_title}s at {industry} companies in {location}.",
        "steps": [
            "Search LinkedIn with the specified filters",
            "Visit each profile",
            "Collect: full name, company, size, LinkedIn URL, one-sentence company description",
        ],
        "output_format": "markdown table sorted by company size",
        "constraints": [
            "Only include profiles with a profile photo",
            "Skip profiles inactive for 6+ months",
        ],
    },
    "web_scraping": {
        "goal": "Scrape {data_type} from {url}.",
        "steps": [
            "Navigate to the target URL",
            "Identify and extract all relevant data",
            "If paginated, continue to next pages until complete",
        ],
        "output_format": "CSV-ready table",
        "constraints": [
            "Do not submit forms or click purchase buttons",
            "If login is required, stop and report",
        ],
    },
}


def get_template(name):
    t = TEMPLATES.get(name)
    if not t:
        return None
    return format_task_prompt(
        raw_input=t["goal"],
        output_format=t["output_format"],
        constraints=t["constraints"],
        steps=t["steps"],
    )


def interactive_formatter():
    print("\n=== Task Prompt Formatter ===\n")

    raw = input("Describe your task (can be rough): ").strip()
    fmt = input("Output format (e.g. 'table', 'bullet list', 'JSON') [default: markdown table]: ").strip()
    fmt = fmt or "markdown table"

    constraints_input = input("Any constraints? (comma-separated, leave blank to skip): ").strip()
    constraints = [c.strip() for c in constraints_input.split(",") if c.strip()] if constraints_input else []

    prompt = format_task_prompt(raw, output_format=fmt, constraints=constraints)

    print("\n" + "=" * 60)
    print("YOUR FORMATTED PROMPT:")
    print("=" * 60)
    print(prompt)
    print("=" * 60)
    print("\nPaste into CloudyBot (cloudybot.ai) or any AI agent.")

    return prompt


if __name__ == "__main__":
    import sys
    if "--template" in sys.argv:
        idx = sys.argv.index("--template")
        name = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        result = get_template(name)
        if result:
            print(result)
        else:
            print(f"Template '{name}' not found. Available: {', '.join(TEMPLATES.keys())}")
    else:
        interactive_formatter()
