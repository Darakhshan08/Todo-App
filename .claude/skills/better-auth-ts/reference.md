# Better Auth API Reference

Comprehensive API reference for Better Auth configuration, methods, and types.

## Table of Contents

- [Server Configuration](#server-configuration)
- [Client Configuration](#client-configuration)
- [Authentication Methods](#authentication-methods)
- [Session Management](#session-management)
- [Database Adapters](#database-adapters)
- [Environment Variables](#environment-variables)
- [TypeScript Types](#typescript-types)

## Server Configuration

### betterAuth() Options

```typescript
interface BetterAuthOptions {
  database: DatabaseAdapter;
  secret?: string;
  baseURL?: string;
  basePath?: string;
  emailAndPassword?: EmailPasswordConfig;
  socialProviders?: SocialProvidersConfig;
  trustedOrigins?: string[];
  plugins?: Plugin[];
  session?: SessionConfig;
}
```

#### database (required)

Database adapter configuration using Prisma or Drizzle:

```typescript
// Prisma
import { prismaAdapter } from "better-auth/adapters/prisma";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

database: prismaAdapter(prisma, {
  provider: "postgresql", // "mysql" | "sqlite"
})

// Drizzle
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { db } from "@/db";

database: drizzleAdapter(db, {
  provider: "pg", // "mysql" | "sqlite"
})
```

#### secret (required in production)

Encryption and signing key (min 32 characters):

```typescript
secret: process.env.BETTER_AUTH_SECRET
// or via environment variables:
// BETTER_AUTH_SECRET or AUTH_SECRET
```

Generate secure secret:
```bash
openssl rand -base64 32
```

#### baseURL (recommended)

Base URL of your application:

```typescript
baseURL: "https://example.com"
// or via environment variable:
// BETTER_AUTH_URL
```

#### basePath (optional)

Custom base path for auth routes (default: "/api/auth"):

```typescript
basePath: "/auth"
```

#### emailAndPassword (optional)

Email/password authentication configuration:

```typescript
emailAndPassword: {
  enabled: true,
  requireEmailVerification?: boolean,
  sendResetPasswordEmail?: (user, url) => Promise<void>,
  sendVerificationEmail?: (user, url) => Promise<void>,
  minPasswordLength?: number, // default: 8
  maxPasswordLength?: number, // default: 128
}
```

#### socialProviders (optional)

OAuth provider configuration:

```typescript
socialProviders: {
  github: {
    clientId: process.env.GITHUB_CLIENT_ID,
    clientSecret: process.env.GITHUB_CLIENT_SECRET,
    redirectURI?: string,
    scope?: string[],
  },
  google: {
    clientId: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    redirectURI?: string,
    scope?: string[],
  },
  facebook: {
    clientId: process.env.FACEBOOK_CLIENT_ID,
    clientSecret: process.env.FACEBOOK_CLIENT_SECRET,
  },
  apple: {
    clientId: process.env.APPLE_CLIENT_ID,
    clientSecret: process.env.APPLE_CLIENT_SECRET,
    teamId: process.env.APPLE_TEAM_ID,
    keyId: process.env.APPLE_KEY_ID,
    privateKey: process.env.APPLE_PRIVATE_KEY,
  },
}
```

#### trustedOrigins (optional)

Allowed CORS origins:

```typescript
trustedOrigins: [
  "https://example.com",
  "https://app.example.com",
]
```

#### plugins (optional)

Better Auth plugins:

```typescript
import { jwt } from "better-auth/plugins";

plugins: [
  jwt({
    jwks: {
      keyPairConfig: {
        alg: "ES256", // "RS256" | "EdDSA"
      },
    },
  }),
]
```

#### session (optional)

Session configuration:

```typescript
session: {
  expiresIn: 60 * 60 * 24 * 7, // 7 days in seconds
  updateAge: 60 * 60 * 24, // 1 day in seconds
  cookieCache?: {
    enabled: boolean,
    maxAge: number,
  },
}
```

## Client Configuration

### createAuthClient() Options

```typescript
interface AuthClientOptions {
  baseURL?: string;
  basePath?: string;
  credentials?: RequestCredentials;
  fetchOptions?: RequestInit;
}
```

#### baseURL (optional)

Custom API base URL:

```typescript
createAuthClient({
  baseURL: "https://api.example.com",
})
```

#### basePath (optional)

Custom base path (default: "/api/auth"):

```typescript
createAuthClient({
  basePath: "/auth",
})
```

#### credentials (optional)

Fetch credentials mode (default: "include"):

```typescript
createAuthClient({
  credentials: "include", // "omit" | "same-origin"
})
```

## Authentication Methods

### Sign Up

#### signUp.email()

```typescript
interface SignUpEmailParams {
  email: string;
  password: string;
  name: string;
  image?: string;
  callbackURL?: string;
}

interface SignUpEmailResponse {
  data: {
    user: User;
    session: Session;
  } | null;
  error: AuthError | null;
}

const result = await authClient.signUp.email(params, {
  onRequest?: (ctx) => void,
  onSuccess?: (ctx) => void,
  onError?: (ctx) => void,
});
```

**Parameters:**
- `email` (string, required) - User email address
- `password` (string, required) - Password (min 8 chars by default)
- `name` (string, required) - Display name
- `image` (string, optional) - Profile image URL
- `callbackURL` (string, optional) - Redirect URL after signup

**Response:**
- `data.user` - Created user object
- `data.session` - Session information
- `error` - Error object if signup failed

### Sign In

#### signIn.email()

```typescript
interface SignInEmailParams {
  email: string;
  password: string;
  rememberMe?: boolean;
  callbackURL?: string;
}

interface SignInEmailResponse {
  data: {
    user: User;
    session: Session;
  } | null;
  error: AuthError | null;
}

const result = await authClient.signIn.email(params);
```

**Parameters:**
- `email` (string, required) - User email
- `password` (string, required) - User password
- `rememberMe` (boolean, optional) - Persistent session (default: true)
- `callbackURL` (string, optional) - Redirect URL after signin

#### signIn.social()

```typescript
interface SignInSocialParams {
  provider: "github" | "google" | "facebook" | "apple";
  callbackURL?: string;
  errorCallbackURL?: string;
  newUserCallbackURL?: string;
  disableRedirect?: boolean;
}

await authClient.signIn.social({
  provider: "github",
  callbackURL: "/dashboard",
  errorCallbackURL: "/error",
  newUserCallbackURL: "/welcome",
  disableRedirect: false,
});
```

**Parameters:**
- `provider` (string, required) - OAuth provider name
- `callbackURL` (string, optional) - Success redirect URL
- `errorCallbackURL` (string, optional) - Error redirect URL
- `newUserCallbackURL` (string, optional) - New user redirect URL
- `disableRedirect` (boolean, optional) - Prevent auto redirect

### Sign Out

#### signOut()

```typescript
interface SignOutResponse {
  success: boolean;
  error: AuthError | null;
}

// Client-side
const result = await authClient.signOut();

// Server-side
const result = await auth.api.signOut({
  headers: await headers(),
});
```

**Response:**
- `success` (boolean) - Whether signout succeeded
- `error` - Error object if signout failed

## Session Management

### useSession Hook

```typescript
interface UseSessionReturn {
  data: Session | null;
  isPending: boolean;
  error: AuthError | null;
  refetch: () => Promise<void>;
}

const { data, isPending, error, refetch } = authClient.useSession();
```

**Returns:**
- `data` - Session object with user info
- `isPending` - Loading state (true while fetching)
- `error` - Error object if session fetch failed
- `refetch` - Function to manually refresh session

### Session Object

```typescript
interface Session {
  user: User;
  session: SessionData;
}

interface User {
  id: string;
  name: string;
  email: string;
  emailVerified: boolean;
  image?: string;
  createdAt: Date;
  updatedAt: Date;
}

interface SessionData {
  id: string;
  userId: string;
  expiresAt: Date;
  token: string;
  ipAddress?: string;
  userAgent?: string;
}
```

## Database Adapters

### Prisma Adapter

```typescript
import { prismaAdapter } from "better-auth/adapters/prisma";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

database: prismaAdapter(prisma, {
  provider: "postgresql", // "mysql" | "sqlite"
})
```

**Required Prisma Schema:**
See `templates/prisma-schema.prisma` for complete schema.

### Drizzle Adapter

```typescript
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { db } from "@/db";

database: drizzleAdapter(db, {
  provider: "pg", // "mysql" | "sqlite"
})
```

**Required Drizzle Schema:**
See `templates/drizzle-schema.ts` for complete schema.

## Environment Variables

### Required Variables

```bash
# Secret key for encryption (min 32 characters)
BETTER_AUTH_SECRET=your-secret-key-here

# Base URL of your application
BETTER_AUTH_URL=http://localhost:3000

# Database connection string
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

### OAuth Provider Variables

```bash
# GitHub OAuth
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Facebook OAuth
FACEBOOK_CLIENT_ID=your-facebook-client-id
FACEBOOK_CLIENT_SECRET=your-facebook-client-secret

# Apple OAuth
APPLE_CLIENT_ID=your-apple-client-id
APPLE_CLIENT_SECRET=your-apple-client-secret
APPLE_TEAM_ID=your-apple-team-id
APPLE_KEY_ID=your-apple-key-id
APPLE_PRIVATE_KEY=your-apple-private-key
```

## TypeScript Types

### Infer Session Type

```typescript
import { authClient } from "@/lib/auth-client";

// Infer session type from client
export type Session = typeof authClient.$Infer.Session;

// Use in components
const session: Session = {
  user: {
    id: "123",
    name: "John Doe",
    email: "john@example.com",
    emailVerified: true,
  },
  session: {
    id: "session-123",
    userId: "123",
    expiresAt: new Date(),
    token: "token-123",
  },
};
```

### Auth Error Type

```typescript
interface AuthError {
  message: string;
  status: number;
  code: string;
}
```

Common error codes:
- `INVALID_CREDENTIALS` - Wrong email/password
- `USER_NOT_FOUND` - User doesn't exist
- `EMAIL_ALREADY_EXISTS` - Email already registered
- `UNAUTHORIZED` - Not authenticated
- `FORBIDDEN` - Not authorized
- `SESSION_EXPIRED` - Session has expired

## API Routes Reference

Better Auth creates these routes automatically:

### Authentication Routes

- `POST /api/auth/sign-up/email` - Email/password signup
- `POST /api/auth/sign-in/email` - Email/password signin
- `POST /api/auth/sign-in/social` - Social provider signin
- `POST /api/auth/sign-out` - Sign out user
- `GET /api/auth/session` - Get current session
- `POST /api/auth/callback/:provider` - OAuth callback

### Email Routes (if email verification enabled)

- `POST /api/auth/send-verification-email` - Send verification email
- `POST /api/auth/verify-email` - Verify email address
- `POST /api/auth/send-reset-password-email` - Send password reset
- `POST /api/auth/reset-password` - Reset password

### OAuth Routes

- `GET /api/auth/oauth/:provider` - Initialize OAuth flow
- `GET /api/auth/oauth/:provider/callback` - OAuth callback handler

### JWT Routes (if JWT plugin enabled)

- `GET /api/auth/token` - Get JWT token
- `GET /api/auth/jwks` - Get JWKS (JSON Web Key Set)

## Best Practices

1. **Always use environment variables** for secrets and credentials
2. **Generate strong secrets** using `openssl rand -base64 32`
3. **Enable TypeScript** for type safety
4. **Implement error handling** in all auth callbacks
5. **Use Server Components** for server-side validation
6. **Configure proper callback URLs** for production
7. **Enable HTTPS** in production
8. **Set secure cookie options** in production
9. **Implement rate limiting** on auth endpoints
10. **Monitor failed login attempts** for security

## Security Considerations

### Secret Management

- Never commit secrets to version control
- Use `.env.local` for local development
- Use environment variables in production
- Rotate secrets regularly
- Use different secrets for different environments

### Session Security

- Use HTTPS in production
- Set secure cookie flags
- Implement session timeout
- Monitor active sessions
- Implement session revocation

### Password Security

- Enforce minimum password length (8+ chars)
- Consider password complexity requirements
- Implement rate limiting on login attempts
- Hash passwords with bcrypt (done by Better Auth)
- Never log or expose passwords

### OAuth Security

- Validate OAuth state parameter
- Use secure redirect URIs
- Validate OAuth tokens
- Implement CSRF protection
- Monitor OAuth events

## Migration Guides

### From NextAuth.js

Key differences:
- `signIn()` → `authClient.signIn.email()` or `authClient.signIn.social()`
- `signOut()` → `authClient.signOut()`
- `useSession()` → `authClient.useSession()`
- `getServerSession()` → `auth.api.getSession()`

### From Auth0

Key differences:
- Use Better Auth's built-in providers instead of Auth0 Universal Login
- Migrate user data from Auth0 to your database
- Update OAuth callback URLs
- Configure social providers directly in Better Auth

## Troubleshooting

### Common Issues

**Issue:** `BETTER_AUTH_SECRET not set`
**Solution:** Generate and set secret in `.env`

**Issue:** `Database connection failed`
**Solution:** Verify DATABASE_URL and ensure database is running

**Issue:** `OAuth provider error`
**Solution:** Verify client ID/secret and callback URL

**Issue:** `Session not persisting`
**Solution:** Ensure cookies are enabled and HTTPS is used

**Issue:** `CORS errors`
**Solution:** Add origin to `trustedOrigins` array

## Further Reading

- [Better Auth Documentation](https://www.better-auth.com)
- [Better Auth GitHub](https://github.com/better-auth/better-auth)
- [Next.js App Router](https://nextjs.org/docs/app)
- [Prisma Documentation](https://www.prisma.io/docs)
- [Drizzle Documentation](https://orm.drizzle.team)
