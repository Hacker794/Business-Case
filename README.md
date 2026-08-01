# Riverside Malls Smart Trolley Business Case

## Overview

This project evaluates whether Riverside Malls should launch a paid pilot of 25 smart trolleys and determines a suitable monthly price.

The analysis recommends launching the pilot at **£200 per trolley per month**. This price produces a positive monthly profit while remaining the lowest of the required price options.

## Recommendation

Riverside Malls should launch a **25-trolley paid pilot at £200 per trolley per month**.

At this price:

- Monthly revenue: **£5,000**
- Monthly variable costs: **£1,000**
- Monthly fixed costs: **£3,000**
- Monthly profit: **£1,000**
- Break-even point: **18.8 trolleys**

## Steps Completed

### Step 1 — Case Framing

The business case was structured using:

- Situation
- Complication
- Key question
- Initial hypothesis
- Decision criteria

The main question was whether Riverside Malls should launch the pilot and what monthly price it should charge.

### Step 2 — Unit Economics

A Python model was created to test four prices:

| Monthly price | Monthly profit | Break-even trolleys |
|---:|---:|---:|
| £150 | -£250 | 27.3 |
| £200 | £1,000 | 18.8 |
| £250 | £2,250 | 14.3 |
| £300 | £3,500 | 11.5 |

The model also generates a profit-versus-price chart.

### Step 3 — Results and Recommendation

The results showed that £150 is not viable because the pilot would lose money and require more than 25 trolleys to break even.

Although £250 and £300 generate more profit, customer willingness to pay has not yet been tested. Therefore, £200 is the safest starting price.

### Step 4 — Product One-Pager

The product one-pager defines:

- Target users
- Customer problem
- Core job to be done
- Minimum viable product
- Features deliberately excluded
- Revenue model
- Pilot success measures
- Main risks and mitigations

The MVP focuses on essential shopping and trolley-management features without adding expensive extras before demand has been proven.

### Step 5 — Consulting Presentation

A six-slide consulting presentation was created covering:

1. Situation and key question
2. Recommendation
3. Unit economics and pricing results
4. Product and MVP scope
5. Risks and next steps
6. Final decision

## Project Structure

```text
Smart-Trolley-Business-Case/
├── case-framing.md
├── unit_economics.py
├── profit_vs_price.png
├── model-results.md
├── product-one-pager.md
└── README.md
```

## Running the Model

Install Matplotlib:

```bash
python3 -m pip install matplotlib
```

Run the unit-economics model:

```bash
python3 unit_economics.py
```

The program prints the profit and break-even results and creates:

```text
profit_vs_price.png
```

## Key Risks

The main risks are:

- Low shopper adoption
- Operator resistance to the price
- Higher-than-expected support costs
- Battery or software reliability problems
- Security and privacy concerns

The pilot should measure usage, customer satisfaction, faults, support costs and operator willingness to continue paying.

## Conclusion

The financial model supports launching the 25-trolley pilot at **£200 per trolley per month**.

This price generates a monthly profit of **£1,000** and provides a break-even cushion of approximately six trolleys. Riverside Malls should use the pilot to collect evidence before increasing the price or expanding the service.