import { http, HttpResponse, delay } from 'msw'
import { apps, graphs } from './data'

let simulateError = false
let randomFailureRate = 0

export function setSimulateError(value: boolean) {
  simulateError = value
}

export function setRandomFailureRate(rate: number) {
  randomFailureRate = Math.max(0, Math.min(1, rate))
}

export const handlers = [
  http.get('/api/apps', async () => {
    await delay(600)

    if (simulateError || (randomFailureRate > 0 && Math.random() < randomFailureRate)) {
      return HttpResponse.json(
        { message: 'Failed to fetch apps' },
        { status: 500 },
      )
    }

    return HttpResponse.json(apps)
  }),

  http.get('/api/apps/:appId/graph', async ({ params }) => {
    await delay(800)

    if (simulateError || (randomFailureRate > 0 && Math.random() < randomFailureRate)) {
      return HttpResponse.json(
        { message: 'Failed to fetch graph' },
        { status: 500 },
      )
    }

    const appId = params.appId as string
    const graph = graphs[appId]

    if (!graph) {
      return HttpResponse.json({ message: 'App not found' }, { status: 404 })
    }

    return HttpResponse.json({
      nodes: structuredClone(graph.nodes),
      edges: structuredClone(graph.edges),
    })
  }),
]
