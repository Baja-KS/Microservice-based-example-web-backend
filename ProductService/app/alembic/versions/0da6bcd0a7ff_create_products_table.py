"""create products table

Revision ID: 0da6bcd0a7ff
Revises: 
Create Date: 2021-03-30 01:11:59.442553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0da6bcd0a7ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, unique=True, index=True),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table("products")
