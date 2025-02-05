"""empty message

Revision ID: d221afa52176
Revises: 
Create Date: 2025-02-05 12:46:39.623915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd221afa52176'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.execute('CREATE EXTENSION IF NOT EXISTS "unaccent";')
    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('firstname', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
    op.execute('DROP EXTENSION IF EXISTS "unaccent";')
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')
