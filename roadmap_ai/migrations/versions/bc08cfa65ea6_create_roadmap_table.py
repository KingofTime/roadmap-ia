"""create roadmap table

Revision ID: bc08cfa65ea6
Revises:
Create Date: 2024-11-07 05:01:16.887273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc08cfa65ea6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roadmaps',
    sa.Column('id', sa.Integer(), nullable=False, auto_increment=True),
    sa.Column('status', sa.Enum('processing', 'done', name='roadmapstatus'), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roadmaps')
    # ### end Alembic commands ###
