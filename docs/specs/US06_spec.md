# Technical Specification - US06: Interface Graphique Premium

## 1. Overview
This specification details the cosmetic and structural overhaul of the application to provide a state-of-the-art "Premium" user experience. The focus is on aesthetics, professional branding, and smooth interactions.

## 2. Design System (Aesthetics)
- **Primary Palette**: 
    - **Navy Blue** (`#1a2a6c`): Stability, law, and professionalism.
    - **Gold** (`#d4af37`): High value, accuracy, and prestige.
    - **Soft Shadow**: `rgba(0, 0, 0, 0.1)` for depth.
- **Glassmorphism**: Use semi-transparent white backgrounds with `backdrop-filter: blur(10px)` for data containers.
- **Typography**: 
    - Headings: `Playfair Display` (via Google Fonts) for a legal/academic look.
    - Body Text: `Outfit` or `Inter` for modern readability.

## 3. UI Components & Layout
### Visual Hierarchy
- **Sticky Header**: A consistent top bar or banner containing the logo.
- **Service Cards**: Use `st.container` with custom CSS classes to wrap functionally distinct blocks (Upload -> Preview -> Summary -> Score -> Audio).

### Custom CSS Strategy
Inject CSS via `st.markdown(unsafe_allow_html=True)` focusing on:
- **Buttons**: Gradient backgrounds, rounded corners (12px), and a lift effect on hover (`transform: translateY(-2px)`).
- **Progress Bars**: Override Streamlit's default colors to match the Navy/Gold theme.
- **Metrics**: Enhanced visualization for the confidence score (US05).

## 4. Visual Assets
- **Logo/Banner**: A high-resolution generated image (`legal_synthesizer_banner.png`) representing legal precision and AI intelligence.
- **Prompt for Generation**: "A professional and sleek digital banner for a Legal Document AI Synthesizer, dark navy blue background with golden geometric patterns representing law and technology, high-end corporate aesthetic."

## 5. Implementation Roadmap
1. **Asset Generation**: Create the banner image using AI tools.
2. **Infrastructure Update**: Create `src/assets/style.css` (optional) or use a dedicated `ui_utils.py` for CSS injection.
3. **Layout Refactoring**: Wrap current features into styled containers.
4. **Final Polish**: Adjust paddings, margins, and transitions for mobile responsiveness.

## 6. Verification Plan
- Cross-browser testing (Chrome, Safari, Firefox).
- Accessibility audit (contrast ratios for gold/navy).
- Mobile responsiveness check (Streamlit's default responsive behavior must be preserved).
