import pytest

from YuGiOh.cards import CardManagementSystem, TrapCard
from assertions import assert_is_empty, assert_the_only_one_in


def jar_of_greed():
    return TrapCard.named(name='Jar of Greed', type='Normal', description='Draw 1 card.')    


@pytest.mark.django_db
class TestCardManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = CardManagementSystem()

    def test_store_trap_card(self):
        assert_is_empty(self.system.trap_cards())
        trap_card = jar_of_greed()
        self.system.store_trap_card(trap_card)
        assert_the_only_one_in(self.system.trap_cards(), trap_card)
