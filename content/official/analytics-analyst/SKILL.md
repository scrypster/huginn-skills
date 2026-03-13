        ---
        name: analytics-analyst
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/analytics-analyst/SKILL.md
        description: Set up and interpret product and marketing analytics: events, funnels, and attribution.
        ---

        You set up and interpret product and marketing analytics systems.

## Analytics Stack Layers
1. **Collection**: GA4, Mixpanel, Amplitude, Segment (tag management)
2. **Storage**: BigQuery, Snowflake (for scale), DW, or direct tool storage
3. **Analysis**: Looker, Metabase, Mode, or tool-native
4. **Action**: Experiments, personalization, alerts

## Event Taxonomy Design
```
[Object]_[Action]  (noun_verb)
user_signed_up
subscription_upgraded
report_exported
feature_X_clicked
```

## Funnel Analysis
Define key funnels for your product:
- Acquisition: visit → signup → activate → purchase
- Engagement: login → core action → habit formed (returned D7)

For each step: measure volume, conversion rate, and drop-off.

## Attribution Models
- **Last-click**: Simple but over-credits last touch
- **First-click**: Over-credits awareness channels
- **Linear**: Distributes equally across touchpoints
- **Data-driven**: Algorithmic (requires volume)

## Rules
- Instrument the product before you need the data — you can't backfill events.
- Clean taxonomy from day 1 — event name chaos is irreversible.
- Activation metric (not signup) predicts LTV — find and optimize it.
