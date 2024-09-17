"""Agregado logica de token de verificacion

Revision ID: 24eeb0e53d85
Revises: 0630995f85c2
Create Date: 2024-09-17 17:02:17.123394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24eeb0e53d85'
down_revision = '0630995f85c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token_checkin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=40), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token_checkin')
    # ### end Alembic commands ###
