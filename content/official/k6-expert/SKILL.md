        ---
        name: k6-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/k6-expert/SKILL.md
        description: Write k6 load tests: scenarios, thresholds, and realistic traffic modeling.
        ---

        You write effective k6 load tests.

## k6 Script
```javascript
import http from 'k6/http'
import { check, sleep } from 'k6'
import { Rate } from 'k6/metrics'

const errorRate = new Rate('errors')

export const options = {
  scenarios: {
    ramp_up: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 100 },  // ramp to 100
        { duration: '5m', target: 100 },  // hold
        { duration: '2m', target: 0 },    // ramp down
      ],
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% under 500ms
    errors: ['rate<0.01'],             // error rate under 1%
  },
}

export default function () {
  const res = http.get('https://api.example.com/users')
  check(res, { 'status is 200': (r) => r.status === 200 })
  errorRate.add(res.status !== 200)
  sleep(1)
}
```

## Rules
- Always define thresholds — without them, results have no pass/fail.
- Use realistic think times (`sleep(1)`) to model actual user behavior.
- Separate scenario scripts for different user journeys.
