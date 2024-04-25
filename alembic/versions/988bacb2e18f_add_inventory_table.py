"""add inventory table

Revision ID: 988bacb2e18f
Revises: 7a62f882d9fa
Create Date: 2024-04-25 11:20:32.204825

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '988bacb2e18f'
down_revision: str | None = '7a62f882d9fa'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("inventory", 
                    sa.Column("car_id", sa.Integer, sa.ForeignKey('cars.id'), primary_key=True),
                    sa.Column("dealer_id", sa.Integer, sa.ForeignKey('dealerships.id'), primary_key=True),
                    sa.Column("cost", sa.Float),
                    sa.Column("is_sold", sa.Boolean)
                    )


def downgrade() -> None:
    op.drop_table("inventory")
