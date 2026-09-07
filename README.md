# nav-calculator
This is a simple Python script for calculating the **Net Asset Value (NAV) per share** of an investment fund.

The calculator assumes that all assets, cash, expenses, and security prices are denominated in **USD**. No foreign exchange conversion is performed.

## How NAV is Calculated

The basic NAV calculation is:

```text
NAV per Share = Net Assets / Shares Outstanding
```

Where:

```text
Net Assets = Total Assets - Accrued Expenses
```

And:

```text
Total Assets = Investment Value + Cash
```

### Investment Value

Each security is valued using:

```text
Investment Value = Quantity × Price
```

For a portfolio containing multiple securities:

```text
Investment Value =
    (Quantity₁ × Price₁)
  + (Quantity₂ × Price₂)
  + ...
  + (Quantityₙ × Priceₙ)
```

All prices are assumed to be in USD.

## Example

Suppose a fund has the following holdings:

| Security  | Quantity |   Price | Market Value |
| --------- | -------: | ------: | -----------: |
| Apple     |   10,000 | $150.00 |   $1,500,000 |
| Microsoft |   20,000 |  $75.00 |   $1,500,000 |
| NVIDIA    |    5,000 | $220.00 |   $1,100,000 |

The total investment value is:

```text
$1,500,000
+ $1,500,000
+ $1,100,000
= $4,100,000
```

If the fund also has:

```text
Cash:                 $500,000
Accrued Expenses:      $25,000
Shares Outstanding:  1,000,000
```

Then:

### Total Assets

```text
$4,100,000 + $500,000
= $4,600,000
```

### Net Assets

```text
$4,600,000 - $25,000
= $4,575,000
```

### NAV per Share

```text
$4,575,000 / 1,000,000
= $4.5750
```

Therefore, the fund's NAV is:

```text
$4.5750 per share
```

## Formula Summary

The complete calculation can be represented as:

```text
                    Σ(Quantity × Price) + Cash - Expenses
NAV per Share = ---------------------------------------------
                         Shares Outstanding
```

Or more simply:

```text
NAV = Net Assets / Shares Outstanding
```

## USD Only

This project intentionally keeps the calculation simple.

There is:

* No foreign exchange calculation
* No multiple currencies
* No FX rates
* No currency conversion

All monetary values are treated as **USD**.

## Precision

The calculator uses Python's `Decimal` type rather than `float` for financial calculations.

This helps avoid common floating-point precision issues when working with monetary values.

## Running the Calculator

Make sure Python 3 is installed, then run:

```bash
python3 nav_calc.py
```

Example output:

```text
Fund: Example USD Fund
NAV per share: $4.5750
```

## Project Structure

```text
nav-calculator/
│
├── nav_calc.py
└── README.md
```

## Scope

This is a deliberately simple NAV calculator intended to demonstrate the basic mechanics of fund valuation.

A production fund accounting system may also need to consider items such as:

* Management fees
* Performance fees
* Subscriptions
* Redemptions
* Dividends
* Interest income
* Corporate actions
* Accrued income
* Trading costs
* Multiple share classes
* Independent NAV reconciliation
* Valuation policies and pricing rules

These are outside the scope of this simple implementation.

