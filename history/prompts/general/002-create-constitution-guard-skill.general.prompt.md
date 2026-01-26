---
id: 002
title: Create constitution-guard skill
stage: general
date: 2026-01-17
surface: agent
model: claude-haiku-4-5-20251001
feature: none
branch: master
user: cli-user
command: Create a reusable skill for governance and constraint enforcement
labels: ["governance", "skill-creation", "constitution", "constraint-enforcement", "sdd"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .claude/skills/constitution-guard.md
tests:
  - none
---

## Prompt

Create this skill as a SINGLE file under: .claude/skills/

Skill Name: constitution_guard

Description: Enforces constitution constraints and prevents scope creep, shortcuts, or manual code writing.

Expected Input: Current constitution, specs, plans, or implementation proposals.

Expected Output: Validation confirmations or violation warnings.

Usage Example: Used before planning or implementation begins.

Constraints:
- No application code
- No agent definitions

## Response snapshot

Created `.claude/skills/constitution-guard.md` as a comprehensive governance skill for Hackathon II. The skill provides:

**Core Guardrails Enforced** (7 categories):
1. Spec-Driven Development (SDD) Mandate – prevents implementation without approved specs and enforces spec→plan→tasks→implement workflow
2. Phase Integrity Constraints – enforces 5-phase sequencing and prevents cross-phase feature mixing
3. Scope Creep Prevention – blocks undocumented features and "nice to have" additions
4. Shortcut & Manual Code Detection – detects attempts to bypass SDD workflow or write code directly
5. Constitution Compliance – validates proposals against project constitution principles
6. Technology Stack Integrity – enforces phase-specific tech stacks (Python console in Phase I, Next.js/FastAPI in Phase II, etc.)
7. No Manual Code Writing Enforcement – detects and blocks manual code edits instead of spec-driven generation

**Validation Checklists**:
- Pre-Planning Checklist (10 items) – verifies specs are complete before plan generation
- Pre-Implementation Checklist (9 items) – validates plan, tasks, and design before coding
- Post-Implementation Checklist (7 items) – confirms code follows SDD practices

**Common Violations & Quick Fixes**:
- "Let me just add a quick feature" → requires spec, plan, tasks
- "This is too small to spec" → all code must be spec-driven
- "We should add caching/optimization for future" → YAGNI principle
- "Let me refactor this code" → only if required by spec/task
- "I'll use FastAPI in Phase I" → stack locked to phase
- "Let me implement auth in Phase I" → auth is Phase II only

**Governance Rules**:
- Authority hierarchy: Constitution > Hackathon Requirements > Spec > Plan > Tasks > Code
- Amendment process for changing constraints
- Violation response protocol with specific steps

**7 Detailed Examples**: Each showing a common violation, the constraint being violated, and the corrective action

The skill serves as the **development guardian** that blocks violations and ensures:
- Spec-driven workflow is followed
- Features stay in scope
- No tech stack violations
- No phase mixing
- No manual code writing
- Constitution principles are honored

## Outcome

- ✅ Impact: Provides automated governance enforcement for Hackathon II project phases, preventing scope creep, shortcuts, and constraint violations
- 🧪 Tests: Manual verification of skill structure and governance logic
- 📁 Files: 1 new governance skill file
- 🔁 Next prompts: Phase I spec creation, plan validation using this skill, implementation with constraint checking
- 🧠 Reflection: Skill establishes clear guardrails for spec-driven development and phase integrity, reducing manual review burden and preventing costly scope creep mid-project

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable (governance tool)
- Prompt variant (if applicable): null
- Next experiment: Integrate constitution-guard checks into /sp.plan and /sp.tasks workflows to provide real-time validation during planning and task breakdown phases
