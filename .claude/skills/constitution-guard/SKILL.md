---
name: constitution-guard
description: Enforces constitution constraints and prevents scope creep, shortcuts, or manual code writing
category: governance
input: Current constitution, specs, plans, or implementation proposals
output: Validation confirmations or violation warnings with corrective actions
context: Used before planning or implementation begins to enforce project standards
constraints:
  - No application code generation
  - No agent definitions
  - Validation and governance only
---

## Overview

`constitution_guard` is a reusable governance skill for Hackathon II – Evolution of Todo. It validates artifacts against the project constitution, prevents scope creep, enforces the spec-driven development (SDD) workflow, and detects attempts to bypass governance rules.

**When to use**: Before planning, during implementation, or when proposals introduce scope changes or policy violations.

**Key responsibility**: Be the guardian of project standards and prevent development from proceeding with violations.

---

## Guardrails & Constraints Enforced

### 1. **Spec-Driven Development (SDD) Mandate**

**The Core Principle**: "You cannot write code manually. You must refine the Spec until Claude Code generates the correct output."

**Guard against**:
- ✗ Proposing implementation without an approved spec
- ✗ Skipping the spec → plan → tasks → implement workflow
- ✗ Code written outside of Claude Code (manual coding)
- ✗ Implementation that diverges from approved specs
- ✗ Undocumented architectural changes

**Validation Process**:
1. Check if feature has a corresponding spec file (specs/[feature-name]/spec.md)
2. Verify spec is marked "Ready for Planning" or approved status
3. Confirm plan exists and references the spec
4. Validate tasks exist and map to plan sections
5. Ensure all code changes reference task IDs

**Violation Response**:
```
⚠️  SPEC-DRIVEN DEVELOPMENT VIOLATION
Feature: [feature-name]
Status: No approved spec found

Action required:
1. Create or approve spec at: specs/[feature-name]/spec.md
2. Mark status as "Ready for Planning"
3. Run /sp.plan to generate technical plan
4. Run /sp.tasks to break into implementation tasks
5. Only then implement via Claude Code

Reference: Hackathon II Constraint - "No manual code writing"
```

---

### 2. **Phase Integrity Constraints**

**The Phases**: Five strictly-sequenced phases, each with defined scope and technology stack.

| Phase | Features | Tech Stack | Scope Boundary |
|-------|----------|-----------|-----------------|
| **I** | 5 Basic CRUD | Python, CLI | In-memory console app |
| **II** | 5 Basic + Auth | Next.js, FastAPI, Neon DB | Full-stack web app |
| **III** | 5 Basic + Chatbot | ChatKit, Agents SDK, MCP | AI-powered chat interface |
| **IV** | 5 Basic + K8s | Docker, Minikube, Helm | Local Kubernetes |
| **V** | All + Advanced | Kafka, Dapr, Cloud K8s | Production cloud deployment |

**Guard against**:
- ✗ Implementing Phase III features (chatbot) in Phase I (console app)
- ✗ Adding Phase V features (Kafka, Dapr) before Phase IV complete
- ✗ Using unauthorized tech stack (e.g., Next.js in Phase I)
- ✗ Mixing features from multiple phases
- ✗ Intermediate/Advanced features before Basic Level complete

**Validation Process**:
1. Identify current phase from git branch or context
2. Extract proposed features from spec/plan/code
3. Cross-reference against phase requirements table
4. Check technology stack compliance
5. Verify no features from future phases

**Violation Response**:
```
⚠️  PHASE INTEGRITY VIOLATION
Proposed Feature: [feature-name]
Current Phase: [phase]
Scope: [feature] is a Phase [n] feature, not Phase [current]

Why this matters:
- [feature] requires [tech-stack] which is not available until Phase [n]
- Building out of order creates rework and breaks sequential learning

Options:
A) Move [feature] to Phase [n] spec
B) Focus on Phase [current] requirements only: [list of phase-appropriate features]

Reference: Hackathon II Phases Overview - Phase [current] scope defined
```

---

### 3. **Scope Creep Prevention**

**The Guard**: Every feature must be explicitly listed in the phase requirements or explicitly rejected in the "Out of Scope" section.

