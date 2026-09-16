# Finigenie BPSP Supplier Payments — Single Page

## Design / implementation plan

1. **Hero:** Explain the core value proposition immediately: corporate cards can fund supplier payments even when suppliers only accept bank transfers.
2. **Challenge:** Four concise pain points from the product deck.
3. **BPSP model:** Four-step visual flow: Buyer → Finigenie → Acquiring partner → Supplier bank account.
4. **Audience value:** Separate benefits for banks, corporates and suppliers.
5. **Product proof:** Dashboard visual showing money flow, transaction status, suppliers and quick actions.
6. **Payment workflow:** Five-step Quick Pay / bulk / cart flow with supporting product screenshot.
7. **Auditability:** Transaction search, live status, PDF/CSV exports, UTR and timestamped trail.
8. **Capabilities:** Core platform vs optional modules, based on the product deck and commercial-offer module list.
9. **Settlement architecture:** Explain the technology/orchestration role and direct supplier settlement without exposing confidential commercial terms.
10. **CTA:** Route to the public Finigenie contact flow.

## Dependencies

- No runtime JavaScript framework or component library.
- Google Fonts: DM Sans + Manrope (can be replaced by the host site's existing font stack).
- Three supporting PNG visuals extracted/cropped from the supplied BPSP product deck.
- All primary diagrams, icons and UI treatments are CSS/HTML; no stock illustration dependency.

## Source handling

The Mashreq commercial offer is confidential and contains engagement-specific pricing and commercial terms. Those details are deliberately **not** included in this public-facing page.

The product deck has a cover-level T+3 settlement statement while the fund-flow architecture includes a T+2 acquiring-partner label. The page therefore avoids making a hard public settlement-time promise and instead emphasizes direct supplier bank settlement.

## Integration

The HTML is intentionally isolated as a single page. Copy the `<main>` content into the target Finigenie page/component, move the three images into the site's asset/public directory, and merge the CSS variables/tokens into the site's existing design system.

The CTA currently points to Finigenie's public contact page. Replace it with the site's internal route if the host application uses a different route.
