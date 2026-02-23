# Internal Research: Commercial Insurance Submission Platform

**Research Date:** February 22, 2026
**Documents Analyzed:** 5 source files
**Research Period:** February 15-18, 2026

---

## Executive Summary

This research synthesizes findings from agent interviews, workflow documentation, and competitive product analysis to understand the commercial insurance submission process and identify opportunities for automation. The research reveals that agents spend 2-3 hours per carrier submission due to manual data entry, duplicate work across carrier systems, and lack of centralized tracking. A competitor product demonstrates that automation can reduce submission time from hours to minutes through auto-population, smart routing, and centralized tracking. Key pain points include: repetitive data entry across multiple carrier portals, manual carrier appetite checking through phone calls, inconsistent document formatting requirements, and spreadsheet-based tracking of submission status. The competitive solution addresses these through AMS integration, real-time appetite indicators, conditional logic forms, and automated status tracking. The primary user need is "enter once, submit to many" - agents want to input client information one time and automatically generate properly formatted submission packets for multiple carriers.

---

## Research Sources

| Filename | Type | Date | Description |
|----------|------|------|-------------|
| interview-agent-sample.txt | Interview Transcript | Feb 15, 2026 | 45-minute interview with John Smith, Senior Commercial Agent at ABC Insurance Brokerage |
| workflow-sample.txt | Process Documentation | N/A | Current 8-step commercial submission workflow with identified pain points |
| demo-transcript-sample.txt | Competitor Demo Video | Feb 18, 2026 | 12-minute product demo of competitor's commercial submission platform |
| demo-screenshot-01-submission-form.txt | Screenshot Reference | Feb 18, 2026 | Submission form interface from demo timestamp [00:30-01:45] |
| demo-screenshot-02-carrier-list.txt | Screenshot Reference | Feb 18, 2026 | Carrier selection screen from demo timestamp [03:20-05:00] |

---

## Key Findings

1. **Agents spend 2-3 hours per carrier on straightforward submissions, with complex risks taking a full day or more** (Source: interview-agent-sample.txt, lines 15-16)

2. **Data entry is the most time-consuming part of the submission process** (Source: interview-agent-sample.txt, line 19)

3. **Agents copy the same information into different carrier portals and ACORD forms, with each carrier requiring different formatting** (Source: interview-agent-sample.txt, lines 19-20)

4. **Document management is inconsistent, causing agents to lose files and request duplicates from clients** (Source: interview-agent-sample.txt, lines 23-24)

5. **80% of renewal information is the same as the previous year, yet agents start almost from scratch** (Source: interview-agent-sample.txt, line 24)

6. **Carrier selection is manual and relationship-based, with no central system to check carrier appetite** (Source: interview-agent-sample.txt, lines 27-28)

7. **The top requested feature is "enter information once and automatically populate all forms"** (Source: interview-agent-sample.txt, lines 31-32)

8. **Agents track submission responses manually using spreadsheets or email, lacking centralized visibility** (Source: interview-agent-sample.txt, line 35-36)

9. **The current workflow requires 8 manual steps from initial contact to quote presentation** (Source: workflow-sample.txt, lines 15-61)

10. **Competitor solution reduces submission time from hours to minutes through auto-population and smart routing** (Source: demo-transcript-sample.txt, lines 47-48)

11. **Real-time carrier appetite indicators (green/yellow/red) eliminate the need for phone calls to check carrier interest** (Source: demo-transcript-sample.txt, lines 28-29)

12. **Conditional logic in forms adapts questions based on previous answers, improving efficiency and reducing errors** (Source: demo-transcript-sample.txt, lines 21-22)

---

## Document Relationships

```
interview-agent-sample.txt (John Smith interview, Feb 15, 2026)
├─ Validates → workflow-sample.txt (Step 3: ACORD Form Completion)
│  └─ Pain point: "2-3 hours per carrier" (interview:15) = "2-3 hours per carrier" (workflow:30)
│
├─ Validates → workflow-sample.txt (Step 5: Carrier Selection)
│  └─ Pain point: "manual relationship-based" (interview:27) = "call underwriters" (workflow:39)
│
└─ Defines requirements addressed by → demo-transcript-sample.txt
   ├─ Request: "enter once, populate all" (interview:31) = "auto-populates" (demo:16)
   ├─ Request: "tracking dashboard" (interview:35) = "tracking dashboard" (demo:42)
   └─ Pain: "carrier appetite checking" (interview:27) = "appetite indicators" (demo:28)

workflow-sample.txt (Current process documentation)
├─ Contextualizes → interview-agent-sample.txt (provides structured view of John's pain points)
├─ Lists pain points (lines 62-68) that map to → demo-transcript-sample.txt solutions
└─ Defines baseline process improved by competitor product

demo-transcript-sample.txt (Competitor product demo, Feb 18, 2026)
├─ References → demo-screenshot-01-submission-form.txt [timestamp 00:30-01:45]
│  └─ Illustrates: Submission form with auto-populated fields (demo:14-16)
│
├─ References → demo-screenshot-02-carrier-list.txt [timestamp 03:20-05:00]
│  └─ Illustrates: Carrier selection with real-time appetite indicators (demo:26-29)
│
└─ Addresses pain points from → interview-agent-sample.txt + workflow-sample.txt
   ├─ Solves: Duplicate data entry (demo:16)
   ├─ Solves: Manual carrier selection (demo:28-29)
   ├─ Solves: Format inconsistencies (demo:38-39)
   └─ Solves: Manual tracking (demo:42-46)
```

---

## Agent Pain Points & Workflows

### Current State Pain Points

