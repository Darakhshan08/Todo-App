---
id: 004
title: Create cli-app-pattern skill
stage: general
date: 2026-01-17
surface: agent
model: claude-haiku-4-5-20251001
feature: none
branch: master
user: cli-user
command: Create a reusable skill for CLI application patterns
labels: ["architecture", "skill-creation", "cli-design", "phase-i", "patterns"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .claude/skills/cli-app-pattern.md
tests:
  - none
---

## Prompt

Create this skill as a SINGLE file under: .claude/skills/

Skill Name: cli_app_pattern

Description: Defines a reusable architectural pattern for deterministic, user-friendly CLI applications.

Expected Input: CLI feature or behavior requirements.

Expected Output: Recommended CLI structure, commands, and interaction patterns.

Usage Example: Used exclusively in Phase I for CLI-based Todo system design.

Constraints:
- No application code
- No agent definitions

## Response snapshot

Created `.claude/skills/cli-app-pattern.md` as a comprehensive architectural pattern guide for Phase I CLI applications. The skill provides:

**Core CLI Design Philosophy** (5 principles):
1. Determinism – Same input always produces same output
2. User-Friendliness – Clear, helpful, obvious interaction
3. Scriptability – Machine-readable, piping support, automation-ready
4. Predictability – Consistent behavior, obvious command structure
5. Simplicity – One tool, one thing, focused scope

**Three-Tier Architecture**:
- User/Command Layer (CLI entry, parsing)
- Application Logic Layer (services, business logic)
- Data/State Layer (in-memory storage)

**Recommended Project Structure**:
- `src/__main__.py` – Entry point
- `src/main.py` – Command dispatcher
- `src/commands/` – Individual command handlers
- `src/models/` – Data models
- `src/services/` – Business logic
- `src/storage/` – Data persistence/retrieval
- `src/utils/` – Formatters, validators, errors
- `tests/` – Unit, integration, E2E tests

**Command Structure & Naming** (verb-noun pattern):
- Consistent command format: `todo <verb> <noun> [options]`
- Standard commands for todo: add, list, update, delete, complete
- Short flags and long form support (e.g., -s / --status)
- Clear required vs optional arguments

**Input Handling & Validation**:
- Argument parser pattern (argparse recommended)
- Three-tier validation: Parse → Validate → Execute
- Comprehensive validation rules (required fields, types, bounds, existence)
- Error handling with specific messages and exit codes

**Output Formatting** (three modes):
- Human-readable (default) – Clear, visual, status indicators
- JSON (--json flag) – Machine-readable for automation
- Compact/Raw (--raw flag) – Minimal, pipe-friendly

**Deterministic Output**:
- Consistent ordering (by ID, alphabetical, by date)
- ISO format dates
- Aligned columns for scanning
- Consistent error message format
- Predictable exit codes

**State Management Patterns**:
- Singleton pattern for global task store (Phase I)
- In-memory dictionary storage
- Abstracted storage layer for future DB migration
- Persistence hooks for Phase II upgrade

**Interaction Models**:
- Non-Interactive Model (recommended for Phase I) – Command-line args → Execute → Exit
- Interactive REPL Model (not recommended) – Session loop → Prompt → Execute
- Rationale: Non-interactive is scriptable, testable, deterministic

**Testing CLI Applications** (three levels):
1. Unit tests – Individual command handlers
2. Integration tests – Command + storage interaction
3. End-to-end tests – Actual CLI invocation
- Verification of determinism, exit codes, JSON validity

**Framework Recommendations**:
- argparse (built-in, simple) – Recommended for Phase I
- Click (moderate complexity)
- Typer (modern, type hints)
- Hydra (complex configs)
- Includes example argparse implementation

**Error Handling Pattern**:
- Exit code convention: 0 (success), 1 (validation), 2 (runtime), 3 (not found)
- Exception hierarchy: TodoError, ValidationError, NotFoundError, RuntimeError
- Specific error messages for users

**User Experience Patterns**:
- Feedback loop: Action → Status → Result
- Clear help text (--help, examples)
- Visual status indicators (✓, ✗, →, •)
- Confirmation for destructive operations
- Deterministic progress

**Phase I Specific Architecture**:
- Entry point → main.py → command router → command handlers → task service → output formatter → task store
- Task model with dataclass (title, description, completed, created_at, updated_at)
- 5 basic commands: add, list, update, delete, complete
- Each command with example syntax and output

**Phase I Command Examples**:
```
$ todo add "Buy groceries" "Milk, eggs"
✓ Task added (ID: 1)

$ todo list
Tasks (1 total):
  1. Buy groceries [pending]

$ todo update 1 --title "Buy groceries and fruits"
✓ Task updated

$ todo delete 1
✓ Task deleted

$ todo complete 1
✓ Task marked complete
```

**Evolution Path to Phase II**:
- CLI commands → Web endpoints (POST, GET, PUT, DELETE, PATCH)
- task_service.py remains mostly unchanged
- task_store.py abstraction allows in-memory → database migration
- Output formatting becomes JSON responses

**CLI Best Practices Checklist** (4 categories):
- Design (command naming, arguments, help, output determinism)
- Implementation (parsing, validation, errors, exit codes)
- Testing (unit, integration, E2E, error cases)
- User Experience (help discovery, examples, feedback, readability)

## Outcome

- ✅ Impact: Provides comprehensive architectural blueprint for Phase I CLI application, ensuring deterministic, user-friendly design that transitions smoothly to Phase II
- 🧪 Tests: Manual verification of architecture patterns and examples
- 📁 Files: 1 new CLI architecture pattern file
- 🔁 Next prompts: Phase I todo spec creation, CLI command design, task breakdown for implementation
- 🧠 Reflection: Skill bridges the gap between SDD principles and concrete CLI implementation. Patterns are specific enough for Phase I execution but general enough to inform future web app architecture.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable (architecture reference)
- Prompt variant (if applicable): null
- Next experiment: Create Phase I todo app specification using this CLI pattern as architectural reference
