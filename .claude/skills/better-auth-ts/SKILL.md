---
name: better-auth-ts
description: Configure Better Auth for Next.js frontend. Sets up Better Auth client, JWT token handling, session management, and auth UI components. Use when the user wants to add authentication to a Next.js project, set up Better Auth, or configure auth providers.
---

# Better Auth Configuration for Next.js

Configures Better Auth authentication and authorization framework for Next.js applications with TypeScript. Supports email/password, social providers, JWT tokens, session management, and pre-built UI components.

## Prerequisites

- Next.js 13+ with App Router
- TypeScript configured
- Database (PostgreSQL, MySQL, or SQLite)
- Node.js 18.17 or later

## Instructions

### Step 1: Install Better Auth

Install the Better Auth core library and optional UI components:

```bash
# Core library (required)
npm install better-auth

# Optional: UI components with shadcn/ui
npm install @daveyplate/better-auth-ui@latest
```

**With other package managers**:
```bash
# pnpm
pnpm add better-auth
pnpm add @daveyplate/better-auth-ui@latest

# yarn
yarn add better-auth
yarn add @daveyplate/better-auth-ui@latest

# bun
bun add better-auth
bun add @daveyplate/better-auth-ui@latest
```

### Step 2: Configure Environment Variables

Create `.env` file in project root with required configuration:

```bash
# Required: Secret key for encryption and hashing (min 32 characters)
BETTER_AUTH_SECRET=your-secret-key-here

# Required: Base URL of your application
BETTER_AUTH_URL=http://localhost:3000

# Required: Database connection string
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# Optional: Social provider credentials
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

**Generate secure secret**:
```bash
openssl rand -base64 32
```

### Step 3: Create Server-Side Auth Instance

Create auth configuration file at `lib/auth.ts` (or `app/lib/auth.ts`, `src/lib/auth.ts`):

```typescript
import { betterAuth } from "better-auth";
import { prismaAdapter } from "better-auth/adapters/prisma";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: "postgresql", // or "mysql" or "sqlite"
  }),
  emailAndPassword: {
    enabled: true,
  },
  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID as string,
      clientSecret: process.env.GITHUB_CLIENT_SECRET as string,
    },
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID as string,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET as string,
    },
  },
});
```

**Alternative: Using Drizzle ORM**:
```typescript
import { betterAuth } from "better-auth";
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { db } from "@/db";

export const auth = betterAuth({
  database: drizzleAdapter(db, {
    provider: "pg", // or "mysql" or "sqlite"
  }),
  emailAndPassword: {
    enabled: true,
  },
});
```

### Step 4: Create API Route Handler

Create catch-all route at `app/api/auth/[...all]/route.ts`:

```typescript
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { POST, GET } = toNextJsHandler(auth);
```

This creates all Better Auth API endpoints:
- `/api/auth/sign-in/email`
- `/api/auth/sign-up/email`
- `/api/auth/sign-in/social`
- `/api/auth/sign-out`
- `/api/auth/session`

### Step 5: Create Client-Side Auth Client

Create client instance at `lib/auth-client.ts`:

```typescript
import { createAuthClient } from "better-auth/react";

export const authClient = createAuthClient({
  // Optional: custom configuration
  baseURL: process.env.NEXT_PUBLIC_APP_URL,
});

// Export TypeScript type for session
export type Session = typeof authClient.$Infer.Session;
```

### Step 6: Access Session Data (useSession Hook)

Use the `useSession` hook in React components to access authentication state:

```typescript
"use client";

import { authClient } from "@/lib/auth-client";
import { redirect } from "next/navigation";

export default function DashboardPage() {
  const {
    data: session,
    isPending,
    error,
    refetch
  } = authClient.useSession();

  if (isPending) {
    return <div>Loading...</div>;
  }

  if (!session || error) {
    redirect("/sign-in");
  }

  return (
    <div>
      <h1>Welcome {session.user.name}</h1>
      <p>Email: {session.user.email}</p>
    </div>
  );
}
```

### Step 7: Implement Authentication Methods

#### Sign Up with Email

```typescript
"use client";

import { authClient } from "@/lib/auth-client";

export function SignUpForm() {
  const handleSignUp = async (formData: FormData) => {
    const { data, error } = await authClient.signUp.email(
      {
        email: formData.get("email") as string,
        password: formData.get("password") as string,
        name: formData.get("name") as string,
        image: formData.get("image") as string, // optional
        callbackURL: "/dashboard", // optional
      },
      {
        onRequest: () => {
          console.log("Sign up request started");
        },
        onSuccess: (ctx) => {
          console.log("Sign up successful", ctx);
        },
        onError: (ctx) => {
          alert(ctx.error.message);
        },
      }
    );
  };

  return (
    <form action={handleSignUp}>
      <input name="name" placeholder="Name" required />
      <input name="email" type="email" placeholder="Email" required />
      <input name="password" type="password" placeholder="Password" required />
      <button type="submit">Sign Up</button>
    </form>
  );
}
```

#### Sign In with Email

```typescript
"use client";

