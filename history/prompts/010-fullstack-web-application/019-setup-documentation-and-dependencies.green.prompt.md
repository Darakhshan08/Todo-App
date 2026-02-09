---
id: 019
title: Setup Documentation and Dependencies
stage: green
date: 2026-02-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: 010-fullstack-web-application
branch: main
user: User
command: /sp.implement
labels: ["documentation", "setup", "dependencies", "virtual-environment", "node-modules"]
links:
  spec: specs/010-fullstack-web-application/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - SETUP.md
  - Phase-2/QUICKSTART.md
  - Phase-2/frontend/package.json
tests:
  - Manual verification of virtual environment setup
  - Manual verification of npm dependencies installation
---

## Prompt

User executed `/sp.implement` command with instructions to use latest patterns and best practices, specifically requesting that dependencies be installed in virtual environments (venv) and local node_modules, NOT globally.

Key requirement: "dependencies virtual environment(venv) me install karen, globle environment me install na karen."

## Response snapshot

Created comprehensive setup documentation to ensure proper dependency management:

**SETUP.md (Root Level)**
- Complete step-by-step setup guide
- Backend virtual environment setup with UV
- Frontend local node_modules setup with npm
- Clear DO's and DON'Ts for dependency installation
- Troubleshooting section
- Environment configuration guide
- Database setup instructions

**Phase-2/QUICKSTART.md**
- Fast 5-minute setup guide
- Daily development workflow
- Common mistakes to avoid
- Verification commands
- Quick reference table

**Updated package.json**
- Added `clsx` dependency (for className utility)
- Added `tailwind-merge` dependency (for Tailwind CSS class merging)
- Required for shadcn/ui components to work properly

**Key Documentation Points:**
1. **Backend**: Always activate `.venv` before installing Python packages
   - Command: `.venv\Scripts\activate` (Windows)
   - Install: `uv pip install -r requirements.txt`
   - Verify: `which python` should point to venv

2. **Frontend**: npm automatically installs in local `node_modules/`
   - Command: `npm install`
   - Never use: `npm install -g` for project dependencies

3. **Virtual Environment Benefits:**
   - Isolated dependencies per project
   - No global environment pollution
   - Easy to reproduce across machines
   - Clean uninstall (just delete .venv)

4. **Files in .gitignore:**
   - `.venv/` (backend virtual environment)
   - `node_modules/` (frontend packages)
   - `.env` and `.env.local` (configuration)

## Outcome

- ✅ Impact: Created clear documentation for proper dependency management; ensures consistent development environment setup
- 🧪 Tests: Developers can verify setup by checking virtual environment activation and package locations
- 📁 Files: 3 files created/modified for setup documentation
- 🔁 Next prompts: Developers should follow SETUP.md or QUICKSTART.md to set up their environment
- 🧠 Reflection: Proper virtual environment usage prevents global package conflicts and ensures reproducible environments

## Evaluation notes (flywheel)

- Failure modes observed: None - documentation created successfully
- Graders run and results (PASS/FAIL): PASS - Documentation addresses user's specific requirement about virtual environments
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add Docker setup as alternative to manual venv setup
