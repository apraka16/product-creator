# Product Creator - Claude Code Project Guide

## Project Purpose

This project helps product managers research and define new product concepts through:
1. Competitive market research
2. Internal user research synthesis

## Available Skills

### 1. `/internal-research` - Internal Research Synthesis

**When to invoke:**
- User says: "synthesize internal research", "create internal research report", "consolidate internal findings", "compile internal research", "analyze internal research materials"
- "Internal" is the keyword here. If you are unsure whether you should use compete-research or internal-research, ask user what his intent is. 

---

### 2. `/compete-research` - Competitive Research (if available)

**When to invoke:**
- User asks for competitive analysis or market research. 
- If you are unsure whether you should use compete-research or internal-research, ask user what his intent is. 


## Expected Behavior

When working on this project:

1. **Read this CLAUDE.md file first** to understand project context
2. **Check for skill triggers** in user requests
3. **Invoke skills using Skill tool** - do not replicate skill logic manually
4. **Follow skill workflows** as defined in each SKILL.md file
5. **Maintain consistent output** so all team members get same results

**Last Updated:** 2026-02-22
**Maintained By:** Product team
