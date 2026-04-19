import { getAgents } from '@/lib/agents';
import { SITE_URL } from '@/lib/constants';
import type { MetadataRoute } from 'next';

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const agents = await getAgents();
  const now = new Date();
  const agentEntries: MetadataRoute.Sitemap = agents.map((a) => ({
    url: `${SITE_URL}/marketplace/${a.id}`,
    lastModified: new Date(a.updated_at),
    changeFrequency: 'weekly',
    priority: 0.7,
  }));
  return [
    { url: `${SITE_URL}/`, lastModified: now, changeFrequency: 'daily', priority: 1 },
    { url: `${SITE_URL}/marketplace`, lastModified: now, changeFrequency: 'hourly', priority: 0.9 },
    ...agentEntries,
  ];
}
