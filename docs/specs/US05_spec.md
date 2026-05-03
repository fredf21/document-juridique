# Technical Specification - US05: Score de Confiance

## 1. Overview
The goal is to provide users with a visual indicator of how confident the AI is in the generated summary. This transparency helps users manage their expectations regarding the AI's "hallucinations" or errors.

## 2. Technical Stack
- **Engine**: Google Gemini (via `google-generativeai`).
- **Data Format**: JSON (to facilitate parsing of both summary and score).
- **Visualization**: Streamlit components (`st.progress`).

## 3. Backend Modification (`src/services/ai_connector.py`)
### Prompt Engineering
The system prompt will be updated to require a JSON response:
```json
{
  "summary": "The generated summary text...",
  "confidence_score": 85
}
```
*Note: The score should be an integer between 0 and 100 representing the AI's own assessment of its factual accuracy and clarity.*

### Logic
- Update `summarize_text` to handle JSON extraction.
- Implement robust parsing in case the LLM doesn't return perfect JSON (use `json.loads` within a try-except).

## 4. UI/UX Integration (`src/app.py`)
### Visualization
- Use `st.progress(score / 100)`.
- **Dynamic Coloring**: Since Streamlit doesn't natively color the progress bar dynamically based on value without hacky CSS, we will use `st.metric` or a color-coded label above the progress bar.
    - **Green** (>80): "Très Fiable"
    - **Orange** (50-80): "Fiabilité Moyenne"
    - **Red** (<50): "Prudence recommandée"

### Layout
The score gauge and label will be placed immediately above the summary text block.

## 5. Implementation Steps
1. **[MODIFY] [ai_connector.py](file:///c:/Users/fredf/CCNB_DEUXIEME_ANNEE/AI1022/PROJET-DE-SESSION/document-juridique/src/services/ai_connector.py)**: Update prompt and return a tuple `(summary, score, error)`.
2. **[MODIFY] [app.py](file:///c:/Users/fredf/CCNB_DEUXIEME_ANNEE/AI1022/PROJET-DE-SESSION/document-juridique/src/app.py)**: Integrate the new return values and display the progress bar/metric.
3. **[TEST]**: Verify that the score is extracted and displayed correctly for various document types.
