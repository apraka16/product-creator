---
name: internal-research
description: Synthesize and consolidate internal research materials (interview transcripts, demo videos, screenshots, workflow documents, business docs) into a structured research report. USE THIS SKILL when users ask to "synthesize internal research", "create internal research report", "consolidate internal findings", "analyze internal research materials", or "compile internal research".
---

# Internal Research

## Overview

This skill helps you synthesize all the information gathered by the user while conducting internal research - such as by speaking to a user or a business exective, a workflow document, screenshots and/ or transcripts from demo videos, etc - and compile the findings into a structured internal research document.

## When to Invoke This Skill

This skill should be AUTOMATICALLY invoked when the user requests:
- "Synthesize the internal research materials"
- "Create/generate an internal research document"
- "Consolidate internal research findings"
- "Compile the internal research into a report"
- "Analyze the internal research materials"
- Any variation asking to create a structured output from research documents
- "Internal" is an important keyword here

## Example Folder Structure

A working example is provided in `assets/examples/sample-product/` showing proper organization:

```
assets/
├── examples/                        ← Reference examples (do not modify)
│   └── sample-product/
│       ├── README.md
│       ├── interview-agent-sample.txt
│       ├── demo-transcript-sample.txt
│       ├── demo-screenshot-01-submission-form.txt
│       ├── demo-screenshot-02-carrier-list.txt
│       └── workflow-sample.txt
└── your-product-name/               ← Your research materials here
    ├── interview-....txt
    ├── demo-transcript-....txt
    └── ...
```

**Naming conventions:**
- Use descriptive, kebab-case filenames
- Include dates for time-sensitive documents (e.g., `interview-agent-john-2026-02-15.txt`)
- Use prefixes to group related files (`demo-`, `interview-`, `workflow-`)
- Number screenshots sequentially if from the same source
- Add descriptive suffixes to clarify content (`-submission-form`, `-carrier-list`)

**Test the skill:** Run internal research on the sample materials to see how it works before adding your own documents.

## Workflow

When a user requests for synthesis of internal research document:

### Step 1: Add documents in required folder

- Ask the user to collect all the documents in the `skills/internal-research/assets` folder 
- Ask the user if there is a demo video. If there is a demo video ask the user to grab screenshots of important timestamp in the video which demonstrates the product feature, along with the transcript of that video. 
- Ask the user to make sure either the transcript and screenshots are in the same folder under `skills/internal-research/assets` or they share similar filename so that you are able to identify the relationship between the screenshot files and the transcript

Overall, guide the user to create the right folder structure and file structure for all the assets so that you are able to understand the relationships clearly. If anything is unclear, ask questions to the users before proceeding further. 

### Step 2: Understand each document and their relationship with each other

Read and analyze all documents in the `assets/` folder:

**For each document, identify:**
- **Type**: Interview transcript, demo video transcript, screenshot, workflow diagram, spreadsheet, business requirement doc, etc.
- **Content summary**: What key information does it contain?
- **Related files**: Which other documents does this connect to?
  - Screenshots from the same demo video (match by filename pattern or timestamp)
  - Transcripts that reference specific workflows shown in other docs
  - Interview quotes that relate to features shown in screenshots
  - Business documents that provide context for user interviews

**Relationship types to map:**
- **Illustrates**: Screenshot illustrates a feature mentioned in transcript
- **Validates**: Interview quote validates a requirement in business doc
- **References**: One document explicitly mentions another
- **Contextualizes**: Background doc provides context for a specific finding
- **Contradicts**: Two sources provide conflicting information (note this!)

**Technical notes:**
- PDFs can be read directly with the Read tool using the `pages` parameter
- For images/screenshots, use the Read tool to view them (it supports PNG, JPG)
- Look for filename patterns (e.g., `demo-transcript.txt` and `demo-screenshot-01.png` are likely related)
- Check timestamps in filenames or document metadata to establish sequence

**Create a mental map** of how all documents relate before proceeding to Step 3. If relationships are unclear, ask the user for clarification.



### Step 3: Create the Internal Research Document

Generate a well-structured markdown file with your findings. It must be concise and should NOT exceed 1500 words. 

The output document should have a filename - `internal-research-` + {product name}.md and must be stored in `research/` folder. 

Create the structure per the documents you have received. Make sure in your output document you have created the relationship of different documents/ files which have been added by the users, so that when there is a need to reference a specific file later, you are able to easily retrieve using the relationship.

Ensure there is a key findings section in the output document.

## Output Format

The internal research document should include these minimum sections:

### Required Sections:

1. **Title**: `# Internal Research: [Product Name]`
   - Include research date

2. **Executive Summary** (200-300 words)
   - High-level overview of key findings
   - Most critical insights at a glance

3. **Research Sources**
   - Table listing all documents analyzed
   - Include filename, type, date, and brief description
   - Example:
   ```
   | Filename | Type | Date | Description |
   |----------|------|------|-------------|
   | interview-agent-john.txt | Interview | 2026-02-15 | Agent discussing submission process |
   | demo-transcript.txt | Demo Video | 2026-02-18 | Competitor product walkthrough |
   ```

4. **Key Findings** (bulleted list, 8-12 findings)
   - Each finding should cite specific source(s)
   - Format: `**Finding statement** (Source: filename, line/page/timestamp)`
   - Example: `**Agents spend 2-3 hours per carrier submission** (Source: interview-agent-john.txt, timestamp 5:30)`

5. **Document Relationships**
   - Visual or textual map showing how documents relate
   - Example:
   ```
   demo-transcript.txt [00:30-01:45]
   └─ Illustrates → demo-screenshot-01-submission-form.png
   └─ References → workflow-sample.pdf (Step 3)

   interview-agent-john.txt (pain point: manual data entry)
   └─ Validates → workflow-sample.pdf (Step 3: ACORD Form Completion)
   └─ Addressed by → demo-transcript.txt (auto-population feature)
   ```

6. **Additional Sections** (add as needed based on content)
   - User Pain Points
   - Feature Requirements
   - Workflow Analysis
   - Competitive Insights
   - Technical Considerations
   - Open Questions

### Formatting Guidelines:

- Use clear heading hierarchy (##, ###, ####)
- Include citations in every section
- Use tables for structured comparisons
- Use bullet points for lists
- Use blockquotes for direct quotes from sources
- Maximum 1500 words total

## Notes

- ALWAYS cite sources (specific areas from the uploaded docs) so the user can verify information by looking into the uploaded documents. 
- Be thorough but concise - focus on actionable intelligence
- Brevity is always better
- Do not repeat any information in the output document
- Do NOT create any new data or information by yourself if you are not able to find a data or information 

