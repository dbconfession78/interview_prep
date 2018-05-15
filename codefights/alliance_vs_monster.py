"""
You and your alliance of warriors are trying to kill a monster to score points in a Kingdom vs. Kingdom (KvK) event. Each unit (both a warrior and a monster are considered a unit) has a certain number of health points (healthPoints) and attack damage value (attackDamage). When one unit attacks another, the health of the unit that is under attack is decreased by the attacker's damage value. If a unit's health points are reduced to zero or less, the unit dies and can't take part in the battle anymore.

The skirmish between the warrior alliance and the monster proceeds in the following way:

    Each turn, you direct one of your warriors to attack the monster.
    If the monster dies, you win.
    If the monster is still alive after an attack, it counter-attacks the same warrior who attacked it in the previous step.
    If all of your warriors die, you lose.

Find the maximum number of your warriors that will remain after defeating the monster. If it's impossible to kill a monster without losing all your warriors, return 0.

Example

    For healthPoints = [110, 30, 50] and attackDamage = [12, 11, 20], the output should be
    allianceVersusMonster(healthPoints, attackDamage) = 2.

    One of the optimal strategies is as follows:
        Attack the monster four times with the second warrior. The monster's health will become 110 - 20 * 4 = 30, while the warrior's health will be 50 - 12 * 4 = 2.
        If you use the second warrior again immediately, it will die. Therefore, use the first warrior instead. Its three attacks will deplete the monster's health by 11 * 3 = 33 points, while the monster will respond only twice. After the third attack it will die instantly. Your first warrior's health will be 30 - 12 * 2 = 6 after the fight ends.
        In this way you are able to save both of your warriors and win the battle.

    For healthPoints = [4, 10, 10, 10] and attackDamage = [10, 1, 1, 1], the output should be
    allianceVersusMonster(healthPoints, attackDamage) = 0.

    Each of your warriors will be able to attack the monster only once because they will die after one counter-attack. Each of the attacks will reduce the monster's health by 1. Thus, after three turns, the monster will still have 1 health point but all of your warrior will be dead.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer healthPoints

    Array of at least two positive integers. healthPoints[0] corresponds to the monster's health, while all the following elements refer to warriors of the alliance.

    Guaranteed constraints:
    2 ≤ healthPoints.length ≤ 30,
    1 ≤ healthPoints[i] ≤ 2 · 109 + 1.

    [input] array.integer attackDamage

    Array of the same length as healthPoints, consisting of positive integers. attackDamage[0] equals the monster's attack damage, while all the following elements refer to warriors of the alliance.

    Guaranteed constraints:
    2 ≤ attackDamage.length ≤ 30,
    1 ≤ attackDamage[i] ≤ 100.

    [output] integer

    The maximum number of your warriors that will remain after defeating the monster, or 0 if it's impossible to kill a monster without losing all your warriors.

"""


def allianceVersusMonster(healthPoints, attackDamage):
    _len = len(healthPoints)
    healthPoints = adjust_hp(healthPoints)

    mon_hp = healthPoints[0]
    mon_ad = attackDamage[0]
    warr_lst = []
    last_stand = []
    warr_count = len(healthPoints) - 1
    for i in range(1, _len):
        warr_lst.append({"id": i, "hp": healthPoints[i], "ad": attackDamage[i]})
    warr_lst = sorted(warr_lst, key=lambda k: k["ad"])

    while warr_lst:
        fighter = warr_lst.pop()
        while fighter["hp"] > mon_ad:
            mon_hp -= fighter["ad"]

            if mon_hp <= 0:
                return warr_count
            fighter["hp"] -= mon_ad

        last_stand.insert(0, fighter)

    while last_stand:
        fighter = last_stand.pop()
        if fighter["hp"] > 0:
            mon_hp -= fighter["ad"]
            if mon_hp <= 0:
                return warr_count
            warr_count -= 1
    return warr_count

def adjust_hp(healthPoints):
    long_idx_hp = None
    long_hp = 0
    should_shrink = False
    for i, elem in enumerate(healthPoints):
        if len(str(healthPoints[i])) > 5:
            should_shrink = True
            if long_idx_hp is None:
                long_hp = len(str(healthPoints[i]))
            else:
                _len = len(str(healthPoints[i]))
                if _len > long_hp:
                    long_hp = _len
            break

    if should_shrink:
        shrink_by = long_hp - 5
        for i in range(len(healthPoints)):
            for j in range(shrink_by):
                healthPoints[i] /= 10
    return healthPoints


def test(sol, retval):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

test(2, allianceVersusMonster([110, 30, 50], [12,11,20]))
test(0, allianceVersusMonster([4, 10, 10, 10], [10,1,1,1]))
test(3, allianceVersusMonster([10, 3, 3, 3], [2,1,5,1]))
test(1, allianceVersusMonster([2000000000, 2000000000], [1, 1]))
test(2, allianceVersusMonster([11, 4, 4, 4], [1,1,1,1]))
test(3, allianceVersusMonster([10, 4, 4, 4],  [1,1,1,1]))
test(1, allianceVersusMonster([5, 10, 10, 10],  [10,2,2,2]))

test(0, allianceVersusMonster([2000000000, 5],  [1,1]))


