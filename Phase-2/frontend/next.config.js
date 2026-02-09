/** @type {import('next').NextConfig} */
const nextConfig = {
  // Allow dev server to be accessed from network IP
  allowedDevOrigins: ['192.168.18.22'],

  // Other Next.js configurations
  reactStrictMode: true,
};

module.exports = nextConfig;
