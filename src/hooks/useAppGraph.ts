import { useQuery } from '@tanstack/react-query'
import { fetchAppGraph } from '@/api/client'

export function useAppGraph(appId: string | null) {
  return useQuery({
    queryKey: ['app-graph', appId],
    queryFn: () => fetchAppGraph(appId!),
    enabled: Boolean(appId),
    staleTime: 30_000,
  })
}
