import pytest

from YuGiOh.cards import CardManagementSystem, TrapCard
from assertions import SystemRestrictionInfringed, assert_is_empty, assert_the_only_one_in


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

    def test_cannot_store_trap_card_when_there_is_one_with_same_name(self):
        trap_card = jar_of_greed()
        another_trap_card = TrapCard.named(name=trap_card.name, type='Continuous', description='Win the game')
        self.system.store_trap_card(trap_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_trap_card(another_trap_card)
        assert exception_info.message_text() == 'There is already a trap card named Jar of Greed.'
        assert_the_only_one_in(self.system.trap_cards(), trap_card)
