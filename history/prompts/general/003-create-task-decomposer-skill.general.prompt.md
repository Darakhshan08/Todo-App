---
id: 003
title: Create task-decomposer skill
stage: general
date: 2026-01-17
surface: agent
model: claude-haiku-4-5-20251001
feature: none
branch: master
user: cli-user
command: Create a reusable skill for task decomposition and execution planning
labels: ["execution", "skill-creation", "task-breakdown", "planning", "sdd"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .claude/skills/task-decomposer.md
tests:
  - none
---

## Prompt

Create this skill as a SINGLE file under: .claude/skills/

Skill Name: task_decomposer

Description: Breaks approved specifications or plans into atomic, Claude Code–executable tasks.

Expected Input: High-level execution or implementation plan.

Expected Output: Ordered list of atomic tasks.

Usage Example: Used before Claude performs any execution.

Constraints:
- No application code
- No agent definitions

## Response snapshot

Created `.claude/skills/task-decomposer.md` as a comprehensive execution planning skill for Hackathon II. The skill provides:

**Core Principles of Task Decomposition** (5 pillars):
1. Atomicity – One clear action per task (not "build auth" but "create login endpoint")
2. Independence – Testable in isolation with no false dependencies
3. Sequencing – Right order with logical prerequisites and parallelization opportunities
4. Specificity – Exact file paths and locations (no ambiguity)
5. Testability – Clear success criteria and acceptance scenarios

**Task Format and Structure**:
- Required format: `- [ ] [ID] [P?] [Story?] Description with exact file path`
- Components: Checkbox, Task ID (T001...), [P] marker (optional), [Story] label (for features), Description
- Valid and invalid examples showing correct vs incorrect task formatting

**Task Organization by Phase** (5-phase model):
1. Phase 1: Setup – Project structure, dependencies, tools
2. Phase 2: Foundation – Blocking prerequisites (models, auth, DB, middleware)
3. Phase 3+: User Stories – One phase per story, organized as: Tests → Models → Services → Endpoints → Integration
4. Final Phase: Polish – Documentation, optimization, deployment

**Dependency Analysis & Sequencing**:
- Three dependency types: Blocking (hard sequential), Shared (multiple users), Independent (parallelizable)
- Dependency graph patterns showing how work flows
- How to identify and mark parallelizable work with [P]

**Task Decomposition Workflow** (6-step process):
1. Parse the plan (extract tech stack, structure, components)
2. Extract user stories (identify features and priorities)
3. Map features to architecture (identify models, services, endpoints)
4. Identify phases (setup, foundation, stories, polish)
5. Create task breakdown (list tasks with dependencies)
6. Validate task quality (atomic, testable, specific)

**Execution Strategy** (how Claude Code uses tasks):
- Task execution model: Read → Open/Create → Write → Test → Commit → Next
- What makes a task executable vs non-executable
- Good vs bad task breakdown with detailed examples

**Parallelization Opportunities**:
- When tasks can run in parallel ([P] marker)
- When they must be sequential
- Parallel execution example showing how independent work can be distributed

**Common Task Decomposition Mistakes** (5 mistakes with fixes):
1. Tasks too large → break into smaller atomic units
2. Tasks too vague → be specific about acceptance criteria
3. Missing file paths → specify exact location
4. False dependencies → mark independent work as [P]
5. Not tied to user stories → link to user story context

**Task Quality Checklist**:
- Format checks (checkbox, ID, file path, labels)
- Content checks (atomic, testable, clear outcome)
- Dependency checks (prerequisites, no circular deps)
- Scope checks (matches spec/plan, no scope creep)

**Integration with Claude Code**:
- How to present tasks (single markdown file format)
- How Claude Code executes tasks (reads, executes in order, references task ID)

**Complete Example**:
- Spec input (user stories with priorities)
- Plan input (architecture, components, structure)
- Task output (phase-by-phase breakdown with dependency graph and parallelization opportunities)

The skill serves as the **execution bridge** that transforms "what to build and how" (spec + plan) into "exactly what to do in what order" (executable tasks).

## Outcome

- ✅ Impact: Provides systematic approach for converting high-level plans into atomic, executable work that Claude Code can complete independently
- 🧪 Tests: Manual verification of task decomposition logic and examples
- 📁 Files: 1 new execution planning skill file
- 🔁 Next prompts: Phase I feature specification, task generation for Todo CRUD, implementation execution
- 🧠 Reflection: Skill enables clear separation between architecture (planning) and execution (tasks), making work parallelizable and traceable. Task decomposition is critical for enabling async, multi-agent, or human development alongside AI-generated code.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable (planning tool)
- Prompt variant (if applicable): null
- Next experiment: Integrate task-decomposer validation into `/sp.tasks` command to auto-check task quality and identify parallelization opportunities before presenting to Claude Code
