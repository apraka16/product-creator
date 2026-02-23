import re

def grade_report(output: str, checks: dict) -> dict:
    """Code based grading returns pass/ fail + actionable feedback"""
    results = {
        "passed": [],
        "failed": [],
        "feeback": []
    }

    def count_words(text: str) -> int:
      # Remove code blocks
      text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
      # Remove inline code
      text = re.sub(r'`[^`]+`', '', text)
      # Remove markdown links [text](url)
      text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
      # Count words
      return len(re.findall(r'\b\w+\b', text))

    # Check if executive summary is available in the report
    if checks.get("has_executive_summary"):
        if "## Executive Summary" in output or "# Executive Summary" in output:
            results["passed"].append("has_executive_summary")
        else:
            results["failed"].append("has_executive_summary")
            results["feedback"].append("ADD: Executive Summary section at the top")
    
    # Check competitor count
    if checks.get("min_competitors"):
          competitor_count = output.lower().count("competitor:")
          if competitor_count >= checks["min_competitors"]:
              results["passed"].append("min_competitors")
          else:
              results["failed"].append("min_competitors")
              results["feedback"].append(f"ADD: Found {competitor_count} competitors, need {checks['min_competitors']}")
    
    # Check if executive summary is available in the report
    if checks.get("has_pricing_section"): 
        if "## Pricing" in output or "### Pricing" in output:
            results["passed"].append("has_pricing_section")
        else: 
            results["failed"].append("has_pricing_section")
            results["feedback"].append("ADD: Pricing section for each competition")

    # Check if word count is within a boundary 1000 to 2000
    if checks.get("min_word_count") and checks.get("max_word_count"):
        if count_words(output) > checks.get("min_word_count") and count_words(output) < checks.get("max_word_count"):
            results["passed"].append("min_word_count")
            results["passed"].append("max_word_count")
        else:
            results["failed"].append("min_word_count")
            results["failed"].append("max_word_count")
            results["feedback"].append(f"REDO: Report word length should be within {checks["min_word_count"]} and {checks["max_word_count"]}")
