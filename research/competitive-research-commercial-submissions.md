# Competitive Research: Commercial Insurance Submissions Feature

**Research Date:** February 22, 2026
**Product Concept:** Commercial submissions feature for Agency Management System on Salesforce
**Target Users:** Insurance brokerages and their staff
**Core Functionality:** Create submission packets (ACORD forms, statement of value, loss reports, questionnaires) and send to insurance carriers

---

## Executive Summary

The commercial insurance submissions market is dominated by a few major players with strong carrier connectivity and AMS integration. Key success factors include:
- **Carrier connectivity** (20-30+ carriers with real-time integrations)
- **Data efficiency** (eliminate duplicate entry, pre-fill from AMS)
- **Multi-line support** (BOP, GL, Commercial Auto, Workers Comp, Umbrella)
- **ACORD form automation** with dynamic questionnaires
- **Speed** (5-minute quote/bind capabilities)

**Market Gap Identified:** Most solutions are standalone platforms or integrated with specific AMS vendors (Applied, Vertafore). A native Salesforce solution could fill a gap for agencies already using Salesforce as their CRM/operational backbone.

---

## Competitive Landscape Overview

The market segments into three categories:
1. **AMS-Integrated Submissions** (Indio, Vertafore Commercial Submissions)
2. **Platform/Marketplace Submissions** (Bold Penguin, IVANS)
3. **Standalone Agency Tools** (Tarmika)

**Pricing:** Most vendors don't publish pricing publicly. Entry points range from $500/month (Indio) to enterprise custom pricing.

---

## Competitor Profiles

### 1. Indio (Vertafore/Applied Epic Integration)

**Company:** Indio Technologies (acquired by Vertafore, July 2020)
**Website:** Part of Vertafore product suite
**Market Position:** Leading digital submissions platform

#### Core Features
- Digitized carrier supplemental forms library
- ACORD form support with conditional logic
- Automated data population from previous submissions
- Electronic signature capabilities
- Client portal for self-service application completion
- Multi-user collaboration with commenting
- Year-over-year data retention for renewals

#### Integration & Connectivity
- **Primary Integration:** Applied Epic, AMS 360
- **Limitation:** Incomplete two-way sync reported by users
- **Data Mapping:** Some gaps between AMS platforms

#### Pricing
- Starting at $500/month (base level)
- Enterprise pricing available on request

#### Target Audience
- P&C insurance agencies
- Commercial brokers handling high application volumes
- Agencies using Applied Epic or AMS 360

#### Strengths
- **Ease of Use:** 4.4/5 rating - intuitive interface
- **Client Experience:** Modern, streamlined application process
- **Time Savings:** Significant reduction in application completion time
- **Support:** Highly rated onboarding and customer support
- **Conditional Logic:** Smart forms adapt based on responses
- **Overall Rating:** 4.5/5 stars (230+ reviews)

#### Weaknesses
- **Integration Limitations:** Incomplete two-way sync with Applied EPIC and Sagitta
- **Onboarding Complexity:** Cumbersome implementation with many participants
- **Form Customization:** Difficulty navigating and customizing for specific clients
- **Pricing:** Higher than some alternatives, may not suit smaller agencies
- **Learning Curve:** Advanced customization requires training

#### Key Differentiators
- Client-focused intuitive design
- Year-over-year data persistence
- Cloud-based, cross-platform accessibility

**Source:** Software Advice, TrustRadius reviews, Vertafore product documentation

---

### 2. Vertafore AMS360 + Commercial Submissions

**Company:** Vertafore (acquired by Roper Technologies, 2020)
**Website:** vertafore.com
**Market Position:** Industry leader serving 98 of top 100 brokers

#### Core Features

**AMS360 Platform:**
- Automated policy entry and carrier downloads
- Renewal acceleration tools
- Document management with e-signatures
- Customizable KPI dashboards
- Advanced search across client/policy data

