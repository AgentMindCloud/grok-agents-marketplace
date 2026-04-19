import { GlassCard } from '@/components/ui/GlassCard';
import type { AgentWithStats } from '@/lib/types';
import { formatCount } from '@/lib/utils';
import { Bot, Download, ShieldCheck, Star } from 'lucide-react';

export function StatsTeaser({ agents }: { agents: AgentWithStats[] }) {
  const totalAgents = agents.length;
  const totalInstalls = agents.reduce((n, a) => n + (a.installs ?? 0), 0);
  const totalStars = agents.reduce((n, a) => n + (a.stars ?? 0), 0);
  const avgSafety = agents.length
    ? Math.round(
        agents.reduce((n, a) => n + (a.safetyScore ?? 0), 0) /
          agents.filter((a) => a.safetyScore).length || 0
      )
    : 0;

  const items: { icon: React.ReactNode; label: string; value: string }[] = [
    {
      icon: <Bot className="h-4 w-4" />,
      label: 'Featured agents',
      value: formatCount(totalAgents),
    },
    {
      icon: <Download className="h-4 w-4" />,
      label: 'Installs to date',
      value: formatCount(totalInstalls),
    },
    {
      icon: <Star className="h-4 w-4" />,
      label: 'Stars across repos',
      value: formatCount(totalStars),
    },
    {
      icon: <ShieldCheck className="h-4 w-4" />,
      label: 'Avg. safety score',
      value: `${avgSafety}/100`,
    },
  ];

  return (
    <div className="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4 lg:gap-4">
        {items.map((s) => (
          <GlassCard key={s.label} padding="md" className="flex flex-col gap-1.5">
            <div className="flex items-center gap-2 text-cyan">
              {s.icon}
              <span className="text-[11px] uppercase tracking-[0.18em] font-mono">{s.label}</span>
            </div>
            <div className="font-display text-2xl tracking-tight tabular-nums text-ink md:text-3xl">
              {s.value}
            </div>
          </GlassCard>
        ))}
      </div>
    </div>
  );
}
