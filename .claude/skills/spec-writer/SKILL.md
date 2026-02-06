---
name: spec-writer
description: Writes clear, feature-level specifications in Markdown following Spec-Driven Development principles
category: specification
input: High-level feature requirements or system intent
output: Well-structured, unambiguous Markdown specifications
context: Used for defining Phase I CLI features and beyond
constraints:
  - No application code generation
  - No agent definitions
  - Specification only (WHAT, WHY; not HOW)
---

## Overview

`spec-writer` is a reusable specification authoring skill for Hackathon II – Evolution of Todo. It guides users through writing clear, unambiguous feature specifications that serve as the single source of truth for development.

**When to use**: Define new features, clarify requirements, or document system intent before planning and implementation.

---

## Specification Writing Principles

Follow these core SDD principles when writing specifications:

### 1. **Focus on WHAT and WHY, not HOW**
   - Define user needs, business goals, and system behavior
   - Avoid implementation details (tech stack, frameworks, architecture)
   - Written for stakeholders, not developers

### 2. **Make Requirements Testable**
   - Each requirement must be independently verifiable
   - Avoid vague language like "good," "fast," "easy"
   - Use acceptance scenarios with Given/When/Then format

### 3. **Prioritize User Scenarios**
   - Lead with user journeys ordered by business impact
   - Assign priority levels (P1, P2, P3) based on value
   - Each scenario should be independently deliverable (MVP slices)

### 4. **Define Measurable Success**
   - Success criteria must be observable, quantifiable outcomes
   - Technology-agnostic (no database, API, or framework mentions)
   - From user/business perspective, not system internals

### 5. **Document Assumptions**
   - Record reasonable defaults for unspecified details
   - Surface ambiguities with [NEEDS CLARIFICATION] (limit to 3)
   - Only ask about decisions with multiple valid interpretations

### 6. **Identify Scope and Boundaries**
   - Explicitly state what IS and IS NOT included
   - Define key entities and their relationships
   - Document dependencies and constraints

---

## Specification Template

Use this structure for all feature specifications:

```markdown
# Feature Specification: [FEATURE NAME]

**Feature ID**: [Identifier, e.g., F-001]
**Created**: [DATE]
**Status**: [Draft | Ready for Planning]
**Context**: [One-sentence summary of why this feature matters]

## User Scenarios & Testing

### User Story 1 - [Brief Title] (Priority: P1)

[Plain language description of the user journey]

**Why this priority**: [Explain the value and business impact]

**Independent Test**: [How this can be tested in isolation and delivers value]

**Acceptance Scenarios**:
1. **Given** [initial state], **When** [action], **Then** [expected outcome]
2. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 2 - [Brief Title] (Priority: P2)

[Repeat structure above]

---

### Edge Cases

- What happens when [boundary condition]?
- How does the system handle [error scenario]?

## Requirements

### Functional Requirements

- **FR-001**: System MUST [specific capability]
- **FR-002**: System MUST [specific capability]
- **FR-003**: Users MUST be able to [key interaction]

*Mark ambiguities only if critical*:
- **FR-004**: System MUST [action] via [NEEDS CLARIFICATION: auth method - email/password vs OAuth?]

### Key Entities (if applicable)

- **[Entity]**: [Description and relationships]
- **[Entity]**: [Description and relationships]

## Success Criteria

### Measurable Outcomes

- **SC-001**: [Observable, quantifiable metric] (e.g., "Users complete task in under 2 minutes")
- **SC-002**: [Business or user outcome] (e.g., "90% task completion rate on first attempt")
- **SC-003**: [System capability] (e.g., "Supports 1000 concurrent users")

## Assumptions

- [Assumption 1 and its justification]
- [Assumption 2 and its justification]
- [Default pattern or standard approach chosen]

## Out of Scope

- [Explicitly excluded items]
- [Features for future phases]

## Dependencies & Constraints

- [External systems or dependencies]
- [Regulatory or technical constraints]
- [Related features or prerequisites]
```

---

## Execution Workflow

### Step 1: Parse Feature Intent

Given high-level feature requirements or system intent:
- Extract key actors (who uses this?)
- Identify primary actions (what do they do?)
- Determine business value (why does it matter?)
- Note any constraints or dependencies

### Step 2: Design User Scenarios

Create independently testable user stories:
1. Lead with P1 scenarios (core value, MVP-ready)
2. Follow with P2 scenarios (enhancement, extended use)
3. Add P3 scenarios (edge cases, advanced features)

**Independent test guideline**: Each story should deliver measurable value if developed alone.

### Step 3: Extract Functional Requirements

Translate user scenarios into system capabilities:
- Use consistent naming (FR-001, FR-002, etc.)
- One capability per requirement
- Make each testable (avoid vague language)

**Identify [NEEDS CLARIFICATION] only if**:
- The decision significantly impacts feature scope or UX
- Multiple valid interpretations exist with different implications
- No reasonable default exists
- **LIMIT: Maximum 3 clarifications total**

### Step 4: Define Measurable Success

Success criteria must be:
- **Observable**: Can be verified without implementation details
- **Quantifiable**: Include specific metrics, percentages, counts
- **User-focused**: From user/business perspective, not system internals
- **Technology-agnostic**: No mention of databases, APIs, frameworks, or languages

