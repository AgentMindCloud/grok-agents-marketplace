import 'server-only';
import mockAgents from '@/data/featured-agents.mock.json';
import { FEATURED_AGENTS_URL } from './constants';
import type { Agent } from './types';

const MOCK: Agent[] = mockAgents as Agent[];

/**
 * Fetch the canonical featured-agents.json from the awesome-grok-agents repo,
 * revalidated every 10 minutes. Falls back to the local mock if the fetch
 * fails (offline dev, rate limit, 404 during bootstrap).
 */
export async function getAgents(): Promise<Agent[]> {
  try {
    const res = await fetch(FEATURED_AGENTS_URL, {
      next: { revalidate: 600, tags: ['agents'] },
      headers: { Accept: 'application/json' },
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = (await res.json()) as unknown;
    if (!Array.isArray(data) || data.length === 0) throw new Error('Empty payload');
    return data as Agent[];
  } catch (err) {
    if (process.env.NODE_ENV !== 'production') {
      console.warn('[agents] using mock — remote fetch failed:', (err as Error).message);
    }
    return MOCK;
  }
}

export async function getAgentById(id: string): Promise<Agent | null> {
  const agents = await getAgents();
  return agents.find((a) => a.id === id) ?? null;
}

export async function getFeaturedAgents(limit = 3): Promise<Agent[]> {
  const agents = await getAgents();
  return [...agents]
    .sort((a, b) => {
      const fa = a.featured ? 1 : 0;
      const fb = b.featured ? 1 : 0;
      if (fa !== fb) return fb - fa;
      return b.installs - a.installs;
    })
    .slice(0, limit);
}

export async function getLatestAgents(limit = 6): Promise<Agent[]> {
  const agents = await getAgents();
  return [...agents]
    .sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
    .slice(0, limit);
}
