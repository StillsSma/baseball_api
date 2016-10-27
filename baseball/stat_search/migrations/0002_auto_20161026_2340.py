from __future__ import unicode_literals
from stat_search.models import Master, Batting, Pitching, Fielding
from django.db import migrations, models
import csv

def add_data(apps, schema_editor):

    with open('Master.csv') as m:
        reader = csv.DictReader(m)

        for row in reader:
            Master.objects.create(
            player_id=row["playerID"],
            birth_year=row["birthYear"],
            birth_month=row["birthMonth"],
            birth_day=row["birthDay"],
            birth_country=row["birthCountry"],
            birth_state=row["birthState"],
            birth_city=row["birthCity"],
            death_year=row["deathYear"],
            death_month=row["deathMonth"],
            death_day=row["deathDay"],
            death_country=row["deathCountry"],
            death_state=row["deathState"],
            death_city=row["deathCity"],
            first_name=row["nameFirst"],
            last_name=row["nameLast"],
            given_name=row["nameGiven"],
            weight=row["weight"],
            height=row["height"],
            bats=row["bats"],
            throws=row["throws"],
            debut=row["debut"],
            final_game=row["finalGame"],
            retro_id=row["retroID"],
            bbref_id=row["bbrefID"],

             )

    with open('Batting.csv') as b:
        reader = csv.DictReader(b)

        for row in reader:
            player = Master.objects.get(player_id=row['playerID'])
            Batting.objects.create(
            player_id=player,
            year=row["yearID"],
            stint=row["stint"],
            team_id=row["teamID"],
            league=row["lgID"],
            games=row["G"],
            at_bats=row["AB"],
            runs=row["R"],
            hits=row["H"],
            doubles=row["2B"],
            triples=row["3B"],
            homeruns=row["HR"],
            runs_batted_in=row["RBI"],
            stolen_bases=row["SB"],
            caught_stealing=row["CS"],
            base_on_balls=row["BB"],
            strikeouts=row["SO"],
            intentional_walks=row["IBB"],
            hit_by_pitch=row["HBP"],
            sacrifice_hits=row["SH"],
            sacfifice_flies=row["SF"],
            grounded_into_double_plays=row["GIDP"],

            )

    with open('Pitching.csv') as p:
        reader = csv.DictReader(p)

        for row in reader:
            player = Master.objects.get(player_id=row['playerID'])
            Pitching.objects.create(
            player_id=player,
            year=row["yearID"],
            stint=row["stint"],
            team_id=row["teamID"],
            league=row["lgID"],
            wins=row["W"],
            losses=row["L"],
            games=row["G"],
            games_started=row["GS"],
            complete_games=row["CG"],
            shutouts=row["SHO"],
            saves=row["SV"],
            outs_pitched=row["IPouts"],
            hits=row["H"],
            earned_runs=row["ER"],
            homeruns=row["HR"],
            walks=row["BB"],
            strikeouts=row["SO"],
            opponent_batting_average=row["BAOpp"],
            earned_run_average=row["ERA"],
            intentional_walks=row["IBB"],
            wild_pitches=row["WP"],
            batters_hit_by_pitch=row["HBP"],
            balks=row["BK"],
            batters_faced_by_pitcher=row["BFP"],
            games_finished=row["GF"],
            runs_allowed=row["R"],
            sacrifices =row["SH"],
            sacrifices_flies=row["SF"],
            grounded_into_double_plays=row["GIDP"],
                )
    with open('Fielding.csv') as f:
        reader = csv.DictReader(f)

        for row in reader:
            player = Master.objects.get(player_id=row['playerID'])
            Fielding.objects.create(
            player_id=player,
            year=row["yearID"],
            stint=row["stint"],
            team_id=row["teamID"],
            league=row["lgID"],
            postion=row["POS"],
            games=row["G"],
            games_started=row["GS"],
            time_played_in_field=row["InnOuts"],
            putouts=row["PO"],
            assists=row["A"],
            errors=row["E"],
            double_plays=row["DP"],
            passed_balls_catchers=row["PB"],
            wild_pitches_catchers=row["WP"],
            opponent_stolen_bases=row["SB"],
            opponent_caught_stealing=row["CS"],
            zone_rating=row["ZR"],
                )


class Migration(migrations.Migration):

    dependencies = [
        ('stat_search', '0001_initial'),
    ]

    operations = [
    migrations.RunPython(add_data),
    ]
