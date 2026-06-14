import type { AppGraph, AppSummary } from '@/types'

export const apps: AppSummary[] = [
  {
    id: 'checkout',
    name: 'Checkout Service',
    description: 'E-commerce checkout flow',
  },
  {
    id: 'analytics',
    name: 'Analytics Pipeline',
    description: 'Real-time event processing',
  },
  {
    id: 'auth',
    name: 'Auth Gateway',
    description: 'Identity and access management',
  },
]

export const graphs: Record<string, AppGraph> = {
  checkout: {
    nodes: [
      {
        id: 'api-gateway',
        type: 'service',
        position: { x: 100, y: 120 },
        data: {
          label: 'API Gateway',
          description: 'Routes incoming checkout requests',
          status: 'healthy',
          loadPercent: 42,
        },
      },
      {
        id: 'payment-svc',
        type: 'service',
        position: { x: 380, y: 60 },
        data: {
          label: 'Payment Service',
          description: 'Processes card and wallet payments',
          status: 'degraded',
          loadPercent: 78,
        },
      },
      {
        id: 'order-db',
        type: 'service',
        position: { x: 380, y: 220 },
        data: {
          label: 'Order DB',
          description: 'Persists order records',
          status: 'healthy',
          loadPercent: 35,
        },
      },
    ],
    edges: [
      { id: 'e1', source: 'api-gateway', target: 'payment-svc' },
      { id: 'e2', source: 'api-gateway', target: 'order-db' },
    ],
  },
  analytics: {
    nodes: [
      {
        id: 'ingest',
        type: 'service',
        position: { x: 80, y: 140 },
        data: {
          label: 'Event Ingest',
          description: 'Receives analytics events',
          status: 'healthy',
          loadPercent: 55,
        },
      },
      {
        id: 'stream',
        type: 'service',
        position: { x: 340, y: 80 },
        data: {
          label: 'Stream Processor',
          description: 'Transforms and enriches events',
          status: 'healthy',
          loadPercent: 62,
        },
      },
      {
        id: 'warehouse',
        type: 'service',
        position: { x: 340, y: 220 },
        data: {
          label: 'Data Warehouse',
          description: 'Long-term analytics storage',
          status: 'down',
          loadPercent: 0,
        },
      },
    ],
    edges: [
      { id: 'e1', source: 'ingest', target: 'stream' },
      { id: 'e2', source: 'stream', target: 'warehouse' },
    ],
  },
  auth: {
    nodes: [
      {
        id: 'auth-api',
        type: 'service',
        position: { x: 120, y: 100 },
        data: {
          label: 'Auth API',
          description: 'Token issuance and validation',
          status: 'healthy',
          loadPercent: 30,
        },
      },
      {
        id: 'session-store',
        type: 'service',
        position: { x: 400, y: 60 },
        data: {
          label: 'Session Store',
          description: 'Redis-backed session cache',
          status: 'healthy',
          loadPercent: 48,
        },
      },
      {
        id: 'user-db',
        type: 'service',
        position: { x: 400, y: 200 },
        data: {
          label: 'User DB',
          description: 'User credentials and profiles',
          status: 'degraded',
          loadPercent: 85,
        },
      },
    ],
    edges: [
      { id: 'e1', source: 'auth-api', target: 'session-store' },
      { id: 'e2', source: 'auth-api', target: 'user-db' },
    ],
  },
}
