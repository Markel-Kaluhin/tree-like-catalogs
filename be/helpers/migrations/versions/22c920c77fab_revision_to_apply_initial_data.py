"""Revision to apply initial data

Revision ID: 22c920c77fab
Revises: 21b9881710e4
Create Date: 2023-07-20 23:40:11.971790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22c920c77fab'
down_revision = '21b9881710e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (1, NULL, 'Rocket');")
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (4, 1, 'Stage1');")
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (5, 1, 'Stage2');")
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (6, 4, 'Engine1');")
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (7, 4, 'Engine2');")
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (8, 4, 'Engine3');")
    op.execute("INSERT INTO public.rocket_node (id, parent_id, name) VALUES (9, 5, 'Engine1');")

    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (1, 6, 'Thrust', 9.493);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (2, 6, 'ISP', 12.156);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (3, 7, 'Thrust', 9.413);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (4, 7, 'ISP', 11.632);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (5, 8, 'Thrust', 9.899);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (6, 8, 'ISP', 12.551);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (7, 9, 'Thrust', 1.622);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (8, 9, 'ISP', 15.11);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (9, 1, 'Mass', 12000);")
    op.execute("INSERT INTO public.rocket_property (id, rocket_node_id, name, value) VALUES (10, 1, 'Height', 18);")

    op.execute("ALTER SEQUENCE public.rocket_node_id_seq RESTART WITH 10;")
    op.execute("ALTER SEQUENCE public.rocket_property_id_seq RESTART WITH 11;")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
