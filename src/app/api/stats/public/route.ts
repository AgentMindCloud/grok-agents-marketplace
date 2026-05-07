import { NextResponse } from 'next/server';
import {
  getActiveAgents7d,
  getApiCallsSaved,
  getCategoryBreakdown,
  getTotalAgentsInstalled,
  getTotalCreators,
  getXPostsGenerated,
} from '@/lib/telemetry-queries';
import { checkIpRateLimit } from '@/lib/telemetry-store';

export const runtime = 'nodejs';
export const revalidate = 30;

function clientIpHash(req: Request): string {
  const fwd = req.headers.get('x-forwarded-for');
  const real = req.headers.get('x-real-ip');
  const raw = (fwd?.split(',')[0]?.trim() ?? real?.trim() ?? 'unknown').toLowerCase();
  let h = 0;
  for (let i = 0; i < raw.length; i++) h = ((h << 5) - h + raw.charCodeAt(i)) | 0;
  return `h${(h >>> 0).toString(36)}`;
}

export async function GET(req: Request) {
  const limit = await checkIpRateLimit(clientIpHash(req));
  if (!limit.ok) {
    return NextResponse.json(
      { error: 'rate_limited' },
      {
        status: 429,
        headers: {
          'Retry-After': Math.ceil(limit.resetMs / 1000).toString(),
          'X-RateLimit-Remaining': '0',
        },
      }
    );
  }

  const [totalAgents, posts, apiSaved, active7d, creators, categories] = await Promise.all([
    getTotalAgentsInstalled(),
    getXPostsGenerated(),
    getApiCallsSaved(),
    getActiveAgents7d(),
    getTotalCreators(),
    getCategoryBreakdown(),
  ]);

  return NextResponse.json(
    {
      generatedAt: new Date().toISOString(),
      totals: {
        agentsInstalled: totalAgents,
        xPostsGenerated: posts,
        apiCallsSaved: apiSaved,
        activeAgents7d: active7d,
        creators,
      },
      categories,
    },
    {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, s-maxage=30, stale-while-revalidate=120',
        'X-RateLimit-Remaining': String(limit.remaining),
      },
    }
  );
}

export function OPTIONS() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