**Commercial Submissions Module** (Separate integration, requires AMS360 20R2+):
- Access to 25+ carriers across 5 commercial lines
- Real-time carrier integrations (CHUBB, Travelers, Nationwide, Liberty Mutual)
- Interview-style dynamic questionnaires
- Pre-fill from AMS360 data
- Multi-carrier quoting in under 5 minutes
- E&S (Excess & Surplus) quoting and binding

#### Supported Lines
- Business Owners Policy (BOP)
- General Liability
- Commercial Auto
- Workers Compensation
- Umbrella/Excess Liability

#### Integration & Connectivity
- **Carrier Network:** 300+ carrier partners
- **Vertafore Ecosystem:** BenefitPoint, PL Rating, WorkSmart, InsurLink, Sircon
- **CRM:** Salesforce (via AMS360 Connect)
- **Mobile:** Full-featured iOS/Android apps
- **VSSO:** Single sign-on across Vertafore products

#### Pricing
- Not publicly disclosed
- Contact: 1-800-444-4813
- Custom pricing based on agency size and needs

#### Target Audience
- Mid-market to large commercial agencies
- Multi-location firms
- Agencies handling both personal and commercial lines
- 160,000+ users across 15,000+ agencies

#### Strengths
- **Comprehensive Platform:** All-in-one AMS with submissions
- **Carrier Connectivity:** 300+ carrier partners with automated downloads
- **Market Dominance:** 98 of top 100 brokers use Vertafore products
- **Integration Ecosystem:** Deep integration across insurance workflow
- **Proven Results:** Customers report 26% revenue growth without adding staff
- **Scalability:** Serves agencies from small to enterprise
- **Mobile Access:** Full-featured mobile capabilities
- **AI-Powered:** AI-assisted communications and campaign creation

#### Weaknesses
- **No Pricing Transparency:** Requires sales consultation
- **Implementation Complexity:** May be challenging for smaller agencies
- **Learning Curve:** Comprehensive features require significant training
- **Vendor Lock-in:** Deep Vertafore ecosystem creates switching costs
- **Separate Module:** Commercial Submissions not native to core AMS360
- **Version Requirements:** Need AMS360 20R2+ for Commercial Submissions
- **Limited Public Reviews:** Difficulty finding detailed user feedback

#### Key Differentiators
- Mature platform with 55+ years industry experience
- Native integration within Vertafore ecosystem
- Strong commercial lines focus
- Direct carrier connectivity at scale

**Source:** Vertafore.com official product pages, SoftwareSuggest

---

### 3. Bold Penguin

**Company:** Bold Penguin
**Website:** boldpenguin.com
**Market Position:** Major submission platform serving 8 of top 10 commercial carriers

#### Core Features

**Terminal** (Small Commercial):
- Universal submission flow for simple to complex risks
- Algorithmic best-fit matching of risk to carrier
- Smart Document Upload (converts static files to submission opportunities)

**SubmissionLink** (Middle Market):
- Processes 500K+ middle market submissions annually
- Median premium: $53K
- Market intelligence with AI-driven insights
- Full submission workflow from lead to placement

**Exchange** (Carrier Distribution):
- Powers submission infrastructure for major carriers
- Algorithmic distribution and routing

#### Scale Metrics
- $20.3+ billion in small commercial new business premium quotes (2024)
- 500K+ middle market submissions annually
- 8 of top 10 commercial carriers use Bold Penguin

#### Pricing
- Not publicly disclosed

#### Target Audience
- Insurance agents and brokers
- Insurance carriers and MGAs
- Agencies handling both small commercial and middle market

#### Strengths
- **Massive Scale:** Industry-leading submission volume
- **Algorithmic Matching:** Sophisticated risk-to-carrier matching technology
- **Full Spectrum:** Handles simple monoline to complex middle-market risks
- **Smart Document Upload:** Converts unstructured data into submission-ready format
- **Carrier Adoption:** Powers distribution for major carriers
- **Market Intelligence:** AI-driven insights and analytics

