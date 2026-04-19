import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./src/**/*.{ts,tsx,mdx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        bg: '#0A0A0A',
        ink: {
          DEFAULT: '#FFFFFF',
          muted: '#E5E5E5',
          subtle: 'rgba(255,255,255,0.5)',
        },
        cyan: {
          DEFAULT: '#00F0FF',
          glow: 'rgba(0,240,255,0.30)',
        },
        green: {
          DEFAULT: '#00FF9D',
          glow: 'rgba(0,255,157,0.30)',
        },
        danger: {
          DEFAULT: '#FF2D55',
        },
        surface: {
          DEFAULT: 'rgba(255,255,255,0.04)',
          raised: 'rgba(255,255,255,0.08)',
        },
        border: {
          subtle: 'rgba(0,240,255,0.15)',
          focus: 'rgba(0,240,255,0.40)',
        },
      },
      borderRadius: {
        sm: '8px',
        md: '16px',
        lg: '24px',
      },
      boxShadow: {
        cyanGlow: '0 0 24px rgba(0,240,255,0.30)',
        greenGlow: '0 0 24px rgba(0,255,157,0.30)',
        cyanGlowSoft: '0 0 12px rgba(0,240,255,0.18)',
      },
      backdropBlur: {
        gi: '20px',
      },
      fontFamily: {
        display: ['var(--font-display)', 'Space Grotesk', 'Inter', 'system-ui', 'sans-serif'],
        body: ['var(--font-body)', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['var(--font-mono)', 'JetBrains Mono', 'ui-monospace', 'monospace'],
      },
      letterSpacing: {
        tightest: '-0.04em',
        tighter: '-0.03em',
      },
      transitionTimingFunction: {
        gi: 'cubic-bezier(0.2, 0.8, 0.2, 1)',
      },
      keyframes: {
        'fade-in-up': {
          '0%': { opacity: '0', transform: 'translateY(8px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        'pulse-slow': {
          '0%, 100%': { opacity: '0.6' },
          '50%': { opacity: '1' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
        'trace-dash': {
          '0%': { strokeDashoffset: '400' },
          '100%': { strokeDashoffset: '0' },
        },
      },
      animation: {
        'fade-in-up': 'fade-in-up 400ms cubic-bezier(0.2, 0.8, 0.2, 1) both',
        'pulse-slow': 'pulse-slow 3.2s ease-in-out infinite',
        shimmer: 'shimmer 1.8s linear infinite',
        'trace-dash': 'trace-dash 3.5s linear infinite',
      },
    },
  },
  plugins: [],
};

export default config;