**Guard against**:
- ✗ Features not in the 5 Basic Level items (Phase I-II) or Intermediate/Advanced (Phase III-V)
- ✗ "Nice to have" features that weren't pre-approved
- ✗ Performance optimizations that weren't in success criteria
- ✗ Refactoring or "code cleanup" not tied to specs
- ✗ "Future-proofing" code for hypothetical requirements

**Validation Process**:
1. Parse proposed feature/change from spec, plan, or code
2. Cross-reference against phase feature list
3. Check if feature appears in spec's "Out of Scope" section
4. Verify acceptance criteria don't request extras
5. Confirm no "YAGNI violations" (You Aren't Gonna Need It)

**Violation Response**:
```
⚠️  SCOPE CREEP DETECTED
Proposed: [feature-name]
Status: Not in Phase [phase] requirements

Phase [phase] Features:
- ✓ Add Task
- ✓ Delete Task
- ✓ Update Task
- ✓ View Task List
- ✓ Mark Complete
[Your feature is not listed above]

Options:
1. Remove [feature] and focus on approved features
2. Document in Out of Scope section if intentionally excluded
3. Create a proposal for Phase [n+1] if this belongs in a later phase

Reference: Hackathon II Todo App Feature Progression
```

---

### 4. **Shortcut & Manual Code Detection**

**The Guard**: Detect attempts to bypass spec-driven workflow or manually write code.

**Guard against**:
- ✗ "Let me just write this function quickly..." (no spec reference)
- ✗ Code changes without corresponding task IDs
- ✗ Implementation PRs that reference no plan or tasks
- ✗ Code reviews that approve implementation without spec verification
- ✗ Direct code generation without spec refinement loop
- ✗ "This is a small fix, no spec needed" reasoning

**Validation Process**:
1. Check PR/commit messages for spec/plan/task references
2. Scan code for task ID comments (e.g., `# Task: T-001`)
3. Verify code files contain header comments linking to spec section
4. Confirm implementation history includes spec-driven iterations
5. Look for "quick fix" or "just adding" language that signals shortcuts

**Violation Response**:
```
⚠️  SHORTCUT DETECTED
Proposal: Direct code implementation without spec reference

Context: [What was proposed]
Problem: No task ID, no spec reference, no plan linkage

The Spec-Driven Approach:
1. Start with WHAT (spec) - User needs and acceptance criteria
2. Move to HOW (plan) - Technical architecture and design
3. Break into tasks - Atomic work units with test cases
4. Then IMPLEMENT - Code changes with task references
5. Validate - Code follows tasks, tasks follow plan, plan follows spec

Required action:
1. Update/create spec at specs/[feature]/spec.md
2. Run /sp.plan to create technical plan
3. Run /sp.tasks to generate implementation tasks
4. Reference task IDs in code comments and commits
5. Then proceed with implementation

Reference: CLAUDE.md - "You cannot write code manually"
```

---

### 5. **Constitution Compliance**

**The Guard**: Enforce project constitution principles and standards.

**Validation Process**:
1. Load constitution from `.specify/memory/constitution.md`
2. Parse declared principles and constraints
3. Check proposed code/architecture against each principle
4. Validate no approved shortcuts or exceptions
5. Ensure governance section is honored

**Violation Response**:
```
⚠️  CONSTITUTION VIOLATION
Principle: [principle-name]
Violation: [what violates the principle]

Constitution States:
"[Quote from principle]"

Your proposal violates this because:
[Specific explanation of how proposal breaks the principle]

Allowed Options:
1. Modify proposal to align with principle
2. Request constitution amendment (requires documentation + approval)
3. Document exception in constitution Exceptions section

Reference: Constitution.md - [Principle Name]
```

---

### 6. **Technology Stack Integrity**

**The Guard**: Enforce phase-specific technology stacks.

**Guard against**:
- ✗ Using FastAPI in Phase I (console-only phase)
- ✗ Adding Next.js before Phase II
- ✗ Using Kafka before Phase V
- ✗ Adding unauthorized dependencies
- ✗ Changing approved tech stack without amendment

**Phase I Stack** (Console App):
- ✓ Python 3.13+
- ✓ Claude Code
- ✓ Spec-Kit Plus
- ✗ No web frameworks, databases, or external services

**Phase II Stack** (Full-Stack Web):
- ✓ Next.js 16+ (App Router)
- ✓ FastAPI
- ✓ SQLModel
- ✓ Neon PostgreSQL
- ✓ Better Auth
- ✗ No Kafka, no MCP, no Kubernetes

**Phase III Stack** (AI Chatbot):
- ✓ All Phase II
- ✓ OpenAI ChatKit
- ✓ OpenAI Agents SDK
- ✓ Official MCP SDK
- ✗ No Kafka, no Kubernetes

**Phase IV Stack** (Local K8s):
- ✓ All Phase III
- ✓ Docker
- ✓ Minikube
- ✓ Helm
- ✓ kubectl-ai, kagent
- ✓ Gordon (Docker AI)
- ✗ No cloud services, no Kafka

**Phase V Stack** (Cloud Deployment):
- ✓ All Phase IV
- ✓ Kafka (Redpanda Cloud or Strimzi)
- ✓ Dapr
- ✓ Cloud K8s (Azure/GCP/Oracle)
- ✓ CI/CD (GitHub Actions)

**Validation Process**:
1. Identify current phase
2. Parse tech stack from proposed code/config
3. Cross-reference against approved stack
4. Check for unauthorized dependencies in requirements files
5. Verify docker images match approved services

**Violation Response**:
```
⚠️  TECHNOLOGY STACK VIOLATION
Detected: [tech-name] in Phase [phase]
Status: [tech-name] is not approved until Phase [n]

Current Phase [phase] Stack:
✓ [approved tech 1]
✓ [approved tech 2]
✗ [violation] - Not until Phase [n]

Reason for phasing:
[Why this tech is sequenced for Phase n]

Action:
1. Remove or defer [tech-name]
2. Use approved alternatives from Phase [phase] stack
3. Document in spec if you need Phase [n] tech in Phase [phase]

Reference: Hackathon II - Technology Stack by Phase
```

---

### 7. **No Manual Code Writing Enforcement**

**The Guard**: Detect attempts to write code directly instead of refining specs.

**Validation Process**:
1. Check if implementation was preceded by spec iteration
2. Look for "let me just write this" language
3. Verify Claude Code was used, not manual editing
4. Confirm spec was refined based on feedback
5. Check for unexplained code changes without task references

**Violation Response**:
```
⚠️  MANUAL CODE WRITING DETECTED
Status: Code appears to be written manually, not via Claude Code

The Constraint:
"You cannot write the code manually. You must refine the Spec until Claude Code generates the correct output."

This means:
1. If the code isn't correct → FIX THE SPEC
2. Iterate spec until Claude Code generates what you need
3. Never edit generated code or write code directly

What happened:
[Detection logic - what suggested manual writing]

Recovery:
1. Revert code changes
2. Identify what the spec was missing
3. Update spec section that caused Claude Code to generate incorrect output
4. Run Claude Code again with refined spec
5. Validate generated code matches refined spec

Reference: CLAUDE.md - Spec-Driven Development Constraint
```

---

## Validation Checklist

Use this checklist before planning, before implementation, and during reviews:

### Pre-Planning Checklist ✓

- [ ] Feature spec exists and is marked "Ready for Planning"
- [ ] Spec covers all user scenarios (P1, P2, P3 if applicable)
- [ ] Functional requirements are testable and technology-agnostic
- [ ] Success criteria are measurable and observable
- [ ] No implementation details leak into spec
- [ ] Assumptions are documented
- [ ] Feature belongs in current phase (not future/past phases)
- [ ] Out of Scope section lists explicitly excluded items
- [ ] No [NEEDS CLARIFICATION] markers remain (or max 3 critical ones)
- [ ] Constitution principles are honored in spec

### Pre-Implementation Checklist ✓

- [ ] Plan exists and references spec sections
- [ ] Plan includes component breakdown, APIs, interfaces
- [ ] Tasks exist, each with task ID and spec/plan references
- [ ] Tasks are atomic and independently testable
- [ ] Technology stack matches current phase
- [ ] No scope creep (all tasks relate to approved features)
- [ ] No shortcuts documented in plan
- [ ] Code references will include task IDs
- [ ] No manual coding has occurred (spec-driven workflow verified)

### Post-Implementation Checklist ✓

- [ ] All code changes reference task IDs
- [ ] Code comments link to spec sections
- [ ] Implementation follows plan exactly (no deviations)
- [ ] No features beyond approved scope
- [ ] Test coverage matches acceptance criteria
- [ ] No manual code edits (all generated via Claude Code)
- [ ] Git history shows spec-driven iteration

---

## Common Violations & Quick Fixes

### Violation: "Let me just add a quick feature"

**Why it's a violation**: Features not in phase requirements create scope creep.

**Fix**:
```
1. Check if feature is in phase requirements
2. If YES → Create spec for that feature
3. If NO → Either remove it or formally propose for next phase
4. Never add undocumented features
```

---

### Violation: "This is too small to spec"

**Why it's a violation**: All code must be spec-driven; size doesn't matter.

**Fix**:
```
1. Write minimal spec (even 1 paragraph counts)
2. Create plan with brief architecture notes
3. Create task(s) with specific outputs
4. Only then implement via Claude Code
5. Small features = quick specs, not no specs
```

---

### Violation: "We should add caching/optimization for future"

**Why it's a violation**: YAGNI (You Aren't Gonna Need It); no hypothetical features.