#### Weaknesses
- **Limited Public Information:** Detailed feature documentation scarce
- **ACORD Form Clarity:** Not explicitly mentioned in available materials
- **Integration Details:** AMS integration capabilities unclear
- **Pricing Opacity:** No public pricing information

#### Key Differentiators
- Algorithmic risk-to-carrier matching at massive scale
- Powers carrier distribution networks (not just agency-side)
- Smart document transformation technology

**Source:** Bold Penguin website, industry announcements

---

### 4. IVANS Ask Kodiak

**Company:** IVANS (part of Applied Systems)
**Website:** ivans.com
**Market Position:** Carrier appetite intelligence platform

#### Core Features
- Instant carrier appetite search by commercial industry
- Risk filtering by state, classification, and risk size
- Cloud-based carrier matching
- Product highlights and underwriting criteria visibility
- Analytics dashboards for search patterns and market trends
- Integration into existing quoting platforms

**Additional IVANS Products:**
- **IVANS Download:** Paperwork management and automation
- **IVANS eServicing:** Carrier connectivity infrastructure

#### Pricing
- Not publicly disclosed

#### Target Audience
- Insurance agents and brokers needing carrier appetite information
- Agencies wanting to eliminate manual carrier research

#### Strengths
- **Eliminates Manual Research:** No more calling carriers for appetite
- **Consolidated Interface:** All appetite data in one place
- **Market Intelligence:** Analytics on search habits and preferred markets
- **Shows Underwriting Criteria:** Visibility into carrier requirements upfront
- **Integration-Friendly:** Plugs into existing quoting platforms

#### Weaknesses
- **Limited Submission Features:** Focuses on appetite matching, not full submission workflow
- **Requires Additional Tools:** Not a complete submission solution standalone
- **Feature Scope:** Narrow focus compared to full-featured platforms

#### Key Differentiators
- Specialized in carrier appetite intelligence phase (pre-submission)
- Analytics and market trend visibility
- Part of Applied Systems ecosystem

**Source:** IVANS website, product documentation

---

### 5. Tarmika

**Company:** Tarmika
**Website:** tarmika.com
**Market Position:** Streamlined multi-carrier quoting platform

#### Core Features
- Single-entry solution for multi-carrier, multi-line quoting
- ACORD application support (save and send to other markets)
- Quote and bind in under 5 minutes
- Market access integration
- Eliminates duplicate data entry across carriers

#### Pricing
- Not publicly disclosed

#### Target Audience
- Independent insurance agents
- Small to mid-sized agencies seeking operational efficiency

#### Strengths
- **Extreme Speed:** 5-minute quote and bind capability
- **Single Data Entry:** One entry point for multiple carriers and lines
- **ACORD Support:** Can save ACORD applications and distribute
- **Modernized Process:** Digital alternative to paper applications
- **Efficiency Focus:** Strong emphasis on reducing manual work

#### Weaknesses
- **Limited Information:** Minimal public documentation available
- **Market Presence:** Smaller profile compared to Applied/Vertafore
- **Integration Details:** AMS connectivity unclear
- **Carrier Network:** Number of carrier connections not specified

#### Key Differentiators
- Emphasis on speed (5-minute turnaround)
- Single-entry, multi-output workflow
- Modernization of paper-based processes

**Source:** Tarmika website references, third-party listings

---

### 6. Applied Epic (with Indio)

**Company:** Applied Systems
**Website:** appliedsystems.com
**Market Position:** Major AMS provider serving 7 of 10 top agencies

#### Core Features
- "Digital Roundtrip of Insurance" ecosystem
- Indio Application Management (included in product suite)
- Book Builder for commercial lines risk intelligence
- Comprehensive agency management platform
- Commercial lines quoting capabilities

#### Pricing
- Not publicly disclosed
- Enterprise-level pricing model

