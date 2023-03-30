"""Initial

Revision ID: 73ffa12c03c8
Revises: 
Create Date: 2022-07-28 22:13:22.811061

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '73ffa12c03c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('username', sa.String(length=32), nullable=True),
                    sa.Column('first_name', sa.String(length=255), nullable=True),
                    sa.Column('last_name', sa.String(length=255), nullable=True),
                    sa.Column('is_banned', sa.Boolean(), server_default='False', nullable=False),
                    sa.Column('deep_link', sa.String(length=225), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
