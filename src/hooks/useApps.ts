import { useQuery } from '@tanstack/react-query'
import { fetchApps } from '@/api/client'

export function useApps() {
  return useQuery({
    queryKey: ['apps'],
    queryFn: fetchApps,
    staleTime: 30_000,
  })
}
