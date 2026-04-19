import { InstallVolumeChart } from '@/components/stats/InstallVolumeChart';
import { SafetyDistribution } from '@/components/stats/SafetyDistribution';
import { SectionFunnel } from '@/components/stats/SectionFunnel';
import { StatsHeadline } from '@/components/stats/StatsHeadline';
import { TopAgentsBar } from '@/components/stats/TopAgentsBar';
import { CircuitTrace } from '@/components/ui/CircuitTrace';
import { Section, SectionHeader } from '@/components/ui/Section';
import { getAgents } from '@/lib/agents';
import { getAllTotals, getCounts, getDailyCounts } from '@/lib/installs';
import { getSectionFunnel, plausibleConfigured } from '@/lib/plausible';
import type { Metadata } from 'next';

export const revalidate = 300;

export const metadata: Metadata = {
  title: 'Stats',
  description:
    'Live install counts, trends, and safety distribution across the GrokInstall catalogue.',
};

export default async function StatsPage() {
  const [agents, totals, funnelRaw] = await Promise.all([
    getAgents(),
    getAllTotals(),
    getSectionFunnel(),
  ]);

  const perAgent = await Promise.all(
    agents.map(async (a) => {
      const live = await getCounts(a.id);
      const installs = Math.max(a.installs ?? 0, totals.get(a.id) ?? 0, live.total);
      return {
        id: a.id,
        name: a.name,
        installs,
        last7d: live.last7d,
        last24h: live.last24h,
        safetyScore: a.safetyScore ?? null,
      };
    })
  );

  const totalInstalls = perAgent.reduce((n, a) => n + a.installs, 0);
  const last24h = perAgent.reduce((n, a) => n + a.last24h, 0);
  const creators = new Set(agents.map((a) => a.creator.handle)).size;

  const ranked = [...perAgent].sort((a, b) => b.installs - a.installs);
  const topAgent = ranked[0];
  const initialDaily = topAgent ? await getDailyCounts(topAgent.id, 30) : [];

  const funnelMap = new Map(funnelRaw.map((r) => [r.name, r.count]));
  const funnelData = [
    { step: 'Pageviews', count: funnelMap.get('pageview') ?? 0 },
    { step: 'Agent views', count: funnelMap.get('agent_viewed') ?? 0 },
    { step: 'Install clicks', count: funnelMap.get('install_clicked') ?? 0 },
  ];

  const safetyScores = agents
    .map((a) => a.safetyScore)
    .filter((s): s is number => typeof s === 'number');

  return (
    <div className="flex flex-col gap-10 pb-16">
      <section className="relative overflow-hidden border-b border-border-subtle">
        <CircuitTrace density="dense" />
        <div className="relative mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8 pt-14 pb-10">
          <SectionHeader
            eyebrow="Stats"
            title="The state of Grok-native agents, live."
            description="Install signals, top performers, and safety posture across every agent in the catalogue. Refreshed every 5 minutes."
          />
        </div>
      </section>

      <Section>
        <div className="flex flex-col gap-6">
          <StatsHeadline
            data={{
              agents: agents.length,
              creators,
              installs: totalInstalls,
              last24hInstalls: last24h,
            }}
          />

          <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
            {topAgent ? (
              <InstallVolumeChart
                agents={perAgent.map((a) => ({ id: a.id, name: a.name }))}
                initialSeries={initialDaily}
                initialAgentId={topAgent.id}
              />
            ) : null}
            <TopAgentsBar data={perAgent} />
            <SectionFunnel data={funnelData} plausibleConfigured={plausibleConfigured()} />
            <SafetyDistribution scores={safetyScores} />
          </div>

          <p className="text-[11px] text-ink-subtle text-center mt-2">
            All metrics are aggregated and anonymous. No personal identifiers are surfaced on this
            page.
          </p>
        </div>
      </Section>
    </div>
  );
}
