// app/dashboard/page.tsx
// Protected dashboard page with user profile and session management

"use client";

import { authClient } from "@/lib/auth-client";
import { redirect } from "next/navigation";
import { useRouter } from "next/navigation";
import Image from "next/image";
import { useState } from "react";

export default function DashboardPage() {
  const router = useRouter();
  const { data: session, isPending, error, refetch } = authClient.useSession();
  const [signingOut, setSigningOut] = useState(false);

  // Loading state
  if (isPending) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-blue-600 border-t-transparent" />
      </div>
    );
  }

  // Redirect if not authenticated
  if (!session || error) {
    redirect("/sign-in");
  }

  const { user } = session;

  // Calculate session expiry
  const expiresAt = new Date(session.session.expiresAt);
  const now = new Date();
  const daysUntilExpiry = Math.ceil(
    (expiresAt.getTime() - now.getTime()) / (1000 * 60 * 60 * 24)
  );

  const handleSignOut = async () => {
    setSigningOut(true);
    await authClient.signOut();
    router.push("/");
    router.refresh();
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <h1 className="text-3xl font-bold tracking-tight text-gray-900">
              Dashboard
            </h1>
            <button
              onClick={handleSignOut}
              disabled={signingOut}
              className="rounded-md bg-red-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 disabled:opacity-50"
            >
              {signingOut ? "Signing out..." : "Sign out"}
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid gap-6 md:grid-cols-2">
          {/* User Profile Card */}
          <div className="rounded-lg bg-white p-6 shadow">
            <h2 className="mb-4 text-xl font-semibold">Your Profile</h2>
            <div className="flex items-center gap-4">
              {user.image ? (
                <Image
                  src={user.image}
                  alt={user.name}
                  width={80}
                  height={80}
                  className="rounded-full"
                />
              ) : (
                <div className="flex h-20 w-20 items-center justify-center rounded-full bg-blue-600 text-3xl font-bold text-white">
                  {user.name.charAt(0).toUpperCase()}
                </div>
              )}
              <div>
                <h3 className="text-lg font-semibold">{user.name}</h3>
                <p className="text-gray-600">{user.email}</p>
                {user.emailVerified && (
                  <span className="mt-2 inline-flex items-center gap-1 rounded-full bg-green-100 px-2 py-1 text-xs font-medium text-green-800">
                    <svg
                      className="h-3 w-3"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fillRule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                        clipRule="evenodd"
                      />
                    </svg>
                    Verified
                  </span>
                )}
              </div>
            </div>
            <div className="mt-6 space-y-3">
              <div className="flex justify-between border-t pt-3">
                <span className="text-sm text-gray-600">User ID</span>
                <span className="text-sm font-mono">{user.id}</span>
              </div>
              <div className="flex justify-between border-t pt-3">
                <span className="text-sm text-gray-600">Joined</span>
                <span className="text-sm">
                  {new Date(user.createdAt).toLocaleDateString()}
                </span>
              </div>
              <div className="flex justify-between border-t pt-3">
                <span className="text-sm text-gray-600">Last Updated</span>
                <span className="text-sm">
                  {new Date(user.updatedAt).toLocaleDateString()}
                </span>
              </div>
            </div>
          </div>

          {/* Session Information Card */}
          <div className="rounded-lg bg-white p-6 shadow">
            <h2 className="mb-4 text-xl font-semibold">Session Info</h2>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-sm text-gray-600">Session ID</span>
                <span className="text-sm font-mono">
                  {session.session.id.slice(0, 12)}...
                </span>
              </div>
              <div className="flex justify-between border-t pt-3">
                <span className="text-sm text-gray-600">Expires</span>
                <span className="text-sm">
                  {expiresAt.toLocaleDateString()} ({daysUntilExpiry} days)
                </span>
              </div>
              {session.session.ipAddress && (
                <div className="flex justify-between border-t pt-3">
                  <span className="text-sm text-gray-600">IP Address</span>
                  <span className="text-sm font-mono">
                    {session.session.ipAddress}
                  </span>
                </div>
              )}
              {session.session.userAgent && (
                <div className="border-t pt-3">
                  <span className="text-sm text-gray-600">User Agent</span>
                  <p className="mt-1 text-xs text-gray-500">
                    {session.session.userAgent}
                  </p>
                </div>
              )}
            </div>
            <button
              onClick={() => refetch()}
              className="mt-6 w-full rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-500"
            >
              Refresh Session
            </button>
          </div>

          {/* Quick Actions Card */}
          <div className="rounded-lg bg-white p-6 shadow md:col-span-2">
            <h2 className="mb-4 text-xl font-semibold">Quick Actions</h2>
            <div className="grid gap-4 sm:grid-cols-3">
              <button className="rounded-md border border-gray-300 bg-white px-4 py-3 text-sm font-medium text-gray-700 hover:bg-gray-50">
                Edit Profile
              </button>
              <button className="rounded-md border border-gray-300 bg-white px-4 py-3 text-sm font-medium text-gray-700 hover:bg-gray-50">
                Change Password
              </button>
              <button className="rounded-md border border-gray-300 bg-white px-4 py-3 text-sm font-medium text-gray-700 hover:bg-gray-50">
                Account Settings
              </button>
            </div>
          </div>

          {/* Stats Card */}
          <div className="rounded-lg bg-white p-6 shadow md:col-span-2">
            <h2 className="mb-4 text-xl font-semibold">Account Stats</h2>
            <div className="grid gap-4 sm:grid-cols-3">
              <div className="rounded-lg bg-blue-50 p-4">
                <div className="text-2xl font-bold text-blue-600">1</div>
                <div className="text-sm text-gray-600">Active Session</div>
              </div>
              <div className="rounded-lg bg-green-50 p-4">
                <div className="text-2xl font-bold text-green-600">
                  {Math.floor(
                    (now.getTime() - new Date(user.createdAt).getTime()) /
                      (1000 * 60 * 60 * 24)
                  )}
                </div>
                <div className="text-sm text-gray-600">Days as Member</div>
              </div>
              <div className="rounded-lg bg-purple-50 p-4">
                <div className="text-2xl font-bold text-purple-600">
                  {user.emailVerified ? "Yes" : "No"}
                </div>
                <div className="text-sm text-gray-600">Email Verified</div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
