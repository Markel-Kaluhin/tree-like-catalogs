"""Indexed both name fields in node and property tables cause I search by each of them

Revision ID: 21b9881710e4
Revises: 374e907a0d3f
Create Date: 2023-07-20 01:35:39.317065

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "21b9881710e4"
down_revision = "374e907a0d3f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_node_name"), "node", ["name"], unique=False)
    op.create_index(op.f("ix_property_name"), "property", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_property_name"), table_name="property")
    op.drop_index(op.f("ix_node_name"), table_name="node")
    # ### end Alembic commands ###
