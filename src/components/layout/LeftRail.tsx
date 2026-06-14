import { LayoutDashboard, Network, Settings, Layers } from 'lucide-react'
import { cn } from '@/lib/utils'

const navItems = [
  { icon: LayoutDashboard, label: 'Dashboard', active: false },
  { icon: Network, label: 'Graphs', active: true },
  { icon: Layers, label: 'Services', active: false },
  { icon: Settings, label: 'Settings', active: false },
]

export function LeftRail() {
  return (
    <nav className="flex w-14 shrink-0 flex-col items-center gap-1 border-r border-[var(--color-border)] bg-white py-4">
      {navItems.map(({ icon: Icon, label, active }) => (
        <button
          key={label}
          type="button"
          title={label}
          className={cn(
            'flex h-10 w-10 items-center justify-center rounded-lg transition-colors',
            active
              ? 'bg-[var(--color-primary)] text-white'
              : 'text-[var(--color-muted-foreground)] hover:bg-[var(--color-accent)] hover:text-[var(--color-foreground)]',
          )}
        >
          <Icon className="h-5 w-5" />
        </button>
      ))}
    </nav>
  )
}
