---
name: shadcn
description: Setup and use Shadcn UI components in Next.js. Installs Shadcn CLI, adds pre-built components (Button, Card, Dialog, Form), and configures themes. Use when adding UI components to Next.js projects.
---

# Shadcn UI Setup and Usage

This skill helps you set up and use Shadcn UI components in Next.js projects with TypeScript and App Router.

## Overview

Shadcn UI is a collection of beautifully designed, accessible UI components built with TypeScript, Tailwind CSS, and Radix UI. Components are copied into your project, giving you full control and customization.

## Prerequisites

- Next.js project with App Router
- TypeScript enabled
- Tailwind CSS configured

## Installation

### Initialize Shadcn UI

Run the initialization command to set up Shadcn UI in your project:

```bash
pnpm dlx shadcn@latest init
```

This command will:
- Detect your framework (Next.js)
- Create `components.json` configuration file
- Install dependencies
- Configure the `cn` utility function
- Set up CSS variables for theming

### Configuration File

The `components.json` file controls how components are added to your project:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

**Key Configuration Options:**
- `style`: Choose "default" or "new-york" design style
- `rsc`: Set to `true` for React Server Components (App Router)
- `tsx`: Use TypeScript
- `baseColor`: Choose from "slate", "gray", "zinc", "neutral", "stone"
- `cssVariables`: Use CSS variables for theming (recommended)
- `iconLibrary`: Use "lucide" for icons

## Adding Components

### Add Individual Components

Use the CLI to add specific components to your project:

```bash
# Add Button component
pnpm dlx shadcn@latest add button

# Add Card component
pnpm dlx shadcn@latest add card

# Add Dialog component
pnpm dlx shadcn@latest add dialog

# Add Form components
pnpm dlx shadcn@latest add form

# Add Input component
pnpm dlx shadcn@latest add input

# Add Label component
pnpm dlx shadcn@latest add label
```

### Add Multiple Components at Once

```bash
pnpm dlx shadcn@latest add button card dialog form input label
```

### Initialize with Components

Create a new project with specific components:

```bash
pnpm dlx shadcn init button card dialog
```

## Theme Configuration

### Global CSS Setup

Configure theme colors using CSS variables in `app/globals.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 0 0% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 0 0% 3.9%;
    --primary: 0 0% 9%;
    --primary-foreground: 0 0% 98%;
    --secondary: 0 0% 96.1%;
    --secondary-foreground: 0 0% 9%;
    --muted: 0 0% 96.1%;
    --muted-foreground: 0 0% 45.1%;
    --accent: 0 0% 96.1%;
    --accent-foreground: 0 0% 9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 89.8%;
    --input: 0 0% 89.8%;
    --ring: 0 0% 3.9%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 0 0% 3.9%;
    --foreground: 0 0% 98%;
    --card: 0 0% 3.9%;
    --card-foreground: 0 0% 98%;
    --popover: 0 0% 3.9%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 0 0% 9%;
    --secondary: 0 0% 14.9%;
    --secondary-foreground: 0 0% 98%;
    --muted: 0 0% 14.9%;
    --muted-foreground: 0 0% 63.9%;
    --accent: 0 0% 14.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 14.9%;
    --input: 0 0% 14.9%;
    --ring: 0 0% 83.1%;
  }
}
```

### Dark Mode Support

Install and configure `next-themes` for dark mode:

```bash
pnpm add next-themes
```

Create a theme provider component `components/theme-provider.tsx`:

```typescript
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"
import { type ThemeProviderProps } from "next-themes/dist/types"

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

Wrap your app in `app/layout.tsx`:

```typescript
import { ThemeProvider } from "@/components/theme-provider"

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
```

Create a mode toggle component `components/mode-toggle.tsx`:

```typescript
"use client"

import * as React from "react"
import { Moon, Sun } from "lucide-react"
import { useTheme } from "next-themes"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function ModeToggle() {
  const { setTheme } = useTheme()

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme("light")}>
          Light
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("dark")}>
          Dark
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("system")}>
          System
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

## Component Usage Examples

### Button Component

```typescript
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="destructive">Delete</Button>
      <Button variant="ghost">Ghost</Button>
      <Button variant="link">Link</Button>
    </div>
  )
}
```

### Card Component with Form

```typescript
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export function LoginCard() {
  return (
    <Card className="w-[350px]">
      <CardHeader>
        <CardTitle>Login to your account</CardTitle>
        <CardDescription>
          Enter your email below to login to your account
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form>
          <div className="grid w-full items-center gap-4">
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="email">Email</Label>
              <Input id="email" type="email" placeholder="Email" />
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="password">Password</Label>
              <Input id="password" type="password" placeholder="Password" />
            </div>
          </div>
        </form>
      </CardContent>
      <CardFooter className="flex justify-between">
        <Button variant="outline">Cancel</Button>
        <Button>Login</Button>
      </CardFooter>
    </Card>
  )
}
```

