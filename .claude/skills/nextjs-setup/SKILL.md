---
name: nextjs-setup
description: Initialize a modern Next.js 16+ project with App Router, TypeScript, and Tailwind CSS. Use when the user wants to create a new Next.js application, set up a Next.js project, or scaffold a modern React application with Next.js framework.
---

# Next.js 16+ Project Setup

Initializes a production-ready Next.js 16+ application with App Router, TypeScript, Tailwind CSS, and proper folder structure following official Next.js conventions.

## Prerequisites

- Node.js 18.17 or later
- Package manager: npm, pnpm, yarn, or bun

## Instructions

### Step 1: Create Next.js Application

Use `create-next-app@latest` to initialize the project with recommended defaults:

**Interactive Mode** (allows customization):
```bash
npx create-next-app@latest
```

**Non-interactive Mode** (uses defaults):
```bash
npx create-next-app@latest my-app --yes
cd my-app
npm run dev
```

**With specific package managers**:
```bash
# pnpm (recommended for performance)
pnpm create next-app@latest my-app --yes

# yarn
yarn create next-app@latest my-app --yes

# bun
bun create next-app@latest my-app --yes
```

The `--yes` flag automatically enables:
- ✅ TypeScript
- ✅ ESLint
- ✅ Tailwind CSS
- ✅ App Router
- ✅ Turbopack (for faster dev builds)
- ✅ Import alias (`@/*`)

### Step 2: Verify Project Structure

The generated project follows this structure:

```
my-app/
├── app/
│   ├── layout.tsx          # Root layout (required)
│   ├── page.tsx            # Home page
│   ├── globals.css         # Global styles with Tailwind
│   └── favicon.ico
├── public/                 # Static assets
├── node_modules/
├── .gitignore
├── next.config.ts          # Next.js configuration
├── tailwind.config.ts      # Tailwind configuration
├── tsconfig.json           # TypeScript configuration
├── postcss.config.mjs      # PostCSS for Tailwind
└── package.json
```

### Step 3: Understand Key Files

**Root Layout** (`app/layout.tsx`):
```typescript
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

**Home Page** (`app/page.tsx`):
```typescript
export default function Page() {
  return (
    <main>
      <h1>Welcome to Next.js 16</h1>
    </main>
  )
}
```

**Tailwind Config** (`tailwind.config.ts`):
```typescript
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
export default config;
```

**TypeScript Config** (`tsconfig.json`):
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "jsx": "preserve",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "allowJs": true,
    "forceConsistentCasingInFileNames": true,
    "incremental": true,
    "noEmit": true,
    "plugins": [{ "name": "next" }],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

### Step 4: App Router Conventions

**File Naming Conventions**:
- `layout.tsx` - Shared UI across routes (required in root)
- `page.tsx` - Makes route publicly accessible
- `route.ts` - API route handler
- `loading.tsx` - Loading UI
- `error.tsx` - Error UI
- `not-found.tsx` - 404 UI

**Folder Structure for Routes**:
```
app/
├── layout.tsx              # Root layout
├── page.tsx                # / route
├── blog/
│   ├── page.tsx            # /blog route
│   ├── layout.tsx          # Blog layout (optional)
│   └── [slug]/
│       └── page.tsx        # /blog/[slug] dynamic route
├── api/
│   └── posts/
│       └── route.ts        # /api/posts endpoint
└── dashboard/
    ├── layout.tsx
    └── page.tsx            # /dashboard route
```

**Important Rules**:
- Cannot have `route.ts` and `page.tsx` at the same route segment
- Root layout MUST include `<html>` and `<body>` tags
- Layouts must accept `children` prop
- All components in `app/` are Server Components by default

### Step 5: Start Development

```bash
# Development mode (with Turbopack)
npm run dev

# Production build
npm run build

# Start production server
npm start

# Lint code
npm run lint
```

Visit `http://localhost:3000` to see your application.

## Common Customizations

### Add Components Directory

```bash
mkdir components
```

Update `tailwind.config.ts`:
```typescript
content: [
  "./app/**/*.{js,ts,jsx,tsx,mdx}",
  "./components/**/*.{js,ts,jsx,tsx,mdx}",
],
```

### Create API Route

```typescript
// app/api/hello/route.ts
export async function GET(request: Request) {
  return Response.json({ message: "Hello from Next.js 16!" })
}
```

### Add Dynamic Route

```typescript
// app/blog/[slug]/page.tsx
export default function BlogPost({
  params
}: {
  params: { slug: string }
}) {
  return <h1>Post: {params.slug}</h1>
}
```

### Create Nested Layout

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="dashboard">
      <nav>Dashboard Nav</nav>
      <main>{children}</main>
    </div>
  )
}
```

## Best Practices

1. **Use Server Components by default** - Only add `'use client'` when needed (interactivity, hooks, browser APIs)
2. **Colocate files** - Keep components, styles, and tests near their routes
3. **Import aliases** - Use `@/` prefix for absolute imports: `import { Button } from '@/components/ui/button'`
4. **Async components** - Fetch data directly in Server Components:
   ```typescript
   export default async function Page() {
     const data = await fetch('https://api.example.com/data')
     const posts = await data.json()
     return <div>{/* render posts */}</div>
   }
   ```
5. **Type safety** - Leverage TypeScript for params, searchParams, and props
6. **Tailwind utilities** - Use utility classes instead of custom CSS

## Troubleshooting

**Port already in use**:
```bash
npm run dev -- -p 3001
```

**Clear cache**:
```bash
rm -rf .next
npm run dev
```

**TypeScript errors**:
```bash
npm run build
# TypeScript will show all errors
```

## Examples

### Full Project Setup Command

```bash
# Create project with pnpm
pnpm create next-app@latest my-nextjs-app --yes

# Navigate and start
cd my-nextjs-app
pnpm dev
```

### Custom Setup (Interactive)

```bash
npx create-next-app@latest

# You'll be prompted:
# ✔ What is your project named? › my-app
# ✔ Would you like to use TypeScript? › Yes
# ✔ Would you like to use ESLint? › Yes
# ✔ Would you like to use Tailwind CSS? › Yes
# ✔ Would you like your code inside a `src/` directory? › No
# ✔ Would you like to use App Router? › Yes
# ✔ Would you like to use Turbopack for `next dev`? › Yes
# ✔ Would you like to customize the import alias? › @/*
```

### Verify Installation

```bash
cd my-app
npm run dev
# Visit http://localhost:3000
# You should see the Next.js welcome page
```

## Additional Resources

- Official Docs: https://nextjs.org/docs
- App Router: https://nextjs.org/docs/app
- TypeScript: https://nextjs.org/docs/app/guides/typescript
- Tailwind CSS: https://tailwindcss.com/docs/guides/nextjs
- Deployment: https://nextjs.org/docs/app/guides/deploying

## Success Criteria

✅ Next.js 16+ project created with App Router
✅ TypeScript configured and working
✅ Tailwind CSS integrated with proper config
✅ Development server runs on `http://localhost:3000`
✅ Project structure follows Next.js conventions
✅ Ready for development with hot reload enabled
