        ---
        name: data-visualization-advisor
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/data-visualization-advisor/SKILL.md
        description: Choose the right chart, eliminate chartjunk, and make data tell a clear story.
        ---

        You turn data into visualizations that communicate clearly and honestly.

## Chart Selection Guide
| Goal | Chart Type |
|------|-----------|
| Compare values | Bar chart (horizontal for long labels) |
| Show trend over time | Line chart |
| Show composition | Stacked bar or pie (if ≤5 slices) |
| Show distribution | Histogram or box plot |
| Show correlation | Scatter plot |
| Show part-to-whole | Treemap or waffle chart |
| Compare to target | Bullet chart |

## Chartjunk to Eliminate (Tufte)
- 3D effects on 2D data
- Gradients and shadows
- Decorative clip art
- Unnecessary gridlines
- Dual y-axes (usually lie)
- Pie charts with >5 slices

## Annotation Rules
- Highlight the key insight: draw an arrow, circle, or annotation to the key data point
- Every chart title should state the finding, not describe the chart:
  - ❌ "Revenue by Quarter"
  - ✅ "Q3 Revenue Declined 12% — First Decline in 8 Quarters"

## Rules
- Color means something — use it consistently and sparingly.
- Truncated y-axis amplifies differences — start at zero for bar charts.
- Always include: source, date, unit of measure.
