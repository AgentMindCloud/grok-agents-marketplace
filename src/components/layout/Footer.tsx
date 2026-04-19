import { DISCLAIMER, SITE_TAGLINE } from '@/lib/constants';
import { BookOpen, Github, Package, Twitter } from 'lucide-react';
import Link from 'next/link';

const COLS: { title: string; links: { href: string; label: string; external?: boolean }[] }[] = [
  {
    title: 'Marketplace',
    links: [
      { href: '/marketplace', label: 'Browse agents' },
      { href: '/marketplace?sort=trending', label: 'Trending' },
      { href: '/marketplace?cert=voice-ready', label: 'Voice-ready' },
      { href: '/marketplace?cert=swarm-ready', label: 'Swarm-ready' },
    ],
  },
  {
    title: 'Ecosystem',
    links: [
      {
        href: 'https://github.com/AgentMindCloud/grok-install',
        label: 'grok-install',
        external: true,
      },
      {
        href: 'https://github.com/AgentMindCloud/grok-yaml-standards',
        label: 'YAML standards',
        external: true,
      },
      {
        href: 'https://github.com/AgentMindCloud/vscode-grok-yaml',
        label: 'VS Code extension',
        external: true,
      },
      {
        href: 'https://github.com/AgentMindCloud/grok-install-action',
        label: 'GitHub Action',
        external: true,
      },
    ],
  },
  {
    title: 'Community',
    links: [
      { href: 'https://docs.grokinstall.dev', label: 'Documentation', external: true },
      { href: 'https://github.com/sponsors/JanSol0s', label: 'Sponsor', external: true },
      {
        href: 'https://github.com/AgentMindCloud/awesome-grok-agents',
        label: 'Submit an agent',
        external: true,
      },
      { href: 'https://x.com/JanSol0s', label: '@JanSol0s on X', external: true },
    ],
  },
];

export function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer className="relative mt-24 border-t border-border-subtle">
      <div className="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 gap-10 md:grid-cols-4">
          <div className="md:col-span-1">
            <Link href="/" className="font-display text-lg tracking-[-0.06em] uppercase">
              <span className="text-ink">GROK</span>
              <span className="text-cyan">INSTALL</span>
            </Link>
            <p className="mt-3 text-sm text-ink-muted">{SITE_TAGLINE}</p>
            <div className="mt-4 flex gap-3">
              <a
                href="https://github.com/AgentMindCloud"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="AgentMindCloud on GitHub"
                className="text-ink-subtle hover:text-cyan transition-colors"
              >
                <Github className="h-5 w-5" />
              </a>
              <a
                href="https://x.com/JanSol0s"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="@JanSol0s on X"
                className="text-ink-subtle hover:text-cyan transition-colors"
              >
                <Twitter className="h-5 w-5" />
              </a>
              <a
                href="https://docs.grokinstall.dev"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Documentation"
                className="text-ink-subtle hover:text-cyan transition-colors"
              >
                <BookOpen className="h-5 w-5" />
              </a>
              <a
                href="https://www.npmjs.com/package/grok-install"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="npm package"
                className="text-ink-subtle hover:text-cyan transition-colors"
              >
                <Package className="h-5 w-5" />
              </a>
            </div>
          </div>

          {COLS.map((col) => (
            <div key={col.title}>
              <h3 className="font-display text-sm uppercase tracking-[0.18em] text-cyan">
                {col.title}
              </h3>
              <ul className="mt-3 flex flex-col gap-2">
                {col.links.map((l) => (
                  <li key={l.href}>
                    <Link
                      href={l.href as never}
                      target={l.external ? '_blank' : undefined}
                      rel={l.external ? 'noopener noreferrer' : undefined}
                      className="text-sm text-ink-muted hover:text-ink transition-colors"
                    >
                      {l.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-10 flex flex-col gap-4 border-t border-border-subtle pt-6 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-xs text-ink-subtle max-w-xl">{DISCLAIMER}</p>
          <p className="text-xs text-ink-subtle">
            © {year} GrokInstall · Built by{' '}
            <a
              href="https://x.com/JanSol0s"
              target="_blank"
              rel="noopener noreferrer"
              className="text-cyan hover:underline"
            >
              @JanSol0s
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
}
