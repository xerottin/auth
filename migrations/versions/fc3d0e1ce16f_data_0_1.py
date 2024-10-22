"""data_0.1

Revision ID: fc3d0e1ce16f
Revises: 9433fd03341d
Create Date: 2024-07-22 09:49:30.001380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'fc3d0e1ce16f'
down_revision: Union[str, None] = '9433fd03341d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_notifications',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('subject', sa.String(), nullable=True),
                    sa.Column('message', sa.String(), nullable=True),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_email_notifications_email'), 'email_notifications', ['email'], unique=False)
    op.create_index(op.f('ix_email_notifications_id'), 'email_notifications', ['id'], unique=False)
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('user_id', name='users_pkey'),
                    sa.UniqueConstraint('email', name='users_email_key'),
                    sa.UniqueConstraint('username', name='users_username_key')
                    )
    op.drop_index(op.f('ix_email_notifications_id'), table_name='email_notifications')
    op.drop_index(op.f('ix_email_notifications_email'), table_name='email_notifications')
    op.drop_table('email_notifications')
    # ### end Alembic commands ###
