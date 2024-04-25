"""add dealerships table

Revision ID: 7a62f882d9fa
Revises: 0e4d5c3ff951
Create Date: 2024-04-25 11:18:10.371041

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a62f882d9fa'
down_revision: str | None = '0e4d5c3ff951'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("dealerships",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("name", sa.Text),
                    sa.Column("address", sa.Text),
                    sa.Column("phone_number", sa.Text)
                    )


def downgrade() -> None:
    op.drop_table("dealerships")
