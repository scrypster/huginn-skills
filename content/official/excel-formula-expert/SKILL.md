        ---
        name: excel-formula-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/excel-formula-expert/SKILL.md
        description: Write complex spreadsheet formulas: XLOOKUP, SUMIFS, pivot tables, and array formulas.
        ---

        You write spreadsheet formulas that solve real data problems.

## Essential Formula Categories

### Lookup
```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
=VLOOKUP(value, table, col_index, FALSE)  -- legacy but common
```

### Conditional Aggregation
```
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)
=COUNTIFS(range1, criteria1, range2, criteria2)
=AVERAGEIFS(avg_range, criteria_range, criteria)
```

### Text Manipulation
```
=TEXTJOIN(", ", TRUE, A1:A10)  -- join with delimiter
=LEFT(A1, FIND(" ", A1)-1)    -- extract first word
=TRIM(CLEAN(A1))               -- clean whitespace/non-printable
```

### Date/Time
```
=EDATE(start_date, months)    -- add months
=NETWORKDAYS(start, end)      -- working days between dates
=EOMONTH(date, 0)            -- last day of month
```

## Rules
- Named ranges make formulas readable — use them.
- XLOOKUP replaces VLOOKUP in all modern versions.
- Array formulas (Ctrl+Shift+Enter or `=ARRAYFORMULA()`) can replace many helper columns.
