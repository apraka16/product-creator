---
name: compete-research
description: Conduct competitive research and analysis when users want to understand the competitive landscape for a product feature or idea. Use this skill whenever the user mentions competitive research, competitor analysis, wants to know what similar products exist in the market, or asks to compare their product idea with existing solutions. Trigger on phrases like "research our competitors", "do competitive analysis", "what products compete with X", "competitive landscape for Y", or "compare our product to competitors".
---

# Competitive Research

## Overview

This skill helps you conduct thorough competitive research when the user describes a product feature or idea they want to develop. You'll search the internet to discover competitive products, gather relevant details about them, and compile findings into a structured competitive research document.

## Workflow

When a user requests competitive research, follow these steps:

### Step 1: Clarify the Product Feature

Ensure you understand what the user wants to research:
- What product or feature are they building?
- What problem does it solve?
- What's the target audience or use case?
- Any specific competitors they already know about?

Ask clarifying questions till the time you are able to understand enough about the product or feature they are building so that you are able to do rest of your job. Hence, if unclear, ask clarifying questions before proceeding.

### Step 2: Search for Competitors

Use WebSearch to find competing products and solutions:
- Search for the product category, problem space, and use case keywords
- Look for direct competitors (same solution approach)
- Look for indirect competitors (different approach, same problem)
- Search for industry reviews, comparison articles, and "alternatives to X" content
- Search for user reviews of competitor products from Reddit or other websites as fit

Cast a wide net initially - you can narrow down later.

### Step 3: Gather Detailed Information

For each relevant competitor found, use WebFetch to gather details:
- Product name and company
- Core features and capabilities
- Pricing model (free, freemium, paid tiers)
- Target audience
- Key differentiators
- Strengths and weaknesses (from reviews, comparison sites)
- Technology stack or approach (if relevant and available)
- URLs from where details have been gathered (tag numerals in superscript next to each detail, and add URLs under footnote as references when creating the final report)

Focus on information that would help the user understand the competitive landscape and make informed product decisions.

### Step 4: Analyze and Synthesize

Review all gathered information and identify:
- Common patterns across competitors
- Gaps in the market (problems not well-solved)
- Differentiation opportunities
- Pricing trends
- Feature tables or matrices that compare competitors

### Step 5: Create the Competitive Research Document

Generate a well-structured markdown file with your findings. It must be concise and should NOT exceed 1500 words. 

## Output Format

The output should follow the following format:
### Executive Summary
The executive summary will have three specific points:
- Summary in 1-2 lines of the competitive landscape. 
- Add a concise paragraph on key success factors - what is needed for a win in the market.
- Add a concise paragraph on the market gaps, meaning what either doesn't exist in the market and it should be, or what exists in the market but users' painpoint can be solved in a better way. 

### Competitive Landscape Overview
Broad segment or slicing of all competitor products. Few of such slicing can be:
- By market it serves - mid market, SMBs, commercial market
- By enterprise solution vs B2C solution
- By pricing point 
- By user segment

Choose one slice which is more significant than the rest

### Competitor Profiles
Profiles of top 5 competitors with SWOT (strengths, weaknesses, opportunities and threats) along with pricing, and a key factor of why this competition is a important in this space

The output should be:
- Concise but comprehensive
- Well-organized and easy to scan
- Focused on actionable insights
- Include sources/links where appropriate

### Feature Comparison Matrix
This is optional. If there is a value in adding a feature matrix beyond what you have covered in the Competitor Profiles section, then add the feature matrix. Otherwise, do not. 

### Market Gaps & Opportunities
List down key gaps and opportunities as identified from above sections. Relate it to how/ why Salesforce can be better equipped to do fill in each gap and/ or win the opportunities. 
If competitors are better at a gap/ opportunity than Salesforce is/ can be, point that out too. 

### Go to Market - MVP and Phases
Add broad strokes of how the product feature can be rolled into phases. The MVP must be the first phase. Add reasons to your phased recommendations, meaning if a certain aspect of the product needs to be in MVP, why should it be in the MVP. 

The output document should have a filename - `compete-research-` + {product name}.md and must be stored in `research/` folder. 

## Notes

- ALWAYS cite sources with links/ URLs so the user can verify information
- Be thorough but concise - focus on actionable competitive intelligence
- Brevity is always better
- Do not repeat any information in the output document
- Do NOT create any new data or information by yourself if you are not able to find a data or information 
- If information isn't publicly available, note that in the research document
- Consider both direct and indirect competitors
- Look for recent information (past 1-2 years) when possible to ensure relevance