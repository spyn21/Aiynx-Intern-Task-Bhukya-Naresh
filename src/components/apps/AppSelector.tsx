import { useEffect } from 'react'
import { useApps } from '@/hooks/useApps'
import { useAppStore } from '@/store/useAppStore'
import { Skeleton } from '@/components/ui/skeleton'
import { Button } from '@/components/ui/button'
import { cn } from '@/lib/utils'
import { AlertCircle, RefreshCw } from 'lucide-react'

export function AppSelector() {
  const { data: apps, isLoading, isError, error, refetch } = useApps()
  const selectedAppId = useAppStore((s) => s.selectedAppId)
  const setSelectedAppId = useAppStore((s) => s.setSelectedAppId)

  useEffect(() => {
    if (apps && apps.length > 0 && !selectedAppId) {
      setSelectedAppId(apps[0].id)
    }
  }, [apps, selectedAppId, setSelectedAppId])

  if (isLoading) {
    return (
      <div className="space-y-2 p-4">
        <Skeleton className="h-4 w-24" />
        <Skeleton className="h-10 w-full" />
        <Skeleton className="h-10 w-full" />
        <Skeleton className="h-10 w-full" />
      </div>
    )
  }

  if (isError) {
    return (
      <div className="flex flex-col items-center gap-2 p-4 text-center">
        <AlertCircle className="h-5 w-5 text-[var(--color-destructive)]" />
        <p className="text-xs text-[var(--color-destructive)]">
          {error instanceof Error ? error.message : 'Failed to load apps'}
        </p>
        <Button variant="outline" size="sm" onClick={() => void refetch()}>
          <RefreshCw className="h-3 w-3" />
          Retry
        </Button>
      </div>
    )
  }

  return (
    <div className="p-4">
      <h2 className="mb-3 text-xs font-semibold uppercase tracking-wide text-[var(--color-muted-foreground)]">
        Apps
      </h2>
      <ul className="space-y-1">
        {apps?.map((app) => (
          <li key={app.id}>
            <button
              type="button"
              onClick={() => setSelectedAppId(app.id)}
              className={cn(
                'w-full rounded-md px-3 py-2 text-left transition-colors',
                selectedAppId === app.id
                  ? 'bg-[var(--color-primary)] text-[var(--color-primary-foreground)]'
                  : 'hover:bg-[var(--color-accent)]',
              )}
            >
              <div className="text-sm font-medium">{app.name}</div>
              <div
                className={cn(
                  'text-xs',
                  selectedAppId === app.id
                    ? 'text-white/80'
                    : 'text-[var(--color-muted-foreground)]',
                )}
              >
                {app.description}
              </div>
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