import { authClient } from "@/lib/auth-client";

export function SignInForm() {
  const handleSignIn = async (formData: FormData) => {
    const { data, error } = await authClient.signIn.email({
      email: formData.get("email") as string,
      password: formData.get("password") as string,
      rememberMe: true, // optional
      callbackURL: "/dashboard", // optional
    });

    if (error) {
      alert(error.message);
    }
  };

  return (
    <form action={handleSignIn}>
      <input name="email" type="email" placeholder="Email" required />
      <input name="password" type="password" placeholder="Password" required />
      <button type="submit">Sign In</button>
    </form>
  );
}
```

#### Sign In with Social Provider

```typescript
"use client";

import { authClient } from "@/lib/auth-client";

export function SocialSignIn() {
  const handleGitHubSignIn = async () => {
    await authClient.signIn.social({
      provider: "github",
      callbackURL: "/dashboard",
      errorCallbackURL: "/error",
      newUserCallbackURL: "/welcome",
    });
  };

  const handleGoogleSignIn = async () => {
    await authClient.signIn.social({
      provider: "google",
      callbackURL: "/dashboard",
    });
  };

  return (
    <div>
      <button onClick={handleGitHubSignIn}>
        Continue with GitHub
      </button>
      <button onClick={handleGoogleSignIn}>
        Continue with Google
      </button>
    </div>
  );
}
```

#### Sign Out

```typescript
"use client";

import { authClient } from "@/lib/auth-client";

export function SignOutButton() {
  const handleSignOut = async () => {
    await authClient.signOut();
  };

  return <button onClick={handleSignOut}>Sign Out</button>;
}
```

### Step 8: Server-Side Authentication

For server-side authentication in API routes or Server Components:

```typescript
import { auth } from "@/lib/auth";
import { headers } from "next/headers";

// Sign out server-side
const { success } = await auth.api.signOut({
  headers: await headers(),
});

// Sign in server-side
const data = await auth.api.signInEmail({
  body: {
    email: "user@example.com",
    password: "password123",
  },
  headers: await headers(),
});
```

### Step 9: Protected Routes Pattern

Create reusable protected route wrapper:

```typescript
"use client";

import { authClient } from "@/lib/auth-client";
import { redirect } from "next/navigation";
import { ReactNode } from "react";

export function ProtectedRoute({ children }: { children: ReactNode }) {
  const { data: session, isPending } = authClient.useSession();

  if (isPending) {
    return <div>Loading...</div>;
  }

  if (!session) {
    redirect("/sign-in");
  }

  return <>{children}</>;
}
```

Use in pages:
```typescript
export default function DashboardPage() {
  return (
    <ProtectedRoute>
      <h1>Protected Dashboard</h1>
    </ProtectedRoute>
  );
}
```

### Step 10: Setup Better Auth UI Components (Optional)

Install UI components and configure provider:

#### Create Provider Component

Create `components/providers.tsx`:

```typescript
"use client";

import { AuthUIProvider } from "@daveyplate/better-auth-ui";
import { authClient } from "@/lib/auth-client";
import { useRouter } from "next/navigation";
import Link from "next/link";

export function Providers({ children }: { children: React.ReactNode }) {
  const router = useRouter();

  return (
    <AuthUIProvider
      authClient={authClient}
      navigate={router.push}
      replace={router.replace}
      onSessionChange={() => router.refresh()}
      Link={Link}
      social={{
        providers: ["github", "google"],
      }}
    >
      {children}
    </AuthUIProvider>
  );
}
```

#### Wrap App in Provider

Update `app/layout.tsx`:

```typescript
import { Providers } from "@/components/providers";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
```

#### Create Dynamic Auth Route

Create `app/auth/[pathname]/page.tsx`:

```typescript
import { AuthView } from "@daveyplate/better-auth-ui";
import { authViewPaths } from "@daveyplate/better-auth-ui";

export function generateStaticParams() {
  return Object.values({
    ...authViewPaths,
    SIGN_IN: "login",
    SIGN_OUT: "logout",
    SIGN_UP: "register",
    FORGOT_PASSWORD: "forgot",
    RESET_PASSWORD: "reset",
  }).map((pathname) => ({ pathname }));
}

export default async function AuthPage({
  params,
}: {
  params: Promise<{ pathname: string }>;
}) {
  const { pathname } = await params;

  return (
    <div className="flex items-center justify-center min-h-screen">
      <AuthView pathname={pathname} />
    </div>
  );
}
```

Now you have pre-built auth pages at:
- `/auth/login`
- `/auth/register`
- `/auth/logout`
- `/auth/forgot`
- `/auth/reset`

## Database Setup

### Prisma Schema Example

```prisma
model User {
  id            String    @id @default(cuid())
  name          String
  email         String    @unique
  emailVerified DateTime?
  image         String?
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  sessions      Session[]
  accounts      Account[]
}

