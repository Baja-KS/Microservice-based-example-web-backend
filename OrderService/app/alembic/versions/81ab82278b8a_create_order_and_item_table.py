"""create order and item table

Revision ID: 81ab82278b8a
Revises: 
Create Date: 2021-03-30 10:48:16.235882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81ab82278b8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("isPending",sa.Boolean,default=True)
    )
    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, unique=True, index=True),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("orderID",sa.Integer,sa.ForeignKey("orders.id"))
    )


def downgrade():
    op.drop_table("items")
    op.drop_table("orders")
