from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Holding:
    name: str
    quantity: Decimal
    price_usd: Decimal


@dataclass
class Fund:
    name: str
    shares_outstanding: Decimal
    cash_usd: Decimal
    holdings: list[Holding]
    accrued_expenses_usd: Decimal = Decimal('0')


def calculate_nav(fund: Fund) -> Decimal:
    """Calculcating NAV per share in USD."""

    #Calculating market value of all investments
    investment_value_usd = sum(
        holding.quantity * holding.price_usd
        for holding in fund.holdings
    )

    # Calculate net assets
    net_assets_usd = (
        investment_value_usd
        + fund.cash_usd
        - fund.accrued_expenses_usd
    )

    if fund.shares_outstanding <= 0:
        raise ValueError("Shares outstanding must be greater than zero")

    # NAV per share
    return net_assets_usd / fund.shares_outstanding


def main():
    fund = Fund(
        name="Example USD Fund",
        shares_outstanding=Decimal("1_000_000"),
        cash_usd=Decimal("500_000"),
        accrued_expenses_usd=Decimal("25_000"),

        holdings=[
            Holding(
                name="Apple",
                quantity=Decimal("10_000"),
                price_usd=Decimal("150.00"),
            ),
            Holding(
                name="Microsoft",
                quantity=Decimal("20_000"),
                price_usd=Decimal("75.00"),
            ),
            Holding(
                name="NVIDIA",
                quantity=Decimal("5_000"),
                price_usd=Decimal("220.00"),
            ),
        ],
    )

    nav = calculate_nav(fund)

    print(f"Fund: {fund.name}")
    print(f"NAV per share: ${nav:.4f}")


if __name__ == "__main__":
    main()
