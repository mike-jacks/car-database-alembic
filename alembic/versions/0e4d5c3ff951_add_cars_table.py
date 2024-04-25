"""add cars table

Revision ID: 0e4d5c3ff951
Revises: 
Create Date: 2024-04-25 11:11:50.562685

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e4d5c3ff951'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("cars", 
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("vin", sa.Text),
                    sa.Column("model", sa.Text),
                    sa.Column("make", sa.Text),
                    sa.Column("engine", sa.Text),
                    sa.Column("year", sa.Integer))


def downgrade() -> None:
    op.drop_table("cars")