#### Target Audience
- Large and mid-sized insurance agencies
- Multi-location brokerages
- Agencies seeking comprehensive ecosystem

#### Strengths
- **Ecosystem Approach:** Integrated suite across entire agency workflow
- **Market Presence:** 7 of 10 top agencies use Applied
- **Indio Integration:** Native integration with leading submission tool
- **Commercial Focus:** Strong commercial lines capabilities
- **Established Platform:** Mature, proven solution

#### Weaknesses
- **Complexity:** Comprehensive platform may be overwhelming
- **Cost:** Likely high enterprise pricing
- **Vendor Lock-in:** Ecosystem creates switching barriers
- **Implementation:** Significant time and resources required

#### Key Differentiators
- Complete agency ecosystem with native submission integration
- "Digital Roundtrip" vision connecting all stakeholders
- Strong market penetration with large agencies

**Source:** Applied Systems website, industry publications

---

## Feature Comparison Matrix

| Feature | Indio | Vertafore AMS360 + Commercial Submissions | Bold Penguin | IVANS Ask Kodiak | Tarmika | Applied Epic |
|---------|-------|-------------------------------------------|--------------|------------------|---------|--------------|
| **ACORD Form Support** | ✓ Yes | ✓ Yes (implied) | ? Unclear | N/A (appetite only) | ✓ Yes | ✓ Yes (via Indio) |
| **Multi-Carrier Connectivity** | ✓ Via AMS integration | ✓ 300+ carriers | ✓ 8 of top 10 carriers | ✓ Appetite data only | ? Unclear | ✓ Extensive |
| **Real-Time Carrier Integration** | ✓ Limited | ✓ 25+ commercial carriers | ✓ Yes | N/A | ? Unclear | ✓ Yes |
| **Electronic Signatures** | ✓ Yes | ✓ Yes | ? Unclear | N/A | ? Unclear | ✓ Yes |
| **Client Portal** | ✓ Yes | ✓ Yes (InsurLink) | ? Unclear | N/A | ? Unclear | ✓ Yes |
| **Conditional Logic Forms** | ✓ Yes | ✓ Yes (interview-style) | ✓ Yes | N/A | ? Unclear | ✓ Yes |
| **Pre-fill from AMS** | ✓ Yes | ✓ Yes | ✓ Smart Document Upload | N/A | ? Unclear | ✓ Yes |
| **Mobile Access** | ✓ Cloud-based | ✓ iOS/Android apps | ? Unclear | ? Unclear | ? Unclear | ✓ Yes |
| **Quote Speed** | Standard | Under 5 minutes | Fast (algorithmic) | N/A | Under 5 minutes | Standard |
| **Commercial Lines** | All major lines | 5 lines (BOP, GL, CA, WC, Umbrella) | All lines | All lines (appetite) | Multi-line | All major lines |
| **E&S Market Support** | ? Unclear | ✓ Yes | ? Unclear | ✓ Yes | ? Unclear | ? Unclear |
| **Salesforce Integration** | ✗ No (Applied/Vertafore only) | ✓ Yes (AMS360 Connect) | ? Unclear | ? Unclear | ? Unclear | Limited |
| **Market Intelligence** | Basic | ✓ AI-powered | ✓ AI-driven | ✓ Yes (core feature) | ? Unclear | ✓ Book Builder |
| **Pricing Transparency** | Starting $500/mo | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not disclosed |
| **Target Agency Size** | Mid to large | Mid to enterprise | All sizes | All sizes | Small to mid | Large to enterprise |

---

## Market Gaps & Opportunities

### Identified Gaps

1. **Native Salesforce Solutions:**
   - Most competitors integrate with Applied or Vertafore AMS platforms
   - Limited native Salesforce solutions despite many agencies using Salesforce for CRM
   - Vertafore offers AMS360 Connect for Salesforce, but it's bi-directional sync, not native

