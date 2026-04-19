'use client';

import { NeonButton } from '@/components/ui/NeonButton';
import { cn } from '@/lib/utils';
import { Check, Copy, ExternalLink, Twitter } from 'lucide-react';
import { useState } from 'react';

type State = 'idle' | 'working' | 'done';

export function InstallOnX({
  agentId,
  xInstallUrl,
  className,
}: {
  agentId: string;
  xInstallUrl?: string;
  className?: string;
}) {
  const [state, setState] = useState<State>('idle');

  const shareCommand = `npx grok-install ${agentId}`;

  async function handleClick() {
    if (xInstallUrl) {
      window.open(xInstallUrl, '_blank', 'noopener,noreferrer');
      return;
    }
    setState('working');
    try {
      await navigator.clipboard.writeText(shareCommand);
      setState('done');
      setTimeout(() => setState('idle'), 1800);
    } catch {
      setState('idle');
    }
  }

  const isIdle = state === 'idle';
  const isWorking = state === 'working';
  const isDone = state === 'done';

  return (
    <div className={cn('flex flex-col gap-3', className)}>
      <NeonButton
        variant={isDone ? 'success' : 'primary'}
        size="lg"
        fullWidth
        onClick={handleClick}
        disabled={isWorking}
        leadingIcon={
          isDone ? (
            <Check className="h-4 w-4" />
          ) : isWorking ? (
            <span className="h-4 w-4 rounded-full border-2 border-bg border-t-transparent animate-spin" />
          ) : xInstallUrl ? (
            <Twitter className="h-4 w-4" />
          ) : (
            <Copy className="h-4 w-4" />
          )
        }
        trailingIcon={xInstallUrl && isIdle ? <ExternalLink className="h-4 w-4" /> : null}
      >
        {isDone
          ? 'Copied command'
          : isWorking
            ? 'Preparing…'
            : xInstallUrl
              ? 'Install on X'
              : 'Copy install command'}
      </NeonButton>
      {!xInstallUrl ? (
        <p className="text-[11px] text-ink-subtle leading-relaxed">
          One-click Install-on-X coming soon. Tap the button to copy the CLI command.
        </p>
      ) : null}
    </div>
  );
}