**Fix**:
```
1. Check if optimization is in success criteria
2. If YES → Spec it, plan it, task it, implement it
3. If NO → Remove from proposal
4. Prioritize approved features over "nice to have" additions
```

---

### Violation: "Let me refactor this code"

**Why it's a violation**: Refactoring not tied to a feature is scope creep.

**Fix**:
```
1. Is refactoring required by a spec/task?
2. If YES → Reference the task in commit
3. If NO → Don't refactor; YAGNI applies
4. Never improve code "just because"
```

---

### Violation: "I'll use FastAPI in Phase I"

**Why it's a violation**: Tech stacks are phase-locked per hackathon requirements.

**Fix**:
```
1. Phase I = Python console only (no frameworks)
2. Phase II = FastAPI introduced
3. Check phase requirements before adding tech
4. Propose constitution amendment if you need to change stack
```

---

### Violation: "Let me implement auth in Phase I"

**Why it's a violation**: Auth is Phase II; Phase I is in-memory console only.

**Fix**:
```
1. Phase I Basic Level = 5 CRUD operations only
2. Auth belongs in Phase II
3. Remove from Phase I spec/plan
4. Create separate spec for Phase II auth
```

---

## Governance Rules

### Hierarchy of Authority

When conflicts arise, apply this hierarchy:

```
1. Constitution Principles (highest)
   ↓
2. Hackathon Requirements (5 phases, stacks, constraints)
   ↓
3. Feature Specification (WHAT)
   ↓
4. Technical Plan (HOW)
   ↓
5. Task Breakdown (BREAKDOWN)
   ↓
6. Implementation Code (lowest)
```

**What this means**: If code violates a task, fix the task. If task violates plan, fix plan. If plan violates spec, fix spec. If spec violates constitution, fix constitution (with amendment).

---

### Amendment Process

To amend constitution or constraints:

1. Document the proposal with justification
2. Show how current constraint blocks a legitimate need
3. Propose specific amendment wording
4. Create ADR (Architecture Decision Record) explaining decision
5. Get explicit approval before proceeding
6. Update constitution.md with version/date
7. Announce to team

**No undocumented exceptions.** If it's not in the constitution, it's not allowed.

---

### Violation Response Protocol

When this skill detects a violation:

1. **Identify the Violation Type** (SDD, Phase, Scope, Stack, Manual Code, Shortcut)
2. **State the Constraint** (quote from Hackathon II docs or constitution)
3. **Explain the Impact** (why this matters for the project)
4. **Offer 2-3 Options** (compliant alternatives)
5. **Block Proceeding** until violation is resolved
6. **Document the Decision** in git history