model Session {
  id           String   @id @default(cuid())
  userId       String
  expiresAt    DateTime
  token        String   @unique
  ipAddress    String?
  userAgent    String?
  user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  createdAt    DateTime @default(now())
  updatedAt    DateTime @updatedAt
}

model Account {
  id                String  @id @default(cuid())
  userId            String
  accountId         String
  providerId        String
  accessToken       String?
  refreshToken      String?
  idToken           String?
  expiresAt         DateTime?
  password          String?
  user              User    @relation(fields: [userId], references: [id], onDelete: Cascade)
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt

  @@unique([providerId, accountId])
}
```

Run migrations:
```bash
npx prisma migrate dev --name init
npx prisma generate
```

## Advanced Configuration

### JWT Plugin

Add JWT support for token-based authentication:

```typescript
import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
  plugins: [
    jwt({
      jwks: {
        keyPairConfig: {
          alg: "ES256",
        },
      },
    }),
  ],
});
```

### Multi-Session Support

Enable users to have multiple active sessions:

```typescript
<AuthUIProvider
  authClient={authClient}
  multiSession
  // ... other props
>
  {children}
</AuthUIProvider>
```

### Custom Base URL

Configure custom base URL for API routes:

```typescript
export const authClient = createAuthClient({
  baseURL: "https://api.example.com",
});
```

## Best Practices

1. **Always use environment variables** for secrets and API keys
2. **Generate strong secrets** using `openssl rand -base64 32`
3. **Use TypeScript** for type safety with session data
4. **Implement proper error handling** in all auth callbacks
5. **Protect sensitive routes** with session checks
6. **Use Server Components** for server-side session validation when possible
7. **Configure proper callback URLs** for production deployments
8. **Enable HTTPS** in production for secure authentication

## Troubleshooting

### Secret Key Not Set Error

```bash
Error: BETTER_AUTH_SECRET environment variable is required in production
```

**Solution**: Generate and set secret in `.env`:
```bash
openssl rand -base64 32
# Add to .env: BETTER_AUTH_SECRET=<generated-secret>
```

### Database Connection Errors

```bash
Error: Can't reach database server
```

**Solution**: Verify DATABASE_URL and ensure database is running:
```bash
# Test connection
npx prisma db push
```

### OAuth Provider Errors

```bash
Error: Invalid OAuth credentials
```

**Solution**:
1. Verify client ID and secret in `.env`
2. Check callback URL is registered with provider
3. Ensure provider is enabled in auth config

### Session Not Persisting

**Solution**: Ensure cookies are properly configured and HTTPS is used in production.

## Examples

### Complete Auth Setup

```typescript
// lib/auth.ts
import { betterAuth } from "better-auth";
import { prismaAdapter } from "better-auth/adapters/prisma";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: "postgresql",
  }),
  emailAndPassword: {
    enabled: true,
  },
  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID as string,
      clientSecret: process.env.GITHUB_CLIENT_SECRET as string,
    },
  },
});
```

```typescript
// lib/auth-client.ts
import { createAuthClient } from "better-auth/react";

export const authClient = createAuthClient();
export type Session = typeof authClient.$Infer.Session;
```

```typescript
// app/api/auth/[...all]/route.ts
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { POST, GET } = toNextJsHandler(auth);
```

### Protected Dashboard Example

```typescript
"use client";

import { authClient } from "@/lib/auth-client";
import { redirect } from "next/navigation";

export default function DashboardPage() {
  const { data: session, isPending } = authClient.useSession();

  if (isPending) return <div>Loading...</div>;
  if (!session) redirect("/sign-in");

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
      <button onClick={() => authClient.signOut()}>
        Sign Out
      </button>
    </div>
  );
}
```

## Additional Files

This skill includes additional reference files and templates:

- **[reference.md](reference.md)** - Comprehensive API reference with all configuration options, methods, and types
- **[examples.md](examples.md)** - Detailed code examples for common authentication patterns
- **[templates/](templates/)** - Ready-to-use templates:
  - `prisma-schema.prisma` - Complete Prisma database schema
  - `drizzle-schema.ts` - Complete Drizzle database schema
  - `.env.example` - Environment variables template
  - `sign-in-page.tsx` - Full sign-in page component
  - `sign-up-page.tsx` - Full sign-up page component
  - `dashboard-page.tsx` - Protected dashboard example

## Additional Resources

- Official Docs: https://www.better-auth.com
- Better Auth UI: https://better-auth-ui.com
- GitHub: https://github.com/better-auth/better-auth
- Examples: https://github.com/better-auth/better-auth/tree/main/examples

## Success Criteria

✅ Better Auth installed and configured
✅ Environment variables set with secure secret
✅ Server-side auth instance created with database adapter
✅ Client-side auth client configured
✅ API routes mounted at `/api/auth/[...all]`
✅ Email/password authentication enabled
✅ Social providers configured (optional)
✅ Session management with `useSession` hook working
✅ Sign in/sign out/sign up methods implemented
✅ Protected routes configured
✅ Better Auth UI components integrated (optional)
✅ Database schema migrated and ready
