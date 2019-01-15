"""Init

Revision ID: 92841eb1b2e0
Revises: 
Create Date: 2019-01-15 00:18:08.812225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92841eb1b2e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FileContents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('RevokedTokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imageId', sa.Integer(), nullable=True),
    sa.Column('firstName', sa.String(length=64), nullable=False),
    sa.Column('lastName', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_firstName'), 'users', ['firstName'], unique=False)
    op.create_index(op.f('ix_users_lastName'), 'users', ['lastName'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_lastName'), table_name='users')
    op.drop_index(op.f('ix_users_firstName'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('RevokedTokens')
    op.drop_table('FileContents')
    # ### end Alembic commands ###