**Examples of strong success criteria**:
- "Users complete checkout in under 3 minutes"
- "System supports 10,000 concurrent users without degradation"
- "95% of searches return results in under 1 second"
- "Task completion rate improves by 40%"

**Examples of weak success criteria** (too technical):
- ❌ "API response time is under 200ms" (use user-facing metric instead)
- ❌ "Database handles 1000 TPS" (implementation detail)
- ❌ "React components render efficiently" (framework-specific)

### Step 5: Document Entities & Assumptions

Identify key data entities (if applicable):
- What data does the feature work with?
- What are the key relationships?
- Avoid implementation details (no database schema)

Document assumptions:
- What unspecified details did you assume?
- What industry standards or defaults did you apply?
- Why did you make each assumption?

### Step 6: Validate Specification Quality

Before submission, verify:

**Content Quality**
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

**Requirement Completeness**
- [ ] No unresolved [NEEDS CLARIFICATION] markers (max 3)
- [ ] Requirements are testable and unambiguous
- [ ] Success criteria are measurable and technology-agnostic
- [ ] All acceptance scenarios use Given/When/Then format
- [ ] Edge cases are identified
- [ ] Scope is clearly bounded

**Feature Readiness**
- [ ] All functional requirements have clear acceptance criteria
- [ ] User scenarios cover primary and secondary flows
- [ ] Feature meets measurable outcomes in Success Criteria
- [ ] Dependencies and assumptions are documented

---

## Common Pitfalls to Avoid

| Pitfall | Example | Correction |
|---------|---------|-----------|
| **Implementation leakage** | "Use Redis to cache results" | "Cache frequently accessed data to improve response time" |
| **Vague requirements** | "Make it fast and easy to use" | "Users complete task in under 2 minutes with one-click actions" |
| **Technology-specific success metrics** | "Database handles 1000 TPS" | "System supports 10,000 concurrent users" |
| **Missing user perspective** | "API validates input data" | "Users receive clear error messages when input is invalid" |
| **Untestable scenarios** | "The feature should be intuitive" | "New users complete task without support on first attempt" |
| **Too many clarifications** | 5+ [NEEDS CLARIFICATION] markers | Consolidate to max 3 critical items; make informed guesses for rest |

---

## Best Practices for Phase I CLI Features

When writing specifications for Phase I CLI commands:

1. **Define Command Contract**
   - What is the command name and syntax?
   - What arguments and flags does it accept?
   - What is the expected output format?

2. **Document User Workflows**
   - What is the primary interaction sequence?
   - How do users invoke the command?
   - What happens on success and failure?

3. **Specify Output Behavior**
   - What information is displayed?
   - What is the format (text, JSON, table)?
   - How are errors presented?

4. **Address Error Handling**
   - What invalid inputs should be rejected?
   - How should the CLI respond to failures?
   - What recovery options are available?

5. **Consider Integration**
   - Does this command interact with other commands?
   - What data structures are shared?
   - How are dependencies coordinated?

---

## Example: Writing a Todo Add Specification

### Minimal Input
"Users should be able to add new todos from the CLI"

### Resulting Specification Structure

```markdown
# Feature Specification: Add Todo Item

**Feature ID**: F-001-add-todo
**Created**: 2026-01-17
**Status**: Draft
**Context**: Allow users to quickly create new tasks from the command line

## User Scenarios & Testing

### User Story 1 - Create Basic Todo (Priority: P1)

User wants to add a simple task description to their todo list...

**Acceptance Scenarios**:
1. **Given** user is at CLI, **When** they run `todo add "Buy groceries"`, **Then** the task is created and confirmed with an ID
2. **Given** the todo is added, **When** user lists todos, **Then** the new task appears with correct text

---

## Success Criteria

- **SC-001**: Todo is created and persisted (visible on subsequent `list` command)
- **SC-002**: User receives immediate confirmation with task ID
- **SC-003**: New todos are added in under 100ms
```

---

## Usage

### Direct Invocation

When you need to write a specification:

```
Write a specification for: [feature description]

Follow the specification template and principles above.
Use the execution workflow to guide your work.
```

### Integration Points

This skill works with:
- `/sp.specify` - Full feature specification with branch and artifact creation
- `/sp.clarify` - Resolve ambiguities in specifications
- `/sp.plan` - Convert specifications into technical plans
- `/sp.tasks` - Break plans into actionable development tasks

---

## Summary Checklist

After writing a specification, verify:

- ✅ **User Scenarios**: P1/P2/P3 stories with independent test descriptions
- ✅ **Requirements**: Functional requirements are testable, numbered, unambiguous
- ✅ **Success Criteria**: Measurable, quantifiable, technology-agnostic
- ✅ **No Implementation**: No frameworks, languages, databases, or code structure
- ✅ **Assumptions**: All reasonable defaults are documented
- ✅ **Scope**: In-scope and out-of-scope items are clear
- ✅ **Clarifications**: Maximum 3 [NEEDS CLARIFICATION] markers for critical decisions
- ✅ **Quality**: Specification is ready for planning and development

---

**Last Updated**: 2026-01-17
**Project**: Hackathon II – Evolution of Todo
**Phase**: Phase I (CLI Design & Specification)
