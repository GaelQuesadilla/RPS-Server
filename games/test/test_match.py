from django.test import TestCase
from games.models import Match
from users.models import Player
from django.core.exceptions import ValidationError


class MatchTestCase(TestCase):
    def setUp(self):
        self.player = Player.objects.create_user(
            username="tester", password="123")

    def test_draw(self):
        result = Match.objects.create(
            player=self.player,
            player_choice="P",
            machine_choice="P",
        )
        self.assertEqual(result.get_result(), "D")

        result = Match.objects.create(
            player=self.player,
            player_choice="R",
            machine_choice="R",
        )
        self.assertEqual(result.get_result(), "D")

        result = Match.objects.create(
            player=self.player,
            player_choice="S",
            machine_choice="S",
        )
        self.assertEqual(result.get_result(), "D")

    def test_win(self):
        result = Match.objects.create(
            player=self.player,
            player_choice="S",
            machine_choice="P",
        )
        self.assertEqual(result.get_result(), "W")

        result = Match.objects.create(
            player=self.player,
            player_choice="P",
            machine_choice="R",
        )
        self.assertEqual(result.get_result(), "W")

        result = Match.objects.create(
            player=self.player,
            player_choice="R",
            machine_choice="S",
        )
        self.assertEqual(result.get_result(), "W")

    def test_loss(self):
        result = Match.objects.create(
            player=self.player,
            player_choice="P",
            machine_choice="S",
        )
        self.assertEqual(result.get_result(), "L")

        result = Match.objects.create(
            player=self.player,
            player_choice="R",
            machine_choice="P",
        )
        self.assertEqual(result.get_result(), "L")

        result = Match.objects.create(
            player=self.player,
            player_choice="S",
            machine_choice="R",
        )
        self.assertEqual(result.get_result(), "L")

    def test_no_valid_case(self):
        try:
            result = Match.objects.create(
                player=self.player, player_choice="X")
            self.fail("The X value must not be allowed")
        except ValidationError as e:
            self.assertTrue(True)