### Dialog Component

```typescript
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"

export function DialogDemo() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline">Open Dialog</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Are you sure?</DialogTitle>
          <DialogDescription>
            This action cannot be undone. This will permanently delete your account.
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  )
}
```

## Best Practices

1. **Component Organization**: Keep Shadcn components in `components/ui/` directory
2. **Customization**: Modify copied components directly - they're yours to customize
3. **Theming**: Use CSS variables for consistent theming across components
4. **Accessibility**: Components are built with accessibility in mind using Radix UI primitives
5. **Type Safety**: All components are fully typed with TypeScript
6. **Server Components**: Most components work as Server Components; use `"use client"` only when needed (forms, interactive elements)

## Common Workflows

### Adding a New Feature with UI

1. Identify required components (e.g., form with input, button, card)
2. Add components: `pnpm dlx shadcn@latest add card input button label`
3. Import and compose components in your page/component
4. Customize styling using Tailwind classes
5. Add interactivity with client-side logic if needed

### Customizing a Component

1. Locate component in `components/ui/`
2. Modify directly - add variants, change styles, extend functionality
3. Component changes are isolated to your project
4. Update types if adding new props

## Troubleshooting

**Issue**: Components not found after adding
- Solution: Check `components.json` aliases match your import paths
- Verify components were added to correct directory

**Issue**: Styles not applying
- Solution: Ensure Tailwind CSS is properly configured
- Check `globals.css` has CSS variables defined
- Verify Tailwind config includes component paths

**Issue**: Dark mode not working
- Solution: Ensure `next-themes` is installed
- Verify ThemeProvider wraps your app in layout
- Check `suppressHydrationWarning` on `<html>` tag

## Resources

- Official Documentation: https://ui.shadcn.com
- Component Gallery: https://ui.shadcn.com/docs/components
- Themes: https://ui.shadcn.com/themes
- Examples: https://ui.shadcn.com/examples

## Included Templates

This skill now includes comprehensive templates for common UI patterns organized in the templates/ directory:

- **Dashboard Layout Template**: Complete dashboard with sidebar navigation, header, and responsive design (`templates/dashboard-layout-template.tsx`)
- **Data Table Template**: Feature-rich table with sorting, filtering, pagination, and row selection (`templates/data-table-template.tsx`)
- **Dialog Template**: Confirmation dialogs and form dialogs with loading states (`templates/dialog-template.tsx`)
- **Login Form Template**: Complete authentication form with validation using react-hook-form and zod (`templates/login-form-template.tsx`)

## Included Examples

Practical, production-ready examples of Shadcn UI components organized in the examples/ directory:

- **Navigation Examples**: Responsive navbar with dropdown menu (`examples/navigation-examples.tsx`)
- **Form Examples**: Contact form with validation (`examples/form-examples.tsx`)
- **Data Display Examples**: Stats cards and progress bars (`examples/data-display-examples.tsx`)
- **Interactive Examples**: Accordions and tabs (`examples/interactive-examples.tsx`)
- **Modal Examples**: AlertDialog and Combobox (`examples/modal-examples.tsx`)
- **Card Examples**: Feature cards with different pricing tiers (`examples/card-examples.tsx`)
- **Utility Examples**: Toast notifications and hover cards (`examples/utility-examples.tsx`)
- **Complete Page Examples**: Dashboard page with multiple components (`examples/dashboard-page-example.tsx`)

## Reference Documentation

Complete API reference for all components with props, variants, and usage organized in the reference/ directory:

- **Overview**: Core concepts, installation, configuration, and utility functions (`reference/reference-overview.md`)
- **Navigation Components**: Accordion, NavigationMenu, Tabs, Menubar (`reference/navigation-components.md`)
- **Form Components**: Form, Input, Textarea, Label, Select, RadioGroup, Checkbox, Switch (`reference/form-components.md`)
- **Interactive Components**: Button, Dialog, AlertDialog, DropdownMenu, ContextMenu, Combobox, Command, Popover, Tooltip, Hover Card, Slider, Toggle, Collapsible, Sheet, Drawer, Toast (`reference/interactive-components.md`)
- **Data Display Components**: Card, Table, Progress, Badge, Alert, Calendar, Avatar, Separator, Skeleton, AspectRatio, Pagination (`reference/data-display-components.md`)
- **Common Patterns**: Best practices, theming, accessibility, responsive design, and troubleshooting (`reference/common-patterns.md`)
