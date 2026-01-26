---
id: 001
title: Create spec-writer skill
stage: general
date: 2026-01-17
surface: agent
model: claude-haiku-4-5-20251001
feature: none
branch: master
user: cli-user
command: Create a reusable skill under .claude/skills/
labels: ["specification", "skill-creation", "sdd", "phase-i"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .claude/skills/spec-writer.md
tests:
  - none
---

## Prompt

Create this skill as a SINGLE file under: .claude/skills/

Skill Name: spec_writer

Description: Writes clear, feature-level specifications in Markdown following Spec-Driven Development principles.

Expected Input: High-level feature requirements or system intent.

Expected Output: Well-structured, unambiguous Markdown specifications.

Usage Example: Used when defining Phase I CLI features.

Constraints:
- No application code
- No agent definitions

## Response snapshot

Created `.claude/skills/spec-writer.md` as a comprehensive, reusable specification authoring skill for the Hackathon II project. The skill includes:

- **Specification Writing Principles**: 6 core SDD principles covering WHAT/WHY focus, testable requirements, user scenario prioritization, measurable success, assumptions, and scope boundaries
- **Specification Template**: Complete markdown template with sections for user scenarios, requirements, success criteria, assumptions, dependencies, and out-of-scope items
- **Execution Workflow**: 6-step process for parsing intent, designing scenarios, extracting requirements, defining success metrics, documenting entities, and validating quality
- **Phase I CLI Guidelines**: Best practices for command-line feature specifications including command contracts, user workflows, output behavior, error handling, and integration patterns
- **Quality Checklist**: Comprehensive validation checklist covering content quality, requirement completeness, and feature readiness
- **Common Pitfalls Table**: Examples and corrections for implementation leakage, vague requirements, and other specification mistakes
- **Example**: Walkthrough of writing a "Todo Add" specification

The skill serves as a standalone reference for writing unambiguous, testable specifications and integrates with existing spec-driven development workflows (sp.specify, sp.clarify, sp.plan, sp.tasks).

## Outcome

- ✅ Impact: Provides reusable, structured guidance for writing SDD specifications throughout the Evolution of Todo project
- 🧪 Tests: Manual verification of file creation and content structure
- 📁 Files: 1 new file created
- 🔁 Next prompts: Phase I feature specification authoring, CLI command definitions
- 🧠 Reflection: Skill consolidates SDD practices into a single, searchable reference that can be extended with project-specific patterns as the Hackathon II project evolves

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable (tool creation)
- Prompt variant (if applicable): null
- Next experiment: Extend skill with project-specific CLI conventions and schema patterns as Phase I features are defined