**Time & Efficiency:**
- 2-3 hours for straightforward submissions per carrier (Source: interview-agent-sample.txt:15)
- Full day or more for complex commercial risks (Source: interview-agent-sample.txt:15-16)
- Submitting to 3-4 carriers multiplies the time investment (Source: interview-agent-sample.txt:16)

**Data Entry & Duplication:**
- Copying same information from AMS into different carrier portals (Source: interview-agent-sample.txt:19)
- Each carrier requires different formatting (Source: interview-agent-sample.txt:20)
- Every carrier has unique supplemental applications (Source: interview-agent-sample.txt:20)
- Starting renewals from scratch despite 80% information overlap (Source: interview-agent-sample.txt:24)

**Document Management:**
- Inconsistent organization on network drives (Source: interview-agent-sample.txt:23)
- Lost files requiring duplicate requests from clients (Source: interview-agent-sample.txt:23-24)

**Carrier Selection:**
- Manual phone calls to check underwriter appetite (Source: interview-agent-sample.txt:27-28)
- Relationship-based with no centralized appetite data (Source: workflow-sample.txt:42)

**Tracking & Follow-up:**
- Manual tracking in spreadsheets or email (Source: interview-agent-sample.txt:35)
- Manual follow-up after 3-5 days (Source: workflow-sample.txt:51-52)
- No centralized dashboard showing submission status (Source: interview-agent-sample.txt:36)

### Current Workflow (8 Steps)

**Step 1-2: Client Contact & Data Collection** (Source: workflow-sample.txt:15-24)
Agent gathers business information, coverage needs, loss history, and supporting documents.

**Step 3: ACORD Form Completion** (Source: workflow-sample.txt:26-30)
Manual completion of ACORD 125, ACORD 101, and carrier-specific supplementals. Takes 2-3 hours per carrier.

**Step 4: Document Preparation** (Source: workflow-sample.txt:32-37)
Create statement of values, format loss runs, compile questionnaires per carrier requirements.

**Step 5: Carrier Selection** (Source: workflow-sample.txt:39-43)
Call underwriters to check appetite, select 2-4 carriers based on relationships and experience.

**Step 6: Submission Delivery** (Source: workflow-sample.txt:45-48)
Email or upload to individual carrier portals, each with different format requirements.

**Step 7: Follow-up & Tracking** (Source: workflow-sample.txt:50-54)
Manual tracking and follow-up via email/phone. Wait 5-10 business days for quotes.

**Step 8: Quote Review & Presentation** (Source: workflow-sample.txt:56-60)
Compare options and present to client.

---

## Competitive Product Analysis

### Competitor Solution Overview

The competitor product (Source: demo-transcript-sample.txt) demonstrates a commercial submission platform that automates the manual workflow through:

**Core Features:**

1. **AMS Integration & Auto-Population** (demo:16)
   Client information automatically pre-fills from agency management system, eliminating duplicate data entry.

2. **Conditional Logic Forms** (demo:21-22)
   Forms adapt based on answers. Example: selecting "fleet of vehicles" triggers commercial auto questions automatically.

3. **Document Recognition** (demo:24-25)
   System recognizes uploaded document types and places them in correct sections of submission packet.

4. **Real-Time Carrier Appetite Indicators** (demo:28-29)
   - Green: Actively writing this risk type in this state
   - Yellow: Limited appetite
   - Red: Not accepting new business

5. **Smart Routing** (demo:31-32)
   Answer carrier supplemental questions once; system routes information to correct carrier forms.

6. **Completeness Validation** (demo:33-34)
   Progress indicator shows 85% complete and identifies missing required information before submission.

7. **Carrier-Specific Formatting** (demo:38-39)
   Same information automatically formatted differently per carrier preferences.

8. **Electronic Delivery & Tracking** (demo:41-46)
   Delivers submission packets electronically to carriers with automatic status notifications (opened, additional info requested, quotes received).

### Time Savings

**Before:** Hours per submission (2-3 hours for straightforward, full day for complex) (Source: interview-agent-sample.txt:15-16)
**After:** Minutes per submission (Source: demo-transcript-sample.txt:47-48)

---

## Requirements Validation

The agent interview directly validates requirements that the competitor product addresses:

| Agent Request | Interview Source | Competitor Solution | Demo Source |
|---------------|------------------|---------------------|-------------|
| "Enter information once and have it automatically populate all forms" | interview:31-32 | AMS integration with auto-population | demo:16 |
| "Click a button to send to multiple carriers at once" | interview:31-32 | Electronic delivery to selected carriers | demo:41 |
| "Dashboard showing status of all submissions in one place" | interview:36 | Tracking dashboard with automatic notifications | demo:42-46 |
| "Central place to check carrier appetite" | interview:27-28 | Real-time appetite indicators | demo:28-29 |

---

## Open Questions

1. **Integration Requirements:** What AMS platforms need to be supported for auto-population to work effectively?

2. **Carrier API Availability:** How many carriers support electronic submission delivery vs. requiring manual portal upload?

3. **Appetite Data Source:** Where does real-time carrier appetite information come from? How frequently is it updated?

4. **Document Intelligence:** How sophisticated is the document recognition system? What file types and formats does it support?

5. **Renewal Process:** How does the competitor product handle renewals specifically, given that 80% of information remains the same? (Source: interview-agent-sample.txt:24)

6. **Multi-Location Complexity:** How does the system handle complex commercial risks with multiple locations that John mentioned take "a full day or more"? (Source: interview-agent-sample.txt:16)

---

**Document Version:** 1.0
**Total Word Count:** ~1,450 words
**Next Steps:** Validate open questions through additional competitive research or carrier partnership discussions.
