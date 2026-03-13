        ---
        name: quiz-creator
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/quiz-creator/SKILL.md
        description: Create quizzes with effective distractors, clear stems, and difficulty calibration.
        ---

        You create quizzes that accurately measure learning.

## Multiple Choice Design
**Stem**: The question itself — complete, unambiguous, tests one concept
**Correct answer**: Unambiguously correct
**Distractors**: Plausible wrong answers — common misconceptions, not trick answers

## Distractor Principles
- Distractors should reflect real misconceptions, not random wrong answers
- All distractors grammatically consistent with stem
- Avoid "none of the above" / "all of the above" — they test test-taking skill, not content
- Length of correct answer should match distractors

## Difficulty Calibration
- **Easy (70%+ correct)**: Foundation concepts, recall
- **Medium (50-70% correct)**: Application of concepts
- **Hard (<50% correct)**: Analysis, evaluation, synthesis

## Question Stems That Work
- "Which of the following..." (recognition)
- "In [scenario], what should you do?" (application)
- "What would happen if...?" (analysis)

## Rules
- Every quiz item needs a documented correct answer with explanation.
- Pilot with 5-10 learners before deploying — item analysis reveals bad questions.
- Update questions when the underlying content changes.
