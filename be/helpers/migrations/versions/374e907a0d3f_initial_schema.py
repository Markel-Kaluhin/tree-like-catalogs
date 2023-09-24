"""Initial schema

Revision ID: 374e907a0d3f
Revises:
Create Date: 2023-07-19 15:27:05.506284

"""
import sqlalchemy as sa
from alembic import op

from helpers.entity.sql_entity import TZDateTime

# revision identifiers, used by Alembic.
revision = "374e907a0d3f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "node",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column(
            "created_at", TZDateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", TZDateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["node.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_node_parent_id"), "node", ["parent_id"], unique=False)
    op.create_table(
        "property",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("node_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("value", sa.DECIMAL(), nullable=False),
        sa.Column(
            "created_at", TZDateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", TZDateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["node_id"],
            ["node.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_property_node_id"),
        "property",
        ["node_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_property_node_id"), table_name="property")
    op.drop_table("property")
    op.drop_index(op.f("ix_node_parent_id"), table_name="node")
    op.drop_table("node")
    # ### end Alembic commands ###