**Never proceed with violations.** The spec-driven workflow works only if all participants stay within constraints.

---

## Usage Examples

### Example 1: Spec-Driven Development Validation

**Scenario**: Developer proposes implementation without spec.

**Input**:
```
I want to implement task search functionality. Here's the code...
```

**Guard Response**:
```
⚠️  SPEC-DRIVEN DEVELOPMENT VIOLATION
Feature: Task Search
Status: No approved spec found

Action required:
1. Create spec at: specs/task-search/spec.md
   Include: user scenarios, functional requirements, success criteria
2. Run /sp.plan to generate technical plan
3. Run /sp.tasks to break into implementation tasks
4. Then share your code tied to task IDs

Phase Context: Task search is not in Phase I requirements
- Phase I: 5 Basic CRUD operations only
- Task search belongs in Phase II or III (filtering/search)

Next steps: Confirm which phase this feature belongs to, then follow SDD workflow.
```

---

### Example 2: Phase Integrity Check

**Scenario**: Developer wants to add Kafka support in Phase II.

**Input**:
```
Our Phase II web app needs Kafka for real-time sync...
```

**Guard Response**:
```
⚠️  PHASE INTEGRITY VIOLATION
Proposed Feature: Kafka integration
Current Phase: Phase II (Full-Stack Web App)
Issue: Kafka is a Phase V (Cloud Deployment) feature

Phase II Requirements:
✓ CRUD operations (add, delete, update, view, complete)
✓ RESTful API endpoints
✓ User authentication
✗ Kafka - Not until Phase V

Why phases are ordered:
1. Phase I: Console proof-of-concept
2. Phase II: Web app + persistence
3. Phase III: AI chatbot interface
4. Phase IV: Kubernetes + containers
5. Phase V: Event-driven architecture (Kafka, Dapr)

Options:
A) Remove Kafka; focus on Phase II requirements
B) Propose architecture that avoids Kafka in Phase II (use DB polling?)
C) Request constitution amendment to move Kafka to Phase IV

Recommendation: Complete Phase II web app first, then add event-driven features in Phase V.
```

---

### Example 3: Scope Creep Detection

**Scenario**: Spec includes "advanced search with filters" in Phase I.

**Input**:
```
Spec for Phase I: Add Task, Delete, Update, View, Complete, and also...
- Full-text search
- Filter by date range
- Sorting options
```

**Guard Response**:
```
⚠️  SCOPE CREEP DETECTED
Proposed: Full-text search, date range filter, sorting
Phase: I (Basic Level)

Phase I Features (Approved):
✓ Add Task
✓ Delete Task
✓ Update Task
✓ View Task List
✓ Mark Complete
✗ Search/Filter (not in Phase I)

Advanced features timeline:
- Phase II: Basic filtering
- Phase III: Advanced search (with AI)
- Phase V: Full-text + complex queries

Action:
1. Remove search/filter/sorting from Phase I spec
2. Keep 5 Basic CRUD operations only
3. Create separate spec for Phase II filtering feature
4. Mark advanced search as "Out of Scope" for Phase I

This keeps Phase I focused and manageable.
```

---

## Summary: The Constitution Guard's Job

This skill is your **development guardian**. Its job is to:

| Responsibility | What It Checks |
|---|---|
| **Spec Integrity** | Specs exist, are approved, complete before planning |
| **Phase Alignment** | Features belong in current phase, stacks match |
| **Scope Control** | No undocumented features, no feature creep |
| **Shortcut Detection** | Spec-driven workflow is followed, no manual coding |
| **Stack Compliance** | Tech choices match current phase |
| **Constitution Honor** | All proposals align with project principles |
| **Governance** | Amendment process is followed for exceptions |

**When in doubt, the constitution_guard blocks and requests clarification.** It's better to clarify than to discover problems after implementation.

---

**Last Updated**: 2026-01-17
**Project**: Hackathon II – Evolution of Todo
**Phase**: All Phases (Governance)
**Authority**: Hackathon II Spec + .specify/memory/constitution.md

