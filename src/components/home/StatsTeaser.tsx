import { GlassCard } from '@/components/ui/GlassCard';
import { formatCount } from '@/lib/utils';
import { Bot, Download, ShieldCheck, Zap } from 'lucide-react';

export interface StatsTeaserData {
  agents: number;
  installs: number;
  last24hInstalls: number;
  avgSafetyScore: number;
}

export function StatsTeaser({ data }: { data: StatsTeaserData }) {
  const items: { icon: React.ReactNode; label: string; value: string }[] = [
    {
      icon: <Bot className="h-4 w-4" />,
      label: 'Featured agents',
      value: formatCount(data.agents),
    },
    {
      icon: <Download className="h-4 w-4" />,
      label: 'Installs lifetime',
      value: formatCount(data.installs),
    },
    {
      icon: <Zap className="h-4 w-4" />,
      label: 'Last 24 hours',
      value: formatCount(data.last24hInstalls),
    },
    {
      icon: <ShieldCheck className="h-4 w-4" />,
      label: 'Avg. safety score',
      value: `${data.avgSafetyScore}/100`,
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
