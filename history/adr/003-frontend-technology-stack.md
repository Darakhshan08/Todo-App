# ADR-003: Frontend Technology Stack

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2026-02-06
- **Feature:** 010-fullstack-web-application
- **Context:** Phase II requires a modern, responsive frontend application that integrates seamlessly with the FastAPI backend, supports JWT authentication with Better Auth, implements responsive UI for task management, and provides optimal developer experience. The constitution mandates Next.js 16+ with App Router, TypeScript, and Tailwind CSS for consistent styling across the team.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence – affects how all frontend components are structured and developed
     2) Alternatives: Multiple viable options considered with tradeoffs (Next.js vs Remix vs Vite)
     3) Scope: Cross-cutting concern affecting all UI components, routing, and user interactions
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Use **Next.js 16+ with App Router ecosystem** for the frontend application:

- **Framework**: Next.js 16+ (App Router) - Modern React framework with file-based routing
- **Styling**: Tailwind CSS - Utility-first CSS framework for rapid UI development
- **UI Components**: shadcn/ui - Pre-built accessible components that integrate with Tailwind
- **Deployment**: Vercel (recommended for Next.js) or compatible hosting platform
- **State Management**: React hooks and Context API (for simplicity and team familiarity)
- **API Integration**: Client-side API calls with proper JWT token handling for authentication

<!-- For technology stacks, list all components:
     - Framework: Next.js 16+ (App Router)
     - Styling: Tailwind CSS
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- ✅ **Developer Experience**: Excellent TypeScript support, fast refresh, and extensive documentation
- ✅ **Performance**: Built-in optimizations, automatic code splitting, and static generation capabilities
- ✅ **Authentication Integration**: Compatible with Better Auth JWT tokens and session management
- ✅ **Responsive Design**: Tailwind CSS enables rapid responsive UI development with consistent styling
- ✅ **Component Reusability**: shadcn/ui provides well-tested, accessible components that speed development
- ✅ **SEO & Accessibility**: Next.js App Router provides excellent SEO capabilities and accessibility out of the box
- ✅ **Team Familiarity**: Consistent with constitution requirements and likely familiar to team members

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- ⚠️ **Vendor Lock-in**: Potential tight coupling with Next.js ecosystem and Vercel deployment
- ⚠️ **Bundle Size**: Risk of large bundle sizes if not properly optimized
- ⚠️ **Learning Curve**: App Router requires understanding of server vs client components
- ⚠️ **Framework Coupling**: Heavy reliance on Next.js conventions may limit flexibility
- ⚠️ **Dependency Complexity**: Multiple interconnected tools (Next.js, Tailwind, shadcn) increase complexity

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

### Alternative Stack A: Remix + Styled Components + Cloudflare Pages
- **Pros**: Flexible routing, superior error handling, better control over data loading
- **Cons**: Smaller ecosystem, less team familiarity, potential authentication integration complexity
- **Why Rejected**: Constitution specifically favors Next.js; team familiarity factor outweighs potential benefits

### Alternative Stack B: Vite + React + Vanilla CSS + Self-hosting
- **Pros**: Faster builds, simpler setup, greater flexibility in CSS approach
- **Cons**: Missing Next.js features (SSR, file routing, SEO), requires more manual setup
- **Why Rejected**: Would lose important Next.js advantages for web application (SEO, routing, deployment simplicity)

### Alternative Stack C: Create React App + Material UI + Traditional Routing
- **Pros**: Proven technology, rich component library in Material UI
- **Cons**: Outdated compared to Next.js 16+ features, no App Router benefits, end-of-life concerns
- **Why Rejected**: Constitution mandates Next.js 16+ with App Router; CRA is no longer maintained

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: ../../specs/010-fullstack-web-application/spec.md
- Implementation Plan: ../../specs/010-fullstack-web-application/plan.md
- Related ADRs: ADR-001 (Layered Architecture Pattern), ADR-004 (Backend Technology Stack)
- Evaluator Evidence: [PHR reference to planning session]
