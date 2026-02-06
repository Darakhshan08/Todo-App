# Better Auth Examples

Comprehensive examples for implementing Better Auth in Next.js applications.

## Table of Contents

- [Basic Setup](#basic-setup)
- [Authentication Forms](#authentication-forms)
- [Protected Routes](#protected-routes)
- [Dashboard Examples](#dashboard-examples)
- [API Route Examples](#api-route-examples)
- [Advanced Patterns](#advanced-patterns)
- [Full Application Example](#full-application-example)

## Basic Setup

### Minimal Setup

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
});
```

```typescript
// lib/auth-client.ts
import { createAuthClient } from "better-auth/react";

export const authClient = createAuthClient();
```

```typescript
// app/api/auth/[...all]/route.ts
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { POST, GET } = toNextJsHandler(auth);
```

### Complete Setup with Multiple Providers

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
    requireEmailVerification: false,
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
  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
    updateAge: 60 * 60 * 24, // 1 day
  },
  trustedOrigins: ["http://localhost:3000"],
});
```

## Authentication Forms

### Sign Up Form with Validation

```typescript
// components/auth/signup-form.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export function SignUpForm() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData(e.currentTarget);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;
    const name = formData.get("name") as string;

    // Validation
    if (!email || !password || !name) {
      setError("All fields are required");
      setLoading(false);
      return;
    }

    if (password.length < 8) {
      setError("Password must be at least 8 characters");
      setLoading(false);
      return;
    }

    const { data, error } = await authClient.signUp.email(
      {
        email,
        password,
        name,
        callbackURL: "/dashboard",
      },
      {
        onRequest: () => {
          console.log("Signing up...");
        },
        onSuccess: () => {
          router.push("/dashboard");
        },
        onError: (ctx) => {
          setError(ctx.error.message);
          setLoading(false);
        },
      }
    );

    if (error) {
      setError(error.message);
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium">
          Name
        </label>
        <input
          id="name"
          name="name"
          type="text"
          required
          className="mt-1 block w-full rounded-md border px-3 py-2"
          placeholder="John Doe"
        />
      </div>

      <div>
        <label htmlFor="email" className="block text-sm font-medium">
          Email
        </label>
        <input
          id="email"
          name="email"
          type="email"
          required
          className="mt-1 block w-full rounded-md border px-3 py-2"
          placeholder="john@example.com"
        />
      </div>

      <div>
        <label htmlFor="password" className="block text-sm font-medium">
          Password
        </label>
        <input
          id="password"
          name="password"
          type="password"
          required
          minLength={8}
          className="mt-1 block w-full rounded-md border px-3 py-2"
          placeholder="••••••••"
        />
      </div>

      {error && (
        <div className="rounded-md bg-red-50 p-3 text-sm text-red-800">
          {error}
        </div>
      )}

      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Signing up..." : "Sign Up"}
      </button>
    </form>
  );
}
```

### Sign In Form with Remember Me

```typescript
// components/auth/signin-form.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";

export function SignInForm() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData(e.currentTarget);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;
    const rememberMe = formData.get("rememberMe") === "on";

    const { data, error } = await authClient.signIn.email({
      email,
      password,
      rememberMe,
      callbackURL: "/dashboard",
    });

    if (error) {
      setError(error.message);
      setLoading(false);
    } else {
      router.push("/dashboard");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="email" className="block text-sm font-medium">
          Email
        </label>
        <input
          id="email"
          name="email"
          type="email"
          required
          className="mt-1 block w-full rounded-md border px-3 py-2"
          placeholder="john@example.com"
        />
      </div>

      <div>
        <label htmlFor="password" className="block text-sm font-medium">
          Password
        </label>
        <input
          id="password"
          name="password"
          type="password"
          required
          className="mt-1 block w-full rounded-md border px-3 py-2"
          placeholder="••••••••"
        />
      </div>

      <div className="flex items-center justify-between">
        <label className="flex items-center">
          <input
            type="checkbox"
            name="rememberMe"
            className="rounded border-gray-300"
          />
          <span className="ml-2 text-sm">Remember me</span>
        </label>
        <Link
          href="/forgot-password"
          className="text-sm text-blue-600 hover:underline"
        >
          Forgot password?
        </Link>
      </div>

      {error && (
        <div className="rounded-md bg-red-50 p-3 text-sm text-red-800">
          {error}
        </div>
      )}

      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Signing in..." : "Sign In"}
      </button>

      <div className="text-center text-sm">
        Don't have an account?{" "}
        <Link href="/sign-up" className="text-blue-600 hover:underline">
          Sign up
        </Link>
      </div>
    </form>
  );
}
```

### Social Authentication Component

```typescript
// components/auth/social-auth.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useState } from "react";

export function SocialAuth() {
  const [loading, setLoading] = useState<string | null>(null);

  const handleSocialSignIn = async (provider: "github" | "google") => {
    setLoading(provider);
    await authClient.signIn.social({
      provider,
      callbackURL: "/dashboard",
      errorCallbackURL: "/error",
      newUserCallbackURL: "/welcome",
    });
  };

  return (
    <div className="space-y-3">
      <div className="relative">
        <div className="absolute inset-0 flex items-center">
          <div className="w-full border-t" />
        </div>
        <div className="relative flex justify-center text-sm">
          <span className="bg-white px-2 text-gray-500">
            Or continue with
          </span>
        </div>
      </div>

      <button
        onClick={() => handleSocialSignIn("github")}
        disabled={loading !== null}
        className="flex w-full items-center justify-center gap-2 rounded-md border bg-white px-4 py-2 hover:bg-gray-50 disabled:opacity-50"
      >
        <svg className="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
        </svg>
        {loading === "github" ? "Connecting..." : "GitHub"}
      </button>

      <button
        onClick={() => handleSocialSignIn("google")}
        disabled={loading !== null}
        className="flex w-full items-center justify-center gap-2 rounded-md border bg-white px-4 py-2 hover:bg-gray-50 disabled:opacity-50"
      >
        <svg className="h-5 w-5" viewBox="0 0 24 24">
          <path
            fill="#4285F4"
            d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
          />
          <path
            fill="#34A853"
            d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
          />
          <path
            fill="#FBBC05"
            d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
          />
          <path
            fill="#EA4335"
            d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
          />
        </svg>
        {loading === "google" ? "Connecting..." : "Google"}
      </button>
    </div>
  );
}
```

## Protected Routes

### Client-Side Protected Route

```typescript
// components/auth/protected-route.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { redirect } from "next/navigation";
import { ReactNode } from "react";

export function ProtectedRoute({
  children,
  redirectTo = "/sign-in",
}: {
  children: ReactNode;
  redirectTo?: string;
}) {
  const { data: session, isPending, error } = authClient.useSession();

  if (isPending) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-blue-600 border-t-transparent" />
      </div>
    );
  }

  if (!session || error) {
    redirect(redirectTo);
  }

  return <>{children}</>;
}
```

### Server-Side Protected Page

```typescript
// app/dashboard/page.tsx
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { redirect } from "next/navigation";

export default async function DashboardPage() {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    redirect("/sign-in");
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
    </div>
  );
}
```

### Role-Based Protected Route

```typescript
// components/auth/role-protected-route.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { redirect } from "next/navigation";
import { ReactNode } from "react";

type UserRole = "admin" | "user" | "moderator";

export function RoleProtectedRoute({
  children,
  allowedRoles,
  redirectTo = "/unauthorized",
}: {
  children: ReactNode;
  allowedRoles: UserRole[];
  redirectTo?: string;
}) {
  const { data: session, isPending } = authClient.useSession();

  if (isPending) {
    return <div>Loading...</div>;
  }

  if (!session) {
    redirect("/sign-in");
  }

  // Assume user has a role property
  const userRole = (session.user as any).role as UserRole;

  if (!allowedRoles.includes(userRole)) {
    redirect(redirectTo);
  }

  return <>{children}</>;
}

// Usage:
// <RoleProtectedRoute allowedRoles={["admin"]}>
//   <AdminPanel />
// </RoleProtectedRoute>
```

## Dashboard Examples

### User Profile Display

```typescript
// components/dashboard/user-profile.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import Image from "next/image";

export function UserProfile() {
  const { data: session, isPending } = authClient.useSession();

  if (isPending) {
    return <div>Loading profile...</div>;
  }

  if (!session) {
    return null;
  }

  const { user } = session;

  return (
    <div className="rounded-lg border bg-white p-6 shadow-sm">
      <div className="flex items-center gap-4">
        {user.image ? (
          <Image
            src={user.image}
            alt={user.name}
            width={64}
            height={64}
            className="rounded-full"
          />
        ) : (
          <div className="flex h-16 w-16 items-center justify-center rounded-full bg-blue-600 text-2xl font-bold text-white">
            {user.name.charAt(0).toUpperCase()}
          </div>
        )}
        <div>
          <h2 className="text-xl font-bold">{user.name}</h2>
          <p className="text-gray-600">{user.email}</p>
          {user.emailVerified && (
            <span className="mt-1 inline-flex items-center gap-1 rounded-full bg-green-100 px-2 py-1 text-xs text-green-800">
              ✓ Verified
            </span>
          )}
        </div>
      </div>
    </div>
  );
}
```

### Sign Out Button Component

```typescript
// components/dashboard/signout-button.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useRouter } from "next/navigation";
import { useState } from "react";

export function SignOutButton() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const handleSignOut = async () => {
    setLoading(true);
    await authClient.signOut();
    router.push("/");
    router.refresh();
  };

  return (
    <button
      onClick={handleSignOut}
      disabled={loading}
      className="rounded-md bg-red-600 px-4 py-2 text-white hover:bg-red-700 disabled:opacity-50"
    >
      {loading ? "Signing out..." : "Sign Out"}
    </button>
  );
}
```

### Session Info Display

```typescript
// components/dashboard/session-info.tsx
"use client";

import { authClient } from "@/lib/auth-client";

export function SessionInfo() {
  const { data: session, refetch } = authClient.useSession();

  if (!session) return null;

  const expiresAt = new Date(session.session.expiresAt);
  const now = new Date();
  const daysUntilExpiry = Math.ceil(
    (expiresAt.getTime() - now.getTime()) / (1000 * 60 * 60 * 24)
  );

  return (
    <div className="rounded-lg border bg-white p-4">
      <h3 className="font-semibold">Session Information</h3>
      <div className="mt-2 space-y-1 text-sm">
        <p>Session ID: {session.session.id}</p>
        <p>Expires: {expiresAt.toLocaleDateString()}</p>
        <p>Days until expiry: {daysUntilExpiry}</p>
        {session.session.ipAddress && (
          <p>IP: {session.session.ipAddress}</p>
        )}
      </div>
      <button
        onClick={() => refetch()}
        className="mt-3 text-sm text-blue-600 hover:underline"
      >
        Refresh session
      </button>
    </div>
  );
}
```

## API Route Examples

### Protected API Route

```typescript
// app/api/user/profile/route.ts
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { NextResponse } from "next/server";

export async function GET() {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    return NextResponse.json(
      { error: "Unauthorized" },
      { status: 401 }
    );
  }

  return NextResponse.json({
    user: session.user,
  });
}

export async function PATCH(request: Request) {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    return NextResponse.json(
      { error: "Unauthorized" },
      { status: 401 }
    );
  }

  const body = await request.json();

  // Update user profile logic here

  return NextResponse.json({
    success: true,
    user: session.user,
  });
}
```

### Custom Authentication Endpoint

```typescript
// app/api/auth/custom-signin/route.ts
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { email, password, customField } = await request.json();

  // Custom validation logic
  if (!customField) {
    return NextResponse.json(
      { error: "Custom field is required" },
      { status: 400 }
    );
  }

  // Use Better Auth's sign in
  const result = await auth.api.signInEmail({
    body: { email, password },
    headers: await headers(),
  });

  if (!result) {
    return NextResponse.json(
      { error: "Invalid credentials" },
      { status: 401 }
    );
  }

  // Custom logic after sign in
  // e.g., log event, update analytics, etc.

  return NextResponse.json({
    success: true,
    user: result.user,
  });
}
```

## Advanced Patterns

### Multi-Step Authentication Flow

```typescript
// components/auth/multi-step-auth.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useState } from "react";

type Step = "email" | "verification" | "details" | "complete";

export function MultiStepAuth() {
  const [step, setStep] = useState<Step>("email");
  const [email, setEmail] = useState("");
  const [verificationCode, setVerificationCode] = useState("");

  const handleEmailSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // Send verification code
    // await sendVerificationCode(email);
    setStep("verification");
  };

  const handleVerification = async (e: React.FormEvent) => {
    e.preventDefault();
    // Verify code
    // const isValid = await verifyCode(email, verificationCode);
    // if (isValid) setStep("details");
  };

  const handleDetailsSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);

    await authClient.signUp.email({
      email,
      password: formData.get("password") as string,
      name: formData.get("name") as string,
    });

    setStep("complete");
  };

  return (
    <div className="max-w-md mx-auto">
      {step === "email" && (
        <form onSubmit={handleEmailSubmit}>
          <h2>Step 1: Enter Email</h2>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="email@example.com"
            required
          />
          <button type="submit">Continue</button>
        </form>
      )}

      {step === "verification" && (
        <form onSubmit={handleVerification}>
          <h2>Step 2: Verify Email</h2>
          <input
            type="text"
            value={verificationCode}
            onChange={(e) => setVerificationCode(e.target.value)}
            placeholder="Enter code"
            required
          />
          <button type="submit">Verify</button>
        </form>
      )}

      {step === "details" && (
        <form onSubmit={handleDetailsSubmit}>
          <h2>Step 3: Complete Profile</h2>
          <input name="name" placeholder="Full Name" required />
          <input name="password" type="password" placeholder="Password" required />
          <button type="submit">Complete</button>
        </form>
      )}

      {step === "complete" && (
        <div>
          <h2>Welcome! Your account is ready.</h2>
        </div>
      )}
    </div>
  );
}
```

### Session Refresh on Focus

```typescript
// components/auth/session-refresh-provider.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useEffect } from "react";

export function SessionRefreshProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const { refetch } = authClient.useSession();

  useEffect(() => {
    const handleFocus = () => {
      // Refresh session when window regains focus
      refetch();
    };

    window.addEventListener("focus", handleFocus);
    return () => window.removeEventListener("focus", handleFocus);
  }, [refetch]);

  return <>{children}</>;
}
```

## Full Application Example

See `templates/auth-pages/` directory for complete authentication page examples including:
- Sign in page
- Sign up page
- Dashboard layout
- Profile page
- Settings page