2. **Pricing Transparency:**
   - Only Indio publicly shares starting pricing ($500/mo)
   - All others require sales consultation, creating friction in evaluation

3. **Small Agency Solutions:**
   - Most platforms target mid-to-large agencies
   - Limited affordable options for smaller brokerages

4. **ACORD Form Clarity:**
   - Most platforms mention ACORD support but lack detailed documentation
   - Opportunity for clear, comprehensive ACORD form automation

5. **Integration Completeness:**
   - User reviews highlight incomplete two-way sync (Indio example)
   - Gap in seamless data flow between submission tools and AMS

### Opportunities for Your Product

1. **Salesforce-Native Advantage:**
   - Agencies already on Salesforce don't need separate AMS integration
   - Native Salesforce = better data model, workflow automation, reporting
   - Leverage Salesforce ecosystem (AppExchange, partners)

2. **Modern User Experience:**
   - Build on modern Salesforce Lightning platform
   - Mobile-first design leveraging Salesforce Mobile
   - Intuitive UI matching Salesforce patterns

3. **Transparent Pricing:**
   - Clear AppExchange pricing could be differentiator
   - Tiered pricing for agencies of all sizes

4. **Comprehensive ACORD Support:**
   - Document exactly which ACORD forms are supported
   - Clear workflow for statement of value, loss reports, custom questionnaires

5. **AI/Automation:**
   - Leverage Salesforce Einstein for predictive carrier matching
   - Automated document assembly from Salesforce data
   - Intelligent form pre-fill from existing client records

6. **Carrier Agnostic:**
   - Don't lock into specific carrier panels
   - Allow agencies to connect their own carrier relationships
   - Focus on submission packet creation vs. real-time rating (phase 1)

---

## Strategic Recommendations

### Phase 1: Core Submission Workflow
- Focus on submission packet creation (ACORD forms, SOV, loss reports, questionnaires)
- Manual carrier delivery (email/portal) before building carrier integrations
- Leverage Salesforce data model for pre-fill
- E-signature integration (DocuSign, Adobe Sign already common in Salesforce)

### Phase 2: Carrier Connectivity
- Build integrations to top 10-15 carriers based on user needs
- Evaluate IVANS network for standardized carrier connectivity
- Consider partnerships vs. building proprietary connections

### Phase 3: Intelligence & Automation
- Carrier appetite matching (à la Ask Kodiak)
- AI-powered submission recommendations
- Market intelligence dashboards

### Differentiation Strategy
1. **Salesforce-Native:** Only true native solution for Salesforce-based agencies
2. **Transparency:** Clear pricing and feature documentation
3. **Flexibility:** Carrier-agnostic approach allows agencies to maintain existing relationships
4. **Modern UX:** Leverage Salesforce Lightning for superior user experience
5. **Scalability:** Start focused (submission packets) then expand to connectivity

### Pricing Considerations
- Consider starting below Indio's $500/mo entry point
- Tiered based on user count or submission volume
- AppExchange listing for discoverability

---

## Conclusion

The commercial insurance submissions market is mature with established players, but there's an opportunity for a native Salesforce solution. Key success factors will be:

1. **Seamless Salesforce integration** leveraging existing data
2. **Clear, comprehensive ACORD form support** with documentation
3. **Carrier-agnostic flexibility** allowing agencies to maintain existing relationships
4. **Modern, intuitive UX** matching Salesforce standards
5. **Competitive pricing** with transparency

**Recommended Next Steps:**
1. Validate demand with Salesforce-using insurance agencies
2. Map detailed workflow for submission packet creation
3. Identify must-have ACORD forms for MVP
4. Explore IVANS partnership for carrier connectivity roadmap
5. Define clear product roadmap with phases

---

**Note on "Borrowed Tyme":** No publicly available information could be found about this product. It may be a regional/private solution, discontinued, or the name may be different. Recommend verifying the exact product name and company for further research.
