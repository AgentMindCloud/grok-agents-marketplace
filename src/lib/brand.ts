/**
 * Raw brand hex values — ONLY for places that can't consume Tailwind, such as
 * `next/og` ImageResponse and Next.js `themeColor` metadata. Everywhere else,
 * use Tailwind utilities backed by these tokens (`bg-bg`, `text-cyan`, etc.)
 * so the locked brand system stays the single source of truth.
 */
export const BRAND = {
  bg: '#0A0A0A',
  ink: '#FFFFFF',
  inkMuted: '#E5E5E5',
  inkSubtle: 'rgba(255,255,255,0.5)',
  cyan: '#00F0FF',
  green: '#00FF9D',
  danger: '#FF2D55',
} as const;
