"""Initial Migrations

Revision ID: d75cb1febed1
Revises: 
Create Date: 2024-01-26 21:25:56.550633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd75cb1febed1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('repeat', sa.Enum('every_day', 'weekdays', 'weekends', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', name='repeat'), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('relay_board_type', sa.Enum('waveshare_rpi_relay_board', name='relayboardtype'), nullable=False),
    sa.Column('relay_position', sa.Integer(), nullable=False),
    sa.Column('start_schedule_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('stop_schedule_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    # ### end Alembic commands ###