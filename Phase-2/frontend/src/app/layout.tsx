/**
 * Root Layout - Application Shell
 */
import { Providers } from "./providers";
import "./globals.css";

export const metadata = {
  title: "Todo App",
  description: "Full-stack todo application with Next.js and FastAPI",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body suppressHydrationWarning>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
