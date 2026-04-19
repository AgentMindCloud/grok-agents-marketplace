import { CircuitTrace } from '@/components/ui/CircuitTrace';
import { NeonButton } from '@/components/ui/NeonButton';
import { StatPill } from '@/components/ui/StatPill';
import { SITE_TAGLINE } from '@/lib/constants';
import { ArrowRight, Github, Zap } from 'lucide-react';

export function Hero() {
  return (
    <section className="relative overflow-hidden border-b border-border-subtle">
      <CircuitTrace className="opacity-[0.85]" density="dense" />
      <div className="relative mx-auto flex w-full max-w-7xl flex-col items-start gap-8 px-4 pb-24 pt-20 sm:px-6 lg:px-8 lg:pt-28 lg:pb-32">
        <span className="inline-flex items-center gap-2 rounded-sm border border-cyan/40 bg-cyan/5 px-3 py-1 text-xs font-mono uppercase tracking-[0.2em] text-cyan">
          <Zap className="h-3.5 w-3.5" /> {SITE_TAGLINE}
        </span>

        <h1 className="max-w-4xl font-display text-4xl font-semibold leading-[0.95] tracking-tightest text-ink sm:text-5xl md:text-6xl lg:text-7xl">
          The community marketplace for{' '}
          <span className="text-cyan text-glow-cyan">Grok-native</span> agents on X.
        </h1>

        <p className="max-w-2xl text-base text-ink-muted sm:text-lg">
          Discover agents certified Grok-Native, Safety-Max, Voice-Ready, and Swarm-Ready. Install
          in one click, inspect the YAML, and ship in minutes.
        </p>

        <div className="flex flex-wrap items-center gap-3">
          <NeonButton
            variant="primary"
            size="lg"
            href="/marketplace"
            trailingIcon={<ArrowRight className="h-4 w-4" />}
          >
            Browse Agents
          </NeonButton>
          <NeonButton
            variant="secondary"
            size="lg"
            href="https://github.com/AgentMindCloud/awesome-grok-agents"
            external
            leadingIcon={<Github className="h-4 w-4" />}
          >
            Submit your agent
          </NeonButton>
        </div>

        <div className="flex flex-wrap gap-2 pt-2">
          <StatPill value="14" label="YAML standards" tone="cyan" />
          <StatPill value="6" label="Certifications" tone="cyan" />
          <StatPill value="One-click" label="Install on X" tone="green" />
        </div>
      </div>
    </section>
  );
}
